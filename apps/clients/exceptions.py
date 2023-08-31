from rest_framework.exceptions import APIException


class ClientNotFound(APIException):
    status_code = 404
    deafult_detail = "The requested client does not exist"