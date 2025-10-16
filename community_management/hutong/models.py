from django.db import models
from django.utils import timezone
from groups.models import Group


class Hutong(models.Model):
    """胡同模型"""
    id = models.AutoField(primary_key=True, verbose_name="胡同唯一标识")
    hutong_name = models.CharField(max_length=255, unique=True, verbose_name="胡同名称")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="所属组别")
    hutong_number = models.CharField(max_length=50, verbose_name="胡同号")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="登记日期")
    last_update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    
    class Meta:
        db_table = "hutong"
        verbose_name = "胡同"
        verbose_name_plural = "胡同"
        indexes = [
            models.Index(fields=['hutong_name'], name='idx_hutong_name'),
            models.Index(fields=['group'], name='idx_hutong_group'),
            models.Index(fields=['hutong_number'], name='idx_hutong_number'),
        ]
    
    def __str__(self):
        return self.hutong_name