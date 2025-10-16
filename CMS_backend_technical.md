# 社区信息管理系统后端技术文档

## 一、后端系统概述

本系统后端部分采用Python 3.11开发，负责核心业务逻辑处理与数据管理，为前端提供RESTful API接口。后端采用Django框架构建，结合Django ORM进行数据库操作，实现了模块化、可扩展的系统架构。

## 二、后端技术栈

### 2.1 核心技术
- **Python 3.11**：主要开发语言，提供强大的数据处理能力和丰富的第三方库支持
  - 支持异步编程，提升系统性能
  - 简洁的语法，提高开发效率

### 2.2 Web框架
- **Django 4.2+**：全功能Web框架，负责HTTP请求处理和API接口实现
  - 内置ORM、管理后台等丰富功能
  - 完善的安全性和可扩展性

### 2.3 API框架
- **Django REST framework 3.14+**：为Django提供RESTful API支持
  - 内置序列化器、视图集等组件
  - 完善的权限控制和分页功能

### 2.4 ORM框架
- **Django ORM**：Django内置的对象关系映射框架，简化数据库操作
  - 支持多种数据库后端
  - 提供高级查询API和数据库迁移

### 2.5 数据库
- **MySQL 8.0**：严格按照数据库设计规范要求，统一使用MySQL 8.0作为数据库系统
  - 高性能，适合生产环境，支持大数据量
  - 字符集：UTF-8
  - 排序规则：utf8mb4_unicode_ci

### 2.6 身份验证
- **Django Auth**：Django内置的认证系统
- **Simple JWT**：基于Token的身份验证机制

### 2.7 数据处理
- **Pandas 1.5+**：强大的数据处理和分析库
- **NumPy 1.23+**：科学计算基础库

### 2.8 图表生成
- **Matplotlib 3.7+**：基础图表生成库
- **Seaborn 0.12+**：高级统计图表库

### 2.9 Windows集成
- **pywin32**：提供Windows API访问，支持系统级功能集成

## 三、后端架构设计

### 3.1 整体架构

后端采用Django标准架构，结合RESTful API设计理念：

1. **表示层**：Django视图和Django REST framework视图集，处理HTTP请求和响应
2. **业务逻辑层**：服务类和业务逻辑函数，实现核心业务功能
3. **数据访问层**：Django模型，负责与数据库交互

### 3.2 目录结构

```
community_management/
├── community_management/
│   ├── __init__.py          # 项目初始化
│   ├── settings.py          # 项目设置
│   ├── urls.py              # 主URL配置
│   ├── wsgi.py              # WSGI配置
│   └── asgi.py              # ASGI配置
├── residents/
│   ├── __init__.py
│   ├── admin.py             # Django管理后台
│   ├── apps.py              # 应用配置
│   ├── models.py            # 居民模型
│   ├── serializers.py       # DRF序列化器
│   ├── views.py             # Django视图
│   ├── viewsets.py          # DRF视图集
│   ├── urls.py              # 应用URL配置
│   ├── services/            # 业务服务
│   │   └── __init__.py
│   └── utils/               # 工具函数
│       └── __init__.py
├── businesses/
│   ├── __init__.py
│   ├── admin.py             # Django管理后台
│   ├── apps.py              # 应用配置
│   ├── models.py            # 商户模型
│   ├── serializers.py       # DRF序列化器
│   ├── views.py             # Django视图
│   ├── viewsets.py          # DRF视图集
│   ├── urls.py              # 应用URL配置
│   ├── services/            # 业务服务
│   │   └── __init__.py
│   └── utils/               # 工具函数
│       └── __init__.py
├── authentication/
│   ├── __init__.py
│   ├── admin.py             # Django管理后台
│   ├── apps.py              # 应用配置
│   ├── models.py            # 认证相关模型
│   ├── serializers.py       # DRF序列化器
│   ├── views.py             # Django视图
│   ├── viewsets.py          # DRF视图集
│   ├── urls.py              # 应用URL配置
│   ├── services/            # 认证服务
│   │   └── __init__.py
│   └── utils/               # 认证工具
│       └── __init__.py
├── statistics/
│   ├── __init__.py
│   ├── admin.py             # Django管理后台
│   ├── apps.py              # 应用配置
│   ├── models.py            # 统计相关模型
│   ├── serializers.py       # DRF序列化器
│   ├── views.py             # Django视图
│   ├── viewsets.py          # DRF视图集
│   ├── urls.py              # 应用URL配置
│   ├── services/            # 统计服务
│   │   └── __init__.py
│   └── utils/               # 统计工具
│       └── __init__.py
├── utils/
│   ├── __init__.py
│   ├── excel_helper.py      # Excel处理工具
│   └── common.py            # 通用工具函数
├── templates/               # HTML模板（如需）
├── static/                  # 静态资源
├── media/                   # 媒体文件
├── db.sqlite3               # SQLite数据库（开发环境）
├── manage.py                # Django管理脚本
├── requirements.txt         # 项目依赖
└── .env                     # 环境变量配置
```

## 四、后端模块详细设计

### 4.1 项目设置模块

#### 4.1.1 功能描述
负责Django项目的全局配置，包括数据库设置、认证设置、中间件配置等。

#### 4.1.2 核心代码结构
```python
# community_management/settings.py
import os
from pathlib import Path
from datetime import timedelta

# 构建路径
BASE_DIR = Path(__file__).resolve().parent.parent

# 密钥配置
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-#your-secret-key-here')

# 调试模式
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# 允许的主机
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

# 安装的应用
INSTALLED_APPS = [
    # Django内置应用
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 第三方应用
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    
    # 自定义应用
    'residents',
    'businesses',
    'authentication',
    'statistics',
    'utils',
]

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根URL配置
ROOT_URLCONF = 'community_management.urls'

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI应用
WSGI_APPLICATION = 'community_management.wsgi.application'

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'community_management'),
        'USER': os.getenv('DB_USER', 'root'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# 认证配置
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 国际化配置
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_TZ = False

# 静态文件配置
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 媒体文件配置
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# REST Framework配置
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Simple JWT配置
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': True,
    
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    
    'JTI_CLAIM': 'jti',
}

# CORS配置
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

# 自定义用户模型
AUTH_USER_MODEL = 'authentication.Admin'

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': os.getenv('LOG_LEVEL', 'INFO'),
    },
}

# 文件上传配置
FILE_UPLOAD_MAX_MEMORY_SIZE = 16 * 1024 * 1024  # 16MB
```

### 4.3 数据模型模块

#### 4.3.1 功能描述
定义系统的数据模型，映射数据库表结构，实现数据的持久化。

#### 4.3.2 核心模型设计
# community/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin

class Community(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='小区唯一标识', auto_created=True)
    community_name = models.CharField(max_length=255, verbose_name='小区名称', blank=False, unique=True)
    group_id = models.ForeignKey('groups.Group', on_delete=models.CASCADE, verbose_name='所属组别ID', blank=False)
    community_number = models.CharField(max_length=50, verbose_name='小区号', blank=False)
    has_property = models.IntegerField(default=0, verbose_name='是否有物业', blank=False, choices=((0, '否'), (1, '是')))
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期', blank=False)
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间', blank=False)
    
    class Meta:
        verbose_name = '小区信息'
        verbose_name_plural = '小区信息'
        db_table = 'communities'
        indexes = [
            models.Index(fields=['community_name']),
            models.Index(fields=['group_id']),
            models.Index(fields=['has_property']),
        ]

# property/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin
from community.models import Community

class Property(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='物业唯一标识', auto_created=True)
    property_name = models.CharField(max_length=255, verbose_name='物业名称', blank=False, unique=True)
    property_address = models.CharField(max_length=255, verbose_name='物业地址', blank=False)
    property_owner = models.CharField(max_length=255, verbose_name='物业负责人', blank=False)
    property_contact_phone = models.CharField(max_length=20, verbose_name='物业联系电话', blank=False)
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期', blank=False)
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间', blank=False)
    
    class Meta:
        verbose_name = '物业信息'
        verbose_name_plural = '物业信息'
        db_table = 'properties'
        indexes = [
            models.Index(fields=['property_name']),
            models.Index(fields=['property_owner']),
            models.Index(fields=['property_contact_phone']),
        ]
    
    def to_dict(self):
        return {
            'id': self.id,
            'property_name': self.property_name,
            'property_address': self.property_address,
            'property_owner': self.property_owner,
            'property_contact_phone': self.property_contact_phone,
            'registration_date': self.registration_date.isoformat(),
            'last_update_time': self.last_update_time.isoformat()
        }

# property_managers/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin
from community.models import Community
from property.models import Property

class PropertyManager(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='物业管理唯一标识', auto_created=True)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='物业ID', blank=False)
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE, verbose_name='所属小区ID', blank=False, unique=True)
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期', blank=False)
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间', blank=False)
    
    class Meta:
        verbose_name = '物业管理'
        verbose_name_plural = '物业管理'
        db_table = 'property_managers'
        indexes = [
            models.Index(fields=['property_id']),
            models.Index(fields=['community_id']),
        ]
    
    def to_dict(self):
        return {
            'id': self.id,
            'property_id': self.property_id.id,
            'community_id': self.community_id.id,
            'registration_date': self.registration_date.isoformat(),
            'last_update_time': self.last_update_time.isoformat()
        }

# businesses/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin
from community.models import Community

class Business(models.Model):
    # 基本信息
    id = models.IntegerField(primary_key=True, verbose_name='商户ID', auto_created=True)
    merchants_name = models.CharField(max_length=100, verbose_name='商户名称', blank=False, db_index=True)
    license_number = models.CharField(max_length=50, verbose_name='营业执照编号', blank=False, db_index=True)
    credit_code = models.CharField(max_length=18, verbose_name='统一社会信用代码', unique=True, blank=False, db_index=True)
    
    # 负责人信息
    legal_person_name = models.CharField(max_length=50, verbose_name='法定代表人姓名', blank=False)
    legal_person_id = models.CharField(max_length=18, verbose_name='法定代表人身份证号', blank=False)
    phone_number = models.CharField(max_length=20, verbose_name='联系电话', blank=True)
    
    # 地址信息
    address = models.CharField(max_length=255, verbose_name='地址', blank=False)
    
    # 经营信息
    business_scope = models.TextField(verbose_name='经营范围', blank=True)
    industry_id = models.ForeignKey('industry.Industry', on_delete=models.PROTECT, verbose_name='所属行业ID', blank=False)
    streets_id = models.ForeignKey('street.Street', on_delete=models.PROTECT, verbose_name='所属街道ID', blank=False)
    establishment_date = models.DateField(verbose_name='成立日期', blank=False)
    
    # 时间信息
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期', blank=False)
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间', blank=False)
    
    # 管理员信息
    created_by = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True, related_name='created_businesses', verbose_name='创建人')
    updated_by = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True, related_name='updated_businesses', verbose_name='更新人')
    
    class Meta:
        verbose_name = '商户信息'
        verbose_name_plural = '商户信息'
        ordering = ['-last_update_time']
        db_table = 'merchants'
        indexes = [
            models.Index(fields=['merchants_name', 'license_number']),
            models.Index(fields=['legal_person_name', 'credit_code']),
            models.Index(fields=['streets_id', 'industry_id']),
        ]
    
    def to_dict(self):
        return {
            'id': self.id,
            'merchants_name': self.merchants_name,
            'license_number': self.license_number,
            'credit_code': self.credit_code,
            'legal_person_name': self.legal_person_name,
            'legal_person_id': self.legal_person_id,
            'phone_number': self.phone_number,
            'address': self.address,
            'business_scope': self.business_scope,
            'industry_id': self.industry_id.id if self.industry_id else None,
            'industry_name': self.industry_id.name if self.industry_id else None,
            'streets_id': self.streets_id.id if self.streets_id else None,
            'street_name': self.streets_id.name if self.streets_id else None,
            'establishment_date': self.establishment_date.isoformat() if self.establishment_date else None,
            'registration_date': self.registration_date.isoformat(),
            'last_update_time': self.last_update_time.isoformat(),
            'created_by': self.created_by.id if self.created_by else None,
            'updated_by': self.updated_by.id if self.updated_by else None
        }

# industry/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin
from community.models import Community

class Industry(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='行业唯一标识', auto_created=True)
    industry_name = models.CharField(max_length=100, verbose_name='行业名称', blank=False, unique=True)
    industry_code = models.CharField(max_length=50, verbose_name='行业代码', blank=False, unique=True)
    
    class Meta:
        verbose_name = '行业信息'
        verbose_name_plural = '行业信息'
        db_table = 'industries'
        indexes = [
            models.Index(fields=['industry_name']),
            models.Index(fields=['industry_code']),
        ]

# street/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin
from community.models import Community

class Street(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='街道唯一标识', auto_created=True)
    street_name = models.CharField(max_length=100, verbose_name='街道名称', blank=False, unique=True)
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期', blank=False)
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间', blank=False)
    
    class Meta:
        verbose_name = '街道信息'
        verbose_name_plural = '街道信息'
        db_table = 'streets'
        indexes = [
            models.Index(fields=['street_name']),
        ]

# residents/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin
from community.models import Community
from ethnicities.models import Ethnicity

class Resident(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='居民ID', auto_created=True)
    name = models.CharField(max_length=50, verbose_name='居民姓名', blank=False)
    id_card = models.CharField(max_length=18, verbose_name='身份证号', blank=False, unique=True)
    gender = models.IntegerField(default=0, verbose_name='性别', blank=False, choices=((0, '男'), (1, '女')))
    birth_date = models.DateField(verbose_name='出生日期', blank=False)
    ethnicity_id = models.ForeignKey('ethnicities.Ethnicity', on_delete=models.PROTECT, verbose_name='民族ID', blank=False)
    political_affiliation = models.IntegerField(default=0, verbose_name='政治面貌', blank=False, 
                                             choices=((0, '群众'), (1, '中共党员'), (2, '共青团员'), 
                                                      (3, '中国国民党革命委员会'), (4, '中国民主同盟'), 
                                                      (5, '中国民主建国会'), (6, '中国民主促进会'), 
                                                      (7, '中国农工民主党'), (8, '中国致公党'), 
                                                      (9, '九三学社'), (10, '台湾民主自治同盟')))
    household_address = models.CharField(max_length=255, verbose_name='户籍地址', blank=False)
    phone_number = models.CharField(max_length=20, verbose_name='联系方式', blank=False)
    marital_status = models.IntegerField(default=0, verbose_name='婚姻状况', blank=False, 
                                       choices=((0, '未婚'), (1, '已婚'), (2, '离异'), (3, '丧偶')))
    education_level = models.IntegerField(default=0, verbose_name='学历', blank=False, 
                                        choices=((0, '文盲'), (1, '小学'), (2, '初中'), 
                                                 (3, '高中'), (4, '大专'), (5, '本科'), (6, '研究生')))
    population_type = models.IntegerField(default=0, verbose_name='人口类型', blank=False, 
                                        choices=((0, '常住人口'), (1, '非常住人口')))
    residential_type = models.IntegerField(default=0, verbose_name='住宅类型', blank=False, 
                                         choices=((0, '楼房'), (1, '平房')))
    own_house = models.IntegerField(default=0, verbose_name='是否自有房', blank=False, 
                                  choices=((0, '是'), (1, '否')))
    is_low_income = models.IntegerField(default=0, verbose_name='是否低保户', blank=False, 
                                      choices=((0, '否'), (1, '是')))
    is_beneficiary = models.IntegerField(default=0, verbose_name='是否五保户', blank=False, 
                                       choices=((0, '否'), (1, '是')))
    is_disabled = models.IntegerField(default=0, verbose_name='是否残疾', blank=False, 
                                    choices=((0, '否'), (1, '是')))
    is_special_support = models.IntegerField(default=0, verbose_name='是否特扶人口', blank=False, 
                                           choices=((0, '否'), (1, '是')))
    is_key_person = models.IntegerField(default=0, verbose_name='是否重点对象', blank=False, 
                                      choices=((0, '否'), (1, '是')))
    is_deceased = models.IntegerField(default=0, verbose_name='是否死亡', blank=False, 
                                    choices=((0, '否'), (1, '是')))
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期', blank=False)
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间', blank=False)
    created_by = models.ForeignKey(Admin, on_delete=models.SET_NULL, verbose_name='创建人', null=True, blank=True)
    updated_by = models.ForeignKey(Admin, on_delete=models.SET_NULL, verbose_name='更新人', null=True, blank=True, related_name='updated_residents')
    
    class Meta:
        verbose_name = '居民信息'
        verbose_name_plural = '居民信息'
        db_table = 'residents'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['ethnicity_id']),
            models.Index(fields=['political_affiliation']),
            models.Index(fields=['population_type']),
            models.Index(fields=['residential_type']),
            models.Index(fields=['marital_status']),
            models.Index(fields=['education_level']),
            models.Index(fields=['id_card']),
        ]
        unique_together = (
            ('id_card',),
        )
        
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'id_card': self.id_card,
            'gender': self.gender,
            'birth_date': self.birth_date.isoformat() if self.birth_date else None,
            'ethnicity_id': self.ethnicity_id,
            'political_affiliation': self.political_affiliation,
            'household_address': self.household_address,
            'phone_number': self.phone_number,
            'marital_status': self.marital_status,
            'education_level': self.education_level,
            'population_type': self.population_type,
            'residential_type': self.residential_type,
            'own_house': self.own_house,
            'is_low_income': self.is_low_income,
            'is_beneficiary': self.is_beneficiary,
            'is_disabled': self.is_disabled,
            'is_special_support': self.is_special_support,
            'is_key_person': self.is_key_person,
            'is_deceased': self.is_deceased,
            'registration_date': self.registration_date.isoformat(),
            'last_update_time': self.last_update_time.isoformat(),
            'created_by': self.created_by.id if self.created_by else None,
            'updated_by': self.updated_by.id if self.updated_by else None
        }

# units/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin
from community.models import Community

class Unit(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='单元ID')
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='楼栋ID', blank=False)
    unit_number = models.CharField(max_length=50, verbose_name='单元号', blank=False)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        verbose_name = '单元信息'
        verbose_name_plural = '单元信息'
        db_table = 'units'
        unique_together = ('building_id', 'unit_number')

# houses/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin
from community.models import Community

class House(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='房屋ID')
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name='单元ID', blank=False)
    number = models.CharField(max_length=20, verbose_name='房屋编号', blank=False)
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='房屋面积', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        verbose_name = '房屋信息'
        verbose_name_plural = '房屋信息'
        db_table = 'houses'
        unique_together = ('unit_id', 'number')

# flats/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin
from community.models import Community

class Flat(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='平房ID')
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE, verbose_name='社区ID', blank=False)
    alley_id = models.ForeignKey('Alley', on_delete=models.CASCADE, verbose_name='胡同ID', blank=False)
    number = models.CharField(max_length=20, verbose_name='平房编号', blank=False)
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='平房面积', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        verbose_name = '平房信息'
        verbose_name_plural = '平房信息'
        db_table = 'flats'
        unique_together = ('community_id', 'alley_id', 'number')

# alleys/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin
from community.models import Community

class Alley(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='胡同ID')
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE, verbose_name='社区ID', blank=False)
    name = models.CharField(max_length=100, verbose_name='胡同名称', blank=False)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        verbose_name = '胡同信息'
        verbose_name_plural = '胡同信息'
        db_table = 'alleys'
        unique_together = ('community_id', 'name')

# groups/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin
from community.models import Community

class Group(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='组别唯一标识', auto_created=True)
    group_number = models.CharField(max_length=50, verbose_name='组别号', blank=False, unique=True)
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期', blank=False)
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间', blank=False)
    
    class Meta:
        verbose_name = '组别信息'
        verbose_name_plural = '组别信息'
        db_table = 'groups'
        indexes = [
            models.Index(fields=['group_number']),
        ]

# house_numbers/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin
from community.models import Community

class HouseNumber(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='门牌号ID')
    number = models.CharField(max_length=50, verbose_name='门牌号', blank=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        verbose_name = '门牌号信息'
        verbose_name_plural = '门牌号信息'
        db_table = 'house_numbers'

# ethnicities/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin

class Ethnicity(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='民族ID', auto_created=True)
    name = models.CharField(max_length=50, verbose_name='民族名称', blank=False, unique=True)
    
    class Meta:
        verbose_name = '民族信息'
        verbose_name_plural = '民族信息'
        db_table = 'ethnicities'
        indexes = [
            models.Index(fields=['name']),
        ]

# low_income_households/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin

class LowIncomeHousehold(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='低保户ID', auto_created=True)
    resident_id = models.OneToOneField('residents.Resident', on_delete=models.CASCADE, verbose_name='居民ID', blank=False)
    authentication_date = models.DateTimeField(verbose_name='认证日期', blank=False)
    bank_account_number = models.CharField(max_length=50, verbose_name='银行卡号', blank=False, unique=True)
    bank_account_name = models.CharField(max_length=100, verbose_name='银行卡账户名称', blank=False)
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期', blank=False)
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间', blank=False)
    
    class Meta:
        verbose_name = '低保户信息'
        verbose_name_plural = '低保户信息'
        db_table = 'low_income_residents'
        indexes = [
            models.Index(fields=['resident_id']),
        ]

# five_guarantee_households/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin

class FiveGuaranteeHousehold(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='五保户ID', auto_created=True)
    resident_id = models.OneToOneField('residents.Resident', on_delete=models.CASCADE, verbose_name='居民ID', blank=False)
    authentication_date = models.DateTimeField(verbose_name='认证日期', blank=False)
    bank_account_number = models.CharField(max_length=50, verbose_name='银行卡号', blank=False, unique=True)
    bank_account_name = models.CharField(max_length=100, verbose_name='银行卡账户名称', blank=False)
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期', blank=False)
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间', blank=False)
    
    class Meta:
        verbose_name = '五保户信息'
        verbose_name_plural = '五保户信息'
        db_table = 'five_guarantees_residents'
        indexes = [
            models.Index(fields=['resident_id']),
        ]

# disabled_persons/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin

class DisabledPerson(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='残疾人ID', auto_created=True)
    resident_id = models.OneToOneField('residents.Resident', on_delete=models.CASCADE, verbose_name='居民ID', blank=False)
    authentication_date = models.DateTimeField(verbose_name='认证日期', blank=False)
    bank_account_number = models.CharField(max_length=50, verbose_name='银行卡号', blank=False, unique=True)
    bank_account_name = models.CharField(max_length=100, verbose_name='银行卡账户名称', blank=False)
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期', blank=False)
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间', blank=False)
    
    class Meta:
        verbose_name = '残疾人信息'
        verbose_name_plural = '残疾人信息'
        db_table = 'disabled_residents'
        indexes = [
            models.Index(fields=['resident_id']),
        ]

# special_support_households/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin

class SpecialSupportHousehold(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='特扶户ID', auto_created=True)
    resident_id = models.OneToOneField('residents.Resident', on_delete=models.CASCADE, verbose_name='居民ID', blank=False)
    authentication_date = models.DateTimeField(verbose_name='认证日期', blank=False)
    bank_account_number = models.CharField(max_length=50, verbose_name='银行卡号', blank=False, unique=True)
    bank_account_name = models.CharField(max_length=100, verbose_name='银行卡账户名称', blank=False)
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期', blank=False)
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间', blank=False)
    
    class Meta:
        verbose_name = '特扶户信息'
        verbose_name_plural = '特扶户信息'
        db_table = 'special_needs_residents'
        indexes = [
            models.Index(fields=['resident_id']),
        ]

# deceased_persons/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin

class DeceasedPerson(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='死亡户ID', auto_created=True)
    resident_id = models.OneToOneField('residents.Resident', on_delete=models.CASCADE, verbose_name='居民ID', blank=False)
    deceased_date = models.DateTimeField(verbose_name='死亡日期', blank=False)
    deceased_place = models.CharField(max_length=100, verbose_name='死亡地点', blank=False)
    deceased_reason = models.CharField(max_length=255, verbose_name='死亡原因', blank=False)
    deceased_contact_name = models.CharField(max_length=100, verbose_name='联系人姓名', blank=False)
    deceased_contact_phone = models.CharField(max_length=20, verbose_name='联系人电话', blank=False)
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期', blank=False)
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间', blank=False)
    
    class Meta:
        verbose_name = '死亡户信息'
        verbose_name_plural = '死亡户信息'
        db_table = 'deceased_residents'
        indexes = [
            models.Index(fields=['resident_id']),
        ]

# key_persons/models.py
from django.db import models
from django.utils import timezone
from authentication.models import Admin

class KeyPerson(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='重点对象ID', auto_created=True)
    resident_id = models.OneToOneField('residents.Resident', on_delete=models.CASCADE, verbose_name='居民ID', blank=False)
    object_type = models.IntegerField(verbose_name='对象类型', blank=False, choices=((0, '信访'), (1, '新疆'), (2, '西藏')))
    object_name = models.CharField(max_length=100, verbose_name='对象姓名', blank=False)
    object_contact_phone = models.CharField(max_length=20, verbose_name='对象联系电话', blank=False)
    object_address = models.CharField(max_length=255, verbose_name='对象住址', blank=False)
    object_responsible_name = models.CharField(max_length=100, verbose_name='负责人姓名', blank=False)
    object_responsible_phone = models.CharField(max_length=20, verbose_name='负责人联系电话', blank=False)
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='登记日期', blank=False)
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间', blank=False)
    
    class Meta:
        verbose_name = '重点对象信息'
        verbose_name_plural = '重点对象信息'
        db_table = 'special_objects'
        indexes = [
            models.Index(fields=['resident_id']),
        ]

**auth_service.py**
```python
# app/services/auth_service.py
from app import db
from app.models.admin import Admin
from app.utils.auth_helper import hash_password, verify_password

class AuthService:
    @staticmethod
    def authenticate(username, password):
        """验证用户凭据"""
        admin = Admin.query.filter_by(username=username, status=1).first()
        if admin and verify_password(password, admin.password_hash):
            return admin
        return None
    
    @staticmethod
    def update_last_login(admin_id):
        """更新最后登录时间"""
        admin = Admin.query.get(admin_id)
        if admin:
            from datetime import datetime
            admin.last_login_time = datetime.utcnow()
            db.session.commit()
    
    @staticmethod
    def get_admin_by_id(admin_id):
        """通过ID获取管理员信息"""
        return Admin.query.get(admin_id)
    
    @staticmethod
    def add_admin(data):
        """添加管理员"""
        # 检查用户名是否已存在
        if Admin.query.filter_by(username=data['username']).first():
            raise Exception('用户名已存在')
        
        # 创建新管理员
        admin = Admin(
            username=data['username'],
            password_hash=hash_password(data['password']),
            real_name=data.get('real_name'),
            phone_number=data.get('phone_number'),
            email=data.get('email'),
            role=data.get('role', 0),
            status=data.get('status', 1)
        )
        
        db.session.add(admin)
        db.session.commit()
        
        return admin
    
    @staticmethod
    def change_password(admin_id, old_password, new_password):
        """修改密码"""
        admin = Admin.query.get(admin_id)
        if not admin:
            raise Exception('用户不存在')
        
        if not verify_password(old_password, admin.password_hash):
            raise Exception('原密码错误')
        
        admin.password_hash = hash_password(new_password)
        db.session.commit()
        
        return True
```

**resident_service.py**
```python
# residents/services.py
from django.db.models import Q
from django.utils import timezone
from residents.models import Resident
from datetime import datetime

class ResidentService:
    @staticmethod
    def get_residents(filters=None, page=1, page_size=10):
        """获取居民列表"""
        queryset = Resident.objects.all()
        
        # 应用过滤条件
        if filters:
            for key, value in filters.items():
                if key == 'name':
                    queryset = queryset.filter(name__icontains=value)
                elif key == 'id_card':
                    queryset = queryset.filter(id_card=value)
                else:
                    queryset = queryset.filter(**{key: value})
        
        # 计算总数
        total = queryset.count()
        
        # 分页
        residents = queryset.order_by('-last_update_time')
                           .all()[(page - 1) * page_size:page * page_size]
        
        return residents, total
    
    @staticmethod
    def get_resident_by_id(resident_id):
        """通过ID获取居民信息"""
        try:
            return Resident.objects.get(id=resident_id)
        except Resident.DoesNotExist:
            return None
    
    @staticmethod
    def add_resident(data):
        """添加居民信息"""
        # 检查身份证号是否已存在
        if Resident.objects.filter(id_card=data['id_card']).exists():
            raise Exception('身份证号已存在')
        
        # 转换日期格式
        if 'birth_date' in data and isinstance(data['birth_date'], str):
            data['birth_date'] = datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
        
        if 'death_date' in data and data['death_date'] and isinstance(data['death_date'], str):
            data['death_date'] = datetime.strptime(data['death_date'], '%Y-%m-%d').date()
        
        # 添加创建时间和更新时间
        data['create_time'] = timezone.now()
        data['last_update_time'] = timezone.now()
        
        # 创建新居民
        resident = Resident.objects.create(**data)
        
        return resident
    
    @staticmethod
    def update_resident(resident_id, data):
        """更新居民信息"""
        try:
            resident = Resident.objects.get(id=resident_id)
        except Resident.DoesNotExist:
            return None
        
        # 检查身份证号是否与其他居民重复
        if 'id_card' in data and data['id_card'] != resident.id_card:
            if Resident.objects.filter(id_card=data['id_card']).exists():
                raise Exception('身份证号已存在')
        
        # 转换日期格式
        if 'birth_date' in data and isinstance(data['birth_date'], str):
            data['birth_date'] = datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
        
        if 'death_date' in data and data['death_date'] and isinstance(data['death_date'], str):
            data['death_date'] = datetime.strptime(data['death_date'], '%Y-%m-%d').date()
        
        # 更新居民信息
        for key, value in data.items():
            setattr(resident, key, value)
        
        # 更新最后更新时间
        resident.last_update_time = timezone.now()
        resident.save()
        
        return resident
    
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
    def get_special_population_stats():
        """获取特殊人群统计数据"""
        stats = {
            'disabled': Resident.objects.filter(is_disabled=1, is_deceased=0).count(),
            'elderly': Resident.objects.filter(is_elderly=1, is_deceased=0).count(),
            'special_support': Resident.objects.filter(is_special_support=1, is_deceased=0).count(),
            'low_income': Resident.objects.filter(is_low_income=1, is_deceased=0).count(),
            'beneficiary': Resident.objects.filter(is_beneficiary=1, is_deceased=0).count(),
            'key_person': Resident.objects.filter(is_key_person=1, is_deceased=0).count()
        }
        
        return stats
```

**business_service.py**
```python
# businesses/services.py
from django.db.models import Count
from django.utils import timezone
from businesses.models import Business, Industry
from datetime import datetime

class BusinessService:
    @staticmethod
    def get_businesses(filters=None, page=1, page_size=10):
        """获取商户列表"""
        queryset = Business.objects.all()
        
        # 应用过滤条件
        if filters:
            for key, value in filters.items():
                if key == 'business_name':
                    queryset = queryset.filter(business_name__icontains=value)
                elif key == 'credit_code':
                    queryset = queryset.filter(credit_code=value)
                else:
                    queryset = queryset.filter(**{key: value})
        
        # 计算总数
        total = queryset.count()
        
        # 分页
        businesses = queryset.order_by('-last_update_time')
                          .all()[(page - 1) * page_size:page * page_size]
        
        return businesses, total
    
    @staticmethod
    def get_business_by_id(business_id):
        """通过ID获取商户信息"""
        try:
            return Business.objects.get(id=business_id)
        except Business.DoesNotExist:
            return None
    
    @staticmethod
    def add_business(data):
        """添加商户信息"""
        # 检查统一社会信用代码是否已存在
        if Business.objects.filter(credit_code=data['credit_code']).exists():
            raise Exception('统一社会信用代码已存在')
        
        # 转换日期格式
        if 'establishment_date' in data and isinstance(data['establishment_date'], str):
            data['establishment_date'] = datetime.strptime(data['establishment_date'], '%Y-%m-%d').date()
        
        # 添加创建时间和更新时间
        data['create_time'] = timezone.now()
        data['last_update_time'] = timezone.now()
        
        # 创建新商户
        business = Business.objects.create(**data)
        
        return business
    
    @staticmethod
    def update_business(business_id, data):
        """更新商户信息"""
        try:
            business = Business.objects.get(id=business_id)
        except Business.DoesNotExist:
            return None
        
        # 检查统一社会信用代码是否与其他商户重复
        if 'credit_code' in data and data['credit_code'] != business.credit_code:
            if Business.objects.filter(credit_code=data['credit_code']).exists():
                raise Exception('统一社会信用代码已存在')
        
        # 转换日期格式
        if 'establishment_date' in data and isinstance(data['establishment_date'], str):
            data['establishment_date'] = datetime.strptime(data['establishment_date'], '%Y-%m-%d').date()
        
        # 更新商户信息
        for key, value in data.items():
            setattr(business, key, value)
        
        # 更新最后更新时间
        business.last_update_time = timezone.now()
        business.save()
        
        return business
    
    @staticmethod
    def delete_business(business_id):
        """删除商户信息"""
        try:
            business = Business.objects.get(id=business_id)
            business.delete()
            return True
        except Business.DoesNotExist:
            return False
    
    @staticmethod
    def get_industry_distribution():
        """获取商户行业分布"""
        # 使用Django ORM的annotate和values进行分组查询
        queryset = Industry.objects.values('industry_name')
                                  .annotate(count=Count('business'))
                                  .order_by('-count')
        
        distribution = [{'name': item['industry_name'], 'count': item['count']} for item in queryset]
        
        return distribution

**物业服务（PropertyService）**
```python
# property/services.py
from property.models import Property
from django.db.models import Q
from datetime import datetime
from django.utils import timezone

class PropertyService:
    @staticmethod
    def get_properties(filters=None, page=1, page_size=10):
        """获取物业列表"""
        # 构建查询集
        queryset = Property.objects.all()
        
        # 应用过滤条件
        if filters:
            if 'name' in filters and filters['name']:
                queryset = queryset.filter(name__icontains=filters['name'])
            if 'contact_person' in filters and filters['contact_person']:
                queryset = queryset.filter(contact_person__icontains=filters['contact_person'])
            if 'contact_phone' in filters and filters['contact_phone']:
                queryset = queryset.filter(contact_phone__icontains=filters['contact_phone'])
            if 'community_id' in filters and filters['community_id']:
                queryset = queryset.filter(community_id=filters['community_id'])
            if 'status' in filters and filters['status'] is not None:
                queryset = queryset.filter(status=filters['status'])
            if 'property_type' in filters and filters['property_type'] is not None:
                queryset = queryset.filter(property_type=filters['property_type'])
        
        # 计算总数
        total_count = queryset.count()
        
        # 分页
        start = (page - 1) * page_size
        end = start + page_size
        properties = queryset.order_by('-last_update_time')[start:end]
        
        # 转换为字典列表
        result = [property.to_dict() for property in properties]
        
        return {
            'total': total_count,
            'page': page,
            'page_size': page_size,
            'data': result
        }
    
    @staticmethod
    def get_property_by_id(property_id):
        """根据ID获取物业信息"""
        try:
            property = Property.objects.get(id=property_id)
            return property.to_dict()
        except Property.DoesNotExist:
            return None
    
    @staticmethod
    def add_property(data):
        """添加物业信息"""
        # 检查licenses号是否已存在
        if Property.objects.filter(license_number=data['license_number']).exists():
            raise Exception('licenses号已存在')
        
        # 转换日期格式
        if 'establish_date' in data and isinstance(data['establish_date'], str):
            data['establish_date'] = datetime.strptime(data['establish_date'], '%Y-%m-%d').date()
        
        # 添加创建时间和更新时间
        data['create_time'] = timezone.now()
        data['last_update_time'] = timezone.now()
        
        # 创建新物业
        property = Property.objects.create(**data)
        
        return property.to_dict()
    
    @staticmethod
    def update_property(property_id, data):
        """更新物业信息"""
        try:
            property = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            return None
        
        # 检查licenses号是否与其他物业重复
        if 'license_number' in data and data['license_number'] != property.license_number:
            if Property.objects.filter(license_number=data['license_number']).exists():
                raise Exception('licenses号已存在')
        
        # 转换日期格式
        if 'establish_date' in data and isinstance(data['establish_date'], str):
            data['establish_date'] = datetime.strptime(data['establish_date'], '%Y-%m-%d').date()
        
        # 更新物业信息
        for key, value in data.items():
            setattr(property, key, value)
        
        # 更新最后更新时间
        property.last_update_time = timezone.now()
        property.save()
        
        return property.to_dict()
    
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
    def get_property_by_community(community_id):
        """获取指定社区的物业信息"""
        properties = Property.objects.filter(community_id=community_id, status=1)
        return [property.to_dict() for property in properties]
```

### 4.6 工具函数模块

#### 4.6.1 JWT工具

**功能描述**：提供JWT相关的工具函数，如Token生成、验证、解析等。

```python
# authentication/utils/jwt_helper.py
import jwt
from django.http import JsonResponse
from functools import wraps
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from authentication.models import Admin
from django.conf import settings


def jwt_required_with_role(role):
    """带角色检查的JWT装饰器"""
    def wrapper(view_func):
        @wraps(view_func)
        def decorator(request, *args, **kwargs):
            auth = JWTAuthentication()
            try:
                # 验证JWT Token
                user, token = auth.authenticate(request)
                
                # 检查用户角色
                if user.role < role:
                    return JsonResponse({'message': '权限不足'}, status=403)
                
                # 将用户添加到请求对象中
                request.user = user
                
                return view_func(request, *args, **kwargs)
            except (InvalidToken, TokenError):
                return JsonResponse({'message': '无效的Token'}, status=401)
        return decorator
    return wrapper


def generate_token(admin_id):
    """生成JWT Token"""
    from rest_framework_simplejwt.tokens import RefreshToken
    
    # 创建刷新令牌
    refresh = RefreshToken.for_user(Admin.objects.get(id=admin_id))
    
    # 获取访问令牌
    access_token = str(refresh.access_token)
    
    return access_token


def decode_token(token):
    """解析JWT Token"""
    from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
    from rest_framework_simplejwt.tokens import AccessToken
    
    try:
        # 解析Token
        access_token = AccessToken(token)
        # 获取用户ID
        user_id = access_token['user_id']
        
        return {
            'user_id': user_id,
            'exp': access_token['exp']
        }
    except TokenError:
        return {'error': '无效的Token'}
    except InvalidToken:
        return {'error': 'Token已过期'}
```

#### 4.6.2 Excel处理工具

**功能描述**：提供Excel文件的导入导出功能。

```python
# utils/excel_helper.py
import pandas as pd
import os
from datetime import datetime
from django.conf import settings


class ExcelHelper:
    @staticmethod
    def export_to_excel(data, filename=None, sheet_name='Sheet1'):
        """将数据导出为Excel文件"""
        # 创建DataFrame
        df = pd.DataFrame(data)
        
        # 生成文件名
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'export_{timestamp}.xlsx'
        
        # 确保文件路径存在
        exports_dir = os.path.join(settings.MEDIA_ROOT, 'exports')
        os.makedirs(exports_dir, exist_ok=True)
        file_path = os.path.join(exports_dir, filename)
        
        # 导出Excel
        df.to_excel(file_path, index=False, sheet_name=sheet_name)
        
        # 返回相对于MEDIA_ROOT的路径
        return os.path.join('exports', filename)
    
    @staticmethod
    def import_from_excel(file_path, sheet_name=0):
        """从Excel文件导入数据"""
        # 构建完整的文件路径
        full_path = os.path.join(settings.MEDIA_ROOT, file_path)
        
        # 读取Excel文件
        df = pd.read_excel(full_path, sheet_name=sheet_name)
        
        # 转换为字典列表
        data = df.to_dict('records')
        
        return data
    
    @staticmethod
    def validate_excel_structure(data, required_columns):
        """验证Excel数据结构是否符合要求"""
        # 检查是否为空
        if not data:
            return False, '数据为空'
        
        # 检查必需列
        first_row = data[0]
        missing_columns = [col for col in required_columns if col not in first_row]
        
        if missing_columns:
            return False, f'缺少必需的列：{', '.join(missing_columns)}'
        
        return True, '验证通过'
```

## 五、后端数据流程

### 5.1 数据输入流程
1. 用户通过前端界面输入数据
2. 前端进行客户端验证
3. 前端将数据以JSON格式发送到后端API
4. 后端接收数据，进行服务端验证
5. 后端将验证通过的数据转换为数据模型对象
6. 后端通过ORM框架将数据持久化到数据库
7. 后端返回操作结果给前端

### 5.2 数据查询流程
1. 前端发送查询请求到后端API
2. 后端验证用户身份和权限
3. 后端解析查询条件和参数
4. 后端通过ORM框架从数据库查询数据
5. 后端将查询结果转换为数据模型对象
6. 后端将数据模型对象序列化为JSON格式
7. 后端将JSON数据返回给前端
8. 前端接收数据，渲染界面

### 5.3 数据更新流程
1. 前端发送更新请求和更新数据到后端API
2. 后端验证用户身份和权限
3. 后端解析更新数据和目标对象标识
4. 后端通过ORM框架查询目标对象
5. 后端更新对象属性
6. 后端通过ORM框架将更新后的数据持久化到数据库
7. 后端返回更新结果给前端

## 六、后端安全机制

### 6.1 身份验证
- 使用Django Auth+Simple JWT进行无状态身份验证
- 密码加盐哈希存储，使用Django内置的密码加密和验证
- 定期更换Django SECRET_KEY
- 实现Token过期机制
- 使用Django的密码验证器确保密码强度

### 6.2 权限控制
- 基于角色的访问控制（RBAC）
- 使用Django REST Framework的权限类实现细粒度的权限检查
- 为不同的API接口设置不同的权限级别
- 使用Django的Group和Permission模型管理用户权限

### 6.3 数据安全
- 使用Django ORM防止SQL注入
- 验证用户输入数据的合法性和完整性，使用Django Forms和ModelForms
- 敏感数据加密存储，使用Django的加密功能
- 实现Django的admin日志记录

### 6.4 请求安全
- 使用Django REST Framework的throttle实现请求频率限制，防止暴力攻击
- 检测异常请求模式
- 使用Django内置的CSRF保护
- 设置合理的HTTP安全头部，使用Django的security middleware

## 七、后端性能优化

### 7.1 数据库优化
- 对常用查询字段创建索引，使用Django的db_index和index_together
- 合理设计复合索引
- 使用Django ORM的select_related和prefetch_related优化查询
- 避免N+1查询问题
- 优化复杂查询语句，使用Django的QuerySet优化
- 使用Django的数据库连接池设置

### 7.2 缓存机制
- 使用Django的缓存框架，集成Redis缓存热点数据
- 实现数据缓存失效策略，使用缓存版本控制
- 使用Django REST Framework的缓存响应
- 使用Django的模板缓存和视图缓存减少数据库查询

### 7.3 异步处理
- 使用Django Channels处理WebSocket连接
- 使用Celery处理耗时操作异步处理
- 使用消息队列解耦系统组件
- 实现异步任务调度

### 7.4 代码优化
- 优化算法和数据结构
- 减少不必要的计算和IO操作
- 使用Django的QuerySet优化处理大数据量
- 使用Django的ContentType框架实现通用关系

## 八、后端部署说明

### 8.1 开发环境部署
1. 安装Python 3.11
2. 创建虚拟环境：`python -m venv venv`
3. 激活虚拟环境：`venv\Scripts\activate`（Windows）
4. 安装项目依赖：`pip install -r requirements.txt`
5. 运行数据库迁移：`python manage.py migrate`
6. 创建超级用户：`python manage.py createsuperuser`
7. 运行开发服务器：`python manage.py runserver`

### 8.2 生产环境部署
1. 配置MySQL数据库
2. 设置环境变量和配置文件
3. 使用Gunicorn/uWSGI作为WSGI服务器
4. 使用Nginx作为反向代理
5. 配置HTTPS
6. 设置监控和日志系统
7. 运行数据库迁移：`python manage.py migrate`
8. 收集静态文件：`python manage.py collectstatic`

```bash
# 使用Gunicorn启动Django应用
gunicorn --workers 4 --bind 127.0.0.1:8000 cms_project.wsgi:application
```

### 8.3 Docker部署
```dockerfile
FROM python:3.11

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y default-libmysqlclient-dev gcc

# 复制项目文件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 设置环境变量
ENV DJANGO_SETTINGS_MODULE=cms_project.settings.production
ENV SECRET_KEY=your-secret-key
ENV DEBUG=False
ENV DATABASE_URL=mysql://user:password@db:3306/community

# 收集静态文件
RUN python manage.py collectstatic --noinput

# 运行数据库迁移
RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "cms_project.wsgi:application"]
```

## 九、后端测试与监控

### 9.1 单元测试
- 使用Django测试框架编写单元测试
- 测试覆盖主要业务逻辑和API接口
- 实现自动化测试
- 运行测试命令：`python manage.py test`

### 9.2 集成测试
- 测试系统各组件之间的交互
- 测试API接口的正确性和完整性
- 测试数据库操作的正确性
- 使用Django的测试客户端进行API测试

### 9.3 性能测试
- 测试系统在高并发下的性能表现
- 测试API接口的响应时间
- 测试数据库查询的性能
- 使用Django Debug Toolbar分析性能瓶颈

### 9.4 监控与日志
- 使用Django的日志系统记录系统运行状态和错误信息
- 实现性能监控和告警机制
- 定期分析日志和监控数据，优化系统性能
- 配置Django的admin日志记录用户操作

## 十、可扩展性设计

### 10.1 模块化设计
- 组件化开发，利用Django的应用(app)结构
- 松耦合高内聚
- 标准化接口设计，使用Django REST Framework的序列化器和视图
- 利用Django的信号系统实现组件间通信

### 10.2 插件机制
- 支持通过Django应用扩展功能
- 标准化的Django应用接口
- 使用Django的app注册机制实现动态加载
- 实现插件配置系统

### 10.3 微服务思想
- 业务模块独立部署（未来扩展）
- 服务间通过RESTful API通信
- 使用Django REST Framework构建标准化API
- 使用消息队列实现服务解耦
- 考虑使用Django的多站点功能支持多租户场景