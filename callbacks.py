from collections import defaultdict

callbacks = defaultdict(list)  # "success" or "failure" -> list of (task_name, fn)

def on_success(task_name):
    def decorator(fn):
        callbacks["success"].append((task_name, fn))
        return fn
    return decorator

def on_failure(task_name):
    def decorator(fn):
        callbacks["failure"].append((task_name, fn))
        return fn
    return decorator

def handle_callback(event, task_name):
    for name, fn in callbacks[event]:
        if name == task_name:
            fn()
