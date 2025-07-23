from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first
    response = drf_exception_handler(exc, context)

    if response is not None:
        if isinstance(response.data, dict):
            messages = []
            for key, value in response.data.items():
                if isinstance(value, list):
                    messages.extend(value)
                else:
                    messages.append(str(value))
            message = " ".join(messages)
        else:
            message = str(response.data)

        return Response({
            "success": False,
            "message": message or "An error occurred.",
            "data": None
        }, status=response.status_code)

    # Handle non-DRF exceptions (like 500 server error)
    return Response({
        "success": False,
        "message": "A server error occurred.",
        "data": None
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)