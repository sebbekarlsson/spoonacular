from requests import Session
from bs4 import BeautifulSoup
from urlparse import urljoin


class Spoonacular(object):

    def __init__(self):
        self.session = Session()
        self.website = 'https://spoonacular.com'
        self.base_url = self.website + '/search'

    def get_recepies_by_ingridients(self, ingridients):
        endpoint = self.base_url + '/findByIngredients'

        items = []

        data = {
            'ingredientList': '\n'.join(ingridients),
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

            items.append(item)

        return items
