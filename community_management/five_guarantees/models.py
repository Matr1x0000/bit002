from django.db import models
from datetime import datetime


class FiveGuarantees(models.Model):
    """
    五保户信息表
    存储五保户的详细信息
    """
    id = models.AutoField(primary_key=True, verbose_name='五保户唯一标识')
    resident = models.ForeignKey('residents.Resident', on_delete=models.CASCADE, 
                               verbose_name='居民ID', related_name='five_guarantees')
    authentication_date = models.DateTimeField(verbose_name='认证日期', null=False)
    bank_account_number = models.CharField(max_length=50, unique=True, 
                                         verbose_name='银行卡号（唯一）', null=False)
    bank_account_name = models.CharField(max_length=100, verbose_name='银行卡账户名称', null=False)
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='登记日期')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    class Meta:
        db_table = 'five_guarantees'
        verbose_name = '五保户信息'
        verbose_name_plural = '五保户信息'
        indexes = [
            models.Index(fields=['resident_id'], name='idx_five_guar_resident_id'),
        ]

    def __str__(self):
        return f'五保户信息 - 居民ID: {self.resident_id}'