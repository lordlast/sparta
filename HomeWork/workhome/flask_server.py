import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/') # get이 기본
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def saving():
    name = request.form['juname']
    count= request.form['jusu']
    adders = request.form['juaddres']
    number = request.form['junumber']

    # headers = {
       # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # data = requests.get(name, headers=headers)

    shop = {

        'name': name,
        'count': count,
        'adders': adders,
        'phone': number

    }

    db.shop.insert_one(shop)

    return jsonify({'result': 'success'})

@app.route('/post', methods=['GET'])
def listing():
    result = list(db.shop.find({}, {'_id': 0}))
    result.reverse()

    return jsonify({'result': 'success', 'shop': result})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)