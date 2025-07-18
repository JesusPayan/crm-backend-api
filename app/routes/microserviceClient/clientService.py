from logger import logger
from models import Client
from datetime import datetime
class ClientService:
    
    def create_new_client(self,data):
        logger.info(f"Creating new client: {data}")
        #return self.client_repository.save(client)
        #validatinf input data
        saved_client = Client.create_new_client(data)
        if saved_client:
            return saved_client
        else:
            return None      
    
    def get_all_clients(self):
        logger.info("Getting all clients service")
        return Client.get_all()
    def get_client_by_id(self,id):
        logger.info(f"Getting client by id: {id}")
        return Client.get_by_id(id)
    def update_client(self,id,data):
        logger.info(f"Updating client by id: {id}")
        return Client.update_client(id,data)    
    def delete_client(self,id):
        logger.info(f"Deleting client by id: {id}")
        return Client.delete_client(id)