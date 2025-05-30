# Event registry mapping event types and widget IDs to callbacks
_event_registry = {
    "click": {},
    "change": {},
    "focus": {},
    "reset": {}  # optional use
}


def command(name):
    """
    Register a top-level command (like 'reset') to a function.
    """
    def decorator(fn):
        _event_registry[name] = fn
        return fn
    return decorator


def on_click(widget_id):
    def decorator(callback_fn):
        _event_registry["click"][widget_id] = callback_fn
        return callback_fn
    return decorator


def on_change(widget_id):
    def decorator(callback_fn):
        _event_registry["change"][widget_id] = callback_fn
        return callback_fn
    return decorator


def on_focus(widget_id):
    def decorator(callback_fn):
        _event_registry["focus"][widget_id] = callback_fn
        return callback_fn
    return decorator


def trigger(widget_id, way):
    """
    Trigger the registered callback for the widget/event.
    """
    if widget_id in _event_registry[way]:
        _event_registry[way][widget_id]()
    elif way == "click":
        print(f"[Warning] No callback registered for click event on '{widget_id}'")
