from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
