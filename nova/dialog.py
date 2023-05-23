from random import choice
import datetime
from os import path
from nova import Config


class DialogList:
    @staticmethod
    def __load_list(name: str) -> list[str]:
        """
        Load a dialog file containing a list of strings.
        Args:
            name: The name of the file to load.

        Returns:
            A list of strings containing the file's contents.
        """
        with open(path.join(Config.dialog_dir, Config.language, name), 'r') as file:
            return file.readlines()

    @staticmethod
    def __replace_vars(text: str) -> str:
        """
        Replace variables within a string with their values.
        Args:
            text: The string to replace variables in.

        Returns:
            A new string with the variables replaced with their values.
        """
        variables = [
            ['part_of_day', DialogList.__load_list(
                'parts_of_day')[int(datetime.datetime.now().hour/6)]],
            ['user_name', Config.user_name]
        ]
        response = text
        for variable, value in variables:
            response = response.replace(variable, value)
        return response

    @staticmethod
    def get_random_greeting() -> str:
        """
        Get a random greeting from the list and replace variables within it.
        Returns:
            A string containing a random greeting.
        """
        greeting = choice(DialogList.__load_list('greeting'))
        return DialogList.__replace_vars(greeting)
