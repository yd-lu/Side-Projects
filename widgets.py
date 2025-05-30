from .state import current_app
from .events import trigger


class Widget:
    def __init__(self):
        global current_app
        self.id = None
        if current_app is not None:
            current_app.widgets.append(self)


class TextBox(Widget):
    def __init__(self, widget_id, placeholder_text):
        super().__init__()
        self.id = widget_id
        self.placeholder = placeholder_text
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val
        trigger(self.id, "change")


class Button(Widget):
    def __init__(self, widget_id, display_label):
        super().__init__()
        self.id = widget_id
        self.label = display_label


class Label(Widget):
    def __init__(self, widget_id, text):
        super().__init__()
        self.id = widget_id
        self.text = text


class Dropdown(Widget):
    def __init__(self, widget_id, prompt, options):
        super().__init__()
        self.id = widget_id
        self.prompt = prompt
        self.options = options
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val
        trigger(self.id, "change")
