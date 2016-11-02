from typing import Any, Callable, Iterable

from eventlet.green import socket

_EnvironType = Dict[str, Any]
_WriteType = Callable[[bytes], None]
# TODO: start_response has two required parameters and one optional, we can't express
# this with Callable at the moment so I don't specify parameters at all for the time being.
_StartResponseType = Callable[..., _WriteType]
_WSGIApplicationType = Callable[[_EnvironType, _StartResponseType], Iterable[bytes]]


def server(sock: socket.socket,
           # TODO: make those (Callable, Any) more concrete
           site: _WSGIApplicationType,
           log: Any = ...,
           environ: Any = ...,
           max_size: int = ...,
           max_http_version: str = ...,
           protocol: type = ...,
           server_event: Any = ...,
           minimum_chunk_size: Any = ...,
           log_x_forwarded_for: bool = ...,
           custom_pool: Any = ...,
           keepalive: bool = ...,
           log_output: bool = ...,
           log_format: Any = ...,
           url_length_limit: Any = ...,
           debug: bool = ...,
           socket_timeout: Any = ...,
           capitalize_response_headers: bool = ...) -> None: ...
