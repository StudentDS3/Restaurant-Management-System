
class InvalidUserException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidPasswordException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidEmailException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidTypeException(Exception):
    def __init__(self, message):
        super().__init__(message)

