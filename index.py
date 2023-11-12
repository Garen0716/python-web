from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("autobiography.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/autobiography")
def autobiography():
    return render_template("autobiography.html")
# app.run()

# @app.route("/")
# def web():
#     return render_template("web.html")

# @app.route("/work")
# def main():
#     return render_template('work.html')


# @app.route('/')
# def index():
#    return render_template("about.html")
    
# app.run()

# @app.route("/index")
# def index():
#     return render_template("about.html")