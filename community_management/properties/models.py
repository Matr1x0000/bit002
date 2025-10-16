from django.db import models


class Property(models.Model):
    """物业信息模型"""
    # Django会自动创建id主键，无需显式定义
    property_name = models.CharField(max_length=255, unique=True, verbose_name='物业名称')
    property_address = models.CharField(max_length=255, verbose_name='物业地址')
    property_owner = models.CharField(max_length=255, verbose_name='物业负责人')
    property_contact_phone = models.CharField(max_length=20, verbose_name='物业联系电话')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='登记日期')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')
    
    class Meta:
        db_table = 'properties'  # 表名
        verbose_name = '物业信息'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['property_name'], name='idx_property_name'),
            models.Index(fields=['property_owner'], name='idx_property_owner'),
            models.Index(fields=['property_contact_phone'], name='idx_property_contact_phone'),
        ]
    
    def __str__(self):
        """返回物业的字符串表示"""
        return self.property_name