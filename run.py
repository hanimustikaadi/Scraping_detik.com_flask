import requests
from bs4 import BeautifulSoup


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detik-populer')
def detik_populer():
    res = requests.get('https://www.detik.com/terpopuler')
    # print(res.status_code)
    soup = BeautifulSoup(res.text, 'html.parser')
    populer_area = soup.find(attrs={'class': 'grid-row list-content'})
    title = populer_area.findAll(attrs={'class': 'media__title'})
    images = populer_area.findAll(attrs={'class': 'media__image'})

    return render_template('index.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)


