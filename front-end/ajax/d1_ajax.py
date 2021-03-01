# @Time     :2021/3/1  22:12
# @Author   :wang-kai
# @tel      :15313929271
# @File    :d1_ajax.py

from flask import Flask, request, render_template

app = Flask(__name__,
            template_folder=r'D:\Test-platform\front-end\ajax'
            )


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return '成功'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    file = request.files.get('pic')
    if file is None:
        return render_template('index.html')
    file.save(file.filename)
    return 'save success'


app.run(debug=True)
