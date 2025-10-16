from datetime import datetime, timedelta
from django.db.models import Count
from merchants.models import Merchant, Industry


class BusinessService:
    """商户服务类"""
    
    @staticmethod
    def get_business_by_id(business_id):
        """根据ID获取商户信息"""
        try:
            merchant = Merchant.objects.get(id=business_id)
            return {
                'id': merchant.id,
                'merchants_name': merchant.merchants_name,
                'credit_code': merchant.credit_code,
                'license_number': merchant.license_number,
                'legal_person_name': merchant.legal_person_name,
                'legal_person_id': merchant.legal_person_id,
                'phone_number': merchant.phone_number,
                'address': merchant.address,
                'business_scope': merchant.business_scope,
                'industry_id': merchant.industry_id,
                'industry_name': merchant.industry.industry_name if merchant.industry else '',
                'street_id': merchant.street_id,
                'establishment_date': str(merchant.establishment_date) if merchant.establishment_date else '',
                'registration_date': str(merchant.registration_date) if merchant.registration_date else '',
                'last_update_time': str(merchant.last_update_time) if merchant.last_update_time else ''
            }
        except Merchant.DoesNotExist:
            return None
    
    @staticmethod
    def get_business_by_credit_code(credit_code):
        """根据信用代码获取商户信息"""
        try:
            merchant = Merchant.objects.get(credit_code=credit_code)
            return {
                'id': merchant.id,
                'merchants_name': merchant.merchants_name,
                'credit_code': merchant.credit_code,
                'license_number': merchant.license_number,
                'legal_person_name': merchant.legal_person_name,
                'legal_person_id': merchant.legal_person_id,
                'phone_number': merchant.phone_number,
                'address': merchant.address,
                'business_scope': merchant.business_scope,
                'industry_id': merchant.industry_id,
                'industry_name': merchant.industry.industry_name if merchant.industry else '',
                'street_id': merchant.street_id,
                'establishment_date': str(merchant.establishment_date) if merchant.establishment_date else '',
                'registration_date': str(merchant.registration_date) if merchant.registration_date else '',
                'last_update_time': str(merchant.last_update_time) if merchant.last_update_time else ''
            }
        except Merchant.DoesNotExist:
            return None
    
    @staticmethod
    def get_all_businesses(page=1, page_size=10):
        """获取所有商户信息（分页）"""
        start = (page - 1) * page_size
        end = start + page_size
        merchants = Merchant.objects.all()[start:end]
        total = Merchant.objects.count()
        
        # 转换为字典列表
        merchant_list = []
        for merchant in merchants:
            merchant_list.append({
                'id': merchant.id,
                'merchants_name': merchant.merchants_name,
                'credit_code': merchant.credit_code,
                'license_number': merchant.license_number,
                'legal_person_name': merchant.legal_person_name,
                'legal_person_id': merchant.legal_person_id,
                'phone_number': merchant.phone_number,
                'address': merchant.address,
                'business_scope': merchant.business_scope,
                'industry_id': merchant.industry_id,
                'industry_name': merchant.industry.industry_name if merchant.industry else '',
                'street_id': merchant.street_id,
                'establishment_date': str(merchant.establishment_date) if merchant.establishment_date else '',
                'registration_date': str(merchant.registration_date) if merchant.registration_date else '',
                'last_update_time': str(merchant.last_update_time) if merchant.last_update_time else ''
            })
        
        return {
            'data': merchant_list,
            'total': total,
            'page': page,
            'page_size': page_size
        }
    
    @staticmethod
    def add_business(data):
        """添加商户信息"""
        try:
            # 创建商户对象
            merchant = Merchant(**data)
            merchant.save()
            # 返回创建的商户信息
            return {
                'id': merchant.id,
                'merchants_name': merchant.merchants_name,
                'credit_code': merchant.credit_code,
                'license_number': merchant.license_number,
                'legal_person_name': merchant.legal_person_name,
                'legal_person_id': merchant.legal_person_id,
                'phone_number': merchant.phone_number,
                'address': merchant.address,
                'business_scope': merchant.business_scope,
                'industry_id': merchant.industry_id,
                'industry_name': merchant.industry.industry_name if merchant.industry else '',
                'street_id': merchant.street_id,
                'establishment_date': str(merchant.establishment_date) if merchant.establishment_date else '',
                'registration_date': str(merchant.registration_date) if merchant.registration_date else '',
                'last_update_time': str(merchant.last_update_time) if merchant.last_update_time else ''
            }
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def update_business(business_id, data):
        """更新商户信息"""
        try:
            merchant = Merchant.objects.get(id=business_id)
            # 更新商户信息
            for key, value in data.items():
                setattr(merchant, key, value)
            merchant.save()
            # 返回更新后的商户信息
            return {
                'id': merchant.id,
                'merchants_name': merchant.merchants_name,
                'credit_code': merchant.credit_code,
                'license_number': merchant.license_number,
                'legal_person_name': merchant.legal_person_name,
                'legal_person_id': merchant.legal_person_id,
                'phone_number': merchant.phone_number,
                'address': merchant.address,
                'business_scope': merchant.business_scope,
                'industry_id': merchant.industry_id,
                'industry_name': merchant.industry.industry_name if merchant.industry else '',
                'street_id': merchant.street_id,
                'establishment_date': str(merchant.establishment_date) if merchant.establishment_date else '',
                'registration_date': str(merchant.registration_date) if merchant.registration_date else '',
                'last_update_time': str(merchant.last_update_time) if merchant.last_update_time else ''
            }
        except Merchant.DoesNotExist:
            return {'error': '商户不存在'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def delete_business(business_id):
        """删除商户信息"""
        try:
            merchant = Merchant.objects.get(id=business_id)
            merchant.delete()
            return True
        except Merchant.DoesNotExist:
            return False
    
    @staticmethod
    def search_businesses(keyword, page=1, page_size=10):
        """搜索商户信息"""
        start = (page - 1) * page_size
        end = start + page_size
        
        # 按名称、信用代码或法人姓名搜索
        merchants = Merchant.objects.filter(
            merchants_name__icontains=keyword
        ) | Merchant.objects.filter(
            credit_code__icontains=keyword
        ) | Merchant.objects.filter(
            legal_person_name__icontains=keyword
        )
        
        total = merchants.count()
        paginated_merchants = merchants[start:end]
        
        # 转换为字典列表
        merchant_list = []
        for merchant in paginated_merchants:
            merchant_list.append({
                'id': merchant.id,
                'merchants_name': merchant.merchants_name,
                'credit_code': merchant.credit_code,
                'license_number': merchant.license_number,
                'legal_person_name': merchant.legal_person_name,
                'legal_person_id': merchant.legal_person_id,
                'phone_number': merchant.phone_number,
                'address': merchant.address,
                'business_scope': merchant.business_scope,
                'industry_id': merchant.industry_id,
                'industry_name': merchant.industry.industry_name if merchant.industry else '',
                'street_id': merchant.street_id,
                'establishment_date': str(merchant.establishment_date) if merchant.establishment_date else '',
                'registration_date': str(merchant.registration_date) if merchant.registration_date else '',
                'last_update_time': str(merchant.last_update_time) if merchant.last_update_time else ''
            })
        
        return {
            'total': total,
            'page': page,
            'page_size': page_size,
            'data': merchant_list,
        }
    
    @staticmethod
    def get_businesses_by_industry(industry_id, page=1, page_size=10):
        """按行业获取商户信息"""
        start = (page - 1) * page_size
        end = start + page_size
        
        merchants = Merchant.objects.filter(industry_id=industry_id)
        total = merchants.count()
        paginated_merchants = merchants[start:end]
        
        # 转换为字典列表
        merchant_list = []
        for merchant in paginated_merchants:
            merchant_list.append({
                'id': merchant.id,
                'merchants_name': merchant.merchants_name,
                'credit_code': merchant.credit_code,
                'license_number': merchant.license_number,
                'legal_person_name': merchant.legal_person_name,
                'legal_person_id': merchant.legal_person_id,
                'phone_number': merchant.phone_number,
                'address': merchant.address,
                'business_scope': merchant.business_scope,
                'industry_id': merchant.industry_id,
                'industry_name': merchant.industry.industry_name if merchant.industry else '',
                'street_id': merchant.street_id,
                'establishment_date': str(merchant.establishment_date) if merchant.establishment_date else '',
                'registration_date': str(merchant.registration_date) if merchant.registration_date else '',
                'last_update_time': str(merchant.last_update_time) if merchant.last_update_time else ''
            })
        
        return {
            'total': total,
            'page': page,
            'page_size': page_size,
            'data': merchant_list,
        }
    
    @staticmethod
    def get_businesses_by_street(street_id, page=1, page_size=10):
        """按街道获取商户信息"""
        start = (page - 1) * page_size
        end = start + page_size
        
        merchants = Merchant.objects.filter(street_id=street_id)
        total = merchants.count()
        paginated_merchants = merchants[start:end]
        
        # 转换为字典列表
        merchant_list = []
        for merchant in paginated_merchants:
            merchant_list.append({
                'id': merchant.id,
                'merchants_name': merchant.merchants_name,
                'credit_code': merchant.credit_code,
                'license_number': merchant.license_number,
                'legal_person_name': merchant.legal_person_name,
                'legal_person_id': merchant.legal_person_id,
                'phone_number': merchant.phone_number,
                'address': merchant.address,
                'business_scope': merchant.business_scope,
                'industry_id': merchant.industry_id,
                'industry_name': merchant.industry.industry_name if merchant.industry else '',
                'street_id': merchant.street_id,
                'establishment_date': str(merchant.establishment_date) if merchant.establishment_date else '',
                'registration_date': str(merchant.registration_date) if merchant.registration_date else '',
                'last_update_time': str(merchant.last_update_time) if merchant.last_update_time else ''
            })
        
        return {
            'total': total,
            'page': page,
            'page_size': page_size,
            'data': merchant_list,
        }
    
    @staticmethod
    def get_industry_distribution():
        """获取商户行业分布统计"""
        # 按行业分组并统计数量
        distribution = Merchant.objects.values('industry_id', 'industry__industry_name').annotate(
            count=Count('id')
        ).order_by('-count')
        
        # 格式化结果
        result = []
        for item in distribution:
            result.append({
                'industry_id': item['industry_id'],
                'industry_name': item['industry__industry_name'],
                'count': item['count']
            })
        
        return result
    
    @staticmethod
    def get_new_businesses_count(time_range='month'):
        """获取新增商户数量统计"""
        # 计算时间范围
        now = datetime.now()
        if time_range == 'day':
            start_date = now - timedelta(days=1)
        elif time_range == 'week':
            start_date = now - timedelta(weeks=1)
        elif time_range == 'month':
            start_date = now - timedelta(days=30)
        elif time_range == 'year':
            start_date = now - timedelta(days=365)
        else:
            start_date = now - timedelta(days=30)
        
        # 统计新增商户数量
        return Merchant.objects.filter(registration_date__gte=start_date).count()
    
    @staticmethod
    def get_all_merchants(page=1, page_size=10):
        """获取所有商户信息（由于模型中没有status字段，提供基础分页查询）"""
        start = (page - 1) * page_size
        end = start + page_size
        
        merchants = Merchant.objects.all()
        total = merchants.count()
        paginated_merchants = merchants[start:end]
        
        # 转换为字典列表
        merchant_list = []
        for merchant in paginated_merchants:
            merchant_list.append({
                'id': merchant.id,
                'merchants_name': merchant.merchants_name,
                'credit_code': merchant.credit_code,
                'license_number': merchant.license_number,
                'legal_person_name': merchant.legal_person_name,
                'legal_person_id': merchant.legal_person_id,
                'phone_number': merchant.phone_number,
                'address': merchant.address,
                'business_scope': merchant.business_scope,
                'industry_id': merchant.industry_id,
                'industry_name': merchant.industry.industry_name if merchant.industry else '',
                'street_id': merchant.street_id,
                'establishment_date': str(merchant.establishment_date) if merchant.establishment_date else '',
                'registration_date': str(merchant.registration_date) if merchant.registration_date else '',
                'last_update_time': str(merchant.last_update_time) if merchant.last_update_time else ''
            })
        
        return {
            'total': total,
            'page': page,
            'page_size': page_size,
            'data': merchant_list,
        }
    
    @staticmethod
    def get_all_industries():
        """获取所有行业信息"""
        industries = Industry.objects.all()
        return [industry.to_dict() for industry in industries]