print("hello world")
print("hello nell and yerba")
print("Hello friends")
print('hello from yerba')

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run()