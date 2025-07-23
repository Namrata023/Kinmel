from rest_framework.response import Response

def success_response(message="Success", data=None, status_code=200):
    return Response({
        "success": True,
        "message": message,
        "data": data
    }, status=status_code)