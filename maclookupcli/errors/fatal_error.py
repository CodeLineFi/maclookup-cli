class FatalError(Exception):

    def __init__(self, code):
        self.code = code
