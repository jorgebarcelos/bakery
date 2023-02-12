from typing import Dict, List
from src.models.models import Client
from src.models.repositories.clients_repository import client_repository


class ClientRegister:
    def insert(self, new_client_information: Dict) -> Dict:
        try:
            client = self.create_client_entity(new_client_information)
            self.registry_client(client)
            response = self.format_response(new_client_information)
            return response
        except KeyError:
            return {"success": False, "error": "Error in insert client"}

    def create_client_entity(self, new_client_information: Dict):
        name = new_client_information['name']
        phone = new_client_information['phone']
        state = new_client_information['state']
        client = Client(name, phone, state)
        return client

    def registry_client(self, client: any):
        client_repository.insert_client(client)

    def format_response(self, new_client_information: Dict) -> Dict:
        return {
            "success": True,
            "attributes": {
                "registry": 1,
                "name": new_client_information["name"],
                "phone": new_client_information["phone"],
                "state": new_client_information["state"],
            },
        }
