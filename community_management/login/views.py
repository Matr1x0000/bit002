from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from datetime import datetime
from admins.models import Admin, Role
import json

def index(request):
    return render(request, 'index.html')


def login(request):
    """
    管理员登录视图
    处理用户身份验证和权限验证
    """
    if request.method == 'GET':
        # 检查用户是否已登录
        if 'admin_id' in request.session:
            # 已登录用户重定向到欢迎页面
            return redirect('../index/')
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        try:
            # 尝试解析JSON数据
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
        except json.JSONDecodeError:
            # 尝试从表单数据中获取
            username = request.POST.get('username')
            password = request.POST.get('password')
        
        # 输入验证
        if not username or not password:
            if request.content_type == 'application/json':
                return JsonResponse({'success': False, 'error': '用户名和密码不能为空'})
            messages.error(request, '用户名和密码不能为空')
            return render(request, 'login.html')
        
        try:
            # 查询管理员
            admin = Admin.objects.get(username=username)
            
            # 检查管理员状态
            if not admin.status:
                if request.content_type == 'application/json':
                    return JsonResponse({'success': False, 'error': '账号已被禁用，请联系管理员'})
                messages.error(request, '账号已被禁用，请联系管理员')
                return render(request, 'login.html')
            
            # 验证密码（这里假设密码是明文存储的，实际项目中应该使用哈希验证）
            # 如果是哈希密码，应该使用 check_password(password, admin.password_hash)
            if admin.password_hash == password:
                # 更新最后登录时间
                admin.last_login_time = datetime.now()
                admin.save()
                
                # 存储用户信息到会话
                request.session['admin_id'] = admin.id
                request.session['username'] = admin.username
                request.session['real_name'] = admin.real_name
                request.session['role_id'] = admin.role.id
                request.session['role_name'] = admin.role.name
                
                # 登录成功
                if request.content_type == 'application/json':
                    return JsonResponse({'success': True, 'message': '登录成功', 'role': admin.role.name})
                
                messages.success(request, '登录成功！')
                return redirect('../index/')
            else:
                # 密码错误
                if request.content_type == 'application/json':
                    return JsonResponse({'success': False, 'error': '密码错误'})
                messages.error(request, '密码错误')
                return render(request, 'login.html')
                
        except Admin.DoesNotExist:
            # 用户不存在
            if request.content_type == 'application/json':
                return JsonResponse({'success': False, 'error': '用户名不存在'})
            messages.error(request, '用户名不存在')
            return render(request, 'login.html')

def logout(request):
    """
    退出登录视图
    清除用户会话信息
    """
    # 清除会话中的用户信息
    request.session.flush()
    messages.info(request, '已成功退出登录')
    return redirect('login')

def check_permission(required_permissions=None):
    """
    权限装饰器
    用于检查用户是否登录以及是否具有所需权限
    
    Args:
        required_permissions: 需要的权限列表
    """
    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            # 检查用户是否登录
            if 'admin_id' not in request.session:
                messages.error(request, '请先登录')
                return redirect('login')
            
            # 检查是否需要特定权限
            if required_permissions:
                # 这里可以根据角色名称或更复杂的权限系统进行检查
                # 简化版本：根据角色名称判断
                user_role = request.session.get('role_name')
                if user_role not in required_permissions:
                    messages.error(request, '您没有权限执行此操作')
                    return redirect('welcome')
            
            return view_func(request, *args, **kwargs)
        return wrapped_view
    return decorator

