from .state import bindings, current_app
from .events import trigger, on_change
from .widgets import TextBox, Dropdown


def reset(app):
    """
    Reset all input widgets in the app to their default state.
    """
    for widget in app.widgets:
        if isinstance(widget, TextBox) or isinstance(widget, Dropdown):
            widget.value = None


class App:
    """
    Main application container.
    Handles widget registration, rendering, and event loop.
    """
    def __init__(self):
        global current_app
        self.widgets = []
        current_app = self

    def add(self, *components):
        """
        Register UI components (widgets) to the app.
        """
        self.widgets.extend(components)

    def render(self):
        """
        Print the current state of all widgets.
        """
        print("\n" + "-" * 40)
        for widget in self.widgets:
            if hasattr(widget, "value"):
                print(f"[{widget.id}] {widget.placeholder if hasattr(widget, 'placeholder') else widget.prompt}: {widget.value}")
            elif hasattr(widget, "label"):
                print(f"[{widget.id}] {widget.label} — Press ENTER to click")
            elif hasattr(widget, "text"):
                print(f"[{widget.id}] {widget.text}")
        print("-" * 40)

    def run(self):
        """
        Main app loop: prompt user input and dispatch events.
        """
        for widget in self.widgets:
            if isinstance(widget, TextBox):
                trigger(widget.id, "focus")
                widget.value = input(f"[{widget.id}] {widget.placeholder}: ")

            elif hasattr(widget, "label"):  # Button
                input(f"[{widget.id}] {widget.label} — Press ENTER to click")
                trigger(widget.id, "click")

            elif hasattr(widget, "text"):  # Label
                print(f"[{widget.id}] {widget.text}")

            elif isinstance(widget, Dropdown):
                trigger(widget.id, "focus")
                opts = ", ".join(f"{i}: {opt}" for i, opt in enumerate(widget.options))
                raw = input(f"[{widget.id}] {widget.prompt} ({opts}): ")
                try:
                    idx = int(raw)
                    if 0 <= idx < len(widget.options):
                        widget.value = widget.options[idx]
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Please enter a number.")

        # Listen for reset command
        while True:
            cmd = input("Type 'reset' to reset, or 'exit' to quit: ").strip().lower()
            if cmd == "reset":
                reset(self)
                self.run()
                break
            elif cmd == "exit":
                break


def bind(source_widget, target_widget, transform):
    """
    Bind the value of `source_widget` to update `target_widget.text`
    using the given `transform` function.
    """
    bindings.append((source_widget.id, target_widget, transform))

    @on_change(source_widget.id)
    def _binding_callback():
        new_value = transform(source_widget.value)
        target_widget.text = new_value
