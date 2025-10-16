from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from properties.services.property_service import PropertyService


@csrf_exempt
def property_api(request):
    """物业信息API接口"""
    # 解析请求参数
    data = json.loads(request.body) if request.body else {}
    method = request.method
    action = data.get('action')
    
    # 根据不同的操作执行不同的方法
    if method == 'GET':
        # 获取单个物业信息
        if 'id' in request.GET:
            property_id = request.GET.get('id')
            property = PropertyService.get_property_by_id(property_id)
            if property:
                return JsonResponse({'success': True, 'data': property})
            else:
                return JsonResponse({'success': False, 'message': '物业不存在'})
        # 获取指定社区的物业信息
        elif 'community_id' in request.GET:
            community_id = request.GET.get('community_id')
            properties = PropertyService.get_property_by_community(community_id)
            return JsonResponse({'success': True, 'data': properties})
        # 获取所有活跃物业
        elif 'active_only' in request.GET:
            properties = PropertyService.get_active_properties()
            return JsonResponse({'success': True, 'data': properties})
        # 获取物业列表
        else:
            page = int(request.GET.get('page', 1))
            page_size = int(request.GET.get('page_size', 10))
            properties = PropertyService.get_all_properties(page, page_size)
            return JsonResponse({'success': True, 'data': properties})
    
    elif method == 'POST':
        if action == 'add':
            # 添加物业
            result = PropertyService.add_property(data)
            if 'error' not in result:
                return JsonResponse({'success': True, 'message': '添加成功', 'data': result})
            else:
                return JsonResponse({'success': False, 'message': result['error']})
        elif action == 'update':
            # 更新物业
            property_id = data.get('id')
            if not property_id:
                return JsonResponse({'success': False, 'message': '缺少物业ID'})
            update_data = data.copy()
            del update_data['id']
            del update_data['action']
            result = PropertyService.update_property(property_id, update_data)
            if 'error' not in result:
                return JsonResponse({'success': True, 'message': '更新成功', 'data': result})
            else:
                return JsonResponse({'success': False, 'message': result['error']})
        elif action == 'delete':
            # 删除物业
            property_id = data.get('id')
            if not property_id:
                return JsonResponse({'success': False, 'message': '缺少物业ID'})
            result = PropertyService.delete_property(property_id)
            if result:
                return JsonResponse({'success': True, 'message': '删除成功'})
            else:
                return JsonResponse({'success': False, 'message': '物业不存在'})
        elif action == 'search':
            # 搜索物业
            keyword = data.get('keyword', '')
            page = data.get('page', 1)
            page_size = data.get('page_size', 10)
            results = PropertyService.search_properties(keyword, page, page_size)
            return JsonResponse({'success': True, 'data': results})
        elif action == 'get_status_count':
            # 获取状态统计
            counts = PropertyService.get_property_count_by_status()
            return JsonResponse({'success': True, 'data': counts})
        else:
            return JsonResponse({'success': False, 'message': '未知的操作'})
    
    else:
        return JsonResponse({'success': False, 'message': '不支持的请求方法'})
