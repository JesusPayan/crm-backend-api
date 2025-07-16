from flask import Blueprint, jsonify, request
from logger import logger
from app.routes.microserviceProducts.productService import ProductService

contracts_api = Blueprint('catalogsApi', __name__)
service = CatalogService()


@contracts_api.route('v1/catalogs', methods=['GET'])
def get_catalogs():
    print("GET /catalogs endpoint reached")
    catalogs = service.get_all_catalogs()
    if catalogs:
        return jsonify({'catalogs': [catalog.to_dict() for catalog in catalogs]}), 200
    else:
        return jsonify({'message': 'Error getting catalogs'}), 400
@contracts_api.route('v1/catalogs', methods=['POST'])
def add_catalog():
    print("POST /contract-add endpoint reached")
    data = request.get_json()
    if data:
        print(f"POST /contract-add endpoint reached {data}")
        logger.info(f"Contrato recibido: {data}")
        catalog_saved = service.create_new_catalog(data)
        logger.info(f"Contrato guardado: {catalog_saved}")
        if catalog_saved:
            return jsonify({
                "message": "Contrato agregado correctamente",
                "data": catalog_saved.to_dict()
            }), 201
        else:
            return jsonify({"message": "Error al agregar el contrato"}), 400
    else:
        return jsonify({"message": "No se recibió información válida"}), 400
    
@contracts_api.route('v1/catalogs/<int:id>', methods=['PUT'])
def update_catalog(id):
    print("PUT /contract endpoint reached", id)
    data = request.get_json()
    catalog_updated = service.update_catalog_by_id(id, data)
    if catalog_updated:
        return jsonify({'message': 'Contract updated successfully'}), 200
    else:
        return jsonify({'message': 'Error updating contract'}), 400 


@contracts_api.route('v1/catalogs/<int:id>', methods=['DELETE'])
def delete_catalog(id):
    print("DELETE /contract endpoint reached", id)
    catalog_deleted = service.delete_catalog_by_id(id)
    if catalog_deleted:
        return jsonify({'message': 'Contract deleted successfully'}), 200
    else:
        return jsonify({'message': 'Error deleting contract'}), 400

@contracts_api.route('v1/catalogs/<int:id>', methods=['GET'])
def get_catalog_by_id(id):
    print("GET /contract endpoint reached", id)
    catalog = service.get_catalog_by_id(id)
    if catalog:
        return jsonify({'contract': catalog.to_dict()}), 200
    else:
        return jsonify({'message': 'Contract not found'}), 404        