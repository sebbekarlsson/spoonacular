# spoonacular recepie python port
> Get recepies by ingridients

## Usage
> To get recepies by ingridients:

    from spoonacular import Spoonacular


    spoon = Spoonacular()


    recepies = spoon.get_recepies_by_ingridients([
        '4 carrots',
        '1kg potatoes',
        '1kg salt',
        '20 grams of curry',
        '1kg pasta'
    ])

> This will return a list of objects looking like this:

    [
        {
           "id": id-of-recepie,
           "name": name-of-recepie,
           "link": link-to-recepie,
           "info": "Uses 4, misses 2"
        }
    ]
