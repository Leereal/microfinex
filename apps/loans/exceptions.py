from rest_framework.exceptions import APIException


class LoanNotFound(APIException):
    status_code = 404
    deafult_detail = "The requested loan does not exist"