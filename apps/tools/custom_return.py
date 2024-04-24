from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status


class CustomResponse(Response):
    """
    A custom response class for Django REST Framework that adds a `status_code`
    attribute to the response data.
    """
    def __init__(self, msg="Exitoso", data={}, status_code=200, **kwargs):
        data = {'type': 'success', 'data': data, 'msg':msg, 'status':status_code}
        super().__init__(data, **kwargs)


class CustomAPIException(APIException):
    """CustomValidationAPIException.

    Esta excepción retorna un Response, por ejemplo, como lo hace el raise serializers.ValidationError
    de un serializador invocado desde una Vista.
    """

    def __init__(self, message, data={}, status_code=status.HTTP_400_BAD_REQUEST):
        self.detail = {'type': 'error', 'data': data, 'msg':message}
        
        super(CustomAPIException, self).__init__()

