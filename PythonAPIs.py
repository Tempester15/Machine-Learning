import requests
import pandas as pd

url = 'https://pokeapi.co/api/v2/pokemon/ditto'
data = requests.get(url)

print(pd.json_normalize(data.json()))

