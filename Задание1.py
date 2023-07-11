import requests
import json

heroes_list = ['Hulk', 'Captain America', 'Thanos']
intelligence = []
url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'

hero_dict = json.loads(requests.get(url).content)

for name in heroes_list:
    for hero in hero_dict:
        if hero['name'] == name:
            intelligence.append(hero['powerstats']['intelligence'])

heroes_intelligence = dict(sorted(zip(heroes_list, intelligence)))

x = list(heroes_intelligence.items())
print(f'Самым умным супергероем является {x[-1]}')