from django.db import models
from django.utils import timezone

# Create your models here.


class Ethnicity(models.Model):
    """
    民族表
    用于存储民族信息，作为Resident模型的外键关联
    """
    name = models.CharField(max_length=50, verbose_name='民族名称', unique=True)

    class Meta:
        verbose_name = '民族'
        verbose_name_plural = '民族管理'
        db_table = 'ethnicities'

    def __str__(self):
        return self.name


class Resident(models.Model):
    """
    居民身份信息表
    存储居民的身份信息，包括姓名、性别、出生日期、联系电话、身份证号等
    """
    # 基本信息
    name = models.CharField(max_length=50, verbose_name='居民姓名')
    id_card = models.CharField(max_length=18, verbose_name='身份证号', unique=True, db_index=True)
    gender = models.SmallIntegerField(
        choices=((0, '男'), (1, '女')),
        default=0,
        verbose_name='性别'
    )
    birth_date = models.DateField(verbose_name='出生日期')
    ethnicity = models.ForeignKey(
        Ethnicity,
        on_delete=models.CASCADE,
        verbose_name='民族',
        related_name='residents'
    )
    political_affiliation = models.SmallIntegerField(
        choices=(
            (0, '群众'),
            (1, '中共党员'),
            (2, '共青团员'),
            (3, '中国国民党革命委员会'),
            (4, '中国民主同盟'),
            (5, '中国民主建国会'),
            (6, '中国民主促进会'),
            (7, '中国农工民主党'),
            (8, '中国致公党'),
            (9, '九三学社'),
            (10, '台湾民主自治同盟')
        ),
        default=0,
        verbose_name='政治面貌'
    )
    household_address = models.CharField(max_length=255, verbose_name='户籍地址')
    phone_number = models.CharField(max_length=20, verbose_name='联系方式')
    
    # 状态信息
    marital_status = models.SmallIntegerField(
        choices=((0, '未婚'), (1, '已婚'), (2, '离异'), (3, '丧偶')),
        default=0,
        verbose_name='婚姻状况'
    )
    education_level = models.SmallIntegerField(
        choices=((0, '文盲'), (1, '小学'), (2, '初中'), (3, '高中'), (4, '大专'), (5, '本科'), (6, '研究生')),
        default=0,
        verbose_name='学历'
    )
    population_type = models.SmallIntegerField(
        choices=((0, '常住人口'), (1, '非常住人口')),
        default=0,
        verbose_name='人口类型'
    )
    residential_type = models.SmallIntegerField(
        choices=((0, '楼房'), (1, '平房')),
        default=0,
        verbose_name='住宅类型'
    )
    own_house = models.SmallIntegerField(
        choices=((0, '是'), (1, '否')),
        default=0,
        verbose_name='是否自有房'
    )
    
    # 特殊标识
    is_low_income = models.SmallIntegerField(
        choices=((0, '否'), (1, '是')),
        default=0,
        verbose_name='是否低保户'
    )
    is_beneficiary = models.SmallIntegerField(
        choices=((0, '否'), (1, '是')),
        default=0,
        verbose_name='是否五保户'
    )
    is_disabled = models.SmallIntegerField(
        choices=((0, '否'), (1, '是')),
        default=0,
        verbose_name='是否残疾'
    )
    is_special_support = models.SmallIntegerField(
        choices=((0, '否'), (1, '是')),
        default=0,
        verbose_name='是否特扶人口'
    )
    is_key_person = models.SmallIntegerField(
        choices=((0, '否'), (1, '是')),
        default=0,
        verbose_name='是否重点对象'
    )
    is_deceased = models.SmallIntegerField(
        choices=((0, '否'), (1, '是')),
        default=0,
        verbose_name='是否死亡'
    )
    
    # 时间信息
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='登记日期')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    class Meta:
        verbose_name = '居民'
        verbose_name_plural = '居民管理'
        db_table = 'residents'
        # 添加索引
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['ethnicity']),
            models.Index(fields=['political_affiliation']),
            models.Index(fields=['population_type']),
            models.Index(fields=['residential_type']),
            models.Index(fields=['marital_status']),
            models.Index(fields=['education_level']),
        ]

    def __str__(self):
        return self.name