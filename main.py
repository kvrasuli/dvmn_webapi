import requests
cities = ['Лондон', 'Череповец', 'Шереметьево']
settings = {'n': '', 'T': '', 'q': '', 'm': '', 'lang': 'ru'}
url_template = 'https://wttr.in/{}'
for city in cities:
  response = requests.get(url_template.format(city), settings)
  print(response.text)