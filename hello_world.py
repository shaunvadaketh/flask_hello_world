from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return render_template('template.html')



@app.route("/hello/<name>")
def hello_person(name):
    
    return render_template('template.html', first_name=name)
@app.route("/jedi/<first_name>/<last_name>")
def jedi_name(first_name, last_name):
     jediname = last_name[0:3] + first_name[0:2]
     return render_template('template_jedi.html', firstname=first_name, lastname=last_name, jediname=jediname)
     
     #return html.format(first_name.title(), last_name.title(), jediname.title())
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))