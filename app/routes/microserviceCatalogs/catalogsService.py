from app.models import Catalog, CatalogValue
from sqlalchemy.exc import SQLAlchemyError
from logger import logger
from app import db


def get_all_catalogs(self):
    try:
        return Catalog.query.all()
    except SQLAlchemyError as e:
        logger.error(f"Error al obtener catálogos: {str(e)}")
        return None

def get_catalog_by_id(self, id):
    try:
        return Catalog.query.filter_by(id=id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error al obtener catálogo por ID: {str(e)}")
        return None

def create_new_catalog(self, data):
    try:
        if data:
            new_catalog = Catalog.create_new_catalog(data)
            return new_catalog
        return None
    except SQLAlchemyError as e:
        logger.error(f"Error al crear catálogo: {str(e)}")
        return None

def update_catalog_by_id(self, id, data):
    logger.info(f"Updating catalog with id: {id} and data: {data}")
    try:
        catalog = Catalog.query.filter_by(id=id).first()
        if not catalog:
            return None
        for key, value in data.items():
            if hasattr(catalog, key):
                setattr(catalog, key, value)
        db.session.commit()
        return catalog
    except SQLAlchemyError as e:
        logger.error(f"Error al actualizar catálogo: {str(e)}")
        return None
    
def delete_catalog_by_id(self, id):
    try:
        catalog = Catalog.query.filter_by(id=id).first()
        if catalog:
            db.session.delete(catalog)
            db.session.commit()
            return True
        return False
    except SQLAlchemyError as e:
        logger.error(f"Error al eliminar catálogo: {str(e)}")
        return False

def delete_all_catalogs(self):
    try:
        catalogs = Catalog.query.all()
        for catalog in catalogs:
            db.session.delete(catalog)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        logger.error(f"Error al eliminar todos los catálogos: {str(e)}")
        return False

def get_all_catalog_values(self):
    try:
        return CatalogValue.query.all()
    except SQLAlchemyError as e:
        logger.error(f"Error al obtener valores de catálogos: {str(e)}")
        return None

def get_catalog_value_by_id(self, id):
    try:
        return CatalogValue.query.filter_by(id=id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error al obtener valor de catálogo por ID: {str(e)}")
        return None

def create_new_catalog_value(self, data):
    try:
        if data:
            new_catalog_value = CatalogValue.create_new_catalog_value(data)
            return new_catalog_value
        return None
    except SQLAlchemyError as e:
        logger.error(f"Error al crear valor de catálogo: {str(e)}")
        return None