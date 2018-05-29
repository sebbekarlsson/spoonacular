from spoonacular import Spoonacular


spoon = Spoonacular()


def test_get_recepies_by_ingridients():
    recepies = spoon.get_recepies_by_ingridients([
        '4 carrots',
        '1kg potatoes',
        '1kg salt',
        '20 grams of curry',
        '1kg pasta'
    ])

    assert isinstance(recepies, list)
    assert len(recepies) > 0
