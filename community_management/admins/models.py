from django.db import models


class Role(models.Model):
    """
    权限组模型
    
    用于管理系统中的不同权限组，定义管理员的操作权限范围。
    """
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="权限组名称"
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="权限组描述"
    )

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
    """
    管理员模型
    
    存储系统管理员的基本信息和登录凭证。
    """
    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="用户名"
    )
    password_hash = models.CharField(
        max_length=255,
        verbose_name="密码哈希值"
    )
    real_name = models.CharField(
        max_length=50,
        verbose_name="真实姓名"
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name="联系电话"
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="admins",
        verbose_name="角色"
    )
    status = models.BooleanField(
        default=True,
        verbose_name="状态",
        help_text="True表示启用，False表示禁用"
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    last_login_time = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="最后登录时间"
    )

    class Meta:
        db_table = "admins"
        verbose_name = "管理员"
        verbose_name_plural = "管理员"
        ordering = ['-create_time']
        indexes = [
            models.Index(fields=['username'], name='idx_admin_username'),
            models.Index(fields=['role'], name='idx_admin_role'),
            models.Index(fields=['status'], name='idx_admin_status'),
        ]

    def __str__(self):
        return f"{self.real_name} ({self.username})"
