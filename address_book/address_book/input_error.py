def input_error(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError as e:
            print("Error:", e)
            return "invalid"
        except TypeError:
            return "Invalid command. Please provide name and phone number"
    return inner
