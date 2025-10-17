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

class Building(models.Model):
    """楼房信息模型"""
    # 居民ID，外键关联到residents表
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE, verbose_name='居民')
    # 楼房号
    building_number = models.IntegerField(verbose_name='楼房号')
    # 户号ID，外键关联到house表
    house_number = models.ForeignKey('address.House', on_delete=models.CASCADE, verbose_name='户号')
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

class Bungalow(models.Model):
    """平房信息模型"""
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE, verbose_name='居民')
    bungalow_number = models.CharField(max_length=50, verbose_name='平房号')
    hutong = models.ForeignKey('address.Hutong', on_delete=models.CASCADE, verbose_name='胡同')
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

class LowIncome(models.Model):
    """
    低保户详细信息模型
    用于存储低保户的详细信息
    """
    # 低保户唯一标识（Django会自动创建自增主键id）
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE, verbose_name='居民ID', db_column='resident_id')
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

class FiveGuarantees(models.Model):
    """
    五保户信息表
    存储五保户的详细信息
    """
    id = models.AutoField(primary_key=True, verbose_name='五保户唯一标识')
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE, 
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

class Disabled(models.Model):
    """
    残疾人信息表
    存储残疾人的详细信息
    """
    id = models.AutoField(primary_key=True, verbose_name='残疾人唯一标识')
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE, 
                               verbose_name='居民ID', related_name='disabled')
    authentication_date = models.DateTimeField(verbose_name='认证日期', null=False)
    bank_account_number = models.CharField(max_length=50, unique=True, 
                                         verbose_name='银行卡号（唯一）', null=False)
    bank_account_name = models.CharField(max_length=100, verbose_name='银行卡账户名称', null=False)
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='登记日期')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    class Meta:
        db_table = 'disabled'
        verbose_name = '残疾人信息'
        verbose_name_plural = '残疾人信息'
        indexes = [
            models.Index(fields=['resident_id'], name='idx_disabled_resident_id'),
        ]

    def __str__(self):
        return f'残疾人信息 - 居民ID: {self.resident_id}'

class Deceased(models.Model):
    """
    死亡户信息表
    存储死亡户的详细信息
    """
    id = models.AutoField(primary_key=True, verbose_name='死亡户唯一标识')
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE, 
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

class SpecialNeeds(models.Model):
    """
    特扶户详细信息模型
    用于存储特扶户的详细信息
    """
    # 特扶户唯一标识（Django会自动创建自增主键id）
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE, verbose_name='居民ID', db_column='resident_id')
    authentication_date = models.DateTimeField(verbose_name='认证日期', null=False)
    bank_account_number = models.CharField(max_length=50, verbose_name='银行卡号（唯一）', unique=True, null=False)
    bank_account_name = models.CharField(max_length=100, verbose_name='银行卡账户名称', null=False)
    registration_date = models.DateTimeField(verbose_name='登记日期', auto_now_add=True, null=False)
    last_update_time = models.DateTimeField(verbose_name='最后更新时间', auto_now=True, null=False)

    class Meta:
        db_table = 'special_needs'
        verbose_name = '特扶户信息'
        verbose_name_plural = '特扶户信息'
        indexes = [
            models.Index(fields=['resident_id'], name='idx_special_needs_resident_id'),
        ]

    def __str__(self):
        return f"特扶户 {self.id} - 居民ID: {self.resident_id}"
    
class SpecialObjects(models.Model):
    """
    重点对象详细信息模型
    用于存储重点对象的详细信息
    """
    # 对象类型选项
    OBJECT_TYPE_CHOICES = [
        (0, '信访'),
        (1, '新疆'),
        (2, '西藏'),
    ]
    
    # 重点对象唯一标识（Django会自动创建自增主键id）
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE, verbose_name='居民ID', db_column='resident_id')
    object_type = models.IntegerField(verbose_name='对象类型', choices=OBJECT_TYPE_CHOICES, null=False)
    object_name = models.CharField(max_length=100, verbose_name='对象姓名', null=False)
    object_contact_phone = models.CharField(max_length=20, verbose_name='对象联系电话', null=False)
    object_address = models.CharField(max_length=255, verbose_name='对象住址', null=False)
    object_responsible_name = models.CharField(max_length=100, verbose_name='负责人姓名', null=False)
    object_responsible_phone = models.CharField(max_length=20, verbose_name='负责人联系电话', null=False)
    registration_date = models.DateTimeField(verbose_name='登记日期', auto_now_add=True, null=False)
    last_update_time = models.DateTimeField(verbose_name='最后更新时间', auto_now=True, null=False)

    class Meta:
        db_table = 'special_objects'
        verbose_name = '重点对象信息'
        verbose_name_plural = '重点对象信息'
        indexes = [
            models.Index(fields=['resident_id'], name='idx_special_obj_resident_id'),
        ]

    def __str__(self):
        return f"重点对象 {self.id} - 居民ID: {self.resident_id} - {self.get_object_type_display()}"

