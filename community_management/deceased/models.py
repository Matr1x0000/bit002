from django.db import models
from datetime import datetime


class Deceased(models.Model):
    """
    死亡户信息表
    存储死亡户的详细信息
    """
    id = models.AutoField(primary_key=True, verbose_name='死亡户唯一标识')
    resident = models.ForeignKey('residents.Resident', on_delete=models.CASCADE, 
                               verbose_name='居民ID', related_name='deceased')
    deceased_date = models.DateTimeField(verbose_name='死亡日期', null=False)
    deceased_place = models.CharField(max_length=100, verbose_name='死亡地点', null=False)
    deceased_reason = models.CharField(max_length=255, verbose_name='死亡原因', null=False)
    deceased_contact_name = models.CharField(max_length=100, verbose_name='联系人姓名', null=False)
    deceased_contact_phone = models.CharField(max_length=20, verbose_name='联系人电话', null=False)
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='登记日期')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    class Meta:
        db_table = 'deceased'
        verbose_name = '死亡户信息'
        verbose_name_plural = '死亡户信息'
        indexes = [
            models.Index(fields=['resident_id'], name='idx_deceased_resident_id'),
        ]

    def __str__(self):
        return f'死亡户信息 - 居民ID: {self.resident_id}'