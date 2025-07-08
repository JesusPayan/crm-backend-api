from flask import Blueprint, render_template, jsonify,request
from models import Student, User  # Asegúrate de que la ruta sea correcta.
from bd_config import db
from bd_config import db
import utils
from logging import Logger 
# Definir el Blueprint correctamente
student_api = Blueprint('studentApi', __name__, template_folder='microserviceStudent')

# Asociar la ruta al Blueprint, no a la aplicación directamente
@student_api.route('/student', methods=['GET', 'POST'])
def get_students():
    students  = db.session.execute("select * from show_active_students;")
    if students.rowcount > 0:
        return jsonify([{"id": e.id, "Name": e.name, "Last_Name": e.last_name, "Age": e.age} for e in students])
    return jsonify([{"message": "No hay estudiantes registrados en la base de datos"} ],404)
@student_api.route('/student-add', methods=['POST'])
def add_student():
        print(request.get_json())
        data,code = utils.validate_json(request.get_json(),"student")
        Logger.logger.info(str(data,'utf-8')) # print(data)
        if code != 200:
            return jsonify(data),code
        else:
            if (Student.save_student(data)):
                db.session.commit()
                return jsonify({"message": "Student added successfully"}),201

    
 
# Registrar el Blueprint con la aplicación Flask (esto debería hacerse en tu archivo principal, por ejemplo, en app.py)
#app.register_blueprint(student_api)