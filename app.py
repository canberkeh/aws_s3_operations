from base_modules.base import BaseObject, command_sleep
from utilities.utilities import Utilities

class Main():
    def __init__(self) -> None:
        self.utilities = Utilities(BaseObject)
        self.command_sleep = command_sleep
