from flask import Flask, render_template, request, session, redirect

from test import idpw_ck
import adb

app = Flask(__name__)

# 세션처리를 위한 키
app.secret_key = b'aaa!111/'

@app.route('/')
def hello():
    return render_template('main.html')

@app.route('/military')
def military():
    return render_template('military.html')

@app.route('/tt')
def tt():
    return render_template('tt.html')

@app.route('/tf')
def tf():
    return render_template('tf.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/to')
def to():
    return render_template('to.html')
@app.route('/traver')
def traver():
    return render_template('traver.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    else:
        name = request.form['username']
        userid = request.form['userid']
        pwd = request.form['pwd']
        # 회원정보를 데이터베이스에 넣기
        adb.insert_user(userid, name, pwd)
        return render_template('register.html')
     
        

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == "GET":
        return render_template('signin.html')
    else:
        userid = request.form['userid']
        pwd = request.form['pwd']
        # 로그인이 맞는 체크해서 데이터가 있으면 성공 없으면 실패
        ret = adb.get_user(userid, pwd)
        if ret != None:
            print(ret[1])
            session['name'] = ret[1]  # 세션에 정보 넣기
            return redirect('/to')
        else:
            return redirect('/signin')
        # return idpw_ck(userid, pwd)

@app.route('/logout')
def logout():
    session.pop('name', None)
    return redirect('/main.html')


@app.route('/action', methods=['GET', 'POST'])
def action():
    if request.method == "GET":
        return '그냥 넘어옴(GET)'
    else:
        name = request.form['fname']
        return '<b>{}</b> 로 검색한 결과입니다. 리스트 쫙~~(POST)'.format(name)

# 축구페이지

# 배구페이지
# 농구페이지

if __name__ == '__main__':
    app.run(debug=True)