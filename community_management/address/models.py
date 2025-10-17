from django.db import models
from django.utils import timezone


class Street(models.Model):
    """街道信息模型"""
    # Django会自动创建id主键，无需显式定义
    street_name = models.CharField(max_length=100, unique=True, verbose_name='街道名称')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='登记日期')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    class Meta:
        db_table = 'street'  # 表名
        verbose_name = '街道信息'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['street_name'], name='idx_street_name'),
        ]

    def __str__(self):
        """返回街道的字符串表示"""
        return self.street_name


class Group(models.Model):
    """组别模型"""
    id = models.AutoField(primary_key=True, verbose_name="组别唯一标识")
    group_number = models.CharField(max_length=50, unique=True, verbose_name="组别号")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="登记日期")
    last_update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")

    class Meta:
        db_table = "groups"
        verbose_name = "组别"
        verbose_name_plural = "组别"
        indexes = [
            models.Index(fields=['group_number'], name='idx_group_number'),
        ]

    def __str__(self):
        return self.group_number


class Hutong(models.Model):
    """胡同模型"""
    id = models.AutoField(primary_key=True, verbose_name="胡同唯一标识")
    hutong_name = models.CharField(max_length=255, unique=True, verbose_name="胡同名称")
    group = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name="所属组别")
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


class Community(models.Model):
    """小区信息模型"""
    community_name = models.CharField(max_length=255, unique=True, verbose_name='小区名称')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name='所属组别')
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


class Apartment(models.Model):
    """楼栋信息模型"""
    community = models.ForeignKey('Community', on_delete=models.CASCADE, verbose_name='小区')
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


class Unit(models.Model):
    """单元信息模型"""
    # 楼栋ID，外键关联到apartments表
    apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE, verbose_name='楼栋')
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


class House(models.Model):
    """户号信息模型"""
    # 单元ID，外键关联到units表
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, verbose_name='单元')
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
