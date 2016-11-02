from typing import Any, Callable, Union

from eventlet.wsgi import _WSGIApplicationType


class WebSocket:
    path = ...  # type: str
    def send(self, message: Union[bytes, str]) -> None: ...
    def wait(self) -> Union[bytes, str]: ...
    def close(self) -> None: ...

class WebSocketWSGI:
    def __init__(self, handler: Callable[[WebSocket], Any]) -> None: ...
    __call__ = ...  # type: _WSGIApplicationType
