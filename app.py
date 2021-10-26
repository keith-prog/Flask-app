from flask import Flask, request, render_template


import datetime

app = Flask(__name__)


@app.get("/")  # HTTP request : GET  /
def index():
    # return datetime.datetime.now().ctime()
    return render_template("index.html", title="Home", heading="Home")


@app.get("/hello")  # HTTP request  GET hello
def hello():
    return "Hello from my first Flask WebApp : it is your fault"


@app.get("/personal")
def personal():
    pass


@app.get("/CV")
def display_CV():

    return render_template("CV.html", heading="My CV",)


# @app.route("/Showform", methods["GET", "POST", "PUT", "DELETE"])


@app.get("/showform")
def display_form():
    return render_template("form.html", title="Welcome", heading="TellUs About yourself")
    """
    Retreive the form.html file from the hard disk, and send it to the browser.
    """
    """with open("form.html") as f:
        html = f.read()
    return html"""


@app.post("/processform")
def save_data():
    """
    Recieve the data from the html form then save it to a disk file. Then reopen with a message into the browser
    """
    # python names = html names
    the_first = request.form["first"]
    the_last = request.form["last"]
    the_dob = request.form["dob"]
    with open("comments.txt", "a") as sf:
        print(f"{the_first}, {the_last}, {the_dob}", file=sf)
    return f"Thanks, {the_first}, we promise not to sell your data."


if __name__ == "__main__":
    app.run(debug=True)
