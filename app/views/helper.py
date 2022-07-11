def validate_input(*args: None) ->bool:
    for arg in args:
        if not arg:
            return False
    return True