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
        return (
            f"Recipe: {self.name}\n"
            f"Cuisine: {self.cuisine}\n"
            f"Ingredients: {ingredients_str}\n"
            f"Instructions: {self.instructions}\n"
        )


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
        Search for recipes that contain specific ingredients.
        If multiple ingredients are provided, return recipes that match all of them.
        """
        if isinstance(ingredients, str):
            ingredients = [ingredients]

        ingredients = set(map(str.lower, ingredients))
        return [
            recipe
            for recipe in self.recipes
            if ingredients.issubset(map(str.lower, recipe.ingredients))
        ]

    def search_by_cuisine(self, cuisine):
        """
        Search for recipes by cuisine type.
        """
        return [
            recipe for recipe in self.recipes if recipe.cuisine.lower() == cuisine.lower()
        ]

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


def interactive_recipe_search():
    # Create a RecipeBook and add recipes
    recipe_book = RecipeBook()

    # Instructions Example
    breakfast_taco_instruction = (
        "Cook the bacon in the oven for 18 to 20 minutes.\n"
        "Saute the green onions with olive oil.\n"
        "Whisk the eggs and pour them into the pan. Stir gently as they cook to create a pillowy texture.\n"
        "Time to assemble: Add scrambled eggs to a tortilla, top with green onion, crumbled bacon, and cheese."
    )

    # Italian Cuisine
    recipe_book.add_recipe(
        Recipe("Spaghetti Carbonara", ["spaghetti", "eggs", "bacon", "parmesan"], "Italian")
    )
    recipe_book.add_recipe(
        Recipe("Margherita Pizza", ["dough", "tomato", "mozzarella", "basil"], "Italian")
    )

    # Mexican Cuisine
    recipe_book.add_recipe(
        Recipe(
            "Breakfast Tacos",
            ["tortilla", "bacon", "eggs", "cheese", "salsa"],
            "Mexican",
            instructions=breakfast_taco_instruction,
        )
    )

    # User Interaction
    print("Welcome to the Recipe Finder!")
    print("Enter a query in the format 'type:query' or 'all' to list all recipes.")
    print("Types: name, ingredient, cuisine. Example: 'ingredient:bacon'.")
    print("Type 'add' to add a new recipe or 'exit' to quit.\n")

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
            print("\nAdding a new recipe...")
            name = input("Recipe Name: ").strip()
            ingredients = input("Ingredients (comma-separated): ").strip().split(",")
            cuisine = input("Cuisine: ").strip()
            aliases = input("Aliases (comma-separated, optional): ").strip().split(",")
            instructions = input("Instructions (optional): ").strip()

            recipe_book.add_recipe(
                Recipe(
                    name,
                    [ingredient.strip() for ingredient in ingredients],
                    cuisine,
                    [alias.strip() for alias in aliases if alias.strip()],
                    instructions=instructions or None,
                )
            )
            print(f"\nRecipe '{name}' added successfully!\n")
            continue

        try:
            search_type, search_query = query.split(":", 1)
            search_query = search_query.strip()

            if search_type.lower() == "name":
                results = recipe_book.find_by_name(search_query)
            elif search_type.lower() == "ingredient":
                results = recipe_book.search_by_ingredient(search_query.split(","))
            elif search_type.lower() == "cuisine":
                results = recipe_book.search_by_cuisine(search_query)
            else:
                print("Invalid search type. Use 'name', 'ingredient', or 'cuisine'.")
                continue

            if results:
                print("\nRecipes Found:\n")
                for recipe in results:
                    print(recipe)
                    print()
            else:
                print("\nNo recipes found.\n")

        except ValueError:
            print("Invalid input format. Use 'type:query' or 'all'.")


# Run the interactive search
if __name__ == "__main__":
    interactive_recipe_search()
