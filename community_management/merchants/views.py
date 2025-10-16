from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from merchants.services.business_service import BusinessService


@csrf_exempt
def business_api(request):
    """商户信息API接口"""
    # 解析请求参数
    data = json.loads(request.body) if request.body else {}
    method = request.method
    action = data.get('action')
    
    # 根据不同的操作执行不同的方法
    if method == 'GET':
        # 获取单个商户信息
        if 'id' in request.GET:
            business_id = request.GET.get('id')
            business = BusinessService.get_business_by_id(business_id)
            if business:
                return JsonResponse({'success': True, 'data': business})
            else:
                return JsonResponse({'success': False, 'message': '商户不存在'})
        # 根据信用代码获取商户信息
        elif 'credit_code' in request.GET:
            credit_code = request.GET.get('credit_code')
            business = BusinessService.get_business_by_credit_code(credit_code)
            if business:
                return JsonResponse({'success': True, 'data': business})
            else:
                return JsonResponse({'success': False, 'message': '商户不存在'})
        # 获取商户列表
        elif 'industry_id' in request.GET:
            # 获取指定行业的商户
            industry_id = request.GET.get('industry_id')
            page = int(request.GET.get('page', 1))
            page_size = int(request.GET.get('page_size', 10))
            businesses = BusinessService.get_businesses_by_industry(industry_id, page, page_size)
            return JsonResponse({'success': True, 'data': businesses})
        elif 'community_id' in request.GET:
            # 获取指定社区的商户
            community_id = request.GET.get('community_id')
            page = int(request.GET.get('page', 1))
            page_size = int(request.GET.get('page_size', 10))
            businesses = BusinessService.get_businesses_by_community(community_id, page, page_size)
            return JsonResponse({'success': True, 'data': businesses})
        # 获取所有商户列表
        elif 'get_all' in request.GET:
            businesses = BusinessService.get_all_businesses()
            return JsonResponse({'success': True, 'data': businesses})
        else:
            # 分页获取商户列表
            page = int(request.GET.get('page', 1))
            page_size = int(request.GET.get('page_size', 10))
            businesses = BusinessService.get_all_businesses(page, page_size)
            return JsonResponse({'success': True, 'data': businesses})
    
    elif method == 'POST':
        if action == 'add':
            # 添加商户
            result = BusinessService.add_business(data)
            if 'error' not in result:
                return JsonResponse({'success': True, 'message': '添加成功', 'data': result})
            else:
                return JsonResponse({'success': False, 'message': result['error']})
        elif action == 'update':
            # 更新商户
            business_id = data.get('id')
            if not business_id:
                return JsonResponse({'success': False, 'message': '缺少商户ID'})
            update_data = data.copy()
            del update_data['id']
            del update_data['action']
            result = BusinessService.update_business(business_id, update_data)
            if 'error' not in result:
                return JsonResponse({'success': True, 'message': '更新成功', 'data': result})
            else:
                return JsonResponse({'success': False, 'message': result['error']})
        elif action == 'delete':
            # 删除商户
            business_id = data.get('id')
            if not business_id:
                return JsonResponse({'success': False, 'message': '缺少商户ID'})
            result = BusinessService.delete_business(business_id)
            if result:
                return JsonResponse({'success': True, 'message': '删除成功'})
            else:
                return JsonResponse({'success': False, 'message': '商户不存在'})
        elif action == 'search':
            # 搜索商户
            keyword = data.get('keyword', '')
            page = data.get('page', 1)
            page_size = data.get('page_size', 10)
            results = BusinessService.search_businesses(keyword, page, page_size)
            return JsonResponse({'success': True, 'data': results})
        elif action == 'get_industry_distribution':
            # 获取行业分布统计
            distribution = BusinessService.get_industry_distribution()
            return JsonResponse({'success': True, 'data': distribution})
        elif action == 'get_new_count':
            # 获取新增商户数量
            time_range = data.get('time_range', 'month')
            count = BusinessService.get_new_businesses_count(time_range)
            return JsonResponse({'success': True, 'data': {'count': count}})
        elif action == 'get_status_distribution':
            # 获取状态分布
            distribution = BusinessService.get_business_status_distribution()
            return JsonResponse({'success': True, 'data': distribution})
        elif action == 'get_all_industries':
            # 获取所有行业
            industries = BusinessService.get_all_industries()
            return JsonResponse({'success': True, 'data': industries})
        else:
            return JsonResponse({'success': False, 'message': '未知的操作'})
    
    else:
        return JsonResponse({'success': False, 'message': '不支持的请求方法'})
