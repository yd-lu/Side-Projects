# Task Runner Framework

A minimal Python framework for defining and executing tasks with dependency resolution and callbacks—like a simplified `make`.

## Features

- Define tasks using decorators: `@task(name)`
- Set dependencies: `@depends_on(...)`
- Add success/failure callbacks: `@on_success`, `@on_failure`
- Run tasks with automatic topological ordering

## Usage

### Define tasks
```python
@task("clean")
def clean():
    print("Cleaning.")

@task("build")
@depends_on("clean")
def build():
    print("Building.")
```

### Run from script
```python
runner = TaskRunner()
runner.run_task("build")
```

### Example in example_tasks.py
Run:

```bash
python example_tasks.py
```

You'll see:
```
Cleaning.
Building.
Finished!
Congratulations.
```
