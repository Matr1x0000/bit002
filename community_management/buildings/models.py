from django.db import models
from django.utils import timezone


class Building(models.Model):
    """楼房信息模型"""
    # 居民ID，外键关联到residents表
    resident = models.ForeignKey('residents.Resident', on_delete=models.CASCADE, verbose_name='居民')
    # 楼房号
    building_number = models.IntegerField(verbose_name='楼房号')
    # 户号ID，外键关联到house表
    house_number = models.ForeignKey('house.House', on_delete=models.CASCADE, verbose_name='户号')
    # 登记日期
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='登记日期')
    # 最后更新时间
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    class Meta:
        # 设置表名
        db_table = 'building'
        # 设置中文显示名称
        verbose_name = '楼房信息'
        verbose_name_plural = '楼房信息'
        # 设置索引
        indexes = [
            # resident_id, house_number_id复合索引
            models.Index(fields=['resident', 'house_number'], name='idx_resident_house_number'),
        ]

    def __str__(self):
        """返回楼房的字符串表示"""
        return f'{self.resident.name} - {self.house_number}单元 - {self.building_number}'