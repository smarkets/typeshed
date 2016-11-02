from typing import Tuple

from eventlet.green import socket

def listen(addr: Tuple[str, int], family: int = ..., backlog: int = ...) -> socket.socket: ...
