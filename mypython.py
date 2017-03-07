# coding: utf-8
from flask import Flask

app = Flask(__name__)
aa='/why'

@app.route('/')
def hello_world():
    return '问题比较多，你好世界 !'

@app.route(aa)
def why():
    return '你好 !'

if __name__ == '__main__':
    app.run()
