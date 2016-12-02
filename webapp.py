from flask import Flask, request ,render_template
from couchdb import Server
app = Flask(__name__)  

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/london") 
def name():         
	return "London is the capital and most populous city of England and the United Kingdom."
@app.route("/paris") 
def paris(): 
 return "Some text about Paris"
	
@app.route("/japan") 
def japan(): 
 return "Some text about Japan"

@app.route("/index/")
@app.route('/index/<name>')
def index(name=None):
    return app.send_static_file('index.html')

@app.route("/services/")
@app.route('/services/<name>')
def services(name=None):
    return render_template('services.html', name=name)

@app.route("/port/")
@app.route('/port/<name>')
def port(name=None):
    return render_template('port.html', name=name)

@app.route("/about/")
@app.route('/about/<name>')
def about(name=None):
    return render_template('about.html', name=name)

@app.route("/team/")
@app.route('/team/<name>')
def team(name=None):
    return render_template('team.html', name=name)

@app.route("/contact/")
@app.route('/contact/<name>')
def contact(name=None):
    return render_template('contact.html', name=name)

if __name__ == "__main__":     
	app.run()
