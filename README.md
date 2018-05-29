# spoonacular recipes python port
> Get recipes by ingridients

## Usage
> To get recipes by ingridients:

    from spoonacular import Spoonacular


    spoon = Spoonacular()


    recipes = spoon.get_recipes_by_ingridients([
        '4 carrots',
        '1kg potatoes',
        '1kg salt',
        '20 grams of curry',
        '1kg pasta'
    ])

> This will return a list of objects looking like this:

    [
        {
           "id": id-of-recipe,
           "name": name-of-recipe,
           "link": link-to-recipe,
           "info": "Uses 4, misses 2"
        }
    ]
