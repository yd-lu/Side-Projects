# Terminal GUI Framework in Python

This is a minimal event-driven GUI framework for building terminal-based applications in Python. It mimics traditional GUI patterns with widgets, events, and reactive updates.

## Features

- Widget system: `TextBox`, `Button`, `Label`, `Dropdown`
- Event system with decorators: `@on_click`, `@on_change`, `@on_focus`
- Binding mechanism: auto-update widgets based on others
- Interactive `App.run()` loop
- Easily extensible and customizable

## Usage Example in example_app.py

```python
from .core import App
from .widgets import TextBox, Button, Label
from .events import on_click

app = App()
name = TextBox("name", "Enter your name")
button = Button("greet", "Greet")
greeting = Label("hello", "")

@on_click("greet")
def say_hello():
    greeting.text = f"Hello, {name.value}"

app.add(name, button, greeting)
app.run()
