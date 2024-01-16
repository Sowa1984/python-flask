# an object of WSGI application 
import os
import logging
import sys
from flask import Flask, redirect, url_for   
app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def hello(): 
    return 'HELLO'

@app.route('/site/<name>/<age>')       
def site(name, age): 
    greetings = 'Hello ' + name + ', age ' + age + '!<br/>'
    return greetings

@app.route('/hello/<name>')
def site2(name):
   greetings = 'Hi '+ name
   return greetings

#def hello_world(name): 
#   return 'hello world %s' % name2 
#app.add_url_rule('/hello/<name2>', 'hello2', hello_world)


@app.route('/user/<name3>') 
def hello_user(name3):     
   if name3 == "rychu":  #dynamic binding of URL to function 
      return redirect(url_for('site', name=name3, age=2))   
   else: 
      return redirect(url_for('site2', name=name3)) 



# decorator to route URL 
#@app.route('/hello')   
  
# binding to the function of route  
#def hello_world():      
#   return 'hello world' 

if __name__=='__main__': 
    app.debug = True
    app.run() 
    app.run(debug = True) 
 

 