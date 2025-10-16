from django.db import models


class PropertyManager(models.Model):
    """物业经理信息模型"""
    # 物业ID，外键关联到properties表
    property = models.ForeignKey(
        'properties.Property',
        on_delete=models.CASCADE,
        verbose_name='物业ID',
        db_column='property_id'
    )
    
    # 所属小区ID，外键关联到communities表，且唯一
    community = models.OneToOneField(
        'communities.Community',
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