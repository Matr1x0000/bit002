from datetime import datetime, timedelta
from django.db.models import Count, Sum
from residents.models import Resident
from low_income.models import LowIncome
from five_guarantees.models import FiveGuarantees
from disabled.models import Disabled
from special_needs.models import SpecialNeeds
from deceased.models import Deceased


class ResidentService:
    @staticmethod
    def get_resident_by_id(resident_id):
        """根据ID获取居民信息"""
        try:
            resident = Resident.objects.get(id=resident_id)
            return resident.to_dict()
        except Resident.DoesNotExist:
            return None
    
    @staticmethod
    def get_resident_by_id_card(id_card):
        """根据身份证号获取居民信息"""
        try:
            resident = Resident.objects.get(id_card=id_card)
            return resident.to_dict()
        except Resident.DoesNotExist:
            return None
    
    @staticmethod
    def get_all_residents(page=1, page_size=10):
        """获取所有居民信息（分页）"""
        start = (page - 1) * page_size
        end = start + page_size
        
        residents = Resident.objects.all()[start:end]
        total = Resident.objects.count()
        
        return {
            'data': [resident.to_dict() for resident in residents],
            'total': total,
            'page': page,
            'page_size': page_size
        }
    
    @staticmethod
    def add_resident(data):
        """添加居民信息"""
        try:
            # 创建居民对象
            resident = Resident(**data)
            resident.save()
            return resident.to_dict()
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def update_resident(resident_id, data):
        """更新居民信息"""
        try:
            resident = Resident.objects.get(id=resident_id)
            
            # 更新字段
            for key, value in data.items():
                setattr(resident, key, value)
            
            resident.save()
            return resident.to_dict()
        except Resident.DoesNotExist:
            return {'error': '居民不存在'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def delete_resident(resident_id):
        """删除居民信息"""
        try:
            resident = Resident.objects.get(id=resident_id)
            resident.delete()
            return True
        except Resident.DoesNotExist:
            return False
    
    @staticmethod
    def search_residents(keyword, page=1, page_size=10):
        """搜索居民信息"""
        start = (page - 1) * page_size
        end = start + page_size
        
        # 按姓名或身份证号搜索
        residents = Resident.objects.filter(
            name__contains=keyword
        ) | Resident.objects.filter(
            id_card__contains=keyword
        )
        
        total = residents.count()
        paginated_residents = residents[start:end]
        
        return {
            'data': [resident.to_dict() for resident in paginated_residents],
            'total': total,
            'page': page,
            'page_size': page_size
        }
    
    @staticmethod
    def get_residents_by_community(community_id, page=1, page_size=10):
        """获取指定社区的居民信息"""
        start = (page - 1) * page_size
        end = start + page_size
        
        residents = Resident.objects.filter(community_id=community_id)
        total = residents.count()
        paginated_residents = residents[start:end]
        
        return {
            'data': [resident.to_dict() for resident in paginated_residents],
            'total': total,
            'page': page,
            'page_size': page_size
        }
    
    @staticmethod
    def get_special_population_stats():
        """获取特殊人群统计信息"""
        stats = {
            'low_income_count': LowIncome.objects.count(),
            'five_guarantee_count': FiveGuarantees.objects.count(),
            'disabled_count': Disabled.objects.count(),
            'special_support_count': SpecialNeeds.objects.count(),
            'deceased_count': Deceased.objects.count()
        }
        return stats
    
    @staticmethod
    def get_new_residents_count(time_range='month'):
        """获取新增居民数量"""
        now = datetime.now()
        
        if time_range == 'day':
            start_date = now - timedelta(days=1)
        elif time_range == 'month':
            start_date = now - timedelta(days=30)
        elif time_range == 'year':
            start_date = now - timedelta(days=365)
        else:
            start_date = now - timedelta(days=30)
        
        return Resident.objects.filter(created_at__gte=start_date).count()
    
    @staticmethod
    def get_resident_distribution_by_gender():
        """获取居民性别分布"""
        distribution = Resident.objects.values('gender').annotate(count=Count('gender'))
        return list(distribution)
    
    @staticmethod
    def get_resident_distribution_by_age_group():
        """获取居民年龄段分布"""
        now = datetime.now()
        age_groups = [
            {'name': '0-18岁', 'min': 0, 'max': 18},
            {'name': '19-35岁', 'min': 19, 'max': 35},
            {'name': '36-59岁', 'min': 36, 'max': 59},
            {'name': '60岁以上', 'min': 60, 'max': 200}
        ]
        
        result = []
        for group in age_groups:
            # 计算出生日期范围
            max_birth_date = now - timedelta(days=group['min'] * 365)
            min_birth_date = now - timedelta(days=group['max'] * 365)
            
            count = Resident.objects.filter(
                birth_date__lte=max_birth_date,
                birth_date__gte=min_birth_date
            ).count()
            
            result.append({
                'age_group': group['name'],
                'count': count
            })
        
        return result