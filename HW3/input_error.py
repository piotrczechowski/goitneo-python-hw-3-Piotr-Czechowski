def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except TypeError:
            return "Invalid command. Please provide name and phone number()."
        except IndexError:
            return "Wrong index number."
    return inner