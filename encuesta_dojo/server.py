from flask import Flask, render_template,redirect,request, session # agregado render_template!
app = Flask(__name__) 
app.secret_key='guarda un secreto'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    
    nombre=request.form['nombre']
    apellido=request.form['apellido']
    localizacion=request.form['localizacion']
    lenguaje=request.form['lenguaje']
    comentario=request.form['comentario']

    session['Dojo']={
        'nombre':nombre,
        'apellido':apellido,
        'localizacion':localizacion,
        'lenguaje':lenguaje,
        'comentario':comentario
    }
    return redirect('/results')


@app.route('/results')
def mostrar_usuario():
    return render_template('results.html')




if __name__=="__main__":
    app.run(debug=True) 