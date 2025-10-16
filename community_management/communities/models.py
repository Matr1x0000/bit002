from django.db import models
from django.utils import timezone


class Community(models.Model):
    """小区信息模型"""
    community_name = models.CharField(max_length=255, unique=True, verbose_name='小区名称')
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, verbose_name='所属组别')
    community_number = models.CharField(max_length=50, verbose_name='小区号')
    has_property = models.BooleanField(default=False, verbose_name='是否有物业')
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    class Meta:
        db_table = 'community'
        verbose_name = '小区信息'
        verbose_name_plural = '小区信息'
        indexes = [
            models.Index(fields=['community_name'], name='idx_community_name'),
            models.Index(fields=['group'], name='idx_community_group'),
            models.Index(fields=['has_property'], name='idx_community_has_property'),
        ]

    def __str__(self):
        return self.community_name