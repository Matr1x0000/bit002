import jwt
from django.http import JsonResponse
from functools import wraps
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from admins.models import Admin
from django.conf import settings


def jwt_required_with_role(role):
    """带角色检查的JWT装饰器"""
    def wrapper(view_func):
        @wraps(view_func)
        def decorator(request, *args, **kwargs):
            auth = JWTAuthentication()
            try:
                # 验证JWT Token
                user, token = auth.authenticate(request)
                
                # 检查用户角色
                if user.role < role:
                    return JsonResponse({'message': '权限不足'}, status=403)
                
                # 将用户添加到请求对象中
                request.user = user
                
                return view_func(request, *args, **kwargs)
            except (InvalidToken, TokenError):
                return JsonResponse({'message': '无效的Token'}, status=401)
        return decorator
    return wrapper


def generate_token(admin_id):
    """生成JWT Token"""
    from rest_framework_simplejwt.tokens import RefreshToken
    
    # 创建刷新令牌
    refresh = RefreshToken.for_user(Admin.objects.get(id=admin_id))
    
    # 获取访问令牌
    access_token = str(refresh.access_token)
    
    return access_token


def decode_token(token):
    """解析JWT Token"""
    from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
    from rest_framework_simplejwt.tokens import AccessToken
    
    try:
        # 解析Token
        access_token = AccessToken(token)
        # 获取用户ID
        user_id = access_token['user_id']
        
        return {
            'user_id': user_id,
            'exp': access_token['exp']
        }
    except TokenError:
        return {'error': '无效的Token'}
    except InvalidToken:
        return {'error': 'Token已过期'}