from django.db import models
from django.utils import timezone


class Group(models.Model):
    """组别模型"""
    id = models.AutoField(primary_key=True, verbose_name="组别唯一标识")
    group_number = models.CharField(max_length=50, unique=True, verbose_name="组别号")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="登记日期")
    last_update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    
    class Meta:
        db_table = "groups"
        verbose_name = "组别"
        verbose_name_plural = "组别"
        indexes = [
            models.Index(fields=['group_number'], name='idx_group_number'),
        ]
    
    def __str__(self):
        return self.group_number