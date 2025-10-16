from django.db import models
from django.utils import timezone


class Apartment(models.Model):
    """楼栋信息模型"""
    community = models.ForeignKey('communities.Community', on_delete=models.CASCADE, verbose_name='小区')
    apartment_number = models.PositiveSmallIntegerField(verbose_name='楼栋号')
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    class Meta:
        db_table = 'apartment'
        verbose_name = '楼栋信息'
        verbose_name_plural = '楼栋信息'
        indexes = [
            models.Index(fields=['community', 'apartment_number'], name='idx_apartment_community_number'),
        ]

    def __str__(self):
        return f'{self.community.community_name} - 楼栋{self.apartment_number}'