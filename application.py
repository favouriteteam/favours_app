from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/<name>")
def greeting(name):
  return "<h1>That's right " + str(name) + ", it works.</h1>"

if __name__ == "__main__":
  app.run()
