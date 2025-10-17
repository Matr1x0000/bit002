from django.db import models


class Industry(models.Model):
    """行业信息模型"""
    # Django会自动创建id主键，无需显式定义
    industry_name = models.CharField(max_length=100, unique=True, verbose_name='行业名称')
    industry_code = models.CharField(max_length=50, unique=True, verbose_name='行业代码')
    
    class Meta:
        db_table = 'industries'  # 表名
        verbose_name = '行业信息'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['industry_name'], name='idx_industry_name'),
            models.Index(fields=['industry_code'], name='idx_industry_code'),
        ]
    
    def __str__(self):
        """返回行业的字符串表示"""
        return f'{self.industry_name} ({self.industry_code})'


class Merchant(models.Model):
    """商户信息模型"""
    # Django会自动创建id主键，无需显式定义
    merchants_name = models.CharField(max_length=100, verbose_name='商户名称')
    credit_code = models.CharField(max_length=18, unique=True, verbose_name='统一社会信用代码')
    license_number = models.CharField(max_length=50, verbose_name='营业执照编号')
    legal_person_name = models.CharField(max_length=50, verbose_name='法人代表姓名')
    legal_person_id = models.CharField(max_length=18, verbose_name='法人代表身份证号')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='联系电话')
    address = models.CharField(max_length=255, verbose_name='地址')
    business_scope = models.TextField(blank=True, null=True, verbose_name='经营范围')
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, verbose_name='所属行业')
    street = models.ForeignKey('address.Street', on_delete=models.CASCADE, verbose_name='所属街道')
    establishment_date = models.DateField(verbose_name='成立日期')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='登记日期')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')
    
    class Meta:
        db_table = 'merchants'  # 表名
        verbose_name = '商户信息'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['credit_code'], name='idx_credit_code'),
            models.Index(fields=['merchants_name'], name='idx_merchants_name'),
            models.Index(fields=['license_number'], name='idx_license_number'),
            models.Index(fields=['legal_person_name'], name='idx_legal_person'),
            models.Index(fields=['street'], name='idx_streets_id'),
            models.Index(fields=['industry'], name='idx_industry_id'),
        ]
    
    def __str__(self):
        """返回商户的字符串表示"""
        return self.merchants_name