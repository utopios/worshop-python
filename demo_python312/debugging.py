# debugging.py

def intentional_errors():
    # 1. Missing `self` in method to demonstrate improved error messages in Python 3.12
    class ExampleClass:
        def __init__(self, value):
            self.value = value

        def display_value():  # Intentionally missing `self`
            print(self.value)

    try:
        obj = ExampleClass(10)
        obj.display_value()
    except TypeError as e:
        print("Caught error:", e)

    # 2. Referencing an undeclared module to trigger a module import error
    try:
        data = json.loads('{"name": "Alice"}')  # Intentionally missing `import json`
    except NameError as e:
        print("Caught error:", e)

# Run intentional errors to observe improved error messages
intentional_errors()