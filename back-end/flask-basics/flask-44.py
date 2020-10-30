# _*_coding: utf-8 _*_
# @Time     :2020/10/30  11:05
# @Author   :wangkai
# @tel      :153139292711
# @ File    :flask-44.py 

from flask import Flask
from flask.views import View
app = Flask(__name__)

class MyView(View):
    methods = ['GET']

    def dispatch_request(self, name):
        return 'Hello %s!' % name


app.add_url_rule('/hello/<name>', view_func=MyView.as_view('myview'))
if __name__ == '__main__':
    app.run()