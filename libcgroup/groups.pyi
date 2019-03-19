# coding: UTF-8

from ctypes import Structure, c_bool, c_char_p, c_int, c_int64, c_uint, c_uint64, pointer
from typing import Type

from .init import c_char_pp
from .iterators import c_int_p

try:
    from enum import IntFlag
except ImportError:
    from enum import IntEnum as IntFlag

from . import _CtypesEnum


class DeleteFlag(_CtypesEnum, IntFlag):
    IGNORE_MIGRATION = ...
    RECURSIVE = ...
    EMPTY_ONLY = ...


class CGroup(Structure):
    pass


CGroupPointer: Type[pointer[CGroup]]
CGroupDoublePointer: Type[pointer[CGroupPointer]]


class CGroupController(Structure):
    pass


CGroupControllerPointer: Type[pointer[CGroupController]]


# struct cgroup *cgroup_new_cgroup(const char *name);
def cgroup_new_cgroup(name: c_char_p) -> CGroupPointer: ...


# struct cgroup_controller *cgroup_add_controller(struct cgroup *cgroup, const char *name);
def cgroup_add_controller(cgroup: CGroupPointer, name: c_char_p) -> CGroupControllerPointer: ...


# struct cgroup_controller *cgroup_get_controller(struct cgroup *cgroup, const char *name);
def cgroup_get_controller(cgroup: CGroupPointer, name: c_char_p) -> CGroupControllerPointer: ...


# void cgroup_free(struct cgroup **cgroup);
def cgroup_free(cgroup: CGroupDoublePointer) -> None: ...


# void cgroup_free_controllers(struct cgroup *cgroup);
def cgroup_free_controllers(cgroup: CGroupPointer) -> None: ...


# int cgroup_create_cgroup(struct cgroup *cgroup, int ignore_ownership);
def cgroup_create_cgroup(cgroup: CGroupPointer, ignore_ownership: c_int) -> c_int: ...


# int cgroup_create_cgroup_from_parent(struct cgroup *cgroup, int ignore_ownership);
def cgroup_create_cgroup_from_parent(cgroup: CGroupPointer, ignore_ownership: c_int) -> c_int: ...


# int cgroup_modify_cgroup(struct cgroup *cgroup);
def cgroup_modify_cgroup(cgroup: CGroupPointer) -> c_int: ...


# int cgroup_delete_cgroup(struct cgroup *cgroup, int ignore_migration);
def cgroup_delete_cgroup(cgroup: CGroupPointer, ignore_ownership: c_int) -> c_int: ...


# int cgroup_delete_cgroup_ext(struct cgroup *cgroup, int flags);
def cgroup_delete_cgroup_ext(cgroup: CGroupPointer, flags: c_int) -> c_int: ...


# int cgroup_get_cgroup(struct cgroup *cgroup);
def cgroup_get_cgroup(cgroup: CGroupPointer) -> c_int: ...


# int cgroup_copy_cgroup(struct cgroup *dst, struct cgroup *src);
def cgroup_copy_cgroup(dst: CGroupPointer, src: CGroupPointer) -> c_int: ...


# int cgroup_compare_cgroup(struct cgroup *cgroup_a, struct cgroup *cgroup_b);
def cgroup_compare_cgroup(cgroup_a: CGroupPointer, cgroup_b: CGroupPointer) -> c_int: ...


# int cgroup_compare_controllers(struct cgroup_controller *cgca, struct cgroup_controller *cgcb);
def cgroup_compare_controllers(cgca: CGroupPointer, cgcb: CGroupPointer) -> c_int: ...


# int cgroup_set_uid_gid(struct cgroup *cgroup, uid_t tasks_uid, gid_t tasks_gid, uid_t control_uid, gid_t control_gid);
def cgroup_set_uid_gid(cgroup: CGroupPointer, tasks_uid: c_uint,
                       tasks_gid: c_uint, control_uid: c_uint, control_gid: c_uint) -> c_int: ...


c_uint_p: Type[pointer[c_uint]]


# int cgroup_get_uid_gid(struct cgroup *cgroup, uid_t *tasks_uid, gid_t *tasks_gid,
#                        uid_t *control_uid, gid_t *control_gid);
def cgroup_get_uid_gid(cgroup: CGroupPointer, tasks_uid: c_uint_p, tasks_gid: c_uint_p,
                       control_uid: c_uint_p, control_gid: c_uint_p) -> c_int: ...


# void cgroup_set_permissions(struct cgroup *cgroup, mode_t control_dperm, mode_t control_fperm, mode_t task_fperm);
def cgroup_set_permissions(cgroup: CGroupPointer, control_dperm: c_uint_p,
                           control_fperm: c_uint_p, task_fperm: c_uint_p) -> None: ...


# int cgroup_add_value_string(struct cgroup_controller *controller, const char *name, const char *value);
def cgroup_add_value_string(controller: CGroupControllerPointer, name: c_char_p, value: c_char_p) -> c_int: ...


# int cgroup_add_value_int64(struct cgroup_controller *controller, const char *name, int64_t value);
def cgroup_add_value_int64(controller: CGroupControllerPointer, name: c_char_p, value: c_int64) -> c_int: ...


# int cgroup_add_value_uint64(struct cgroup_controller *controller, const char *name, u_int64_t value);
def cgroup_add_value_uint64(controller: CGroupControllerPointer, name: c_char_p, value: c_uint64) -> c_int: ...


# int cgroup_add_value_bool(struct cgroup_controller *controller, const char *name, bool value);
def cgroup_add_value_bool(controller: CGroupControllerPointer, name: c_char_p, value: c_bool) -> c_int: ...


# int cgroup_get_value_string(struct cgroup_controller *controller, const char *name, char **value);
def cgroup_get_value_string(controller: CGroupControllerPointer, name: c_char_p, value: c_char_pp) -> c_int: ...


c_int64_p: Type[pointer[c_int64]]


# int cgroup_get_value_int64(struct cgroup_controller *controller, const char *name, int64_t *value);
def cgroup_get_value_int64(controller: CGroupControllerPointer, name: c_char_p, value: c_int64_p) -> c_int: ...


c_uint64_p: Type[pointer[c_uint64]]


# int cgroup_get_value_uint64(struct cgroup_controller *controller, const char *name, u_int64_t *value);
def cgroup_get_value_uint64(controller: CGroupControllerPointer, name: c_char_p, value: c_uint64_p) -> c_int: ...


c_bool_p: Type[pointer[c_bool]]


# int cgroup_get_value_bool(struct cgroup_controller *controller, const char *name, bool *value);
def cgroup_get_value_bool(controller: CGroupControllerPointer, name: c_char_p, value: c_bool_p) -> c_int: ...


# int cgroup_set_value_string(struct cgroup_controller *controller, const char *name, const char *value);
def cgroup_set_value_string(controller: CGroupControllerPointer, name: c_char_p, value: c_char_p) -> c_int: ...


# int cgroup_set_value_int64(struct cgroup_controller *controller, const char *name, int64_t value);
def cgroup_set_value_int64(controller: CGroupControllerPointer, name: c_char_p, value: c_int64) -> c_int: ...


# int cgroup_set_value_uint64(struct cgroup_controller *controller, const char *name, u_int64_t value);
def cgroup_set_value_uint64(controller: CGroupControllerPointer, name: c_char_p, value: c_uint64) -> c_int: ...


# int cgroup_set_value_bool(struct cgroup_controller *controller, const char *name, bool value);
def cgroup_set_value_bool(controller: CGroupControllerPointer, name: c_char_p, value: c_bool) -> c_int: ...


# int cgroup_get_value_name_count(struct cgroup_controller *controller);
def cgroup_get_value_name_count(controller: CGroupControllerPointer) -> c_int: ...


# char *cgroup_get_value_name(struct cgroup_controller *controller, int index);
def cgroup_get_value_name(controller: CGroupControllerPointer, index: c_int) -> c_char_p: ...


c_int_pp: Type[pointer[c_int_p]]


# int cgroup_get_procs(char *name, char *controller, pid_t **pids, int *size);
def cgroup_get_procs(name: c_char_p, controller: c_char_p, pids: c_int_pp, size: c_int_p) -> c_int: ...


# int cg_chmod_recursive(struct cgroup *cgroup, mode_t dir_mode, int dirm_change, mode_t file_mode, int filem_change);
def cg_chmod_recursive(cgroup: CGroupPointer, dir_mode: c_uint, dirm_change: c_int,
                       file_mode: c_uint, filem_change: c_int) -> c_int: ...


# TODO: undefined
# char *cgroup_get_cgroup_name(struct cgroup *cgroup);
# def cgroup_get_cgroup_name(cgroup: CGroupPointer) -> c_char_p: ...
