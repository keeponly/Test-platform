# _*_coding: utf-8 _*_
# @Time     :2020/10/30  11:05
# @Author   :wangkai
# @tel      :153139292711
# @ File    :flask-44.py 

from flask import Flask, request
from flask.views import View
app = Flask(__name__)

class MyView(View):
    methods = ['GET','POST']

    def dispatch_request(self):
        return 'Hello {}!'.format(request.methods)


app.add_url_rule('/hello/<name>', view_func=MyView.as_view('user'))
if __name__ == '__main__':
    app.run()