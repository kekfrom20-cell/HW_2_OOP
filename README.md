# Recipe Manager (OOP Project)

## Описание проекта

Проект представляет собой систему управления рецептами, разработанную с использованием объектно-ориентированного программирования (OOP).

Функциональность:
- создание и хранение ингредиентов
- формирование рецептов
- объединение одинаковых ингредиентов
- масштабирование рецептов
- генерация списка покупок
- работа с диетическими рецептами

---

## Структура проекта

Hw/
├── Ingredient.py       # класс Ingredient
├── Recipe.py           # класс Recipe
├── ShoppingList.py     # класс ShoppingList
├── DietaryRecipe.py    # наследник Recipe

tests/
└── test_recipes.py     # pytest тесты

---

## Установка и запуск проекта

### 1. Клонирование репозитория

git clone <ссылка_на_репозиторий>
cd HW_2_OOP

### 2. Создание виртуального окружения (рекомендуется)

python -m venv venv

Активировать:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 3. Установка зависимостей

pip install -r requirements.txt

---


## Запуск проекта

Проект является библиотекой классов (консольного интерфейса нет).

Пример использования:

python
from Hw.Ingredient import Ingredient
from Hw.Recipe import Recipe
from Hw.ShoppingList import ShoppingList

# создаём ингредиенты
flour = Ingredient("Мука", 500, "г")
cheese = Ingredient("Сыр", 200, "г")

# создаём рецепт
pizza = Recipe("Пицца", [flour, cheese])

# масштабируем рецепт
big_pizza = pizza.scale(2)

# список покупок
sl = ShoppingList()
sl.add_recipe(pizza, 2)
print(sl.get_list())

---

## Запуск тестов

pytest

Если есть проблемы с импортами:

PYTHONPATH=. pytest

---

## Тестирование

Тесты проверяют:
- создание объектов
- работу методов классов
- объединение ингредиентов
- масштабирование рецептов
- работу списка покупок
- обработку ошибок

---

## Автор

Кузина Екатерина Константиновна  ББИ2501