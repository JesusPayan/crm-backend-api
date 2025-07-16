from flask import Flask
from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey, TIMESTAMP, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from logger import logger
from datetime import datetime
from app import db
from sqlalchemy.testing.exclusions import db_spec
from test.test_pydoc.pydocfodder import A_staticmethod_ref2
# from extensions import db



# Tabla: clients
class Client(db.Model):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cve_internal = Column(String(50))
    name = Column(String(100))
    mother_lastname = Column(String(100))
    father_lastname = Column(String(100))
    telephone1 = Column(String(20))
    telefono2 = Column(String(20))
    email1 = Column(String(100))
    email2 = Column(String(100))
    status = Column(Integer)
    status_desc = Column(String(100))
    created_at = Column(TIMESTAMP)
    created_by = Column(String(100))
    updated_at = Column(TIMESTAMP)
    updated_by = Column(String(100))

    contracts = relationship("Contract", back_populates="client")


# Tabla: products
class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cve_internal = Column(String(50))
    description = Column(String(255))
    price = Column(DECIMAL(10, 2))
    image = Column(LargeBinary)
    status = Column(Integer)
    status_desc = Column(String(100))
    created_at = Column(TIMESTAMP)
    created_by = Column(String(100))
    updated_at = Column(TIMESTAMP)
    updated_by = Column(String(100))

    contracts = relationship("Contract", back_populates="product")
    def to_dict(self):
        return {
        "id": self.id,
        "description": self.description,
        "price": str(self.price),
        "image": str(self.image),  # Puedes personalizar esto
        "status": self.status,
        "status_desc": self.status_desc,
        "created_at": self.created_at.isoformat() if self.created_at else None,
        "created_by": self.created_by,
        "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        "updated_by": self.updated_by
    }
    @staticmethod
    def get_by_id(id):
        product = db.session.query(Product).filter_by(id=id).first()
        return product

    @staticmethod
    def delete_product(id):
        product = db.session.query(Product).filter_by(id=id).delete()
        db.session.commit()
        return product
    @staticmethod
    def create_new_product(data):
        if data:
                logger.info(f"Creating new product: {data}")
                
                if data['description'] is not None:
                    description = data['description']
                cve_internal = description[0:3]+ '-' + description[4:]    
                print(cve_internal)
                if data['price'] is not None:
                    price = data['price']
                if data['status'] is not None:    
                    status = data['status']
                if data['status_desc'] is not None:
                    status_desc = data['status_desc']
                if data['created_by'] is not None:
                    created_by = data['created_by']
   
                product = Product(
                    cve_internal=cve_internal,
                    created_at=datetime.now(),
                    description=description,
                    price=price,
                    status=status,
                    status_desc=status_desc,
                    created_by=created_by
                )
                db.session.add(product)
                db.session.flush()
                db.session.commit()
                return product
        else:
            return product  

# Tabla: contracts
class Contract(db.Model):
    __tablename__ = 'contract'

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(Integer)
    status_desc = Column(String(100))
    created_at = Column(TIMESTAMP)
    created_by = Column(String(100))
    updated_at = Column(TIMESTAMP)
    updated_by = Column(String(100))

    client = relationship("Client", back_populates="contracts")
    product = relationship("Product", back_populates="contracts")
    @staticmethod
    def get_all_contracts():
        contracts = db.session.query(Contract).all()
        return contracts
    @staticmethod
    def get_by_id(id):
        contract = db.session.query(Contract).filter_by(id=id).first()
        return contract

    @staticmethod
    def delete_contract(id):
        contract = db.session.query(Contract).filter_by(id=id).delete()
        db.session.commit()
        return contract
    @staticmethod
    def create_new_contract(data):
        if data:
                logger.info(f"Creating new contract: {data}")
                if data['client_id'] is not None:
                    client_id = data['client_id']
                if data['product_id'] is not None:
                    product_id = data['product_id']
                if data['start_date'] is not None:
                    start_date = data['start_date']
                if data['end_date'] is not None:
                    end_date = data['end_date']
                if data['status'] is not None:
                    status = data['status']
                if data['status_desc'] is not None:
                    status_desc = data['status_desc']
                if data['created_by'] is not None:
                    created_by = data['created_by']
    
                contract = Contract(
                    client_id=client_id,
                    product_id=product_id,
                    start_date=start_date,
                    end_date=end_date,
                    created_at=datetime.now(),
                    status=status,
                    status_desc=status_desc,
                    created_by=created_by
                )
                db.session.add(contract)
                db.session.flush()
                db.session.commit()
                return contract

        else:
            return None
    def to_dict(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "product_id": self.product_id,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "status": self.status,
            "status_desc": self.status_desc,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "created_by": self.created_by,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "updated_by": self.updated_by
        }
# Tabla: catalogs
class Catalog(db.Model):
    __tablename__ = 'catalogs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cve_table = Column(String(50))
    desc_table = Column(String(100))
    status = Column(Integer)
    status_desc = Column(String(100))
    created_at = Column(TIMESTAMP)
    created_by = Column(String(100))
    updated_at = Column(TIMESTAMP)
    updated_by = Column(String(100))

    values = relationship("CatalogValue", back_populates="catalog")

    @staticmethod
    def get_all_catalogs():
        catalogs = db.session.query(Catalog).all()
        return catalogs
    @staticmethod
    def get_by_id(id):
        catalog = db.session.query(Catalog).filter_by(id=id).first()
        return catalog

    @staticmethod
    def delete_catalog(id):
        catalog = db.session.query(Catalog).filter_by(id=id).delete()
        db.session.commit()
        return catalog
    @def create_new_catalog(data):
        if data:
                logger.info(f"Creating new catalog: {data}")
                if data['cve_table'] is not None:
                    cve_table = data['cve_table']
                if data['desc_table'] is not None:
                    desc_table = data['desc_table']
                if data['status'] is not None:
                    status = data['status']
                if data['status_desc'] is not None:
                    status_desc = data['status_desc']
                if data['created_by'] is not None:
                    created_by = data['created_by']
    
                catalog = Catalog(
                    cve_table=cve_table,
                    desc_table=desc_table,
                    status=status,
                    status_desc=status_desc,
                    created_at=datetime.now(),
                    created_by=created_by)
                db.session.add(catalog)
                db.session.flush()
                db.session.commit()
                return catalog
        else:
            return None 
    @staticmethod
    def update_catalog_by_id(id, data):
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
    
    def to_dict(self):
        return {
            "id": self.id,
            "cve_table": self.cve_table,
            "desc_table": self.desc_table,
            "status": self.status,
            "status_desc": self.status_desc,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "created_by": self.created_by,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "updated_by": self.updated_by
        }

# Tabla: catalog_values
class CatalogValue(db.Model):
    __tablename__ = 'catalog_value'

    catalog_id = Column(Integer, ForeignKey('catalogs.id'), primary_key=True)
    sequence_id = Column(Integer, primary_key=True)
    key01 = Column(String(100))
    key02 = Column(String(100))
    key03 = Column(String(100))
    key04 = Column(String(100))
    value01 = Column(String(255))
    value02 = Column(String(255))
    value03 = Column(String(255))
    value04 = Column(String(255))
    status = Column(Integer)
    status_desc = Column(String(100))
    created_at = Column(TIMESTAMP)
    created_by = Column(String(100))
    updated_at = Column(TIMESTAMP)
    updated_by = Column(String(100))

    catalog = relationship("Catalog", back_populates="values")
