from flask import Flask, render_template,request
import re

app=Flask(__name__)

@app.route('/')

def home():

    return render_template('home.html')


#expresion que operamos en la ventana
patron=re.compile('^([A-Z]{1})([0-9]{3})([a-z])+([\W]{3})$')

@app.route('/logica',methods=['POST'])
def logica():
    if request.method=='POST':
        expresion=request.form['expresion']

        if(patron.match(expresion)):

                return validacion()
        else:
               return error()
    else:
        return error() 

@app.route('/home/error')
def error():
    return render_template('error.html')

@app.route('/home/validacion')
def validacion():
    return render_template('validacion.html')

#escuchar siempre
if __name__=='__main__':
    app.run(debug=True)



