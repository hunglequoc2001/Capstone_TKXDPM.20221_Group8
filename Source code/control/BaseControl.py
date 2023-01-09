from abc import ABC, abstractmethod

class BaseControl(ABC):
    def __init__(self,view):
        super().__init__()
        self.view=view
