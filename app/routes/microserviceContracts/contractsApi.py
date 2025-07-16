from flask import Blueprint, jsonify, request
from logger import logger
from app.routes.microserviceProducts.productService import ProductService

contracts_api = Blueprint('contractsApi', __name__)
service = ProductService()

@contracts_api.route('v1/contracts', methods=['POST'])
def add_contract():
    print("POST /contract-add endpoint reached")
    data = request.get_json()
    if data:
        print(f"POST /contract-add endpoint reached {data}")
        logger.info(f"Contrato recibido: {data}")
        contract_saved = service.create_new_contract(data)
        logger.info(f"Contrato guardado: {contract_saved}")
        if contract_saved:
            return jsonify({
                "message": "Contrato agregado correctamente",
                "data": contract_saved.to_dict()
            }), 201
        else:
            return jsonify({"message": "Error al agregar el contrato"}), 400
    else:
        return jsonify({"message": "No se recibió información válida"}), 400
    @contracts_api.route('v1/contracts/<int:id>', methods=['PUT'])
    def update_contract(id):
        print("PUT /contract endpoint reached", id)
        data = request.get_json()
        contract_updated = service.update_contract_by_id(id, data)
        if contract_updated:
            return jsonify({'message': 'Contract updated successfully'}), 200
        else:
            return jsonify({'message': 'Error updating contract'}), 400     

    @contracts_api.route('v1/contracts/<int:id>', methods=['DELETE'])
    def delete_contract(id):
        print("DELETE /contract endpoint reached", id)
        contract_deleted = service.delete_contract_by_id(id)
        if contract_deleted:
            return jsonify({'message': 'Contract deleted successfully'}), 200
        else:
            return jsonify({'message': 'Error deleting contract'}), 400

    @contracts_api.route('v1/contracts', methods=['GET'])
    def get_contracts():
        print("GET /contracts endpoint reached")
        contracts = service.get_all_contracts()
        if contracts:
            return jsonify({'contracts': [contract.to_dict() for contract in contracts]}), 200
        else:
            return jsonify({'message': 'Error getting contracts'}), 400

    @contracts_api.route('v1/contracts/<int:id>', methods=['GET'])
    def get_contract_by_id(id):
        print("GET /contract endpoint reached", id)
        contract = service.get_contract_by_id(id)
        if contract:
            return jsonify({'contract': contract.to_dict()}), 200
        else:
            return jsonify({'message': 'Contract not found'}), 404

    return contracts_api
    