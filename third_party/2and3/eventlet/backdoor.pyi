from typing import Any, Dict

from eventlet.green import socket

def backdoor_server(sock: socket.socket, locals: Dict[str, Any] = ...) -> None: ...
