from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    __state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self.__state = state
        self.__state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def renderizar(self, next_state):
        self.__state.renderizar(next_state)


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """
    @property
    def context(self) -> Context:
        return self.__context

    @context.setter
    def context(self, context: Context) -> None:
        self.__context = context

    @abstractmethod
    def renderizar(self) -> None:
        pass
