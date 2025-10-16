from django.db import models
from django.utils import timezone


class Unit(models.Model):
    """单元信息模型"""
    # 楼栋ID，外键关联到apartments表
    apartment = models.ForeignKey('apartments.Apartment', on_delete=models.CASCADE, verbose_name='楼栋')
    # 单元号
    unit_number = models.SmallIntegerField(verbose_name='单元号')
    # 登记日期
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='登记日期')
    # 最后更新时间
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    class Meta:
        # 设置表名
        db_table = 'unit'
        # 设置中文显示名称
        verbose_name = '单元信息'
        verbose_name_plural = '单元信息'
        # 设置索引
        indexes = [
            # unit_number索引
            models.Index(fields=['unit_number'], name='idx_unit_number'),
            # apartment_id索引
            models.Index(fields=['apartment'], name='idx_unit_apartment'),
        ]

    def __str__(self):
        """返回单元的字符串表示"""
        return f'{self.apartment.community.community_name} - {self.apartment.apartment_number}栋-{self.unit_number}单元'