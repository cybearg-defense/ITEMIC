import logging
import json

from typing import Any, Union
from copy import deepcopy


class jdict(dict):
    """
    The class gives access to the dictionary through the attribute  name.
    """
    def __getattr__(self, name: str) -> Union[Any]:
        try:
            return self.__getitem__(name)
        except KeyError:
            raise AttributeError(name + ' not in dict')

    def __setattr__(self, key: str, value: Any) -> None:
        self.__setitem__(key, value)

    def __deepcopy__(self, memo):
        return jdict((k, deepcopy(v, memo)) for k, v in self.items())


json._default_decoder = json.JSONDecoder(object_pairs_hook=jdict)


class ItemicCore(dict):
    def __init__(self, logger: logging.Logger = None, **kwargs):
        super().__init__(**kwargs)
        self._itemic_logger = logger

    def __getattr__(self, name: str) -> Union[Any]:
        try:
            return self.__getitem__(name)
        except KeyError:
            raise AttributeError(name + ' not in dict')

    def __setattr__(self, key: str, value: Any) -> None:
        self.__setitem__(key, value)

    def __deepcopy__(self, memo):
        return jdict((k, deepcopy(v, memo)) for k, v in self.items())

    @property  # this logger is intended for use only within the class
    def _itemic_logger(self) -> logging.Logger:
        return self._itemic_logger

    @_itemic_logger.setter
    def _itemic_logger(self, value: str):
        if isinstance(value, str):
            self._itemic_logger = value


class ItemicData(ItemicCore):
    _default_dict = {}

    def __init__(self, itemic_json: str = None, itemic_dict: dict = None, **kwargs):
        super().__init__(**kwargs)
        self._itemic_json = itemic_json
        self._itemic_dict = itemic_dict

    @property
    def itemic_dict(self) -> dict:
        if not self._itemic_dict:
            self._itemic_dict = self._default_dict
        return self._itemic_dict

    @itemic_dict.setter
    def itemic_dict(self, value: dict):
        try:
            json.dumps(value)
            self.itemic_dict = value
        except Exception as e:
            self._itemic_logger.error(f"Unexpected error setting ITEMic dict", e)
            raise

    @property
    def itemic_json(self) -> str:
        return json.dumps(self._itemic_dict)

    @itemic_json.setter
    def itemic_json(self, value: str):
        try:
            self._itemic_dict = json.loads(value)
        except Exception as e:
            self._itemic_logger.error(f"Unexpected error setting ITEMic JSON", e)
            raise


class ItemicHandler(ItemicCore):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def itemic_scan(self):
        raise NotImplementedError
