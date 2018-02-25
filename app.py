from flask import Flask, abort, render_template, request
import datetime
import os

app = Flask(__name__)
print datetime.datetime.now()

#Sunday
@app.route('/change/')
def hello_world():
    return render_template('0.html')

#Monday
@app.route('/Stroke/')
def stroke():	
	now = datetime.datetime.now()			
	day = now.day
	code = 'h2t'
	print "Current day: %d" % now.day
	if now.day < 26:
		return render_template('yes.html', variable=code)
	else:
		return render_template('1.html')
#Tuesday
@app.route('/xmp/')
def letters():
	code = 'tj3'
	now = datetime.datetime.now()		
	if now.day < 27:
		return render_template('yes.html', variable=code)
	else:
		return render_template('2.html')
#Wendsday 
@app.route('/Y/')
def primt():
	code = 'r4o'
	now = datetime.datetime.now()		
	if now.day < 28:
		return render_template('yes.html', variable=code)
	else:
		return render_template('3.html')

@app.route('/dina/')
def dina():    
    return 'http://52.16.114.125:8080/F/'

#Thursday
@app.route('/F/')
def last(final=None):
	code = '6gt'
	now = datetime.datetime.now()		
	if now.day < 29:
		return render_template('yes_final.html', variable=code)
	else:
		return abort(404)
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0',port=8080,debug=True)