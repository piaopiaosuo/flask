from flask import Flask, render_template, request, redirect

print(__name__)
app = Flask(__name__)

USERS = {
    1: {'name': "加小心", 'age': 18, 'gender': '男',
        'text': "程序员客栈中国非常领先的自由工作平台，为中高端程序员、产品经理和设计师等等互联网相关人员提供稳定的线上工作机会，包括自由工作、远程工作和兼职工作，还支持按需雇佣，工作模式非常多，感兴趣的推荐大家尝试一下。虽然名称叫程序员客栈，但是除了程序员，像产品经理，设计师等等互联网相关人员，都能在上面找到适合自己的项目。感兴趣的可以体验一下"},
    2: {'name': "王佳敏", 'age': 19, 'gender': '女',
        "text": "开发邦，互联网软件外包服务平台，十年互联网软件技术开发经验，成功执行近百个项目，专业从事软件外包开发，软件定制开发，互联网系统开发，APP开发，微信开发，团队核心成员均具有十年以上软件互联网技术开发经验，毕业于工科名校，先后为华为公司、商汤科技、工信部中国软件评测中心、神州数码、深鉴科技、中软集团、中国万网、中石油吐哈气举中心"}
}


@app.route('/detail/<int:nid>', methods=['GET', ])
def detail(nid):
    return USERS[nid]


@app.route('/index', methods=['GET', 'POST'])
def index():
    return USERS


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'alex' and pwd == "123":
            return redirect('/index')
        return render_template('login.html', error="用户名或密码错误")
    # return 'Hello World!'


if __name__ == '__main__':
    app.run()
