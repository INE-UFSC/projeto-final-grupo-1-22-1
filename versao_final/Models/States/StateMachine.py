class StateMachine():
    def __init__(self, states_dict, initial_state):
        self.__states_dict = states_dict
        self.__initial_state = initial_state if initial_state in self.__states_dict else list(
            self.__states_dict.keys())[0]
        self.__state = initial_state

    @property
    def initial_state(self):
        return self.__initial_state

    def transition_to(self, new_state):
        if self.__state != new_state:
            self.__state = new_state

    def render_state(self, window):
        try:
            current_state_instance = self.__states_dict[self.__state](
                window, self.transition_to)
        except:
            current_state_instance = self.__states_dict[self.__initial_state](
                window, self.transition_to)
        finally:
            current_state_instance.renderizar()
            return current_state_instance
