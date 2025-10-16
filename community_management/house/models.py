from django.db import models
from django.utils import timezone


class House(models.Model):
    """户号信息模型"""
    # 单元ID，外键关联到units表
    unit = models.ForeignKey('units.Unit', on_delete=models.CASCADE, verbose_name='单元')
    # 户号
    house_number = models.CharField(max_length=20, verbose_name='户号')
    # 登记日期
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='登记日期')
    # 最后更新时间
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    class Meta:
        # 设置表名
        db_table = 'house'
        # 设置中文显示名称
        verbose_name = '户号信息'
        verbose_name_plural = '户号信息'
        # 设置索引
        indexes = [
            # unit_id索引
            models.Index(fields=['unit'], name='idx_house_unit'),
        ]

    def __str__(self):
        """返回户号的字符串表示"""
        return f'{self.unit.apartment.community.community_name} - {self.unit.apartment.apartment_number}栋-{self.unit.unit_number}单元-{self.house_number}'