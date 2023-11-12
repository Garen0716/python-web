from flask import Flask
from flask import Flask, render_template,request
from waitress import serve
app = Flask(__name__)


@app.route("/")
def index():
    homepage = "<h1>楊子青Python網頁</h1>"
    homepage += "<a href=/web>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    return homepage
   

@app.route("/web")
def web():
    return render_template("web.html")
@app.route("/work")
def work():
    return render_template("work.html",title="work")



# @app.route("/")
# def web():
#     return render_template("web.html")

# @app.route("/work")
# def main():
#     return render_template('work.html')
# if __name__ == "__main__":
#     serve(app, host="0.0.0.0", port=8080)   

# app.run()