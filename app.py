from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename

import utils


app = Flask(__name__, static_url_path='/static')

app.debug = True


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/data", methods=['POST'])
def process():
    data = dict(request.form)
    post_url = data['post']
    flair = utils.get_flair(post_url)
    return {
        'flair': flair
    }

    # try:
    #     flair = utils.get_flair(post_url)
    # except:
    #     return {'error':'Something went wrong! Make sure the URL is valid'}
    # return {
    #     'flair': flair
    # }



@app.route("/automated_testing", methods=['POST'])
def automated_testing_handler():
    file = dict(request.files)
    value = file[list(file.keys())[0]].read()
    value = value.decode().split('\n')
    value = list(filter(None, value))
    print(value)
    func = utils.get_flair
    resp = {}
    for i in value:
        resp[i] = func(i)
    return jsonify(resp)

if __name__ == "__main__":
    app.run(port=5555)
