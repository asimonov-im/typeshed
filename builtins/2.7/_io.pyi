from typing import Any, Iterable, Tuple, List, Union

DEFAULT_BUFFER_SIZE = ...  # type: int


class BlockingIOError(IOError):
    characters_written = ...  # type: int

class UnsupportedOperation(ValueError, IOError): ...


class _IOBase(object):
    closed = ...  # type: getset_descriptor
    def __enter__(self) -> "_IOBase": ...
    def __exit__(self, type, value, traceback) -> bool: ...
    def __iter__(self) -> "_IOBase": ...
    def _checkClosed(self) -> None: ...
    def _checkReadable(self) -> None: ...
    def _checkSeekable(self) -> None: ...
    def _checkWritable(self) -> None: ...
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def next(self) -> str: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = ...) -> str: ...
    def readlines(self, hint: int = ...) -> List[str]: ...
    def seek(self, offset: int, whence: int = ...) -> None: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int = ...) -> int: ...
    def writable(self) -> bool: ...
    def writelines(self, lines: Iterable[str]) -> None: ...

class _BufferedIOBase(_IOBase):
    def read1(self, n: int) -> str: ...
    def read(self, n: int = ...) -> str: ...
    def readinto(self, buffer: bytearray) -> int: ...
    def write(self, s: str) -> int: ...
    def detach(self) -> "_BufferedIOBase": ...

class BufferedRWPair(_BufferedIOBase):
    def peek(self, n: int = ...) -> str: ...

class BufferedRandom(_BufferedIOBase):
    name = ...  # type: str
    raw = ...  # type: _IOBase
    mode = ...  # type: str
    def peek(self, n: int = ...) -> str: ...

class BufferedReader(_BufferedIOBase):
    name = ...  # type: str
    raw = ...  # type: _IOBase
    mode = ...  # type: str
    def peek(self, n: int = ...) -> str: ...

class BufferedWriter(_BufferedIOBase):
    name = ...  # type: str
    raw = ...  # type: _IOBase
    mode = ...  # type: str

class BytesIO(_BufferedIOBase):
    def __setstate__(self, tuple) -> None: ...
    def __getstate__(self) -> tuple: ...
    def getvalue(self) -> str: ...

class _RawIOBase(_IOBase):
    def readall(self) -> str: ...
    def read(self, n: int = ...) -> str: ...

class FileIO(_RawIOBase):
    mode = ...  # type: str
    closefd = ...  # type: bool
    def readinto(self, buffer: bytearray)-> int: ...
    def write(self, pbuf: str) -> int: ...

class IncrementalNewlineDecoder(object):
    newlines = ...  # type: AnyStr
    def decode(self, input, final) -> Any: ...
    def getstate(self) -> Tuple[Any, int]: ...
    def setstate(self, state: Tuple[Any, int]) -> None: ...
    def reset(self) -> None: ...

class _TextIOBase(_IOBase):
    errors = ...  # type: Optional[]
    newlines = ...  # type: AnyStr
    encoding = ...  # type: Optional[]
    def read(self, n: int = ...) -> str: ...
    def write(self): ...
    def detach(self): ...

class StringIO(_TextIOBase):
    line_buffering = ...  # type: bool
    def getvalue(self) -> str: ...
    def __setstate__(self, state: tuple): ...
    def __getstate__(self) -> tuple: ...

class TextIOWrapper(_TextIOBase):
    name = ...  # type: str
    line_buffering = ...  # type: bool
    buffer = ...  # type: str
    _CHUNK_SIZE = ...  # type: int

def open(file: Union[int, str], mode: str = ...) -> _IOBase: ...
