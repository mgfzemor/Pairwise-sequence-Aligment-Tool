from flask import Flask
from flask import render_template
from flask import request
from needleman_wunsch import *
app = Flask(__name__)

DEBUG = True

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    ret = False
    if request.method == 'POST':
        m = request.form['m']
        n = request.form['n']
        match = request.form['match']
        mismatch = request.form['mismatch']
        indel = request.form['indel']
        sep, AlignA, AlignB, F, id, score = needleman_wunsch(m,n,match,mismatch,indel)
        ret = True
        return render_template('index.html',ret=ret, sep=sep, AlignA=AlignA, AlignB=AlignB, F=F, id=id, score=score)
    else:
        return render_template('index.html')
