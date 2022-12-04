
from flask import Flask, render_template

app = Flask(__name__)

from app.rutas.referenciales.funcionario.funcionario_rutas import funcionariomod

# Versión corta
app.register_blueprint(funcionariomod, url_prefix="/funcionario")