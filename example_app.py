app = App()
name = TextBox("name", "Enter your name")
button = Button("greet", "Greet")
greeting = Label("hello", "")

@on_click("greet")
def say_hello():
    greeting.text = f"Hello, {name.value}"

app.add(name, button, greeting)
app.run()
