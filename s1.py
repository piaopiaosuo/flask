from collections import namedtuple

from flask import Flask, render_template, request, redirect, session, url_for, views, make_response, abort, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# 直接写
# app.debug = True
# app.secret_key = "abcdefg"
# app.config['DEBUG'] = False


# 通过文件导入配置
# app.config.from_pyfile('settings.py')

# 通过object导入
app.config.from_object("settings.DevelopmentConfig")
print(app.config)

USERS = {
    1: {'name': "加小心", 'age': 18, 'gender': '男',
        'text': "程序员客栈中国非常领先的自由工作平台，为中高端程序员、产品经理和设计师等等互联网相关人员提供稳定的线上工作机会，包括自由工作、远程工作和兼职工作，还支持按需雇佣，工作模式非常多，感兴趣的推荐大家尝试一下。虽然名称叫程序员客栈，但是除了程序员，像产品经理，设计师等等互联网相关人员，都能在上面找到适合自己的项目。感兴趣的可以体验一下"},
    2: {'name': "王佳敏", 'age': 19, 'gender': '女',
        "text": "开发邦，互联网1软件外包服务平台，十年互联网软件技术开发经验，成功执行近百个项目，专业从事软件外包开发，软件定制开发，互联网系统开发，APP开发，微信开发，团队核心成员均具有十年以上软件互联网技术开发经验，毕业于工科名校，先后为华为公司、商汤科技、工信部中国软件评测中心、神州数码、深鉴科技、中软集团、中国万网、中石油吐哈气举中心"}
}


@app.route('/detail/<int:nid>', methods=['GET', ])
def detail(nid):
    # if not session.get('user_info'):
    #     url = url_for('li')
    #     return redirect(url)
    # return redirect('/login')
    return USERS[nid]


@app.route('/index', methods=['GET', 'POST'], defaults={'aaa': 123, 'bbb': 456}, strict_slashes=True,
           # redirect_to='http://www.baidu.com'
           )
def index(aaa, bbb):
    print(aaa)
    print(bbb)
    app.logger.warning('A value for debugging')

    if not session.get('user_info'):
        return redirect('/login')
    return USERS


@app.route('/login', methods=['GET', 'POST'], endpoint="li")
def login():
    print(vars(request))
    if request.method == "GET":
        # abort(404)
        res = make_response({'data': 123}, 200)

        # print('username' in session)
        # session.pop('username', None)
        # session['user'] = '123'
        # res.status = 203
        res.headers['X-Something'] = 'A value'
        return res
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        session['user_info'] = 'alex'
        if user == 'alex' and pwd == "123":
            return redirect('/index')
        return render_template('login.html', error="用户名或密码错误")
    # return 'Hello World!'


# app.add_url_rule('/login', 'li', login, methods=['GET', 'POST'])

# print("login.__name__", login.__name__)


class IndexView(views.MethodView):
    methods = ['GET', 'POST']

    def get(self):
        print(request)
        return 'index.get'

    def post(self):
        return 'index.post'


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']

        print(f.filename)
        print(secure_filename(f.filename))

        f.save('./uploaded_file.png')
        return "上传成功"


@app.route('/set-cookie')
def set_cookie():
    resp = make_response("这是一个设置cookie")
    # username = request.cookies.get('username')  # 读取cookie
    # print(username)
    resp.set_cookie('username', 'the username')  # 设置cookie
    return resp


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


User = namedtuple('User', ['username', 'theme', 'image'])


@app.route("/me")
def me_api():
    user = User._make(['xiaoxin', 'blue, dark', 'haha'])
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("li", filename=user.image),
    }


@app.route("/users")
def users_api():
    users = [User._make(['xiaoxin', 'blue, dark', 'haha']), User._make(['xiaoxin1', 'blue, dark', 'haha1'])]
    return jsonify([user for user in users])


app.add_url_rule('/cbv-index', view_func=IndexView.as_view(name='cbv_index'))  # name = endpoint

if __name__ == '__main__':
    app.run()
