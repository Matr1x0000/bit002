from django.db import models
from django.utils import timezone


class Role(models.Model):
    """权限组模型"""
    id = models.AutoField(primary_key=True, verbose_name="权限组唯一标识")
    name = models.CharField(max_length=50, unique=True, verbose_name="权限组名称")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="权限组描述")
    
    class Meta:
        db_table = "roles"
        verbose_name = "权限组"
        verbose_name_plural = "权限组"
        indexes = [
            models.Index(fields=['name'], name='idx_role_name'),
        ]
    
    def __str__(self):
        return self.name


class Admin(models.Model):
    """管理员模型"""
    id = models.AutoField(primary_key=True, verbose_name="管理员唯一标识")
    username = models.CharField(max_length=50, unique=True, verbose_name="用户名")
    password_hash = models.CharField(max_length=255, verbose_name="密码哈希值")
    real_name = models.CharField(max_length=50, verbose_name="真实姓名")
    phone_number = models.CharField(max_length=20, verbose_name="联系电话")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="角色")
    status = models.BooleanField(default=True, verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    last_login_time = models.DateTimeField(blank=True, null=True, verbose_name="最后登录时间")
    
    class Meta:
        db_table = "admins"
        verbose_name = "管理员"
        verbose_name_plural = "管理员"
        indexes = [
            models.Index(fields=['username'], name='idx_admin_username'),
        ]
    
    def __str__(self):
        return f"{self.real_name} ({self.username})"