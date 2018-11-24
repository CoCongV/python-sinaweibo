class TokenException(Exception):
    pass


class TokenExpired(TokenException):
    code = 21332
    message = "token expired"


class RequestError(Exception):
    pass
