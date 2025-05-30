from registry import task_registry, func_dependency_map
from callbacks import handle_callback

class TaskRunner:
    def __init__(self):
        self.tasks = task_registry
        self.func_dependency = func_dependency_map

    def resolve_dependencies(self, task_name):
        visited = set()
        visiting = set()
        result = []
        def dfs(name):
            if name in visiting:
                raise ValueError("Cycle detected.")
            if name in visited:
                return
            visiting.add(name)
            for upstream_name in self.func_dependency[self.tasks[name].func]:
                dfs(upstream_name)
            visiting.discard(name)
            visited.add(name)
            result.append(name)
        dfs(task_name)
        result.pop()
        return result

    def run_task(self, task_name):
        result = self.resolve_dependencies(task_name)
        result.append(task_name)
        for name in result:
            try:
                self.tasks[name].run()
                if self.tasks[name].status == "SUCCESS":
                    handle_callback("success", name)
                else:
                    handle_callback("failure", name)
            except:
                handle_callback("failure", name)
