from django.shortcuts import render
from datetime import datetime, timedelta
from django.db.models import Count
from residents.models import Resident, Deceased, Disabled, LowIncome, FiveGuarantees, SpecialNeeds
from merchants.models import Merchant

def get_statistics_data(period='year'):
    """根据时间周期从数据库获取统计数据"""
    # 计算时间范围
    now = datetime.now()
    if period == 'year':
        start_date = now - timedelta(days=365)
    else:  # month
        start_date = now - timedelta(days=30)
    
    # 获取总人口（不包括死亡人口）
    total_population = Resident.objects.filter(is_deceased=0).count()
    
    # 获取商户总数
    total_merchants = Merchant.objects.count()
    
    # 获取新增人口（按登记日期）
    new_population = Resident.objects.filter(
        registration_date__gte=start_date,
        is_deceased=0
    ).count()
    
    # 获取新增商户（按登记日期）
    new_merchants = Merchant.objects.filter(
        registration_date__gte=start_date
    ).count()
    
    # 获取死亡人口总数
    total_deceased = Resident.objects.filter(is_deceased=1).count()
    
    # 获取新增死亡人口
    new_deceased = Deceased.objects.filter(
        registration_date__gte=start_date
    ).count()
    
    # 获取残疾人总数
    total_disabled = Resident.objects.filter(is_disabled=1).count()
    
    # 获取新增残疾人
    new_disabled = Disabled.objects.filter(
        registration_date__gte=start_date
    ).count()
    
    # 获取特扶人口总数
    total_special_needs = Resident.objects.filter(is_special_support=1).count()
    
    # 获取新增特扶人口
    new_special_needs = SpecialNeeds.objects.filter(
        registration_date__gte=start_date
    ).count()
    
    # 获取低保户总数
    total_low_income = Resident.objects.filter(is_low_income=1).count()
    
    # 获取新增低保户
    new_low_income = LowIncome.objects.filter(
        registration_date__gte=start_date
    ).count()
    
    # 获取五保户总数
    total_five_guarantees = Resident.objects.filter(is_beneficiary=1).count()
    
    # 获取新增五保户
    new_five_guarantees = FiveGuarantees.objects.filter(
        registration_date__gte=start_date
    ).count()
    
    return {
        'total_population': total_population,
        'total_merchants': total_merchants,
        'new_population': new_population,
        'new_merchants': new_merchants,
        'total_deceased': total_deceased,
        'new_deceased': new_deceased,
        'total_disabled': total_disabled,
        'new_disabled': new_disabled,
        'total_special_needs': total_special_needs,
        'new_special_needs': new_special_needs,
        'total_low_income': total_low_income,
        'new_low_income': new_low_income,
        'total_five_guarantees': total_five_guarantees,
        'new_five_guarantees': new_five_guarantees
    }

def index(request):
    """首页视图，提供统计数据"""
    # 获取时间周期参数，默认为year，只允许year或month
    period = request.GET.get('period', 'year')
    # 验证period参数，只允许'year'或'month'
    if period not in ['year', 'month']:
        period = 'year'
    
    # 获取统计数据
    stats_data = get_statistics_data(period)
    
    # 从session中获取登录用户信息
    username = request.session.get('username')
    print(f"用户名: {username}")
    
    # 构建上下文数据
    context = {
        'period': period,
        'username': username,
        **stats_data
    }
    
    return render(request, 'index.html', context)
