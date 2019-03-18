# coding: UTF-8

from ctypes import Structure, c_char_p, c_int, c_uint, pointer
from typing import Type

from . import _CtypesEnum
from .groups import CGroupPointer
from .init import c_char_pp

try:
    from enum import IntFlag
except ImportError:
    from enum import IntEnum as IntFlag


class CGFlags(_CtypesEnum, IntFlag):
    USECACHE = ...
    USE_TEMPLATE_CACHE = ...


class DaemonType(_CtypesEnum, IntFlag):
    UNCHANGE_CHILDREN = ...
    CANCEL_UNCHANGE_PROCESS = ...


# int cgroup_attach_task(struct cgroup *cgroup);
def cgroup_attach_task(cgroup: CGroupPointer) -> c_int: ...


# int cgroup_attach_task_pid(struct cgroup *cgroup, pid_t tid);
def cgroup_attach_task_pid(cgroup: CGroupPointer, tid: c_int) -> c_int: ...


# int cgroup_change_cgroup_path(const char *path, pid_t pid, const char *const controllers[]);
def cgroup_change_cgroup_path(path: c_char_p, pid: c_int, controllers: c_char_pp) -> c_int: ...


# int cgroup_get_current_controller_path(pid_t pid, const char *controller, char **current_path);
def cgroup_get_current_controller_path(pid: c_int, controller: c_char_p, current_path: c_char_pp) -> c_int: ...


# int cgroup_init_rules_cache(void);
def cgroup_init_rules_cache() -> c_int: ...


# int cgroup_reload_cached_rules(void);
def cgroup_reload_cached_rules() -> c_int: ...


class FILE(Structure):
    pass


FILE_p: Type[pointer[FILE]]


# void cgroup_print_rules_config(FILE *fp);
def cgroup_print_rules_config(fp: FILE_p) -> None: ...


# int cgroup_change_all_cgroups(void);
def cgroup_change_all_cgroups() -> c_int: ...


# int cgroup_change_cgroup_flags(uid_t uid, gid_t gid, const char *procname, pid_t pid, int flags);
def cgroup_change_cgroup_flags(uid: c_uint, gid: c_uint, procname: c_char_p, pid: c_int, flags: c_int) -> c_int: ...


# int cgroup_change_cgroup_uid_gid_flags(uid_t uid, gid_t gid, pid_t pid, int flags);
def cgroup_change_cgroup_uid_gid_flags(uid: c_uint, gid: c_uint, pid: c_int, flags: c_int) -> c_int: ...


# int cgroup_change_cgroup_uid_gid(uid_t uid, gid_t gid, pid_t pid);
def cgroup_change_cgroup_uid_gid(uid: c_uint, gid: c_uint, pid: c_int) -> c_int: ...


# int cgroup_register_unchanged_process(pid_t pid, int flags);
def cgroup_register_unchanged_process(pid: c_int, flags: c_int) -> c_int: ...
