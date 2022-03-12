

from flask import Flask,render_template
import config

app = Flask(__name__)
app.config.from_object(config) # 加载配置文件
# app.config['JSON_AS_ASCII']=False #不转码，保证汉字正常显示

@app.route('/')
def helloword():
    # return  "hello,world2! 你好"
    return {"username":"知乎1"}

@app.route('/about')
def about():
    return render_template("about.html")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# redirect(url_for("index")) 重定向，指定到url_for指定的指定方法的路径
