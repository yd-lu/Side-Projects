# Terminal GUI Framework in Python

This is a minimal event-driven GUI framework for building terminal-based applications in Python. It mimics traditional GUI patterns with widgets, events, and reactive updates.

## Features

- Widget system: `TextBox`, `Button`, `Label`, `Dropdown`
- Event system with decorators: `@on_click`, `@on_change`, `@on_focus`
- Binding mechanism: auto-update widgets based on others
- Interactive `App.run()` loop
- Easily extensible and customizable

## Example

```python
from gui_framework.core import App
from gui_framework.widgets import TextBox, Button, Label
from gui_framework.events import on_click

app = App()
name = TextBox("name", "Enter your name")
greeting = Label("greeting", "")
submit = Button("submit", "Submit")

@on_click("submit")
def greet():
    greeting.text = f"Hello, {name.value}!"

app.add(name, submit, greeting)
app.run()
