# coding: UTF-8

from ctypes import Structure, c_char_p, c_int, c_short, c_void_p, pointer
from dataclasses import dataclass
from enum import IntEnum
from typing import Type

from . import _CtypesEnum


class WalkType(_CtypesEnum, IntEnum):
    PRE_DIR = ...
    POST_DIR = ...


class FileType(_CtypesEnum, IntEnum):
    FILE = ...
    DIR = ...
    OTHER = ...


@dataclass
class FileInfo(Structure):
    type: FileType = ...
    path: c_char_p = ...
    parent: c_char_p = ...
    full_path: c_char_p = ...
    depth: c_short = ...


c_void_pp: Type[pointer[c_void_p]]
c_int_p: Type[pointer[c_int]]
FileInfoPointer: Type[pointer[FileInfo]]


# int cgroup_walk_tree_begin(const char *controller, const char *base_path, int depth,
#                            void **handle, struct cgroup_file_info *info, int *base_level);
def cgroup_walk_tree_begin(controller: c_char_p, base_path: c_char_p, depth: c_int,
                           handle: c_void_pp, info: FileInfoPointer, base_level: c_int_p) -> c_int: ...


# int cgroup_walk_tree_next(int depth, void **handle, struct cgroup_file_info *info, int base_level);
def cgroup_walk_tree_next(depth: c_int, handle: c_void_pp, info: FileInfoPointer, base_level: c_int) -> c_int: ...


# int cgroup_walk_tree_end(void **handle);
def cgroup_walk_tree_end(handle: c_void_pp) -> c_int: ...


# int cgroup_walk_tree_set_flags(void **handle, int flags);
def cgroup_walk_tree_set_flags(handle: c_void_pp, flags: c_int) -> c_int: ...


# int cgroup_read_value_begin(const char *controller, const char *path,
#                             char *name, void **handle, char *buffer, int max);
def cgroup_read_value_begin(controller: c_char_p, path: c_char_p, name: c_char_p,
                            handle: c_void_pp, buffer: c_char_p, max: c_int) -> c_int: ...


# int cgroup_read_value_next(void **handle, char *buffer, int max);
def cgroup_read_value_next(handle: c_void_pp, buffer: c_char_p, max: c_int) -> c_int: ...


# int cgroup_read_value_end(void **handle);
def cgroup_read_value_end(handle: c_void_pp) -> c_int: ...


@dataclass
class Stat(Structure):
    name: c_char_p = ...
    value: c_char_p = ...


StatPointer: Type[pointer[Stat]]


# int cgroup_read_stats_begin(const char *controller, const char *path, void **handle, struct cgroup_stat *stat);
def cgroup_read_stats_begin(controller: c_char_p, path: c_char_p, handle: c_void_pp, stat: StatPointer) -> c_int: ...


# int cgroup_read_stats_next(void **handle, struct cgroup_stat *stat);
def cgroup_read_stats_next(handle: c_void_pp, stat: StatPointer) -> c_int: ...


# int cgroup_read_stats_end(void **handle);
def cgroup_read_stats_end(handle: c_void_pp) -> c_int: ...


# int cgroup_get_task_begin(const char *cgroup, const char *controller, void **handle, pid_t *pid);
def cgroup_get_task_begin(cgroup: c_char_p, controller: c_char_p, handle: c_void_pp, pid: c_int_p) -> c_int: ...


# int cgroup_get_task_next(void **handle, pid_t *pid);
def cgroup_get_task_next(handle: c_void_pp, pid: c_int_p) -> c_int: ...


# int cgroup_get_task_end(void **handle);
def cgroup_get_task_end(handle: c_void_pp) -> c_int: ...


@dataclass
class MountPoint(Structure):
    name: c_char_p = ...
    path: c_char_p = ...


MountPointPointer: Type[pointer[MountPoint]]


# int cgroup_get_controller_begin(void **handle, struct cgroup_mount_point *info);
def cgroup_get_controller_begin(handle: c_void_pp, info: MountPointPointer) -> c_int: ...


# int cgroup_get_controller_next(void **handle, struct cgroup_mount_point *info);
def cgroup_get_controller_next(handle: c_void_pp, info: MountPointPointer) -> c_int: ...


# int cgroup_get_controller_end(void **handle);
def cgroup_get_controller_end(handle: c_void_pp) -> c_int: ...


@dataclass
class ControllerData(Structure):
    name: c_char_p = ...
    hierarchy: c_int = ...
    num_cgroups: c_int = ...
    enabled: c_int = ...


ControllerDataPointer: Type[pointer[ControllerData]]


# int cgroup_get_all_controller_begin(void **handle, struct controller_data *info);
def cgroup_get_all_controller_begin(handle: c_void_pp, info: ControllerDataPointer) -> c_int: ...


# int cgroup_get_all_controller_next(void **handle, struct controller_data *info);
def cgroup_get_all_controller_next(handle: c_void_pp, info: ControllerDataPointer) -> c_int: ...


# int cgroup_get_all_controller_end(void **handle);
def cgroup_get_all_controller_end(handle: c_void_pp) -> c_int: ...


# int cgroup_get_subsys_mount_point_begin(const char *controller, void **handle, char *path);
def cgroup_get_subsys_mount_point_begin(controller: c_char_p, handle: c_void_pp, path: c_char_p) -> c_int: ...


# int cgroup_get_subsys_mount_point_next(void **handle, char *path);
def cgroup_get_subsys_mount_point_next(handle: c_void_pp, path: c_char_p) -> c_int: ...


# int cgroup_get_subsys_mount_point_end(void **handle);
def cgroup_get_subsys_mount_point_end(handle: c_void_pp) -> c_int: ...
