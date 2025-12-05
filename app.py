from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello DevOps! Ez már a feature/update-message branch módosított üzenete."


if __name__ == "__main__":
    # 0.0.0.0 kell Docker miatt is (különben csak localhoston látszik a konténeren belül)
    app.run(host="0.0.0.0", port=8080)
    
    