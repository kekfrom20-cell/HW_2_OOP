from Hw.Ingredient import Ingredient


class Recipe:
    def __init__(self, title, ingredients=None):
        self.title = title
        self.ingredients = ingredients if ingredients else []

    def add_ingredient(self, ingredient):
        for existing in self.ingredients:
            if existing == ingredient:
                existing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0

    def scale(self, ratio):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Некорректный коэффициент")

        new_ingredients = [
            Ingredient(
                ingredient.name,
                ingredient.quantity * ratio,
                ingredient.unit
            )
            for ingredient in self.ingredients
        ]

        return Recipe(self.title, new_ingredients)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        ingredients_text = "\n".join(
            str(ingredient) for ingredient in self.ingredients
        )
        return f"{self.title}\n{ingredients_text}"