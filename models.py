from flask import Flask
from bd_config import db
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date,  TIMESTAMP,DECIMAL,LargeBinary
from sqlalchemy.orm import relationship
from logger import logger
from datetime import datetime
import json
from flask.json import jsonify
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
    @staticmethod
    def delete_client(id):
        client = db.session.query(Client).filter_by(id=id).delete()
        db.session.commit()
        return client
    @staticmethod
    def get_all():
        # client_list = db.session.execute("SELECT * FROM client")
        
        client_list = db.session.query(Client).all()
        
        if client_list:
            return client_list
        else:
            return None
    @staticmethod
    def get_by_id(id):
        client = db.session.query(Client).filter_by(id=id).first()
        
        return client
    @staticmethod
    def update_client(id,data):
        client = db.session.query(Client).filter_by(id=id).update(data)
        db.session.commit()
        
        return client
    @staticmethod
    def create_new_client(data):
        logger.info(f"Creating new client input recived: {data}")
        if data['name']:
            name = data['name']
        if data['father_lastname']:
            fatherLastname = data['father_lastname']
        if data['mother_lastname']:
            mother_lastname = data['mother_lastname']
        if data['status']:
            status = data['status']
        if data['status_desc']:
            status_desc = data['status_desc']
        if data['telephone1']:
            telephone1 = data['telephone1']
        if data['email1']:
            email1 = data['email1']
        if data['email2'] is not None:
            email2 = data['email2']
        else:
            email2 = email1
        if data['telephone2'] is not None:
            telephone2 = data['telephone2']
        else:
            telephone2 = telephone1
        if data['created_by']:
            created_by = data['created_by']
        created_at = datetime.now()
        
        new_client = Client(name=name,
                        father_lastname=fatherLastname,
                        mother_lastname=mother_lastname,
                        status=status,
                        status_desc=status_desc,
                        telephone1=telephone1,
                        telefono2=telephone2,
                        email1=email1,
                        email2=email2,
                        created_at=created_at,
                        created_by=created_by)
        try:
            db.session.add(new_client)
            db.session.flush()
            db.session.commit()
            return new_client
        except Exception as e:
            logger.error(f"Error creating new client: {e.with_traceback()}")
        
            


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


# Tabla: contracts
class Contract(db.Model):
    __tablename__ = 'contracts'

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


# Tabla: catalog_values
class CatalogValue(db.Model):
    __tablename__ = 'catalog_values'

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

db.create_all()


