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
    carbonara_instruction = (
        "\nBring a large pot of salted water to a boil. Cook the spaghetti until al dente.\n",
        "Dice the guanciale and cook it in a skillet over medium heat until crispy. Remove from heat and set aside.\n",
        "In a bowl, whisk together eggs, yolks, and Pecorino Romano cheese. Add freshly cracked black pepper.\n",
        "Drain the pasta, reserving some cooking water. Add the pasta to the skillet with guanciale.\n",
        "Off the heat, pour the egg mixture over the pasta and toss quickly to combine. Use reserved pasta water to adjust the sauce.\n",
        "Serve immediately with additional Pecorino Romano and black pepper."
    )
    margherita_instruction = (
 "\nPreheat the oven to its highest setting (usually 500°F/260°C) with a pizza stone inside.\n",
        "Roll out the pizza dough to your desired thickness.\n",
        "Spread crushed San Marzano tomatoes over the dough, leaving a border for the crust.\n",
        "Add slices of fresh mozzarella and drizzle olive oil on top\n.",
        "Bake on the preheated pizza stone for 7-10 minutes or until the crust is golden and the cheese is bubbling.\n",
        "Remove from the oven and immediately add fresh basil leaves. Serve hot."
    )
    alfredo_instruction = (
"\nBring a large pot of salted water to a boil and cook the fettuccine until al dente.\n",
        "In a skillet, melt butter over medium heat. Add garlic and sauté until fragrant.\n",
        "Add sliced chicken breast and cook until golden and cooked through. Remove and set aside.\n",
        "Lower the heat and add heavy cream to the skillet. Simmer gently, then stir in grated Parmesan cheese until smooth.\n",
        "Toss the cooked fettuccine in the sauce and add the chicken back in. Season with salt and pepper to taste.\n",
        "Serve hot with extra Parmesan cheese."
    )

    lasagna_instruction = (
   "\nPreheat the oven to 375°F (190°C).\n",
        "In a skillet, heat olive oil and sauté onions and garlic until softened. Add ground beef and cook until browned.\n",
        "Stir in tomato sauce, season with salt and pepper, and simmer for 10 minutes.\n",
        "In a bowl, mix ricotta cheese with grated Parmesan and chopped fresh basil.\n",
        "In a baking dish, layer tomato sauce, lasagna sheets, ricotta mixture, and shredded mozzarella.\n",
        "Repeat layers until ingredients are used up, ending with mozzarella.\n",
        "Cover with foil and bake for 25 minutes. Remove the foil and bake for an additional 15 minutes until the top is golden.\n",
        "Let rest for 10 minutes before serving."
    )

    burger_instruction = (
 "\nPreheat a grill or skillet over medium-high heat\n.",
        "Form ground beef into 4 equal patties, season with salt and pepper.\n",
        "Grill or cook patties for 3-4 minutes per side until desired doneness.\n",
        "Toast the buns on the grill or in a skillet.\n",
        "Assemble the burger with patties, lettuce, tomato, pickles, and condiments."
    )
apple_pie_instruction = (
  "\nToss apples with sugars, spices, and lemon juice.",
        "Thicken mixture with flour and cornstarch, then add to pie crust.",
        "Dot with butter, add top crust, brush with cream, and sprinkle with coarse sugar.",
        "Bake for 45-50 minutes. Cool before serving."
)
    # Sample Recipes
    
  # Italian Cuisine
    recipe_book.add_recipe(Recipe("Spaghetti Carbonara", ["spaghetti", "eggs", "guanciale", "romano cheese"], "Italian", ["pasta","ramano","carbonara","cheese", "spageti","carborna","italian food","egg"],carbonara_instruction))
    recipe_book.add_recipe(Recipe("Margherita Pizza", ["dough", "tomato", "mozzarella", "basil","olive oil"], "Italian",["cheese","pizza","piza","italian food"],margherita_instruction))
    recipe_book.add_recipe(Recipe("Chicken Alfredo",  ["fettuccine", "chicken breast", "butter", "heavy cream", "parmesan", "garlic"], "Italian", ["pasta", "alfredo","italian food"],alfredo_instuction))
    recipe_book.add_recipe(Recipe("Lasagna", ["lasagna sheets", "ground beef", "onion", "garlic", "tomato sauce", "ricotta", "mozzarella", "parmesan", "basil", "olive oil"], "Italian",["beef","cheese","tomato","italian food","oil","tomato"],lasagna_instruction))
    
    # Mexican Cuisine
    recipe_book.add_recipe(Recipe("Beef Tacos", ["tortilla", "beef", "lettuce", "cheese", "salsa"], "Mexican", ["taco","tacos with beef","taco with beef","mex","mexican food","tacos","beef taco"]))
    recipe_book.add_recipe(Recipe("Breakfast Tacos", ["tortilla", "bacon", "eggs", "cheese", "salsa"], "Mexican", ["taco","tacos","breakfast","mex","mexican food","breakfast taco"], breakfast_taco_instruction))
    recipe_book.add_recipe(Recipe("Pork Tacos", ["tortilla", "pork", "lettuce", "cheese", "salsa"], "Mexican", ["taco", "tacos with pork","taco with pork","pork taco","mex","mexican food","tacos"]))
    recipe_book.add_recipe(Recipe("Guacamole", ["avocado", "onion", "tomato", "lime"], "Mexican",["guac","mex","mexican food"]))
    recipe_book.add_recipe(Recipe("Enchiladas", ["tortilla", "chicken", "cheese", "enchilada sauce"], "Mexican",["mex","mexican food"]))
    recipe_book.add_recipe(Recipe("Burritos", ["tortilla", "rice", "beans", "meat", "cheese"], "Mexican",["mexican food","chicken","beef","mex"]))


    # American Cuisine
    recipe_book.add_recipe(Recipe("Pancakes", ["flour", "milk", "eggs", "butter", "syrup"], "American", ["pancake","egg","american","american food","breakfast food","breakfast"]))
    recipe_book.add_recipe(Recipe("Burger", ["burger buns", "ground beef", "lettuce (optional)", "tomato (optional)", "cheese (optional)","american"], "American", ["lettuce","tomato","cheese","cheeseburger","beef","cheese burger","a burger","hamburger","american","american food"]))
    recipe_book.add_recipe(Recipe("Apple Pie",["apples", "granulated sugar", "brown sugar", "lemon juice","cinnamon", "nutmeg", "ginger", "butter", "flour", "cornstarch", "heavy cream", "coarse sugar", "pie crusts"], "American",["dessert", "pie","american food"],apple_pie_instructions))

    
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
