from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from admins.services.auth_service import AuthService
from authentication.utils.jwt_helper import jwt_required_with_role


@csrf_exempt
def auth_api(request):
    """认证相关API接口"""
    # 解析请求参数
    data = json.loads(request.body) if request.body else {}
    method = request.method
    action = data.get('action')
    
    if method == 'POST':
        if action == 'login':
            # 用户登录
            username = data.get('username')
            password = data.get('password')
            if not username or not password:
                return JsonResponse({'success': False, 'message': '用户名和密码不能为空'})
            
            result = AuthService.login(username, password)
            if result['success']:
                return JsonResponse({'success': True, 'data': result})
            else:
                return JsonResponse({'success': False, 'message': result['message']})
        
        elif action == 'logout':
            # 用户登出
            token = request.headers.get('Authorization', '').split(' ')[-1]
            result = AuthService.logout(token)
            return JsonResponse(result)
        
        elif action == 'change_password':
            # 修改密码
            admin_id = data.get('admin_id')
            old_password = data.get('old_password')
            new_password = data.get('new_password')
            
            if not admin_id or not old_password or not new_password:
                return JsonResponse({'success': False, 'message': '参数不完整'})
            
            result = AuthService.change_password(admin_id, old_password, new_password)
            return JsonResponse(result)
        
        elif action == 'reset_password':
            # 重置密码
            admin_id = data.get('admin_id')
            new_password = data.get('new_password')
            
            if not admin_id or not new_password:
                return JsonResponse({'success': False, 'message': '参数不完整'})
            
            result = AuthService.reset_password(admin_id, new_password)
            return JsonResponse(result)
        
        elif action == 'add_admin':
            # 添加管理员
            result = AuthService.add_admin(data)
            return JsonResponse(result)
        
        else:
            return JsonResponse({'success': False, 'message': '未知的操作'})
    
    elif method == 'GET':
        if 'admin_id' in request.GET:
            # 获取管理员信息
            admin_id = request.GET.get('admin_id')
            admin_info = AuthService.get_admin_info(admin_id)
            if admin_info:
                return JsonResponse({'success': True, 'data': admin_info})
            else:
                return JsonResponse({'success': False, 'message': '管理员不存在'})
        else:
            # 获取管理员列表
            page = int(request.GET.get('page', 1))
            page_size = int(request.GET.get('page_size', 10))
            admins = AuthService.get_all_admins(page, page_size)
            return JsonResponse({'success': True, 'data': admins})
    
    else:
        return JsonResponse({'success': False, 'message': '不支持的请求方法'})
