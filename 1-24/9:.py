class Recipe:
    def __init__(self, name, ingredients, cuisine, aliases=None):
        """
        Initialize a recipe with a name, list of ingredients, cuisine type, and optional aliases.
        """
        self.name = name
        self.ingredients = ingredients
        self.cuisine = cuisine
        self.aliases = aliases or []  # Alternate names for the recipe

    def __str__(self):
        """
        Return a string representation of the recipe.
        """
        ingredients_str = ", ".join(self.ingredients)
        return f"Recipe: {self.name}\nCuisine: {self.cuisine}\nIngredients: {ingredients_str}"


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

    def search_by_ingredient(self, ingredient):
        """
        Search for recipes that contain a specific ingredient.
        """
        return [recipe for recipe in self.recipes if ingredient.lower() in map(str.lower, recipe.ingredients)]

    def search_by_cuisine(self, cuisine):
        """
        Search for recipes by cuisine type.
        """
        return [recipe for recipe in self.recipes if recipe.cuisine.lower() == cuisine.lower()]

    def get_all_recipes(self):
        """
        Return all recipes in the collection.
        """
        return self.recipes

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
    
    # Italian Cuisine
    recipe_book.add_recipe(Recipe("Spaghetti Carbonara", ["spaghetti", "eggs", "bacon", "parmesan"], "Italian", ["pasta","parm","carbonara","cheese", "spageti","italian","carborna","italian food","egg"]))
    recipe_book.add_recipe(Recipe("Margherita Pizza", ["dough", "tomato", "mozzarella", "basil"], "Italian",["cheese","pizza","piza","italian","italian food"]))
    recipe_book.add_recipe(Recipe("Chicken Alfredo", ["penne", "chicken", "alfredo sauce","parmesan", "butter"], "Italian", ["pasta", "alfredo","italian","italian food"]))
    recipe_book.add_recipe(Recipe("Lasagna", ["pasta", "ricotta", "ground beef", "tomato sauce"], "Italian",["beef","cheese","tomato","italian","italian food"]))
    
    # Mexican Cuisine
    recipe_book.add_recipe(Recipe("Beef Tacos", ["tortilla", "beef", "lettuce", "cheese", "salsa"], "Mexican", ["taco","tacos with beef","taco with beef","mexican","mex","mexican food","tacos","beef taco"]))
    recipe_book.add_recipe(Recipe("Breakfast Tacos", ["tortilla", "bacon", "eggs", "cheese", "salsa"], "Mexican", ["taco","tacos","breakfast","mexican","mex","mexican food","breakfast taco"]))
    recipe_book.add_recipe(Recipe("Pork Tacos", ["tortilla", "pork", "lettuce", "cheese", "salsa"], "Mexican", ["taco", "tacos with pork","taco with pork","pork taco","mexican","mex","mexican food","tacos"]))
    recipe_book.add_recipe(Recipe("Guacamole", ["avocado", "onion", "tomato", "lime"], "Mexican",["mexican","guac","mex","mexican food"]))
    recipe_book.add_recipe(Recipe("Enchiladas", ["tortilla", "chicken", "cheese", "enchilada sauce"], "Mexican",["mexican","mex","mexican food"]))
    recipe_book.add_recipe(Recipe("Burritos", ["tortilla", "rice", "beans", "meat", "cheese"], "Mexican",["mexican food","chicken","beef","mex","mexican"]))


    # American Cuisine
    recipe_book.add_recipe(Recipe("Pancakes", ["flour", "milk", "eggs", "butter", "syrup"], "American", ["pancake","egg","american","american food","breakfast food","breakfast"]))
    recipe_book.add_recipe(Recipe("Burger", ["bun", "beef patty", "lettuce", "tomato", "cheese","american"], "American", ["cheeseburger","cheese burger","a burger","hamburger","american","american food"]))
    recipe_book.add_recipe(Recipe("Grilled Cheese Sandwich", ["bread", "cheese", "butter"], "American",["grilled cheese","american","american food"]))

    print("Welcome to Jer's Recipe Finder!")
    print("Enter a recipe name, an ingredient, a cuisine type, or 'all' to list all recipes.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Search: ").strip()
        if query.lower() == "exit":
            print("Goodbye!")
            break

        # Display all recipes
        if query.lower() == "all":
            print("\nAll Recipes:\n")
            print(recipe_book)
            continue

        # Perform the combined search
        recipes_by_name = recipe_book.find_by_name(query)
        recipes_by_ingredient = recipe_book.search_by_ingredient(query)
        recipes_by_cuisine = recipe_book.search_by_cuisine(query)

        # Combine all results into a set to avoid duplicates
        results = set()
        results.update(recipes_by_name)
        results.update(recipes_by_ingredient)

        if results:
            print("\nRecipes Found:\n")
            for recipe in results:
                print(recipe)
                print()
        else:
            print("\nNo Recipes Available.\n")


# Run the interactive search
if __name__ == "__main__":
    interactive_recipe_search()
