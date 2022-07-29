import traceback
from classes.componentes.Window import Window
class StateMachine():
    def __init__(self, states_dict: dict, initial_state: str) -> None:
        self.__states_dict = states_dict
        self.__initial_state = initial_state if initial_state in self.__states_dict else list(
            self.__states_dict.keys())[0]
        self.__state = initial_state

    @property
    def initial_state(self) -> str:
        return self.__initial_state

    def __transition_to(self, new_state: str) -> None:
        if self.__state != new_state:
            self.__state = new_state

    def render_state(self, window: Window) -> None:
        try:
            current_state_instance = self.__states_dict[self.__state](
                window, self.__transition_to)
        except Exception as e:
            current_state_instance = self.__states_dict[self.__initial_state](
                window, self.__transition_to)
            print(traceback.format_exc())
        finally:
            current_state_instance.renderizar()
            return current_state_instance
