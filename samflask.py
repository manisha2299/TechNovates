from flask import Flask
import demo
app = Flask(__name__)
@app.route('/')
def display():
    demo.fun()
if __name__ == '__main__':
   app.run()