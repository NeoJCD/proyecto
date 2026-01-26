from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

@api_view(['GET'])
@throttle_classes([AnonRateThrottle, UserRateThrottle])
def vista_limitada(request):
    return Response({
        "mensaje": "¡Hola Neomar! Si ves esto, el servidor funciona.",
        "aviso": "Si refrescas 3 veces, te bloquearé."
    })