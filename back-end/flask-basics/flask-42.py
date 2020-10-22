# _*_coding: utf-8 _*_
# @Time     :2020/10/22  16:46
# @Author   :wangkai
# @tel      :153139292711
# @ File    :flask-42.py 

from flask import Flask, request, render_template, config


app = Flask(__name__)


@app.route('/case')
def index():
    id= request.args.get('id')  # 地址问号后面的
    return f'{id}' # f相当于format


if __name__ == '__main__':

    app.run(debug=True)