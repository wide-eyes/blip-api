from flask import Flask, json, make_response
import random
import requests
from requests import Response

app = Flask(__name__)

random.seed()

blips_url = 'https://raw.githubusercontent.com/wide-eyes/blip/master/blips.txt'

def load_blips():
    res = requests.get(blips_url)
    if res.status_code == 200:
        return [blip for blip in res.text.split('\n') if blip != '']
    else:
        return None

app.blips = load_blips()

@app.route('/blip')
def get_blip():
    if len(app.blips) > 0:
        return json.dumps({ 'author': 'tsujeeth', 'text': random.choice(app.blips) })
    else:
        return json.dumps({})

@app.route('/update')
def update_blips():
    new_blips = load_blips()
    if new_blips:
        app.blips = new_blips
        return make_response(), 200
    else:
        return make_response(), 500

if __name__ == "__main__":
    app.run(debug=True)
