from wtforms import Form 
from wtforms import StringField, IntegerField, PasswordField, FloatField
from wtforms import EmailField
from wtforms import validators
from wtforms import RadioField

class UserForm(Form): 
    matricula=IntegerField("Matricula",[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese valor valido")
    ])
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre valido")
    ])
    apaterno=StringField("Apaterno",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un apellido valido")
    ])
    amaterno=StringField("Amaterno",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un apellido valido")
    ])
    correo=EmailField("Correo", [
        validators.Email(message="Ingresa un correo valido")
    ])

class CinepolisForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El nombre es obligatorio")
    ])
    compradores = IntegerField("Cantidad Compradores", [
        validators.DataRequired(message="Ingrese cuántas personas compran"),
        validators.NumberRange(min=1, message="Debe haber al menos 1 comprador")
    ])
    boletas = IntegerField("Cantidad de Boletas", [
        validators.DataRequired(message="Ingrese cantidad de boletas"),
        validators.NumberRange(min=1, message="Debe comprar al menos una boleta")
    ])
    tarjeta = RadioField("¿Tiene Tarjeta CINECO?", choices=[('si', 'Sí'), ('no', 'No')], default='no')