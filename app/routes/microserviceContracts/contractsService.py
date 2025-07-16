from app.models import Contract
from sqlalchemy.exc import SQLAlchemyError
from logger import logger
from app import db


class ContractService:
    def get_all_contracts(self):
        try:
            return Contract.query.all()
        except SQLAlchemyError as e:
            logger.error(f"Error al obtener contratos: {str(e)}")
            return None

    def get_contract_by_id(self, id):
        try:
            return Contract.query.filter_by(id=id).first()
        except SQLAlchemyError as e:
            logger.error(f"Error al obtener contrato por ID: {str(e)}")
            return None

    def create_new_contract(self, data):
        try:
            if data:
                new_contract = Contract.create_new_contract(data)
                return new_contract
            return None
        except SQLAlchemyError as e:
            logger.error(f"Error al crear contrato: {str(e)}")
            return None
    def update_contract_by_id(self, id, data):
        logger.info(f"Updating contract with id: {id} and data: {data}")
        try:
            contract = Contract.query.filter_by(id=id).first()
            if not contract:
                return None
            for key, value in data.items():
                if hasattr(contract, key):
                    setattr(contract, key, value)
            db.session.commit()
            return contract
        except SQLAlchemyError as e:
            logger.error(f"Error al actualizar contrato: {str(e)}")
            return None