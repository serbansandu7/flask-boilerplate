
class InvalidCredentials(Exception):
    def __init__(self, *args, **kwargs):
        self.status = kwargs["status"]
        del kwargs["status"]
        super().__init__(*args, **kwargs)
