import pytest

from Hw.Ingredient import Ingredient
from Hw.Recipe import Recipe
from Hw.ShoppingList import ShoppingList


# =========================
# Ingredient
# =========================

def test_ingredient_creation():
    i = Ingredient("Мука", 500, "г")

    assert i.name == "Мука"
    assert i.quantity == 500.0
    assert i.unit == "г"


def test_ingredient_str():
    i = Ingredient("Мука", 500, "г")

    assert str(i) == "Мука: 500.0 г"


def test_ingredient_eq():
    a = Ingredient("Мука", 500, "г")
    b = Ingredient("Мука", 200, "г")
    c = Ingredient("Сахар", 500, "г")
    d = Ingredient("Мука", 500, "кг")

    assert a == b
    assert a != c
    assert a != d


# =========================
# Recipe
# =========================

def test_recipe_creation():
    i = Ingredient("Мука", 500, "г")
    r = Recipe("Пицца", [i])

    assert r.title == "Пицца"
    assert r.ingredients == [i]


def test_add_ingredient():
    r = Recipe("Пицца")

    r.add_ingredient(Ingredient("Мука", 500, "г"))
    r.add_ingredient(Ingredient("Мука", 200, "г"))

    assert len(r.ingredients) == 1
    assert r.ingredients[0].quantity == 700.0


def test_scale_creates_new_object():
    r = Recipe("Пицца", [Ingredient("Мука", 500, "г")])

    scaled = r.scale(2)

    assert scaled is not r
    assert scaled.ingredients[0].quantity == 1000.0
    assert r.ingredients[0].quantity == 500.0


def test_scale_invalid():
    r = Recipe("Пицца")

    with pytest.raises(ValueError):
        r.scale(0)


def test_len_recipe():
    r = Recipe(
        "Пицца",
        [
            Ingredient("Мука", 500, "г"),
            Ingredient("Сыр", 200, "г"),
        ]
    )

    assert len(r) == 2


# =========================
# ShoppingList
# =========================

def test_add_recipe():
    r = Recipe("Пицца", [Ingredient("Мука", 500, "г")])

    sl = ShoppingList()
    sl.add_recipe(r, 2)

    result = sl.get_list()

    assert len(result) == 1
    assert result[0].quantity == 1000.0


def test_add_recipe_invalid_portions():
    sl = ShoppingList()
    r = Recipe("Пицца")

    with pytest.raises(ValueError):
        sl.add_recipe(r, 0)


def test_remove_recipe():
    r1 = Recipe("Пицца", [Ingredient("Мука", 500, "г")])
    r2 = Recipe("Паста", [Ingredient("Сыр", 200, "г")])

    sl = ShoppingList()

    sl.add_recipe(r1, 1)
    sl.add_recipe(r2, 1)

    sl.remove_recipe("Пицца")

    result = sl.get_list()

    assert all(i.name != "Мука" for i in result)


def test_remove_non_existing():
    sl = ShoppingList()

    sl.remove_recipe("Несуществующий")  # не должно падать

    assert sl.get_list() == []


def test_get_list_sums_same_ingredients():
    r1 = Recipe("Пицца", [Ingredient("Мука", 500, "г")])
    r2 = Recipe("Хлеб", [Ingredient("Мука", 300, "г")])

    sl = ShoppingList()
    sl.add_recipe(r1, 1)
    sl.add_recipe(r2, 1)

    result = sl.get_list()

    assert len(result) == 1
    assert result[0].quantity == 800.0


def test_get_list_sorted():
    r = Recipe(
        "Тест",
        [
            Ingredient("Яйца", 2, "шт"),
            Ingredient("Банан", 1, "шт"),
            Ingredient("Мука", 500, "г"),
        ]
    )

    sl = ShoppingList()
    sl.add_recipe(r, 1)

    result = sl.get_list()

    names = [i.name for i in result]

    assert names == sorted(names)


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
    assert len(sl2.get_list()) == 1