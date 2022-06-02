from CoreConfig.ConfigDictionary import ConfigDictionary
# from ClientIO.SocketClient import SocketClient
# from ModuleControllingCommand.ThermalPrinter import Print
from PublicData.QueryDataHandler import QueryDataHandler
from threading import Thread
from AutoScript import AutoScript
import time
import random

class StartServing:
    def execute(self):
        self.initial_auto_script()
        # thermal_socket_client = SocketClient(
        #         server_host=ConfigDictionary.config_dict["thermal_printer"]["host"],
        #         server_port=ConfigDictionary.config_dict["thermal_printer"]["port"]
        #     )
        
        # thermal_socket_client.start_connecting()
        # Print.thermal_socket_client = thermal_socket_client

    @staticmethod
    def initial_auto_script():
        Thread(
            target=InitialAutoScript().execute,
            daemon=True
        ).start()


class InitialAutoScript:
    def __init__(self):
        self.message = ''
        self.obj = AutoScript(callback_show_message=QueryDataHandler.parking_detail_label)
        self.obj.stop = True

    def execute(self):
        QueryDataHandler.parking_detail_label('{}'.format(self.obj.script_list))
        self.start_auto_script()
        while True:
            # print(QueryDataHandler.process_status)
            if QueryDataHandler.process_status is True:
                # number = random.randrange(1,99)
                # self.message = '{}\n{}'.format(number, self.message)
                # QueryDataHandler.parking_detail_label(self.message)
                # time.sleep(0.5)
                self.obj.stop = False
            else:
                self.obj.stop = True

    def start_auto_script(self):
        Thread(
            target=self.obj.execute,
            daemon=True
        ).start()