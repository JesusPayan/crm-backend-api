from flask import Flask, jsonify
from bd_config import db
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, create_engine, TIMESTAMP,DECIMAL,LargeBinary
from sqlalchemy.orm import relationship
# Base = declarative_base()
# No es necesario declarar Base si se usa db.Model

#class Role(db.Model):  # Cambié db.model a db.Model
#    __tablename__ = 'roles'
#    id = db.Column(db.Integer, primary_key=True)  # Cambié db.column a db.Column
#    role_name = db.Column(db.String(40), nullable=False)  # Cambié roleName a role_name para seguir la convención
#    users = relationship("User", back_populates="role")  # Cambié el nombre de la relación a users
class Client(db.Model):
    __tablename__ = 'clients'

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
    __tablename__ = 'products'

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
    client_id = Column(Integer, ForeignKey('clients.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
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


