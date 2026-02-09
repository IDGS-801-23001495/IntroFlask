from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
from forms import CinepolisForm

import forms

app = Flask(__name__)
app.secret_key='clave secreta'

csrf=CSRFProtect()


@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():
    form = CinepolisForm(request.form)
    total_pagar = 0
    mensaje_error = ""
    descuento_aplicado = ""
    descuento_cineco = "" 
    PRECIO_BOLETA = 12000

    if request.method == 'POST' and form.validate():
        nombre = form.nombre.data
        n_compradores = form.compradores.data
        n_boletas = form.boletas.data
        tiene_tarjeta = form.tarjeta.data

        max_permitido = n_compradores * 7
        if n_boletas > max_permitido:
            mensaje_error = f"No se pueden comprar más de 7 boletas por persona (Máx: {max_permitido})"
        else:
            total_pagar = n_boletas * PRECIO_BOLETA

            if n_boletas > 5:
                total_pagar *= 0.85 # 15% desc
                descuento_aplicado = "Se aplicó un 15% de descuento por comprar más de 5 boletas."
            elif 3 <= n_boletas <= 5:
                total_pagar *= 0.90 # 10% desc
                descuento_aplicado = "Se aplicó un 10% de descuento por comprar entre 3 y 5 boletas."

            if tiene_tarjeta == 'si':
                total_pagar *= 0.90 # 10% desc adicional
                descuento_cineco = "¡Descuento adicional del 10% aplicado por usar tarjeta CINECO!"

    return render_template("cinepolis.html", form=form, total=total_pagar, 
                           error=mensaje_error, desc1=descuento_aplicado, desc2=descuento_cineco)

@app.route("/")
def index():
    titulo="Flask IDGS801"
    lista=["Juan", "Mario", "Pedro", "Dinenno"]
    return render_template("index.html", titulo=titulo, lista=lista)


@app.route("/operasBas", methods=["GET","POST"])
def opera():
    n1=0
    n2=0
    res=0
    if request.method=='POST':
        n1=request.form.get('n1')
        n2=request.form.get('n2')
        res=float(n1)+float(n2)
    return render_template("operasBas.html", n1=n1, n2=n2, res=res)


@app.route("/resultado", methods=["GET","POST"])
def resultado():
    n1=request.form.get('n1')
    n2=request.form.get('n2')
    tem=float(n1)+float(n2)
    return f"La suma es: {tem}"





@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")



@app.route("/usuarios", methods=["GET", "POST"])
def usuarios():
    mat=0
    nom=''
    apa=''
    ama=''
    email=''
    usuarios_class=forms.UserForm(request.form)
    if request.method=='POST' and usuarios_class.validate():
        mat=usuarios_class.matricula.data
        nom=usuarios_class.nombre.data
        apa=usuarios_class.apaterno.data
        ama=usuarios_class.amaterno.data
        email=usuarios_class.correo.data
        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)

    return render_template("usuarios.html", form=usuarios_class,
                           mat=mat,nom=nom, apa=apa, ama=ama, email=email)



@app.route("/hola")
def hola():
    return "HOLA MUNDO"

@app.route("/user/<string:user>")
def user(user):
    return f"HOLA, {user}|"

@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>El numero es, {n}</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1>¡Hola, {username} Tu ID es: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1>La suma es: {n1+n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="juan"):
    return f"<h1>Hola, {param}</h1>"

@app.route("/operas")
def operas():
    return '''
        <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        </br>
        <label for="name">apaterno:</label>
        <input type="text" id="name" name="name" required>
        </form>
        '''

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True) ##(debug=True) es para no tener que estar reiniciando el servidor y se pueda actualizar en tiempo real