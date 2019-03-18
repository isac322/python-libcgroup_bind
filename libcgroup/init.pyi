# coding: UTF-8

from ctypes import c_char_p, c_int, pointer
from typing import Type


def cgroup_init() -> c_int: ...


c_char_pp: Type[pointer[c_char_p]]


def cgroup_get_subsys_mount_point(controller: c_char_p, mount_point: c_char_pp) -> c_int: ...
