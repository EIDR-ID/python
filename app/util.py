def attempt(func):
    try:
        return func(), None
    except Exception as e:
        return None, e
