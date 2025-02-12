from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    print("Hello I am coming to you from the Python Shell")
    return "Hello I am coming to you from the web page"

if __name__=="__main__":
    app.run()

