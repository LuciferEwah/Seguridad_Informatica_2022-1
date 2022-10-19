
from flask import Flask, render_template, request

app = Flask(__name__)

g = 421
p = 601

@app.route('/')
def principal():
    return render_template('principal/index.html',g=g,p=p)

@app.route("/servidor",methods=["GET","POST"])
def servidor():
    a = 234
    A = (g^a)%p
    b = int(request.form.get('dato1'))
    B  = (g^b)%p
    K1 = (A^b)%p
    K2 = (B^a)%p
    return render_template('cliente/index.html',g=g,p=p,A=A,K1=K1,K2=K2)

if __name__ == '__main__':
    app.run()
    