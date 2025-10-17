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

class PropertyManager(models.Model):
    """物业经理信息模型"""
    # 物业ID，外键关联到properties表
    property = models.ForeignKey(
        'Property',
        on_delete=models.CASCADE,
        verbose_name='物业ID',
        db_column='property_id'
    )
    
    # 所属小区ID，外键关联到communities表，且唯一
    community = models.OneToOneField(
        'address.Community',
        on_delete=models.CASCADE,
        verbose_name='所属小区ID',
        db_column='community_id'
    )
    
    # 登记日期，自动设置为当前时间
    registration_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='登记日期'
    )
    
    # 最后更新时间，自动更新为当前时间
    last_update_time = models.DateTimeField(
        auto_now=True,
        verbose_name='最后更新时间'
    )
    
    class Meta:
        # 设置表名
        db_table = 'property_manager'
        # 设置中文名称
        verbose_name = '物业经理信息'
        verbose_name_plural = '物业经理信息'
        # 设置索引
        indexes = [
            models.Index(fields=['property', 'community'], name='idx_property_community'),
        ]
    
    def __str__(self):
        """返回物业经理的字符串表示"""
        return f"物业经理-物业:{self.property_id}-小区:{self.community_id}"