from Hw.Recipe import Recipe
from Hw.Ingredient import Ingredient


class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError(
                "Количество порций должно быть положительным"
            )

        scaled_recipe = recipe.scale(portions)

        for ingredient in scaled_recipe.ingredients:
            self._items.append(
                (ingredient, recipe.title)
            )

    def remove_recipe(self, title):
        self._items = [
            item
            for item in self._items
            if item[1] != title
        ]

    def get_list(self):
        ingredients_dict = {}

        for ingredient, _ in self._items:
            key = (ingredient.name, ingredient.unit)

            if key in ingredients_dict:
                ingredients_dict[key] += ingredient.quantity
            else:
                ingredients_dict[key] = ingredient.quantity

        result = [
            Ingredient(name, quantity, unit)
            for (name, unit), quantity
            in ingredients_dict.items()
        ]

        result.sort(key=lambda x: x.name)

        return result

    def __add__(self, other):
        new_list = ShoppingList()

        new_list._items = (
            self._items.copy() +
            other._items.copy()
        )

        return new_list