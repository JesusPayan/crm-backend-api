from flask import Blueprint, jsonify, request
# from bd_config import db
from logger import logger
from app.routes.microserviceClient.clientService import ClientService
import json




clients_api = Blueprint('clientsApi', __name__)
service = ClientService()
# Obtener clientes
# @clients_api.route('v1/clients', methods=['GET','POST'])

@clients_api.route('/get_clients', methods=['GET'])
def get_clients():
    print("GET /clients endpoint reached")
    client_list = service.get_all_clients()
    if client_list is None:
        return jsonify({"message": "Clientes no encontrados"}), 404
    else:
        return jsonify([{"id": e.id, "cve_internal": e.cve_internal, "Name": e.name, "father_lastname": e.father_lastname, "mother_lastname": e.mother_lastname, "telephone1": e.telephone1
                , "telefono2": e.telefono2, "email1": e.email1, "email2": e.email2,
                "status": e.status, "status_desc": e.status_desc,
                "created_at": e.created_at, "created_by": e.created_by, "updated_at": e.updated_at, "updated_by": e.updated_by, "message": "Success"} for e in client_list])
@clients_api.route('/get_client/<int:id>', methods=['GET'])
def get_client(id):
    print("GET /client endpoint reached")
    client = service.get_client(id)
    if client is None:
        return jsonify({"message": "Cliente no encontrado"}), 404
    else:
        return jsonify([{"id": e.id, "cve_internal": e.cve_internal, "Name": e.name, "father_lastname": e.father_lastname, "mother_lastname": e.mother_lastname, "telephone1": e.telephone1
                , "telefono2": e.telefono2, "email1": e.email1, "email2": e.email2,
                "status": e.status, "status_desc": e.status_desc,
                "created_at": e.created_at, "created_by": e.created_by, "updated_at": e.updated_at, "updated_by": e.updated_by, "message": "Success"} for e in client])
# Agregar cliente
@clients_api.route('/create_client', methods=['POST'])
def add_client():
    data = request.get_json()
    print("POST /client-add endpoint reached")
    logger.info(f"Cliente recibido: {data}")
    if not data:
        return jsonify({"message": "Informacion no recibida"}), 400
    elif not data['name'] or not data['email1']:
        return jsonify({"message": "Informacion incompleta"}), 400
    else:
        
        client_saved  = service.create_new_client(data)
        if client_saved:
            return jsonify({"message": "Cliente agregado correctamente"}), 201
        else:
            return jsonify({"message": "Error al agregar el cliente"}), 400 
@clients_api.route('/update_client/<int:id>', methods=['PUT'])
def update_client(id):
    print("PUT /client-update endpoint reached")
    data = request.get_json()
    logger.info(f"Cliente recibido: {data}")
    if not data:
        return jsonify({"message": "Informacion no recibida"}), 400
    elif not data['name'] or not data['email1']:    
        return jsonify({"message": "Informacion incompleta"}), 400
    else:
        client_updated = service.update_client(id,data)
        if client_updated:
            return jsonify({"message": "Cliente actualizado correctamente"}), 200
        else:
            return jsonify({"message": "Error al actualizar el cliente"}), 400




# Esto es clave
__all__ = ['client_api']