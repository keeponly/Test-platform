# @Time     :2020/12/14  19:45
# @Author   :wang-kai
# @tel      :15313929271
# @File    :flask_44可插拔试图01.py

from flask import Flask, request
from flask.views import View

app = Flask(__name__)


class User_View(View):
    mtthods = ['GET', 'POST']

    def get(self):
        return 'get'

    def post(self):
        return 'post'

    def dispatch_request(self):  # 分配请求,固定写法
        dispath_patten = {'GET': self.get, 'POST': self.post}
        method = request.method
        return dispath_patten.get(method)()


app.add_url_rule('/', view_func=User_View.as_view('user'),
                 methods=['GET', 'POST'])
if __name__ == '__main__':
    app.run(debug=True)





