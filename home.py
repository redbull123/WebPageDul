from flask import Flask, redirect, url_for
from flask import render_template


app = Flask(__name__)

@app.route("/")
def brownie():
		return render_template('brownies.html')
		
if __name__ == '__main__':
	app.run('192.168.2.10',80,debug=True)