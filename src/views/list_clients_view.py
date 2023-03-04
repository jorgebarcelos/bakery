from typing import Dict


class ListClientsView:
    def clients_list(self, client_list: Dict):
        clients = client_list["clients"]

        print('Clientes Encontrados: \n')

        for client in clients:
            message = f'''
                Client name: {client['name']}
                Client phone: {client['phone']}
                Client state: {client['state']}
            '''
            print(message)
