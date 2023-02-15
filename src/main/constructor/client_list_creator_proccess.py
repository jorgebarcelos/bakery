from src.views.client_register_view import ClientRegisterViews
from src.controllers.client_register_controller import ClientRegisterController


def client_list_creator_proccess():
    client_register_views = ClientRegisterViews()
    client_register_controller = ClientRegisterController()

    new_client_information = client_register_views.registry_client_view()
    response = client_register_controller.insert(new_client_information)
    if response['success']:
        client_register_views.registry_client_success(response["attributes"])
    else:
        client_register_views.registry_client_fail(response["error"])
