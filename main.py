
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        marathi_text = request.form['marathi_text']
        # Implement translation logic here
        translated_text = "TRANSLATED_TEXT"
        return render_template('index.html', translated_text=translated_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
