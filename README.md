# spoonacular recipes python port
> Get recipes by ingredients

## Usage
> To get recipes by ingredients:

    from spoonacular import Spoonacular


    spoon = Spoonacular()


    recipes = spoon.get_recipes_by_ingredients([
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
           "info": "Uses 4, misses 2",
           "image": link-to-image
        }
    ]

## Installation
> Clone down repository and run:

    python setup.py install

> OR through pip:

    pip install spoonacular
