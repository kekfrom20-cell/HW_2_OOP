import pytest
from Hw.Ingredient import Ingredient
from Hw.Recipe import Recipe
from Hw.ShoppingList import ShoppingList


def test_add_recipe():
    recipe = Recipe("Пицца", [Ingredient("Мука", 500, "г")])

    sl = ShoppingList()
    sl.add_recipe(recipe, 2)

    result = sl.get_list()

    assert len(result) == 1
    assert result[0].quantity == 1000.0


def test_add_invalid_portions():
    sl = ShoppingList()
    recipe = Recipe("Пицца")

    with pytest.raises(ValueError):
        sl.add_recipe(recipe, 0)


def test_remove_recipe():
    r1 = Recipe("Пицца", [Ingredient("Мука", 500, "г")])
    r2 = Recipe("Паста", [Ingredient("Сыр", 200, "г")])

    sl = ShoppingList()

    sl.add_recipe(r1, 1)
    sl.add_recipe(r2, 1)

    sl.remove_recipe("Пицца")

    result = sl.get_list()

    assert all(i.name != "Мука" for i in result)


def test_merge_same_ingredients():
    r1 = Recipe("Пицца", [Ingredient("Мука", 500, "г")])
    r2 = Recipe("Хлеб", [Ingredient("Мука", 300, "г")])

    sl = ShoppingList()

    sl.add_recipe(r1, 1)
    sl.add_recipe(r2, 1)

    result = sl.get_list()

    assert len(result) == 1
    assert result[0].quantity == 800.0


def test_add_operator():
    r1 = Recipe("Пицца", [Ingredient("Мука", 500, "г")])
    r2 = Recipe("Паста", [Ingredient("Сыр", 200, "г")])

    sl1 = ShoppingList()
    sl2 = ShoppingList()

    sl1.add_recipe(r1, 1)
    sl2.add_recipe(r2, 1)

    sl3 = sl1 + sl2

    assert len(sl3.get_list()) == 2
    assert len(sl1.get_list()) == 1