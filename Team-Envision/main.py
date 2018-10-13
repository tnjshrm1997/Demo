from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
	return "Hello World!"


# @app.route("/hello", methods=['POST'])
# def hello():
# 	if request.method=='POST':
# 		file = request.form['api_url']
# 		print(file)
# 	return render_template('hello.html')

if __name__=="__main__":
	app.run(debug=True)