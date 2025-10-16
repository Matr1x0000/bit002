from django.db import models
from django.utils import timezone


class Bungalow(models.Model):
    """平房信息模型"""
    resident = models.ForeignKey('residents.Resident', on_delete=models.CASCADE, verbose_name='居民')
    bungalow_number = models.CharField(max_length=50, verbose_name='平房号')
    hutong = models.ForeignKey('hutong.Hutong', on_delete=models.CASCADE, verbose_name='胡同')
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    class Meta:
        db_table = 'bungalow'
        verbose_name = '平房信息'
        verbose_name_plural = '平房信息'
        indexes = [
            models.Index(fields=['resident', 'bungalow_number'], name='idx_bungalow_resident_number'),
        ]

    def __str__(self):
        return f'{self.bungalow_number} - {self.resident.name}'