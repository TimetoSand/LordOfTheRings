import json
import os
import random
import requests
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = os.environ.get('API_KEY')

endpoint = "https://the-one-api.dev/v2"
header = {
    "Authorization": f"Bearer {API_KEY}"
}
params = {
    "name": "Frodo Baggins"
}

img_urls = ['https://static0.srcdn.com/wordpress/wp-content/uploads/2020/07/The-Lord-of-the-Rings.jpg',
            'https://tse1.mm.bing.net/th/id/OIP.AFcQeuaINwUUDEC1T-lxugHaEo?pid=ImgDet&rs=1',
            'https://static1.srcdn.com/wordpress/wp-content/uploads/2020/11/Aragorn-Lord-of-the-rings-return-of'
            '-the-king-sequels.jpg',
            'https://images.alphacoders.com/817/81771.jpg',
            'https://www.cheatsheet.com/wp-content/uploads/2021/01/LOTR.jpg',
            'https://www.mmobomb.com/file/2011/02/The-Lord-of-the-Rings-Online-2.jpg',
            'https://www.hdwallpaper.nu/wp-content/uploads/2015/04/lord-of-the-rings-wallpaper-5.jpg',
            'https://i1.wp.com/twinfinite.net/wp-content/uploads/2020/03/legolas.jpg?w=1000&ssl=1',
            'https://wallpaperforu.com/wp-content/uploads/2021/03/Wallpaper-Green-Leafed-Tree-The-Lord-Of-The'
            '-Rings-The-Ho32-768x432.jpg',
            'https://www.indiewire.com/wp-content/uploads/2020/12/MCDLOOF_EC162.jpg',
            'http://igeekout.net/wp-content/uploads/2016/12/Lord-of-the-Rings-The-Races-of-Arda-pic-06-Elves'
            '-Elrond.jpg',
            'https://www.telegraph.co.uk/content/dam/tv/2017/11/08/lordofrings-xlarge_trans_NvBQzQNjv4Bq'
            '-pfgFGBz9L_4V5dRQnfCxd6yN5CV7Pul_xM_LGnPwu0.jpg',
            'https://i.pinimg.com/originals/0f/72/dd/0f72ddd9d6bd1d85bc79f116bbbabc7f.jpg']
img_url_list = random.sample(img_urls, 5)

response_quote = requests.get(f"{endpoint}/quote/", headers=header)
response_quote.raise_for_status()
data_quote = response_quote.json()
# print(data_quote)
# print("***********")

quotes = data_quote['docs']
gg = random.sample(quotes, 5)
character_ids = []
for i in range(len(gg)):
    character_ids.append(gg[i]['character'])

character_id = gg[0]['character']

the_quotes = []
for quote in gg:
    the_quotes.append(quote['dialog'])

# print(the_quotes)

dudes = []
for id_c in character_ids:
    response_character = requests.get(f"{endpoint}/character/{id_c}", headers=header)
    response_character.raise_for_status()
    data_c = response_character.text
    data_c = json.loads(data_c)
    dudes.append(data_c)

the_characters = []
for dude in dudes:
    character = dude['docs'][0]['name']
    the_characters.append(character)

# print(the_characters)

content_dict = {'quotes': the_quotes, 'characters': the_characters, 'img': img_url_list}


@app.route("/")
def home():
    return render_template("index.html", dict=content_dict)


if __name__ == "__main__":
    app.run(debug=True)
