from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/question1")
def question1():
    return render_template("question1.html")
@app.route("/question2")
def question2():
    score = request.args.get("score", 0, type=int)
    return render_template("question2.html", score=score)

@app.route("/question3")
def question3():
    score = request.args.get("score", 0, type=int)
    return render_template("question3.html", score=score)

@app.route("/question4")
def question4():
    score = request.args.get("score", 0, type=int)
    return render_template("question4.html", score=score)

@app.route("/question5")
def question5():
    score = request.args.get("score", 0, type=int)
    return render_template("question5.html", score=score)

@app.route("/results")
def results():
    score = request.args.get("score", 0, type=int)
    return render_template("results.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)