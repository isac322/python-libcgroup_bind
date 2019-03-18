# coding: UTF-8

from ctypes import c_char_p, c_int

from .groups import CGroupPointer


# int cgroup_config_load_config(const char *pathname);
def cgroup_config_load_config(pathname: c_char_p) -> c_int: ...


# int cgroup_unload_cgroups(void);
def cgroup_unload_cgroups() -> c_int: ...


# int cgroup_config_unload_config(const char *pathname, int flags);
def cgroup_config_unload_config(pathname: c_char_p, flags: c_int) -> c_int: ...


# int cgroup_config_set_default(struct cgroup *new_default);
def cgroup_config_set_default(new_default: CGroupPointer) -> c_int: ...


# int cgroup_init_templates_cache(char *pathname);
def cgroup_init_templates_cache(pathname: c_char_p) -> c_int: ...


# int cgroup_reload_cached_templates(char *pathname);
def cgroup_reload_cached_templates(pathname: c_char_p) -> c_int: ...


# int cgroup_config_create_template_group(struct cgroup *cgroup, char *template_name, int flags);
def cgroup_config_create_template_group(cgroup: CGroupPointer, template_name: c_char_p, flags: c_int) -> c_int: ...
