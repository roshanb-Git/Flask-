## integrate HTML with Flask
## HTTP verb and GET and POST


#import libraries
from flask import Flask, redirect , url_for,render_template,request

#initialization of WSGI application 
app =Flask(__name__)


#Craete Decorators
@app.route('/')
def welcome():
    return render_template('index.html')


##Result checker
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths  =float(request.form['maths'])
        c =float(request.form['c'])
        data_science  =float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=''
    return redirect(url_for('success',score=total_score))

##decorator success 
@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res='PASS'
    else:
        res='FAIL'
    return render_template('result.html',result=res)

##Decorator Fail
@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is "+ str(score)


if __name__=='__main__':
    app.run(debug=True)