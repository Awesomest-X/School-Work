import difflib  # Library to handle close matches


class Recipe:
    def __init__(self, name, ingredients, cuisine, aliases=None):
        self.name = name
        self.ingredients = ingredients
        self.cuisine = cuisine
        self.aliases = aliases or []

    def __str__(self):
        ingredients_str = ", ".join(self.ingredients)
        return f"Recipe: {self.name}\nCuisine: {self.cuisine}\nIngredients: {ingredients_str}"


class RecipeBook:
    def __init__(self):
        self.recipes = []
        self.alias_map = {}

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        self.alias_map[recipe.name.lower()] = recipe
        for alias in recipe.aliases:
            self.alias_map[alias.lower()] = recipe

    def find_by_name(self, name):
        # Exact match
        if name.lower() in self.alias_map:
            return self.alias_map[name.lower()]
        # Fuzzy match for close names
        close_matches = difflib.get_close_matches(name.lower(), self.alias_map.keys(), n=1, cutoff=0.7)
        if close_matches:
            return self.alias_map[close_matches[0]]
        return None

    def search_by_ingredient(self, ingredient):
        return [recipe for recipe in self.recipes if ingredient.lower() in map(str.lower, recipe.ingredients)]

    def search_by_cuisine(self, cuisine):
        cuisines = [recipe.cuisine.lower() for recipe in self.recipes]
        # Exact match
        if cuisine.lower() in cuisines:
            return [recipe for recipe in self.recipes if recipe.cuisine.lower() == cuisine.lower()]
        # Fuzzy match for close cuisines
        close_matches = difflib.get_close_matches(cuisine.lower(), cuisines, n=1, cutoff=0.7)
        if close_matches:
            return [recipe for recipe in self.recipes if recipe.cuisine.lower() == close_matches[0]]
        return []

    def __str__(self):
        if not self.recipes:
            return "No recipes available."
        return "\n\n".join(str(recipe) for recipe in self.recipes)


def interactive_recipe_search():
    recipe_book = RecipeBook()
    
    # Italian Cuisine
    recipe_book.add_recipe(Recipe("Spaghetti Carbonara", ["spaghetti", "eggs", "bacon", "parmesan"], "Italian", ["pasta", "carbonara", "cheese"]))
    recipe_book.add_recipe(Recipe("Margherita Pizza", ["dough", "tomato", "mozzarella", "basil"], "Italian"))
    recipe_book.add_recipe(Recipe("Penne Alfredo", ["penne", "cream", "parmesan", "butter"], "Italian", ["pasta", "alfredo"]))
    recipe_book.add_recipe(Recipe("Lasagna", ["pasta", "ricotta", "ground beef", "tomato sauce"], "Italian", ["pasta", "beef", "cheese"]))

    # Mexican Cuisine
    recipe_book.add_recipe(Recipe("Tacos", ["tortilla", "beef", "lettuce", "cheese", "salsa"], "Mexican", ["taco"]))
    recipe_book.add_recipe(Recipe("Guacamole", ["avocado", "onion", "tomato", "lime"], "Mexican"))
    recipe_book.add_recipe(Recipe("Enchiladas", ["tortilla", "chicken", "cheese", "enchilada sauce"], "Mexican"))
    recipe_book.add_recipe(Recipe("Burritos", ["tortilla", "rice", "beans", "meat", "cheese"], "Mexican"))

    # American Cuisine
    recipe_book.add_recipe(Recipe("Pancakes", ["flour", "milk", "eggs", "butter", "syrup"], "American", ["pancake"]))
    recipe_book.add_recipe(Recipe("Burger", ["bun", "beef patty", "lettuce", "tomato", "cheese"], "American", ["cheeseburger", "hamburger"]))
    recipe_book.add_recipe(Recipe("Grilled Cheese Sandwich", ["bread", "cheese", "butter"], "American", ["grilled cheese"]))

    print("Welcome to the Recipe Finder!")
    print("Enter a recipe name, an ingredient, a cuisine type, or 'all' to list all recipes.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Search: ").strip()
        if query.lower() == "exit":
            print("Goodbye!")
            break

        if query.lower() == "all":
            print("\nAll Recipes:\n")
            print(recipe_book)
            continue

        # Search by name or alias
        recipe_by_name = recipe_book.find_by_name(query)
        if recipe_by_name:
            print("\nRecipe Found:\n")
            print(recipe_by_name)
            continue

        # Search by ingredient
        recipes_by_ingredient = recipe_book.search_by_ingredient(query)
        if recipes_by_ingredient:
            print("\nRecipes with Ingredient:\n")
            for recipe in recipes_by_ingredient:
                print(recipe)
                print()
            continue

        # Search by cuisine
        recipes_by_cuisine = recipe_book.search_by_cuisine(query)
        if recipes_by_cuisine:
            print("\nRecipes with Cuisine:\n")
            for recipe in recipes_by_cuisine:
                print(recipe)
                print()
            continue

        # Handle no matches
        print("\nNo recipes found. Did you mean something else?\n")


# Run the interactive search
if __name__ == "__main__":
    interactive_recipe_search()
