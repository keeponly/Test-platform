# @Time     :2020/12/14  20:54
# @Author   :wang-kai
# @tel      :15313929271
# @File    :flask_44可插拔试图02.py

from flask import Flask, request
from flask.views import MethodView

app = Flask(__name__)


class projectview(MethodView):

    def get (self):
        return 'get'

    def post(self):
        return 'post'


app.add_url_rule('/', view_func=projectview.as_view('project_view'))
if __name__ == '__main__':
    app.run(debug=True)

