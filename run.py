from app import app

@app.route("/")
def hello_world():
    return "<p>Hello Word</p>"

if __name__== "__main__":
    app.run(debug=True)