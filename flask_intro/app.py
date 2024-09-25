from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        name = request.form.get("name")
    return render_template("greet.html", name=name)

    name = request.form.get("name", "world")
    return render_template("greet.html", name=name)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
