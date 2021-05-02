class SetSettings:
    def __init__(self, token: str, version: int = 1):
        self.token: str = token
        self.version: int = version
        self.headers: dict = dict(Authorization=self.token)
        self.url: str = 'http://devapi.set.uz'
        self.main_api: str = f'{self.url}/api/v{self.version}/integration'
