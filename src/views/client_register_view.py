import os
from typing import Dict


class ClientRegisterViews:
    def registry_client_view(self) -> str:
        self.__clear()

        print('Insert new client \n\n')
        name = input('Type the client name: ')
        phone = input('Type the client phone: ')
        state = input('Type the client state: ')

        new_client_informations = {'name': name, 'phone': phone, 'state': state}
        return new_client_informations

    def registry_client_success(self, client_registry: Dict) -> None:
        self.__clear()

        message = f'''
        Client registred
        * Infos:
            Client Name: {client_registry['name']},
            Client Phone: {client_registry['phone']},
            Client State: {client_registry['state']},
        '''
        print(message)

    def registry_client_fail(self, error: str) -> None:
        self.__clear()

        message = f'''
            Erro on insert client
            {error}
        '''
        print(message)

    def __clear(self):
        os.system('cls || clear')
