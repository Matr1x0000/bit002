from admins.models import Admin
from authentication.utils.jwt_helper import generate_token
from django.contrib.auth.hashers import check_password, make_password


class AuthService:
    @staticmethod
    def login(username, password):
        """用户登录验证"""
        try:
            # 根据用户名查找用户
            admin = Admin.objects.get(username=username)
            
            # 验证密码
            if check_password(password, admin.password):
                # 生成Token
                token = generate_token(admin.id)
                
                return {
                    'success': True,
                    'token': token,
                    'user_info': {
                        'id': admin.id,
                        'username': admin.username,
                        'name': admin.name,
                        'role': admin.role,
                        'role_name': admin.get_role_display(),
                        'department': admin.department
                    }
                }
            else:
                return {'success': False, 'message': '密码错误'}
        except Admin.DoesNotExist:
            return {'success': False, 'message': '用户名不存在'}
    
    @staticmethod
    def logout(token):
        """用户登出"""
        # JWT是无状态的，客户端删除token即可
        # 这里可以添加token黑名单等逻辑（可选）
        return {'success': True, 'message': '登出成功'}
    
    @staticmethod
    def change_password(admin_id, old_password, new_password):
        """修改密码"""
        try:
            admin = Admin.objects.get(id=admin_id)
            
            # 验证旧密码
            if check_password(old_password, admin.password):
                # 设置新密码
                admin.password = make_password(new_password)
                admin.save()
                return {'success': True, 'message': '密码修改成功'}
            else:
                return {'success': False, 'message': '旧密码错误'}
        except Admin.DoesNotExist:
            return {'success': False, 'message': '用户不存在'}
    
    @staticmethod
    def reset_password(admin_id, new_password):
        """重置密码（管理员操作）"""
        try:
            admin = Admin.objects.get(id=admin_id)
            admin.password = make_password(new_password)
            admin.save()
            return {'success': True, 'message': '密码重置成功'}
        except Admin.DoesNotExist:
            return {'success': False, 'message': '用户不存在'}
    
    @staticmethod
    def get_admin_info(admin_id):
        """获取管理员信息"""
        try:
            admin = Admin.objects.get(id=admin_id)
            return {
                'id': admin.id,
                'username': admin.username,
                'name': admin.name,
                'role': admin.role,
                'role_name': admin.get_role_display(),
                'department': admin.department,
                'created_at': admin.created_at,
                'last_login': admin.last_login
            }
        except Admin.DoesNotExist:
            return None
    
    @staticmethod
    def update_admin_info(admin_id, data):
        """更新管理员信息"""
        try:
            admin = Admin.objects.get(id=admin_id)
            
            # 排除不能更新的字段
            if 'password' in data:
                del data['password']
            if 'username' in data:
                del data['username']
            
            # 更新字段
            for key, value in data.items():
                setattr(admin, key, value)
            
            admin.save()
            return {
                'success': True,
                'message': '信息更新成功',
                'data': AuthService.get_admin_info(admin_id)
            }
        except Admin.DoesNotExist:
            return {'success': False, 'message': '用户不存在'}
    
    @staticmethod
    def add_admin(data):
        """添加管理员"""
        try:
            # 检查用户名是否已存在
            if Admin.objects.filter(username=data['username']).exists():
                return {'success': False, 'message': '用户名已存在'}
            
            # 创建管理员对象
            admin_data = data.copy()
            # 密码加密
            admin_data['password'] = make_password(data['password'])
            
            admin = Admin(**admin_data)
            admin.save()
            
            return {
                'success': True,
                'message': '管理员创建成功',
                'data': AuthService.get_admin_info(admin.id)
            }
        except Exception as e:
            return {'success': False, 'message': str(e)}
    
    @staticmethod
    def get_all_admins(page=1, page_size=10):
        """获取所有管理员列表"""
        start = (page - 1) * page_size
        end = start + page_size
        
        admins = Admin.objects.all()[start:end]
        total = Admin.objects.count()
        
        return {
            'data': [
                {
                    'id': admin.id,
                    'username': admin.username,
                    'name': admin.name,
                    'role': admin.role,
                    'role_name': admin.get_role_display(),
                    'department': admin.department,
                    'created_at': admin.created_at
                }
                for admin in admins
            ],
            'total': total,
            'page': page,
            'page_size': page_size
        }