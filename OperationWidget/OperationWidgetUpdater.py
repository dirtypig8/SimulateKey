from abc import ABCMeta


class StateHandlerInterface(metaclass=ABCMeta):
    next_widget = str()
    previous_widget = str()
    index_widget = str()

    def handle_command(self, command):
        if command == "next":
            OperationWidgetUpdater.operation_widget.update_current_widget_by_name(self.next_widget)
            OperationWidgetUpdater.set_state(self.next_widget)

        elif command == "back":
            OperationWidgetUpdater.operation_widget.update_current_widget_by_name(self.previous_widget)
            OperationWidgetUpdater.set_state(self.previous_widget)

        elif command == "index":
            OperationWidgetUpdater.operation_widget.update_current_widget_by_name(self.index_widget)
            OperationWidgetUpdater.set_state(self.index_widget)


class Index(StateHandlerInterface):
    next_widget = "input_password"
    previous_widget = "decide"
    index_widget = "decide"


class SettingWidget(StateHandlerInterface):
    next_widget = "index"
    previous_widget = "index"
    index_widget = "index"


class InputPassword(StateHandlerInterface):
    next_widget = "setting"
    previous_widget = "index"
    index_widget = "index"


state_to_state_handler_instance_dict = {
    "index": Index,
    "setting": SettingWidget,
    "input_password": InputPassword 
}


class OperationWidgetUpdater:
    operation_widget = None
    state = None
    state_in_text = str()

    @staticmethod
    def initialize_updater(operation_widget):
        OperationWidgetUpdater.operation_widget = operation_widget

    @staticmethod
    def set_state(state):
        OperationWidgetUpdater.state = state_to_state_handler_instance_dict[state]()
        OperationWidgetUpdater.state_in_text = state

    @staticmethod
    def update_widget_by_command(command):
        OperationWidgetUpdater.state.handle_command(command)

    @staticmethod
    def update_widget_to_index():
        OperationWidgetUpdater.state.handle_command("index")
