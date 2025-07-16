from flask import Blueprint, jsonify, request
from logger import logger
from app.routes.microserviceProducts.productService import ProductService

products_api = Blueprint('productsApi', __name__)
service = ProductService()
@products_api.route('/update_product_by_id/<int:id>', methods=['PUT'])
def update_product(id):
    print("PUT /product endpoint reached", id)
    data = request.get_json()
    product_updated = service.update_product_by_id(id, data)
    if product_updated:
        return jsonify({'message': 'Product updated successfully'}), 200
    else:
        return jsonify({'message': 'Error updating product'}), 400
@products_api.route('/delete_all_products', methods=['DELETE'])
def delete_all_products():
    print("DELETE /products endpoint reached")
    products_deleted = service.delete_all_products()
    if products_deleted:
        return jsonify({'message': 'Products deleted successfully'}), 200
    else:
        return jsonify({'message': 'Error deleting products'}), 400

@products_api.route('/delete_product_by_id/<int:id>', methods=['DELETE'])
def delete_product(id):
    print("DELETE /product endpoint reached", id)
    product_deleted = service.delete_product_by_id(id)
    if product_deleted:
        return jsonify({'message': 'Product deleted successfully'}), 200
    else:
        return jsonify({'message': 'Error deleting product'}), 400
@products_api.route('/delete_product_by_name/<string:name>', methods=['DELETE'])
def delete_product_by_name(name):
    print("DELETE /product endpoint reached", name)
    product_deleted = service.delete_product(name)
    if product_deleted:
        return jsonify({"message": "Producto eliminado correctamente"}), 200
    else:
        return jsonify({"message": "Error al eliminar el producto"}), 400
@products_api.route('/get_product_by_status/<string:status>', methods=['GET'])
def get_product_by_status(status):
    print("GET /product_by_status endpoint reached for status:", status) 
    products_list = service.get_product_by_status(status)
    if products_list:
        # Asume que cada producto tiene un método to_dict()
        return jsonify({
            "message": "Productos encontrados",
            "data": [product.to_dict() for product in products_list]
        }), 200
    else:    
        return jsonify({"message": "Productos no encontrados"}), 404
@products_api.route('/get_products', methods=['GET'])
def get_products():
    print("GET /products endpoint reached")
    products_list = service.get_all_products()
    if products_list:
        # Asume que cada producto tiene un método to_dict()
        return jsonify({
            "message": "Productos encontrados",
            "data": [product.to_dict() for product in products_list]
        }), 200
    else:    
        return jsonify({"message": "Productos no encontrados"}), 404

@products_api.route('/get_product/<string:name>', methods=['GET'])
def get_product(name):
    print("GET /product endpoint reached")
    product = service.get_product(name)
    if product:
        return jsonify({
            "message": "Producto encontrado",
            "data": product.to_dict()
        }), 200
    else:    
        return jsonify({"message": "Producto no encontrado"}), 404

@products_api.route('/get_product_by_id/<int:id>', methods=['GET'])
def get_product_by_id(id):
    print("GET /product endpoint reached")
    product = service.get_product_by_id(id)
    if product:
        return jsonify({
            
            "data": product.to_dict()
        }), 200
    else:    
        return jsonify({
            "message": "Producto no encontrado"
            }), 404
        

@products_api.route('/create_product', methods=['POST'])
def add_product():

    print("POST /product-add endpoint reached")
    data = request.get_json()
    if data:
        print(f"POST /product-add endpoint reached {data}")
        logger.info(f"Producto recibido: {data}")
        product_saved = service.create_new_product(data)
        logger.info(f"Producto guardado: {product_saved}")
        if product_saved:
            return jsonify({
                "message": "Producto agregado correctamente",
                "data": product_saved.to_dict()
            }), 201
        else:
            return jsonify({"message": "Error al agregar el producto"}), 400
    else:
        return jsonify({"message": "No se recibió información válida"}), 400