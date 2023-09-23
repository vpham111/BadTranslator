from flask import Flask, render_template
from forms import LanguageForm
import requests, json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwertyuiop'

url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "419d19d013msha3631d5dc6f3895p1b17f6jsn672ae0cd4f78",
	"X-RapidAPI-Host": "rapid-translate-multi-traduction.p.rapidapi.com"
}


@app.route('/', methods = ['GET', 'POST'])
def main():
    form = LanguageForm()
    if form.is_submitted():
        in_lang = form.selectin.data
        text_in = form.textin.data
        out_lang = form.selectout.data
        print(in_lang, text_in, out_lang)
        payload = {
	        "from": f"{in_lang}",
	        "to": f"{out_lang}",
	        "q": f"{text_in}"
        }
        response = requests.post(url, json=payload, headers=headers)
        form.textout.data = response.json()[0]
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug = True)