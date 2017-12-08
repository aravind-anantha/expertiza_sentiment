from flask import Flask, render_template, request, jsonify, redirect
from flask_api import status
from nltk.tokenize import sent_tokenize
from SOCAL import SOCAL
import logging
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)


def get_hsl(val):
    value = float(val)
    H = value*10 + 60
    S = 80
    L = 35

    if value > 4:
    	H = 100
    if value < -6:
    	H = 0
    return "hsl(" + str(H) + ", " + str(S) + "%, " + str(L) + "%)"


@app.route('/', methods=['GET'])
def index():
	return redirect('sentiment')


@app.route('/sentiment', methods=['GET'])
def sentiment():
    return render_template("sentiment.html")


@app.route('/visualize_sentiment', methods=['GET', 'POST'])
def visualize_sentiment():
    if request.method == 'GET':
        review = request.args.get('review')
    elif request.method == 'POST':
        review = request.json['review']

    temp = ''
    out = ''
    sentiment = SOCAL()
    if review != '':
        sentences = sent_tokenize(review)
        for sentence in sentences:
        	temp = sentiment.so_cal_run(str(sentence))
        	sentence = sentence.replace(sentence, '<font style="color:' + get_hsl(temp) + ';">' + sentence + '</font>')
        	print sentence
        	out += sentence + ' '
 

    return out, status.HTTP_200_OK




if __name__ == '__main__':
    app.run()