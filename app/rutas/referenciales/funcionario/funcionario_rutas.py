from flask import Blueprint, render_template
from app.modelos.referenciales.funcionario.funcionarioModel import funcionarioModel

# Se crea el módulo para Blueprint
funcionariomod = Blueprint("funcionario", __name__, template_folder="templates")
cli_model = funcionarioModel()

# Los endpoints
@funcionariomod.route('/')
def index():
    items = cli_model.listarTodos()
    print(items)
    #return render_template('funcionario/index.html', item = items)
    return render_template('funcionario/index.html')


