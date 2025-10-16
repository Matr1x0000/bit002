from properties.models import Property
from datetime import timezone


class PropertyService:
    @staticmethod
    def get_property_by_id(property_id):
        """根据ID获取物业信息"""
        try:
            property = Property.objects.get(id=property_id)
            return property.to_dict()
        except Property.DoesNotExist:
            return None
    
    @staticmethod
    def get_all_properties(page=1, page_size=10):
        """获取所有物业信息（分页）"""
        start = (page - 1) * page_size
        end = start + page_size
        
        properties = Property.objects.all()[start:end]
        total = Property.objects.count()
        
        return {
            'data': [property.to_dict() for property in properties],
            'total': total,
            'page': page,
            'page_size': page_size
        }
    
    @staticmethod
    def add_property(data):
        """添加物业信息"""
        try:
            # 创建物业对象
            property = Property(**data)
            property.save()
            return property.to_dict()
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def update_property(property_id, data):
        """更新物业信息"""
        try:
            property = Property.objects.get(id=property_id)
            
            # 更新字段
            for key, value in data.items():
                setattr(property, key, value)
            
            property.last_update_time = timezone.now()
            property.save()
            
            return property.to_dict()
        except Property.DoesNotExist:
            return {'error': '物业不存在'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def delete_property(property_id):
        """删除物业信息"""
        try:
            property = Property.objects.get(id=property_id)
            property.delete()
            return True
        except Property.DoesNotExist:
            return False
    
    @staticmethod
    def search_properties(keyword, page=1, page_size=10):
        """搜索物业信息"""
        start = (page - 1) * page_size
        end = start + page_size
        
        # 按名称或地址搜索
        properties = Property.objects.filter(
            name__contains=keyword
        ) | Property.objects.filter(
            address__contains=keyword
        ) | Property.objects.filter(
            contact_person__contains=keyword
        )
        
        total = properties.count()
        paginated_properties = properties[start:end]
        
        return {
            'data': [property.to_dict() for property in paginated_properties],
            'total': total,
            'page': page,
            'page_size': page_size
        }
    
    @staticmethod
    def get_property_by_community(community_id):
        """获取指定社区的物业信息"""
        properties = Property.objects.filter(community_id=community_id, status=1)
        return [property.to_dict() for property in properties]
    
    @staticmethod
    def get_active_properties():
        """获取所有正常运行的物业信息"""
        properties = Property.objects.filter(status=1)
        return [property.to_dict() for property in properties]
    
    @staticmethod
    def get_property_count_by_status():
        """按状态统计物业数量"""
        status_counts = Property.objects.values('status').annotate(count=1)
        status_map = {
            0: '未启用',
            1: '正常',
            2: '已停用'
        }
        
        result = []
        for item in status_counts:
            result.append({
                'status': item['status'],
                'status_name': status_map.get(item['status'], '未知'),
                'count': item['count']
            })
        
        return result