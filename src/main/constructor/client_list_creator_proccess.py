from src.models.models import Client
from src.views.client_register_view import ClientRegisterViews
from src.controllers.client_list_creator_controller import client_list_creator
from src.controllers.client_register_controller import client_register_controller


def client_list_creator_proccess():
    client_list_view = ClientRegisterViews().registry_client_view()
    # client_list_controller = ClientListCreator()

    name = client_list_view.registry_client_view()
    print(f'EITA PESTE!!!!{name}')

    # new_client_list = client_list_view.clients_list()
    # for data in client_list_creator.get_all_clients():
    #     print(data)

    # print(response)
