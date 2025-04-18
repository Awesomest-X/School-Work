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
        Return a string representation of the recipe.
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

    def __str__(self):
        """
        Return a string representation of all recipes in the recipe book.
        """
        if not self.recipes:
            return "No recipes available."
        return "\n\n".join(str(recipe) for recipe in self.recipes)


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
    recipe_book.add_recipe(Recipe("Breakfast Tacos", ["tortilla", "bacon", "eggs", "cheese", "salsa"], "Mexican", 
                                  ["taco", "tacos", "breakfast"], breakfast_taco_instruction))
    recipe_book.add_recipe(Recipe("Pancakes", ["flour", "milk", "eggs", "butter", "syrup"], "American", 
                                  ["pancake", "breakfast food", "breakfast"]))
    recipe_book.add_recipe(Recipe("Margherita Pizza", ["dough", "tomato", "mozzarella", "basil"], "Italian", 
                                  ["cheese", "pizza", "italian food"]))

    print("Welcome to Jer's Recipe Finder!")
    print("Enter queries like:\n- 'name: pancakes'\n- 'ingredient: eggs'\n- 'cuisine: Mexican'\n"
          "- 'ingredient: bacon and eggs'\n- 'all' to list all recipes.\nType 'add' to add a new recipe or 'exit' to quit.\n")

    while True:
        query = input("Search: ").strip()
        if query.lower() == "exit":
            print("Goodbye!")
            break

        if query.lower() == "all":
            print("\nAll Recipes:\n")
            print(recipe_book)
            continue

        if query.lower() == "add":
            print("\nAdd a New Recipe")
            name = input("Enter recipe name: ").strip()
            ingredients = input("Enter ingredients (comma-separated): ").strip().split(",")
            cuisine = input("Enter cuisine type: ").strip()
            aliases = input("Enter aliases (comma-separated, optional): ").strip().split(",") or []
            instructions = input("Enter cooking instructions (optional): ").strip()
            recipe = Recipe(name, ingredients, cuisine, aliases, instructions)
            recipe_book.add_recipe(recipe)
            print("\nRecipe added successfully!\n")
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
                print(recipe)
                print()
        else:
            print("\nNo Recipes Found.\n")


# Run the interactive search
if __name__ == "__main__":
    interactive_recipe_search()
