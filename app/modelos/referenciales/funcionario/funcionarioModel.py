from flask import current_app as app
#from app.conexion.Conexion import Conexion

class funcionarioModel:
    
    def listarTodos(self):
        try:
    #        conexion = Conexion()
    #        con = conexion.getConexion()
    #        cursor = con.cursor()
    #        cursor.execute("SELECT id, descripcion FROM public.nacionalidades")
    #        items = cursor.fetchall()
    #        cursor.close()
    #        con.close()
    #        return items
            return "funcionarioModel > listarTodos > return"
        except:
            app.logger.error('Ha ocurrido un error al listar Funcionario')