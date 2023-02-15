from typing import List


class ClientRepository:
    def __init__(self) -> None:
        self.client_list = []

    def insert_client(self, client: any):
        self.client_list.append(client)
        print(self.client_list)

    def return_all_clients(self) -> List:
        return self.client_list


client_repository = ClientRepository()
