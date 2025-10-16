from django.db import models


class Street(models.Model):
    """街道信息模型"""
    # Django会自动创建id主键，无需显式定义
    street_name = models.CharField(max_length=100, unique=True, verbose_name='街道名称')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='登记日期')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')
    
    class Meta:
        db_table = 'street'  # 表名
        verbose_name = '街道信息'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['street_name'], name='idx_street_name'),
        ]
    
    def __str__(self):
        """返回街道的字符串表示"""
        return self.street_name