from flask import Flask, render_template
from forms import LanguageForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwertyuiop'

@app.route('/', methods = ['GET', 'POST'])
def main():
    form = LanguageForm()
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug = True)