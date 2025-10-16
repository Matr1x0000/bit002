from django.db import models
from django.utils import timezone


class LowIncome(models.Model):
    """
    低保户详细信息模型
    用于存储低保户的详细信息
    """
    # 低保户唯一标识（Django会自动创建自增主键id）
    resident = models.ForeignKey('residents.Resident', on_delete=models.CASCADE, verbose_name='居民ID', db_column='resident_id')
    authentication_date = models.DateTimeField(verbose_name='认证日期', null=False)
    bank_account_number = models.CharField(max_length=50, verbose_name='银行卡号（唯一）', unique=True, null=False)
    bank_account_name = models.CharField(max_length=100, verbose_name='银行卡账户名称', null=False)
    registration_date = models.DateTimeField(verbose_name='登记日期', auto_now_add=True, null=False)
    last_update_time = models.DateTimeField(verbose_name='最后更新时间', auto_now=True, null=False)

    class Meta:
        db_table = 'low_income'
        verbose_name = '低保户信息'
        verbose_name_plural = '低保户信息'
        indexes = [
            models.Index(fields=['resident_id'], name='idx_low_income_resident_id'),
        ]

    def __str__(self):
        return f"低保户 {self.id} - 居民ID: {self.resident_id}"