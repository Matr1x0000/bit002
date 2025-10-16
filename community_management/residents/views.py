from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from residents.services.resident_service import ResidentService
from authentication.utils.jwt_helper import jwt_required_with_role


@csrf_exempt
def resident_api(request):
    """居民信息API接口"""
    # 解析请求参数
    data = json.loads(request.body) if request.body else {}
    method = request.method
    action = data.get('action')
    
    # 根据不同的操作执行不同的方法
    if method == 'GET':
        # 获取单个居民信息
        if 'id' in request.GET:
            resident_id = request.GET.get('id')
            resident = ResidentService.get_resident_by_id(resident_id)
            if resident:
                return JsonResponse({'success': True, 'data': resident})
            else:
                return JsonResponse({'success': False, 'message': '居民不存在'})
        # 根据身份证号获取居民信息
        elif 'id_card' in request.GET:
            id_card = request.GET.get('id_card')
            resident = ResidentService.get_resident_by_id_card(id_card)
            if resident:
                return JsonResponse({'success': True, 'data': resident})
            else:
                return JsonResponse({'success': False, 'message': '居民不存在'})
        # 获取居民列表
        else:
            page = int(request.GET.get('page', 1))
            page_size = int(request.GET.get('page_size', 10))
            residents = ResidentService.get_all_residents(page, page_size)
            return JsonResponse({'success': True, 'data': residents})
    
    elif method == 'POST':
        if action == 'add':
            # 添加居民
            result = ResidentService.add_resident(data)
            if 'error' not in result:
                return JsonResponse({'success': True, 'message': '添加成功', 'data': result})
            else:
                return JsonResponse({'success': False, 'message': result['error']})
        elif action == 'update':
            # 更新居民
            resident_id = data.get('id')
            if not resident_id:
                return JsonResponse({'success': False, 'message': '缺少居民ID'})
            update_data = data.copy()
            del update_data['id']
            del update_data['action']
            result = ResidentService.update_resident(resident_id, update_data)
            if 'error' not in result:
                return JsonResponse({'success': True, 'message': '更新成功', 'data': result})
            else:
                return JsonResponse({'success': False, 'message': result['error']})
        elif action == 'delete':
            # 删除居民
            resident_id = data.get('id')
            if not resident_id:
                return JsonResponse({'success': False, 'message': '缺少居民ID'})
            result = ResidentService.delete_resident(resident_id)
            if result:
                return JsonResponse({'success': True, 'message': '删除成功'})
            else:
                return JsonResponse({'success': False, 'message': '居民不存在'})
        elif action == 'search':
            # 搜索居民
            keyword = data.get('keyword', '')
            page = data.get('page', 1)
            page_size = data.get('page_size', 10)
            results = ResidentService.search_residents(keyword, page, page_size)
            return JsonResponse({'success': True, 'data': results})
        elif action == 'get_by_community':
            # 获取指定社区的居民
            community_id = data.get('community_id')
            page = data.get('page', 1)
            page_size = data.get('page_size', 10)
            if not community_id:
                return JsonResponse({'success': False, 'message': '缺少社区ID'})
            results = ResidentService.get_residents_by_community(community_id, page, page_size)
            return JsonResponse({'success': True, 'data': results})
        elif action == 'get_special_stats':
            # 获取特殊人群统计
            stats = ResidentService.get_special_population_stats()
            return JsonResponse({'success': True, 'data': stats})
        elif action == 'get_new_count':
            # 获取新增居民数量
            time_range = data.get('time_range', 'month')
            count = ResidentService.get_new_residents_count(time_range)
            return JsonResponse({'success': True, 'data': {'count': count}})
        elif action == 'get_gender_distribution':
            # 获取性别分布
            distribution = ResidentService.get_resident_distribution_by_gender()
            return JsonResponse({'success': True, 'data': distribution})
        elif action == 'get_age_distribution':
            # 获取年龄分布
            distribution = ResidentService.get_resident_distribution_by_age_group()
            return JsonResponse({'success': True, 'data': distribution})
        else:
            return JsonResponse({'success': False, 'message': '未知的操作'})
    
    else:
        return JsonResponse({'success': False, 'message': '不支持的请求方法'})
