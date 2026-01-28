# petrolera/authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication

class CookiesJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # 1. Intentamos buscar el token en las Cookies
        access_token = request.COOKIES.get('access_token')
        
        # 2. Si no hay cookie, devolvemos None (Django probará otros métodos)
        if not access_token:
            return None
        
        try:
            # 3. Validamos el token manualmente
            validated_token = self.get_validated_token(access_token)
            
            # 4. Buscamos al usuario dueño de ese token
            user = self.get_user(validated_token)
            
            # 5. ¡Éxito! Devolvemos al usuario y el token
            return (user, validated_token)
        except:
            return None