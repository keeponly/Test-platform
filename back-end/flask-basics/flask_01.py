# @Time     :2020/9/22  13:13
# @Author   :wang-kai
# @tel      :15313929271
# @File     :flask_01
import flask
from flask import Flask, request, render_template
import os
path = os.getcwd()
print(path)
# app = Flask(__name__,
#             template_folder='D:\Test-platform\front-end\templates')
#
# # 添加路由
# @app.route('/')
# def index():
#     a = request
#     # 将请求参数存为字典
#     args = request.args
#     # 获取请求参数
#     name =args.get('username')
#     print(name)
#     return render_template('home_page.html')
#
#
# # 运行服务器
# app.run()