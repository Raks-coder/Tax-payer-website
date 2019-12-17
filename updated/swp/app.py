
from flask import Flask,render_template,request,flash,redirect,url_for
from flask_mongoalchemy import MongoAlchemy 
import redis;

app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


wsgi_app= app.wsgi_app

r=redis.StrictRedis(host='localhost',port=6379,db=0,decode_responses=True);


@app.route("/")
def hello():
	return render_template ("home.html")

 
@app.route("/signup",methods=['GET','POST'])
def signup():
	if request.method=='GET':
		return render_template("signup.html")
	elif request.method=='POST':
		firstname=request.form['firstname'];
		lastname=request.form['lastname'];
		gender=request.form['gender'];
		contact=request.form['contact'];
		aadhar=request.form['aadhar'];
		email=request.form['email'];
		password=request.form['password'];
		r.hset(aadhar,'firstname',firstname)
		r.hset(aadhar,'lastname',lastname)
		r.hset(aadhar,'gender',gender)
		r.hset(aadhar,'contact',contact)
		r.hset(aadhar,'aadhar',aadhar)
		r.hset(aadhar,'email',email)
		r.hset(aadhar,'password',password)
		return render_template('registered.html');


@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='GET':
		return render_template('Login.html');
	elif request.method=='POST':
		aadhar=request.form.get('aadhar',False)
		email=request.form.get('email',False)
		password=request.form.get ('password',False)
		yo=r.hget(aadhar,'password')
		if (password==yo):
			return redirect(url_for('calculate'))
		else:
			return "<h1>It seems your password is incorrect or aadhar is not registered</h1>"
	else:
		return "<h2>Invalid input</h2>"

@app.route('/calculate',methods=['GET','POST'])
def calculate():
	if request.method=='GET':
		return render_template('loggedin.html');
	elif request.method=='POST':
		aadhar=int(request.form['aadhar'])
		age=int(request.form['age'])
		income=float(request.form['income'])
		# r.hset(aadhar,'age',age)
		# r.hset(aadhar,'income',income)
		if(age<60 and income>=2.50 and income<5):
			tax=str(0.09*income*100000)
			r.hset(aadhar,'tax',tax)
			return ("""<head><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"></head><body class="container jumbotron" style="background-color: #f4bf42;text-align:center"><h1>Tax to be Payed in rupees </h1></body>"""+tax+"""<div><h3>In order to proceed to the payment click here<h3></div><div><a href="https://onlineservices.tin.egov-nsdl.com/etaxnew/tdsnontds.jsp">Pay</a></div><h3>To return to website home page click here</h3><div><a href="/">Home</a></div>""")
		elif(age<60 and income>=5 and income<10):
			tax=str((0.24*income*100000)+12500)
			r.hset(aadhar,'tax',tax)	
			return ("""<head><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"></head><body class="container jumbotron" style="background-color: #f4bf42;text-align:center"><h1>Tax to be Payed in rupees </h1></body>"""+tax+"""<div><h3>In order to proceed to the payment click here<h3></div><div><a href="https://onlineservices.tin.egov-nsdl.com/etaxnew/tdsnontds.jsp">Pay</a></div><h3>To return to website home page click here</h3><div><a href="/">Home</a></div>""")
		elif(age<60 and income>=10):
			tax=str((0.34*income*10000)+112500)
			r.hset(aadhar,'tax',tax)
			return ("""<head><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"></head><body class="container jumbotron" style="background-color: #f4bf42;text-align:center"><h1>Tax to be Payed in rupees </h1></body>"""+tax+"""<div><h3>In order to proceed to the payment click here<h3></div><div><a href="https://onlineservices.tin.egov-nsdl.com/etaxnew/tdsnontds.jsp">Pay</a></div><h3>To return to website home page click here</h3><div><a href="/">Home</a></div>""")
		elif(age>60 and income>=3 and income<5):
			tax=str(0.09*income*100000)
			r.hset(aadhar,'tax',tax)
			return ("""<head><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"></head><body class="container jumbotron" style="background-color: #f4bf42;text-align:center"><h1>Tax to be Payed in rupees </h1></body>"""+tax+"""<div><h3>In order to proceed to the payment click here<h3></div><div><a href="https://onlineservices.tin.egov-nsdl.com/etaxnew/tdsnontds.jsp">Pay</a></div><h3>To return to website home page click here</h3><div><a href="/">Home</a></div>""")
		elif(age>60 and income>=5 and income<10):
			tax=str((0.24*income*100000)+10000)	
			r.hset(aadhar,'tax',tax)
			return ("""<head><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"></head><body class="container jumbotron" style="background-color: #f4bf42;text-align:center"><h1>Tax to be Payed in rupees </h1></body>"""+tax+"""<div><h3>In order to proceed to the payment click here<h3></div><div><a href="https://onlineservices.tin.egov-nsdl.com/etaxnew/tdsnontds.jsp">Pay</a></div><h3>To return to website home page click here</h3><div><a href="/">Home</a></div>""")
		elif(age>60 and income>=10):
			tax=str((0.34*income*10000)+110000)
			r.hset(aadhar,'tax',tax)
			return ("""<head><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"></head><body class="container jumbotron" style="background-color: #f4bf42;text-align:center"><h1>Tax to be Payed in rupees </h1></body>"""+tax+"""<div><h3>In order to proceed to the payment click here<h3></div><div><a href="https://onlineservices.tin.egov-nsdl.com/etaxnew/tdsnontds.jsp">Pay</a></div><h3>To return to website home page click here</h3><div><a href="/">Home</a></div>""")
		elif(age>80 and income>=5 and income<=10):
			tax=str(0.24*income*100000)	
			r.hset(aadhar,'tax',tax)
			return ("""<head><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"></head><body class="container jumbotron" style="background-color: #f4bf42;text-align:center"><h1>Tax to be Payed in rupees </h1></body>"""+tax+"""<div><h3>In order to proceed to the payment click here<h3></div><div><a href="https://onlineservices.tin.egov-nsdl.com/etaxnew/tdsnontds.jsp">Pay</a></div><h3>To return to website home page click here</h3><div><a href="/">Home</a></div>""")
		elif(age>80 and income>=10):
			tax=str((0.34*income*10000)+100000)
			r.hset(aadhar,'tax',tax)
			return ("""<head><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"></head><body class="container jumbotron" style="background-color: #f4bf42;text-align:center"><h1 style="align:center">Tax to be Payed in rupees </h1></body>"""+tax+"""<div><h3>In order to proceed to the payment click here<h3></div><div><a href="https://onlineservices.tin.egov-nsdl.com/etaxnew/tdsnontds.jsp">Pay</a></div><h3>To return to website home page click here</h3><div><a href="/">Home</a></div>""")
		else:
			return "<h1> Error</h1>"	
			

@app.route('/view',methods=['GET','POST'])
def view():
	if request.method=='GET':
		return render_template('tax.html')
	if request.method=='POST':
		aadhar=request.form['aadhar']
		yes=r.hget(aadhar,'tax')
		return render_template('view.html',tax=yes)	
			
@app.route('/signout',methods=['GET'])
def signout():
	return render_template('signout.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
	if request.method=='GET': 	
		return render_template('fin.html')
	elif request.method=='POST':
		aadhar=request.form['aadhar']
		text1=request.form['text1']
		text2=request.form['text2']
		text3=request.form['text3']	
		r.hset(aadhar,'text1',text1)
		r.hset(aadhar,'text2',text2)
		r.hset(aadhar,'text3',text3)
		return render_template('wecan.html')

@app.route('/recovery',methods=['GET','POST'])
def recovery():
	if request.method=='GET':
		return render_template('3.html')
	elif request.method=='POST':
		return redirect(url_for('password'))

@app.route('/password',methods=['GET','POST'])
def password():
	if request.method=='GET':
		return render_template('1.html')
	elif request.method=='POST':
		return render_template('2.html')

@app.route('/save-tax',methods=['GET'])
def save_tax():
		return render_template('tax-save.html')

if __name__=='__main__':
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run(debug=True)	
