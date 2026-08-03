from flask import Flask, render_template, redirect
import random

app = Flask(__name__)

score = 0
out = False


def commentary(runs):
    if runs == 0:
        return "Dot ball. No run."
    if runs == 6:
        return "SIX! That's out of the ground!"
    if runs == 4:
        return "FOUR! Cracking shot!"
    return f"{runs} run(s). Good running between the wickets."


@app.route("/")
def home():
    global score, out
    score = 0
    out = False
    return render_template("index.html")


@app.route("/game")
def game():
    return render_template("game.html",
                            score=score,
                            computer="-",
                            message="Choose a run")


@app.route("/play/<int:user>")
def play(user):
    global score, out

    computer = random.randint(0, 6)

    if user == computer:
        out = True
        return redirect("/result")

    score += user

    return render_template("game.html",
                            score=score,
                            computer=computer,
                            message=commentary(user))


@app.route("/result")
def result():
    global score
    return render_template("result.html", score=score)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
