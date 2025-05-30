from registry import task, depends_on
from callbacks import on_success, on_failure
from runner import TaskRunner

@task("clean")
def clean():
    print("Cleaning.")

@task("build")
@depends_on("clean")
def build():
    print("Building.")

@task("finish")
@depends_on("build")
def finish():
    print("Finished!")

@on_success("finish")
def cheers():
    print("Congratulations.")

@on_failure("finish")
def retry():
    print("Retry.")

if __name__ == "__main__":
    runner = TaskRunner()
    runner.run_task("finish")
