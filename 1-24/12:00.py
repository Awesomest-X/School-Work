class Recipe:
    def __init__(self, name, ingredients, cuisine, aliases=None, instructions=None):
        """
        Initialize a recipe with a name, list of ingredients, cuisine type, optional aliases, and instructions.
        """
        self.name = name
        self.ingredients = ingredients
        self.cuisine = cuisine
        self.instructions = instructions or "Instructions not available."
        self.aliases = aliases or []  # Alternate names for the recipe

    def __str__(self):
        """
        Return a string representation of the recipe with full details.
        """
        ingredients_str = ", ".join(self.ingredients)
        return (f"Recipe: {self.name}\nCuisine: {self.cuisine}\nIngredients: {ingredients_str}\n"
                f"Instructions:\n{self.instructions}")


class RecipeBook:
    def __init__(self):
        """
        Initialize an empty recipe collection and a dictionary for aliases.
        """
        self.recipes = []
        self.alias_map = {}

    def add_recipe(self, recipe):
        """
        Add a new recipe to the collection and update the alias map.
        """
        self.recipes.append(recipe)
        # Add the primary name to the alias map
        self.alias_map[recipe.name.lower()] = [recipe]
        for alias in recipe.aliases:
            alias = alias.lower()
            if alias not in self.alias_map:
                self.alias_map[alias] = []
            self.alias_map[alias].append(recipe)

    def find_by_name(self, name):
        """
        Search for a recipe by its exact name or alias.
        """
        return self.alias_map.get(name.lower(), [])

    def search_by_ingredient(self, ingredients):
        """
        Search for recipes that contain all specified ingredients.
        """
        ingredients = [ingredient.strip().lower() for ingredient in ingredients]
        return [
            recipe for recipe in self.recipes
            if all(ingredient in map(str.lower, recipe.ingredients) for ingredient in ingredients)
        ]

    def search_by_cuisine(self, cuisine):
        """
        Search for recipes by cuisine type.
        """
        return [recipe for recipe in self.recipes if recipe.cuisine.lower() == cuisine.lower()]

    def general_search(self, query):
        """
        Perform a general search across name, aliases, ingredients, and cuisine.
        """
        query_lower = query.lower()
        results = set()

        # Search by name and aliases
        results.update(self.alias_map.get(query_lower, []))

        # Search by ingredients
        results.update([recipe for recipe in self.recipes if query_lower in map(str.lower, recipe.ingredients)])

        # Search by cuisine
        results.update([recipe for recipe in self.recipes if query_lower == recipe.cuisine.lower()])

        return results

    def get_recipe_by_name(self, name):
        """
        Get the full recipe by its exact name.
        """
        recipes = self.find_by_name(name)
        return recipes[0] if recipes else None


# Interactive Input Bar
def interactive_recipe_search():
    # Create a RecipeBook and add recipes
    recipe_book = RecipeBook()

    breakfast_taco_instruction = (
        "\nCook the bacon in the oven for 18 to 20 minutes.\n"
        "Then sauté the green onions with olive oil.\n"
        "Whisk the eggs and pour them into the pan. Gently stir the eggs as they cook to create the perfect pillowy texture.\n"
        "Time to assemble. Add a good spoonful or two of scrambled eggs to a tortilla. Top it off with green onion, crumbled bacon, and cheese."
    )

    # Sample Recipes
    
  # Italian Cuisine
    recipe_book.add_recipe(Recipe("Spaghetti Carbonara", ["spaghetti", "eggs", "bacon", "parmesan"], "Italian", ["pasta","parm","carbonara","cheese", "spageti","carborna","italian food","egg"]))
    recipe_book.add_recipe(Recipe("Margherita Pizza", ["dough", "tomato", "mozzarella", "basil"], "Italian",["cheese","pizza","piza","italian food"]))
    recipe_book.add_recipe(Recipe("Chicken Alfredo", ["penne", "chicken", "alfredo sauce","parmesan", "butter"], "Italian", ["pasta", "alfredo","italian food"]))
    recipe_book.add_recipe(Recipe("Lasagna", ["pasta", "ricotta", "ground beef", "tomato sauce"], "Italian",["beef","cheese","tomato","italian food"]))
    
    # Mexican Cuisine
    recipe_book.add_recipe(Recipe("Beef Tacos", ["tortilla", "beef", "lettuce", "cheese", "salsa"], "Mexican", ["taco","tacos with beef","taco with beef","mex","mexican food","tacos","beef taco"]))
    recipe_book.add_recipe(Recipe("Breakfast Tacos", ["tortilla", "bacon", "eggs", "cheese", "salsa"], "Mexican", ["taco","tacos","breakfast","mex","mexican food","breakfast taco"], breakfast_taco_instruction))
    recipe_book.add_recipe(Recipe("Pork Tacos", ["tortilla", "pork", "lettuce", "cheese", "salsa"], "Mexican", ["taco", "tacos with pork","taco with pork","pork taco","mex","mexican food","tacos"]))
    recipe_book.add_recipe(Recipe("Guacamole", ["avocado", "onion", "tomato", "lime"], "Mexican",["guac","mex","mexican food"]))
    recipe_book.add_recipe(Recipe("Enchiladas", ["tortilla", "chicken", "cheese", "enchilada sauce"], "Mexican",["mex","mexican food"]))
    recipe_book.add_recipe(Recipe("Burritos", ["tortilla", "rice", "beans", "meat", "cheese"], "Mexican",["mexican food","chicken","beef","mex"]))


    # American Cuisine
    recipe_book.add_recipe(Recipe("Pancakes", ["flour", "milk", "eggs", "butter", "syrup"], "American", ["pancake","egg","american","american food","breakfast food","breakfast"]))
    recipe_book.add_recipe(Recipe("Burger", ["bun", "beef patty", "lettuce", "tomato", "cheese","american"], "American", ["cheeseburger","cheese burger","a burger","hamburger","american","american food"]))
    print("Welcome to Jer's Recipe Finder!")
    print("Enter queries like:\n- 'name: pancakes'\n- 'ingredient: eggs'\n- 'cuisine: Mexican'\n"
          "- 'all' to list all recipes.\nType 'exit' to quit.\n")

    while True:
        query = input("Search: ").strip()
        if query.lower() == "exit":
            print("Goodbye!")
            break

        if query.lower() == "all":
            print("\nAll Recipes:\n")
            for recipe in recipe_book.recipes:
                print(f"- {recipe.name} ({recipe.cuisine})")
            continue

        # Detect query type or perform general search
        if query.startswith("name:"):
            name = query[len("name:"):].strip()
            results = recipe_book.find_by_name(name)
        elif query.startswith("ingredient:"):
            ingredients = query[len("ingredient:"):].strip().split("and")
            results = recipe_book.search_by_ingredient(ingredients)
        elif query.startswith("cuisine:"):
            cuisine = query[len("cuisine:"):].strip()
            results = recipe_book.search_by_cuisine(cuisine)
        else:
            # Perform general search
            results = recipe_book.general_search(query)

        # Display results
        if results:
            print("\nRecipes Found:\n")
            for recipe in results:
                print(f"- {recipe.name} ({recipe.cuisine})")
            print("\nType the name of a recipe to view its details or 'back' to perform another search.\n")

            while True:
                selected_recipe = input("Enter recipe name: ").strip()
                if selected_recipe.lower() == "back":
                    break
                recipe = recipe_book.get_recipe_by_name(selected_recipe)
                if recipe:
                    print("\nRecipe Details:\n")
                    print(recipe)
                    print("\nType 'back' to return to the search results.\n")
                else:
                    print("Recipe not found. Please try again or type 'back' to search again.")
        else:
            print("\nNo Recipes Found.\n")


# Run the interactive search
if __name__ == "__main__":
    interactive_recipe_search()
