from typing import Dict, List
from src.models.repositories.clients_repository import client_repository


class ClientListCreator:
    def create_client_list(self) -> Dict:
        try:
            client_list = self.get_all_clients()
            return self.format_response(client_list)
        except Exception as exception:
            return {'success': False, 'error': str(exception)}

    def get_all_clients() -> List:
        clients = client_repository.return_all_clients()
        if clients is []:
            raise Exception('No registred clients')
        return clients

    def format_response(self, client_list: List) -> Dict:
        return {'success': True, 'client_list': client_list}
