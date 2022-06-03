from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('pacientes.html')

@main.route('/altas')
def altas_medicas():
    return render_template('altas.html')