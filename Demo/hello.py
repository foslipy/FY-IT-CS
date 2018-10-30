from flask import Flask
app = Flask(__name__)
 

@app.route("/about")
@app.route("/")
def hello1():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run()
