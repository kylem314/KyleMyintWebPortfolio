from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/projects")
def chessJS():
    return render_template("projects.html")

@app.route("/advancedTTT")
def advancedTTT():
    return render_template("advancedTTT.html")

@app.route("/journal")
def journals():
    return render_template("journal.html")

@app.route("/groupwebproject")
def groupwebproject():
    return render_template("groupwebproject.html")

@app.route("/chessOO")
def chessOO():
    return render_template("chessOO.html")

if __name__ == "__main__":
    app.run(debug=True)