from app.models import Product
from sqlalchemy.exc import SQLAlchemyError
from logger import logger
from app import db
class ProductService:
    def __init__(self):
        pass
    def get_product_by_id(self, id):
        try:
            return Product.query.filter_by(id=id).first()
        except SQLAlchemyError as e:
            logger.error(f"Error al obtener producto por ID: {str(e)}")
            return None
    def delete_product_by_id(self, id):
        try:
            product = Product.query.filter_by(id=id).first()
            if product:
                db.session.execute("DELETE FROM product WHERE id = :id", {"id": id})
                db.session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            logger.error(f"Error al eliminar producto por ID: {str(e)}")
            return False
        
    def delete_product_by_name(self, name):
        try:
            product = Product.query.filter_by(description=name).first()
            if product:
                db.session.delete(product)
                db.session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            logger.error(f"Error al eliminar producto por nombre: {str(e)}")
            return False
    def delete_all_products(self):
        try:
            products = Product.query.all()
            for product in products:
                db.session.delete(product)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            logger.error(f"Error al eliminar todos los productos: {str(e)}")
            return False                

    def get_all_products(self):
        try:
            return Product.query.all()
        except SQLAlchemyError as e:
            logger.error(f"Error al obtener productos: {str(e)}")
            return None

    def get_product(self, name):
        try:
            return Product.query.filter_by(description=name).first()
        except SQLAlchemyError as e:
            logger.error(f"Error al obtener producto por nombre: {str(e)}")
            return None

    def create_new_product(self, data):
        try:
            if data:
                new_product = Product.create_new_product(data)
                return new_product
            return None
        except SQLAlchemyError as e:
            logger.error(f"Error al crear producto: {str(e)}")
            return None

    def update_product(self, id, data):
        try:
            product = Product.query.filter_by(des).first()
            if not product:
                return None
            for key, value in data.items():
                if hasattr(product, key):
                    setattr(product, key, value)
            db.session.commit()
            return product
        except SQLAlchemyError as e:
            logger.error(f"Error al actualizar producto: {str(e)}")
            return None

    def delete_product(self, id):
        try:
            product = Product.query.filter_by(id=id).first()
            if product:
                db.session.delete(product)
                db.session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            logger.error(f"Error al eliminar producto: {str(e)}")
            return False

    # Otros filtros según atributos específicos:
    def get_product_by_status(self, status):
        return Product.query.filter_by(status_desc=status).all()
    def update_product_by_id(self, id, data):
        logger.info(f"Updating product with name: {id} and data: {data}")
        try:
            product = Product.query.filter_by(id=id).first()
            if not product:
                return None
            for key, value in data.items():
                if hasattr(product, key):
                    setattr(product, key, value)
            db.session.commit()
            return product
        except SQLAlchemyError as e:
            logger.error(f"Error al actualizar producto: {str(e)}")
            return None 
