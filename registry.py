from collections import defaultdict
from task import Task

task_registry = {}  # task_name -> Task instance
func_dependency_map = defaultdict(list)  # function -> list of task names it depends on

def task(name):
    def decorator(fn):
        deps = func_dependency_map[fn]
        _task = Task(name, fn)
        task_registry[name] = _task
        return fn
    return decorator

def depends_on(*deps):
    def decorator(fn):
        func_dependency_map[fn] = deps
        return fn
    return decorator
