from flask import Flask, request, render_template, request, jsonify

app = Flask(__name__)

import DBcm
from appconfig import config


@app.get("/")
def index():

    return render_template("index.html", title="Home", heading="Home")


@app.get("/bio")
def bio():
    return render_template("bio.html", title="Bio", heading="Bio")


@app.get("/interests")
def personal():
    return render_template("interests.html", title="Interests", heading="My Interestes")


@app.get("/CV")
def display_CV():

    return render_template("CV.html", heading="My CV")


@app.get("/technologies")
def tech():
    return render_template(
        "technologies.html", heading="My Favorite Computing Technologies"
    )


@app.get("/technologies/artificial_intelligence")
def AI():
    return render_template("AI.html", heading="Artificial Intelligence")


@app.get("/technologies/facial_recognition")
def facial_recognition():
    return render_template("facial_recognition.html", heading="Facial Recognition")


@app.get("/technologies/quantum")
def Quantum():
    return render_template("quantum.html", heading="Quantum Computing")


@app.get("/showform")
def display_form():
    return render_template(
        "form.html", title="Welcome", heading="Please Leave a message"
    )


@app.route("/savedata", methods=["POST"])
def save_data():
    """
    Recieve the data from the html form then save it to a disk file. Then reopen with a message into the browser
    """
    # python names = html names
    the_name = request.form["name"]
    the_email = request.form["email"]
    the_message = request.form["message"]
    # save the pieces of data to the database table.
    with DBcm.UseDatabase(config) as db:

        SQL = """
            insert into comments
            (name, email, message)
            values
            ( %s, %s, %s)
            """
        db.execute(SQL, (the_name, the_email, the_message))
    return render_template(
        "thanks.html", title="Thanks for your message", who=the_name, what=the_message,
    )


@app.get("/getdata")
def grab_latest_data():
    with DBcm.UseDatabase(config) as db:

        SQL = """
               select name, message, time
               from comments order by time desc
               """
        db.execute(SQL)
        data = db.fetchall()
    return render_template("message.html", title="Welcome", data=data,)


if __name__ == "__main__":
    app.run(debug=True)  # pragma: no cover
