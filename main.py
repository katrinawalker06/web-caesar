from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] =True

form= """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color:#eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }

        </style>
    </head>
        <body>
            <form method=post>
                <label for="rotate-by">Rotate by:</label>
                <input id="rotate-by" type="text" name="rot" />
                <input textarea="text" name="text" />
                <input type="submit" />  
            </form>
        </body>
</html>
"""

@app.route("/")
def index ():
    return form

@app.route("/", methods=['POST'])
def encrypt ():
  rotate_string= request.form['text']
  return '<h1>' + text + '</h1>'

app.run()
