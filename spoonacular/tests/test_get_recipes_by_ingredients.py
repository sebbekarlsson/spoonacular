from spoonacular import Spoonacular


spoon = Spoonacular()


def test_get_recipes_by_ingridients():
    recipes = spoon.get_recipes_by_ingredients([
        '4 carrots',
        '1kg potatoes',
        '1kg salt',
        '20 grams of curry',
        '1kg pasta'
    ])

    assert isinstance(recipes, list)
    assert len(recipes) > 0
