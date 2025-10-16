from django.db import models
from django.utils import timezone


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
    resident = models.ForeignKey('residents.Resident', on_delete=models.CASCADE, verbose_name='居民ID', db_column='resident_id')
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
