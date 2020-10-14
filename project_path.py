# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 21:24
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : project_path.py
import os
# 文件的路径 放到这里
project_path = os.path.split(os.path.realpath(__file__))[0]
print(project_path)
# html的路径
html_path = os.path.join(project_path, 'front-end', 'templates')
# folder 路径
css_path = os.path.join(project_path, 'front-end', 'folder')
