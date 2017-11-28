from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] =True

form= """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;                             
            }}

        </style>
    </head>
        <body>
            <form method="post">
                <label for="rotate-by">Rotate by:</label>
                <input id="rotate-by" value="0" type="text" name="rot" />
                <h1><textarea type="textarea" name="text">{0} </textarea></h1>
                <input type="submit" />  
            </form>
        </body>
</html>
"""

@app.route("/")
def index ():
  return form.format("")

@app.route("/", methods=['POST'])
def encrypt ():
  text=request.form["text"]
  rot=int(request.form["rot"])
  return form.format(rotate_string(text,rot))

app.run()
