from flask import Flask, render_template,request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/demo")
def demo():
    return render_template("index2.html")

@app.route("/demofinal", methods=['POST'])
def demofinal():
    text = request.form['api_url']
	
    
    return render_template("index3.html", label)


if __name__ == "__main__":
    app.run(debug=True)