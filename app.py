from flask import Flask, render_template
from flask.globals import request
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('main.html')

@app.route('/baseball')
def baseball():
    return render_template('baseball.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/action', methods=['GET', 'POST'])
def action():
    if request.method == "GET":
        return '그냥 넘어옴(GET)'
    else:
        name = request.form['fname']
        return '<b>{}</b> 로 검색한 결과입니다. 리스트 쫙~~(POST)'.format(name)

# 축구페이지
@app.route('/football')
def football():
    return '''
    <html>
    <body>

    <h2>여기는 축구페이지</h2>
    <img src="https://post-phinf.pstatic.net/MjAxOTA0MTBfMSAg/MDAxNTU0OTA0MTU0OTUy.wbiyoTJa-UaWgue-EcZYcwWPDxjcAUO8UEjd-ZT3rsAg.Vmg-tfnQz59yfac-MIA3AdmQQupDTpCUYkMLHA-RVbYg.JPEG/%EC%86%90%ED%9D%A5%EB%AF%BC.jpg" alt="축구">

    </body>
    </html>
    '''
# 배구페이지
# 농구페이지

if __name__ == '__main__':
    app.run(debug=True)