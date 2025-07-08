from flask import Blueprint, render_template, jsonify,request
from models import Group  # Asegúrate de que la ruta sea correcta.
from bd_config import db
from utils import validate_json
import utils
from logging import Logger

# Definir el Blueprint correctamente
group_api = Blueprint('groupApi', __name__, template_folder='microserviceGroup')
@group_api.route('/groups', methods=['GET'])
def show_groups():
    groups =  Group.get_all_groups()
    if groups:
        return jsonify([{"id": e.id, "Name": e.group_name,"Nivel": e.group_level, "Capacidad": e.group_capacity} for e in db.session.query(Group).all()]),200
    else:
        return jsonify([{"message": "No hay grupos registrados en la base de datos"} ],404)
    
@group_api.route('/group-add', methods=['POST'])
def add_group():
    
    if request.get_json():
        print(str(request.get_json())) 
        input_json = request.get_json()
        if input_json:
            data,code,message = validate_json(request.get_json(),"group")
            if code != 200:
                return jsonify({"message": f"{message}"}),code
            else:
                return jsonify({"message": f"{message}"},data),code
            
                
                   

        
 
    
     
