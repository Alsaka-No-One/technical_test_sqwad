from flask import Flask, request

app = Flask(__name__)

from shopify import is_shopify_shop

@app.route('/')
def root():
    return "Hello World!"

@app.route('/is_shopify/')
def is_shopify():
    url = request.args.get('link')
    answer = is_shopify_shop(url)
    if answer == True:
        return "True"
    return "False"