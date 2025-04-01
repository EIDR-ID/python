class BaseObjectException(Exception):
    """Custom exception for Base Object Builder"""
    def __init__(self, message):
        super().__init__(message)
        self.message = message