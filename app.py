from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///logins.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "super secret key"


app.app_context().push()
db=SQLAlchemy(app)



class modelos(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    login= db.Column(db.String(50))
    senha= db.Column(db.String(100))

    def __init__(self,login,senha):
        self.login=login
        self.senha=senha
        
    


    def verificar(login,senha):
        validacao=modelos.query.filter_by(login=login,senha=senha).first()
        if validacao:
            return
        


@app.route('/register',methods=['POST','GET'])
def registro():
    
    
    if request.method=='POST':

        
        
        if request.form.get('login') and request.form.get('senha'):
        
        
            login=request.form.get('login')
            senha=request.form.get('senha')

            

            usuario=modelos(login,senha)
            db.session.add(usuario)
            db.session.commit()

            return redirect(url_for('login'))

    
    return render_template('registro.html',registros=modelos.query.all())


@app.route('/login',methods=['POST','GET'])
def login():

    
    if request.method=='POST':
        login=request.form.get('login')
        senha=request.form.get('senha')
        validacao=modelos.query.filter_by(login=login,senha=senha).first()
            
        if validacao:
                
            return redirect(url_for('foi'))

        else:
            flash('Dados inválidos')
            return redirect('/login')


    return render_template('login.html')
                


            
        

    
    

        

             
            

        

        
      

@app.route('/foi',methods=['POST','GET'])
def foi():
    return 'FOI GAROTO'


    
    

    
            

            

    
        



    




if __name__=='__main__':
    db.create_all()
    app.run(debug=True)