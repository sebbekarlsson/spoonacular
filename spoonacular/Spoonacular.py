from requests import Session
from bs4 import BeautifulSoup
from urlparse import urljoin
import re


class Spoonacular(object):

    def __init__(self):
        self.session = Session()
        self.website = 'https://spoonacular.com'
        self.base_url = self.website + '/search'

    def get_recipes_by_ingredients(self, ingredients):
        endpoint = self.base_url + '/findByIngredients'

        items = []

        data = {
            'ingredientList': '\n'.join(ingredients),
            'number': 25,
            'ranking': 1,
            'onlyOpenLicense': False
        }

        response = self.session.post(endpoint, data=data)

        soup = BeautifulSoup(response.text, 'html.parser')

        _items = soup.find_all('div', {'class': 'recipePreviewBox'})

        for _item in _items:
            item = {}
            item['id'] = _item.find('div', {'class': 'recipeId'}).text
            item['name'] = _item.find('h4').text
            item['link'] = urljoin(self.website, _item.find('a').get('href'))
            item['info'] = _item.find('span').text
            item['image'] = _item.find('div', {'class': 'img'}).get('style')
            item['image'] = re.findall('url.*?\((.*?)\)', item['image'])
            item['image'] = item['image'][0] if item['image'] else None

            items.append(item)

        return items
