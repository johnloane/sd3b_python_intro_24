from flask import Flask, render_template, request, redirect


app = Flask(__name__)


SPORTS = ["Basketball", "Badminton", "Volleyball"]
REGISTRANTS = {}


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name:
        message = "You forgot the name"
        return render_template("error.html", message=message)
    if not sport:
        message = "You need to select a sport"
        return render_template("error.html", message=message)
    if sport not in SPORTS:
        message = "Stop hacking my website"
        return render_template("error.html", message=message)
    REGISTRANTS[name] = sport
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
