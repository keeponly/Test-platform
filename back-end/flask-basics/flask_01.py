# @Time     :2020/9/22  13:13
# @Author   :wang-kai
# @tel      :15313929271
# @File     :flask_01
import flask
from flask import Flask

app = Flask(__name__)


# 添加路由
@app.route('/')
def index():
    return 'hello'


# 运行服务器
app.run()