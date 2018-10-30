#coding: utf-8
from flask import Flask

app = Flask(__name__)

@app.route('/index/')
def index():
    return render_template('/templates/index.html')

if __name__ == '__main__':
    app.run(debug=True)

