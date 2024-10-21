from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'hello'


if __name__ == "__main__":
    app.run(port=3000,debug=True)


     