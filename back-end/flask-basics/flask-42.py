# _*_coding: utf-8 _*_
# @Time     :2020/10/22  16:46
# @Author   :wangkai
# @tel      :153139292711
# @ File    :flask-42.py 

from flask import Flask, request, render_template, config
from project_path import html_path, css_path
app = Flask(__name__,
            template_folder=html_path,
            static_folder=css_path)
@app.route('/')
app.run(debug=True)