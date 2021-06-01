from flask import Flask, render_template, request, redirect, url_for, flash
import joblib
from joblib.numpy_pickle import load
from joblib import dump, load
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
from werkzeug.utils import secure_filename
import textract


from procesador import preProcesador


app=Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_DB'] = 'Flask_Deploy'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASS'] = ''
# mysql=MySQL(app)
# Sesion 

app.secret_key='mysecretkey'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/cargarHV', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':

        f = request.files['hoja']
        nombreArchivo=f.filename.replace(" ","")
        f.save(secure_filename(nombreArchivo))
        texto=textract.process(nombreArchivo).decode('utf-8')
        texto=preProcesador(texto)
        tfidf_vect=joblib.load('models/vect_tfidf.pkl')
        
        tfidf = tfidf_vect.transform([texto])
        model_gb=joblib.load('models/modelo_gb.pkl')
        prediccion=model_gb.predict(tfidf)[0]
        flash("Predicción = "+str(prediccion))
        return redirect(url_for('index'))

'''
@app.route('/predecir', methods=["POST"])
def predecir():
    if request.method=='POST':
        TestTweet= [request.form['TestTweet']]
        nb=load('models/NaiveBayes.pkl')
        vec=load('models/tfidf_vect.pkl')
        valorTrans=vec.transform(TestTweet)
        prediccion=nb.predict(valorTrans)
      
        flash("Predicción = "+str(prediccion[0]))
        return redirect(url_for('index'))
       
'''

if __name__=='__main__':
    app.run(port=3000, debug=True)