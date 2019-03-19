# coding: UTF-8

from ctypes import CFUNCTYPE, c_char_p, c_int, c_void_p
from enum import IntEnum
from typing import Any, Union

from . import _CtypesEnum


class LogLevel(_CtypesEnum, IntEnum):
    ERROR = ...
    WARNING = ...
    INFO = ...
    DEBUG = ...


# typedef void (*cgroup_logger_callback)(void *userdata, int level, const char *fmt, va_list ap);
cgroup_logger_callback = CFUNCTYPE(c_void_p, c_int, c_char_p, c_void_p)


# extern void cgroup_set_logger(cgroup_logger_callback logger, int loglevel, void *userdata);
def cgroup_set_logger(logger: cgroup_logger_callback, loglevel: Union[c_int, int], userdata: c_void_p) -> None: ...


# extern void cgroup_set_default_logger(int loglevel);
def cgroup_set_default_logger(loglevel: Union[c_int, int]) -> None: ...


# extern void cgroup_set_loglevel(int loglevel);
def cgroup_set_loglevel(loglevel: Union[c_int, int]) -> None: ...


# TODO: replace Any
# extern void cgroup_log(int loglevel, const char *fmt, ...);
def cgroup_log(loglevel: Union[c_int, int], fmt: Union[c_char_p, bytes], *args: Any) -> None: ...


# extern int cgroup_parse_log_level_str(const char *levelstr);
def cgroup_parse_log_level_str(level_str: Union[c_char_p, bytes]) -> Union[c_int, int]: ...
