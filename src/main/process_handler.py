from src.main.constructor.introduction_process import introduction_process
from src.main.constructor.client_register_constructor import client_register_proccess
from src.main.constructor.client_list_creator_proccess import client_list_creator_proccess


def start():
    while True:
        command = introduction_process()
        if command == '1':
            client_register_proccess()
        elif command == '2':
            client_list_creator_proccess()
        elif command == '6':
            exit()
        else:
            print('Error')
