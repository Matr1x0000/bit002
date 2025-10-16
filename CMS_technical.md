# 社区信息管理系统技术文档

## 一、系统概述

本系统是基于Python 3.11开发的社区信息管理系统，核心目标是实现对社区居民及商户信息的高效管理，并提供全面的统计分析功能，以辅助社区管理人员深入了解社区状况并优化服务质量。系统采用前后端分离架构：后端采用Python 3.11和Django框架作为开发语言和Web框架，负责核心业务逻辑处理与数据管理，提供RESTful API接口；前端运用HTML5、CSS3、JavaScript技术栈，结合Bootstrap和ECharts构建直观且交互友好的用户操作界面。前端通过HTTP/HTTPS协议与后端Django REST Framework提供的RESTful API进行通信，实现完整的系统功能。

## 二、系统架构

### 2.1 总体架构设计

系统采用经典的三层架构设计，结合前后端分离模式，具体包括：

1. **表示层（前端）**：提供用户界面，负责数据展示和用户交互
   - 基于HTML5/CSS3/JavaScript(ES6+)构建Web界面
   - 使用Bootstrap 5.2+实现响应式设计
   - 集成ECharts 5.4+提供数据可视化
   - 使用jQuery 3.6+简化DOM操作和AJAX请求
   - 通过HTTP/HTTPS协议与后端Django REST Framework提供的RESTful API通信

2. **应用层（后端业务逻辑）**：处理核心业务逻辑，实现各功能模块
   - Django 4.2+框架处理HTTP请求
   - Django REST Framework 3.14+实现RESTful API接口
   - 进行权限验证和数据过滤
   - 业务逻辑处理和数据转换

3. **数据访问层**：负责与数据库交互，进行数据的增删改查操作
   - Django ORM框架
   - 模型定义和数据操作
   - 查询构建和优化

4. **数据库**：MySQL 8.0（统一使用，包括开发和生产环境）
   - 字符集：UTF-8
   - 排序规则：utf8mb4_unicode_ci

### 2.2 系统架构图

```
┌─────────────────────────────────────────────────────────┐
│                      表示层（前端）                       │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐     │
│  │ 用户界面UI   │  │ 数据可视化   │  │ 交互组件     │     │
│  │ (HTML/CSS/JS)│  │  (ECharts)   │  │ (Bootstrap)  │     │
│  └─────────────┘  └─────────────┘  └──────────────┘     │
└───────────────────────┬─────────────────────────────────┘
                        │ HTTP/HTTPS 通信
┌───────────────────────▼─────────────────────────────────┐
│                     应用层（后端）                        │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐     │
│  │ API接口层    │  │ 业务逻辑层   │  │ 认证授权层   │     │
│  │ (Django REST)│  │ (视图/服务)   │  │ (Django Auth)│     │
│  └─────────────┘  └─────────────┘  └──────────────┘     │
└───────────────────────┬─────────────────────────────────┘
                        │  ORM映射
┌───────────────────────▼─────────────────────────────────┐
│                     数据访问层                           │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐     │
│  │ ORM框架     │  │ 数据模型     │  │ 查询构建器    │     │
│  │ (Django ORM)│  │ (Models)     │  │ (QuerySet)   │     │
│  └─────────────┘  └─────────────┘  └──────────────┘     │
└───────────────────────┬─────────────────────────────────┘
                        │  SQL操作
┌───────────────────────▼─────────────────────────────────┐
│                       数据库                             │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐     │
│  │ MySQL       │  │ MySQL       │  │ 数据存储     │     │
│  │ (统一使用)   │  │ (统一使用)   │  │ (表、索引)   │     │
│  └─────────────┘  └─────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────┘
```

## 三、功能模块设计

详见[社区信息管理系统功能模块设计](CMS_design.md)

## 四、数据库设计

系统数据库采用MySQL 8.0，包含以下核心表：
1. **居民信息表（residents）**：存储居民基本信息，包括姓名、身份证号、联系方式等
2. **楼房信息表（buildings）**：存储楼房基本信息
3. **小区信息表（communities）**：存储小区基本信息
4. **单元信息表（units）**：存储单元基本信息
5. **房屋信息表（houses）**：存储房屋基本信息
6. **平房信息表（flats）**：存储平房基本信息
7. **胡同信息表（alleys）**：存储胡同基本信息
8. **门牌号信息表（house_numbers）**：存储门牌号基本信息
9. **组别信息表（groups）**：存储组别基本信息
10. **物业信息表（properties）**：存储物业基本信息
11. **物业管理表（property_managers）**：存储物业与小区的管理关系
12. **商户信息表（merchants）**：存储商户基本信息
13. **行业信息表（industries）**：存储行业基本信息
14. **街道信息表（streets）**：存储街道基本信息
15. **低保户信息表（low_income_residents）**：存储低保户相关信息
16. **五保户信息表（five_guarantee_residents）**：存储五保户相关信息
17. **残疾人信息表（disabled_residents）**：存储残疾人相关信息
18. **特扶户信息表（special_support_residents）**：存储特扶户相关信息
19. **死亡户信息表（deceased_residents）**：存储死亡人员相关信息
20. **重点对象信息表（special_objects）**：存储重点关注对象相关信息
21. **管理员信息表（admins）**：存储系统管理员信息
22. **民族表（ethnicities）**：存储民族基本信息
23. **权限组表（roles）**：存储权限组信息

**表功能**：详见[数据库表设计](CMS_db_design.md)

## 五、技术栈选择

**前端技术栈**：详见[前端技术文档](CMS_frontend_technical.md)
**后端技术栈**：详见[后端技术文档](CMS_backend_technical.md)

### 5.1 后端技术

1. **核心语言**：Python 3.11
   - 提供强大的数据处理能力和丰富的第三方库支持
   - 支持异步编程，提升系统性能
   - 简洁的语法，提高开发效率

2. **Web框架**：Django 4.2+
   - 全功能Web框架，内置ORM、管理后台等丰富功能
   - MVC(MTV)架构模式，结构清晰
   - 内置Admin后台管理系统
   - 完善的文档和社区支持

3. **REST框架**：Django REST Framework 3.14+
   - 强大的RESTful API构建工具
   - 内置序列化器、视图集、路由等组件
   - 完善的权限控制和分页功能

4. **ORM框架**：Django ORM
   - 内置在Django框架中，与框架无缝集成
   - 强大的查询构建器和数据模型定义
   - 数据库迁移支持

5. **数据库**：
   - MySQL 8.0（统一使用）：高性能，适合生产环境，支持大数据量
   - 字符集：UTF-8
   - 排序规则：utf8mb4_unicode_ci

6. **身份验证**：
   - Django内置认证系统
   - Simple JWT：基于Token的身份验证机制，支持双Token（access token和refresh token）认证
   - 内置密码哈希和验证功能

7. **数据处理**：
   - Pandas 1.5+：强大的数据处理和分析库
   - NumPy 1.23+：科学计算基础库

8. **图表生成**：
   - Matplotlib 3.7+：基础图表生成库
   - Seaborn 0.12+：高级统计图表库

9. **Windows集成**：pywin32
   - 提供Windows API访问
   - 支持系统级功能集成

### 5.2 前端技术

1. **基础技术**：HTML5、CSS3、JavaScript (ES6+)
   - 构建跨平台的Web界面
   - 支持现代浏览器特性

2. **UI框架**：Bootstrap 5.2+
   - 响应式设计，适配不同屏幕尺寸
   - 丰富的UI组件库
   - 现代化的视觉设计

3. **数据可视化**：ECharts 5.4+
   - 强大的图表库，支持多种图表类型
   - 交互式数据展示
   - 性能优化，支持大数据量展示

4. **前端交互**：jQuery 3.6+
   - 简化DOM操作
   - 提供AJAX支持
   - 跨浏览器兼容性

## 六、模块划分

### 6.1 后端模块划分

系统采用Django的应用（App）结构进行模块化设计，每个应用负责特定的业务领域：

1. **authentication应用**
   - 用户认证与授权（基于Simple JWT）
   - 角色和权限管理
   - 用户信息维护

2. **residents应用**
   - 居民信息的CRUD操作
   - 居民信息查询和过滤
   - 特殊人群（低保户、五保户、残疾人、特扶户、死亡户、重点对象）管理
   - 居民信息统计分析

3. **businesses应用**
   - 商户信息的CRUD操作
   - 商户信息查询和过滤
   - 商户信息统计分析

4. **properties应用**
   - 物业信息的CRUD操作
   - 物业信息查询和过滤
   - 物业管理关系维护

5. **statistics应用**
   - 各类数据统计
   - 报表生成
   - 数据可视化支持

6. **community应用**
   - 小区信息管理
   - 小区基础数据维护

7. **groups应用**
   - 组别信息管理

8. **industry应用**
   - 行业信息管理

9. **street应用**
   - 街道信息管理

10. **units应用**
    - 单元信息管理

11. **houses应用**
    - 房屋信息管理

12. **alleys应用**
    - 胡同信息管理

13. **flats应用**
    - 平房信息管理

14. **house_numbers应用**
    - 门牌号信息管理

15. **ethnicities应用**
    - 民族信息管理

16. **utils应用**
    - 公共工具函数
    - Excel处理工具

### 6.2 前端模块划分

1. **登录模块**
   - 登录页面
   - 身份验证
   - 会话管理

2. **主页模块**
   - 数据概览
   - 快捷操作
   - 最新动态

3. **居民信息管理模块**
   - 居民信息列表
   - 居民信息详情
   - 居民信息编辑/新增表单

4. **商户信息管理模块**
   - 商户信息列表
   - 商户信息详情
   - 商户信息编辑/新增表单

5. **物业信息管理模块**
   - 物业信息列表
   - 物业信息详情
   - 物业信息编辑/新增表单

6. **统计分析模块**
   - 各类统计图表
   - 报表展示
   - 数据分析结果

7. **系统管理模块**
   - 用户管理界面
   - 系统配置界面
   - 数据备份恢复界面

## 七、组件交互流程

### 7.1 用户认证流程

1. 用户访问系统登录页面
2. 用户输入用户名和密码
3. 前端发送POST请求到后端Django Simple JWT的/token/认证API
4. 后端通过Django认证系统验证用户凭据
5. 后端生成JWT Token（access token和refresh token）
6. 后端返回双Token给前端
7. 前端存储Token（通常在localStorage中）
8. 后续请求携带access token进行身份验证
9. 当access token过期时，前端使用refresh token向/token/refresh/接口请求新的access token
10. 如果refresh token也过期，用户需要重新登录

### 7.2 数据查询流程

1. 用户在前端界面发起数据查询请求
2. 前端构造请求参数，携带JWT Token
3. 前端发送GET请求到后端API
4. 后端通过Django REST framework验证Token合法性
5. 后端视图集解析请求参数，调用Django ORM执行数据查询
6. 后端序列化器将查询结果转换为JSON格式
7. 后端返回查询结果给前端
8. 前端接收数据，渲染界面

### 7.3 数据提交流程

1. 用户在前端填写表单或编辑数据
2. 前端进行数据验证
3. 前端构造数据对象，携带JWT Token
4. 前端发送POST/PUT请求到后端API
5. 后端通过Django REST framework验证Token合法性
6. 后端序列化器解析请求数据，执行数据验证
7. 后端通过Django ORM执行数据存储或更新操作
8. 后端返回操作结果给前端
9. 前端根据返回结果显示成功或失败信息

## 八、数据流转机制

### 8.1 数据输入流程

1. 用户通过前端界面输入数据
2. 前端进行客户端验证
3. 前端将数据以JSON格式发送到后端
4. 后端Django REST framework视图接收数据
5. 后端序列化器进行服务端验证和数据转换
6. 后端通过Django ORM将数据持久化到数据库

### 8.2 数据查询流程

1. 前端发送查询请求到后端
2. 后端Django REST framework视图解析查询条件
3. 后端通过Django ORM查询集(QuerySet)从数据库查询数据
4. 后端序列化器将查询结果序列化为JSON格式
5. 后端返回JSON数据给前端
6. 前端解析JSON数据，渲染到界面

### 8.3 数据更新流程

1. 用户在前端界面发起数据更新请求
2. 前端进行数据校验和预处理
3. 前端通过封装的API请求函数（apiPost/apiPut/apiPatch等）发送请求到后端Django REST Framework API
4. 后端验证用户JWT Token权限和数据有效性
5. 后端Django ORM执行数据更新操作到MySQL数据库
6. 后端返回操作结果（包括状态码、消息和数据）给前端
7. 前端根据返回结果更新界面显示，并处理可能的错误情况
8. 如遇Token过期，前端自动使用refresh token刷新access token并重试请求

## 九、关键技术实现细节

### 9.1 数据库设计与优化

1. **索引优化**：
   - 对常用查询字段创建索引
   - 合理设计复合索引
   - 利用Django的索引工具进行管理

2. **查询优化**：
   - 使用Django ORM的select_related和prefetch_related避免N+1查询问题
   - 优化QuerySet查询，使用values()和only()减少数据传输
   - 利用Django的查询优化工具分析和改进查询性能

3. **事务管理**：
   - 使用Django的atomic装饰器和上下文管理器处理事务
   - 合理设置事务隔离级别
   - 关键业务操作使用事务保证数据一致性

### 9.2 安全机制

1. **认证与授权**：
   - 用户认证：基于Django内置认证系统和Simple JWT，支持双Token（access token和refresh token）认证机制
   - 基于角色的权限控制（RBAC）：结合Django内置权限系统和自定义权限模型
   - 视图级权限控制：基于Django REST Framework权限类实现
   - 对象级权限控制：实现精细化的数据访问控制
   - JWT Token管理：Token有效期管理、自动刷新机制和安全存储

2. **数据安全**：
   - 密码加密存储：使用Django内置的密码哈希机制
   - 敏感数据加密传输：全站HTTPS加密，确保数据传输安全
   - SQL注入防护：通过Django ORM和参数化查询自动防护
   - XSS攻击防护：集成Django安全中间件，前端进行输入验证和输出编码
   - CSRF攻击防护：使用Django内置的CSRF Token机制，前端请求自动携带
   - 数据备份与恢复策略：定期数据库备份，支持全量和增量备份
   - 敏感数据存储：关键信息加密存储，限制敏感数据访问权限

3. **操作审计**：
   - 用户操作日志记录：集成Django admin日志系统，记录关键操作
   - 系统关键操作审计：敏感操作双重确认和日志记录
   - 异常行为监控：实时监控登录失败、异常访问等行为
   - 安全告警机制：针对可疑行为自动触发告警

4. **会话安全**：
   - HTTP-only Cookie：防止客户端脚本访问Cookie
   - SameSite Cookie：限制Cookie跨站发送
   - 会话超时设置：自动登出长时间不活跃用户
   - 防止会话固定攻击：登录成功后重新生成会话ID

5. **请求安全**：
   - 请求频率限制
   - 异常请求检测

### 9.3 错误处理

1. **全局异常处理**：
   - 实现自定义异常类
   - 全局异常捕获与处理
   - 统一错误响应格式（包含错误码、错误消息和详细信息）

2. **API错误处理**：
   - 基于HTTP状态码的错误分类（400参数错误、401未认证、403无权限、404资源不存在、500服务器错误等）
   - 详细的错误信息返回
   - 异常日志记录（包含请求参数、用户信息和错误堆栈）

3. **前端错误处理**：
   - API请求封装中的统一错误处理
   - Token过期自动刷新和请求重试机制
   - 表单验证错误展示
   - 用户友好的错误提示
   - 错误码与错误消息映射

### 9.4 前端数据请求与展示

1. **API请求封装**：
   - 独立函数封装（apiGet、apiPost、apiPut、apiPatch、apiDelete、apiUpload）
   - 请求拦截器（统一添加JWT Token认证信息）
   - 响应拦截器（统一处理响应结果和错误）
   - Token过期自动刷新和请求重试队列
   - 错误处理机制（区分400参数错误、401认证错误、403权限错误等）

2. **数据展示组件**：
   - 表格展示组件（支持排序、筛选、分页）
   - 表单组件（支持验证、自动填充）
   - 详情展示组件
   - 模态框组件

3. **数据可视化**：
   - 基于ECharts 5.4+的图表展示
   - 动态数据更新
   - 交互式图表
   - 响应式图表设计

### 9.5 跨平台兼容性

1. **浏览器兼容性**：
   - 支持主流浏览器（Chrome、Firefox、Safari、Edge）
   - 兼容IE 11及以上版本

2. **操作系统兼容性**：
   - 支持Windows 7、Windows 10、Windows 11
   - 支持Linux、macOS等主流操作系统

## 十、部署与打包

### 10.1 开发环境部署

1. 安装Python 3.11和MySQL 8.0
2. 创建虚拟环境：`python -m venv venv`
3. 激活虚拟环境：`venv\Scripts\activate`（Windows）或 `source venv/bin/activate`（Linux/Mac）
4. 安装项目依赖：`pip install -r requirements.txt`
5. 配置`.env`文件，设置数据库连接参数和其他环境变量
6. 运行数据库迁移：`python manage.py migrate`
7. 创建超级用户：`python manage.py createsuperuser`
8. 启动Django开发服务器：`python manage.py runserver`
9. 前端资源直接通过Django静态文件服务访问

### 10.2 生产环境部署

1. 安装Python 3.11和MySQL 8.0
2. 创建虚拟环境：`python -m venv venv`
3. 激活虚拟环境：`venv\Scripts\activate`（Windows）或 `source venv/bin/activate`（Linux/Mac）
4. 安装项目依赖：`pip install -r requirements.txt`
5. 配置`.env`文件，设置数据库连接参数和其他环境变量
6. 运行数据库迁移：`python manage.py migrate`
7. 收集静态文件：`python manage.py collectstatic`
8. 配置Web服务器（Nginx）作为反向代理
9. 配置WSGI服务器（Gunicorn或uWSGI）运行Django应用
10. 设置环境变量和配置文件
11. 启动Nginx和WSGI服务

### 10.3 容器化部署（Docker）

1. 确保安装了Docker和Docker Compose
2. 创建`Dockerfile`和`docker-compose.yml`文件
3. 配置服务、网络和卷
4. 构建和启动容器：`docker-compose up -d`

### 10.4 Nginx配置示例

```nginx
server {
    listen 80;
    server_name example.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name example.com;
    
    ssl_certificate /path/to/ssl/cert.pem;
    ssl_certificate_key /path/to/ssl/key.pem;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    location /static/ {
        alias /path/to/static/;
        expires 30d;
    }
    
    location /media/ {
        alias /path/to/media/;
    }
}
```

## 十一、项目结构

```
community_management/
├── community_management/         # 项目主目录
│   ├── __init__.py               # 项目初始化
│   ├── settings.py               # 项目设置
│   ├── urls.py                   # 主URL配置
│   ├── wsgi.py                   # WSGI配置
│   └── asgi.py                   # ASGI配置
├── residents/                    # 居民管理应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 居民模型
│   ├── serializers.py            # DRF序列化器
│   ├── views.py                  # Django视图
│   ├── viewsets.py               # DRF视图集
│   ├── urls.py                   # 应用URL配置
│   ├── services/                 # 业务服务
│   │   └── __init__.py
│   └── utils/                    # 工具函数
│       └── __init__.py
├── businesses/                   # 商户管理应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 商户模型
│   ├── serializers.py            # DRF序列化器
│   ├── views.py                  # Django视图
│   ├── viewsets.py               # DRF视图集
│   ├── urls.py                   # 应用URL配置
│   ├── services/                 # 业务服务
│   │   └── __init__.py
│   └── utils/                    # 工具函数
│       └── __init__.py
├── authentication/               # 认证应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 认证相关模型
│   ├── serializers.py            # DRF序列化器
│   ├── views.py                  # Django视图
│   ├── viewsets.py               # DRF视图集
│   ├── urls.py                   # 应用URL配置
│   ├── services/                 # 认证服务
│   │   └── __init__.py
│   └── utils/                    # 认证工具
│       └── __init__.py
├── properties/                   # 物业管理应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 物业模型
│   ├── serializers.py            # DRF序列化器
│   ├── views.py                  # Django视图
│   ├── viewsets.py               # DRF视图集
│   ├── urls.py                   # 应用URL配置
├── statistics/                   # 统计应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 统计相关模型
│   ├── serializers.py            # DRF序列化器
│   ├── views.py                  # Django视图
│   ├── viewsets.py               # DRF视图集
│   ├── urls.py                   # 应用URL配置
├── community/                    # 小区管理应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 小区模型
├── groups/                       # 组别管理应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 组别模型
├── industry/                     # 行业管理应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 行业模型
├── street/                       # 街道管理应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 街道模型
├── units/                        # 单元管理应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 单元模型
├── houses/                       # 房屋管理应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 房屋模型
├── alleys/                       # 胡同管理应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 胡同模型
├── flats/                        # 平房管理应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 平房模型
├── house_numbers/                # 门牌号管理应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 门牌号模型
├── ethnicities/                  # 民族管理应用
│   ├── __init__.py
│   ├── admin.py                  # Django管理后台
│   ├── apps.py                   # 应用配置
│   ├── models.py                 # 民族模型
├── utils/                        # 工具应用
│   ├── __init__.py
│   ├── excel_helper.py           # Excel处理工具
│   └── common.py                 # 通用工具函数
├── static/                       # 静态资源
├── media/                        # 媒体文件
├── templates/                    # HTML模板
├── db.sqlite3                    # SQLite数据库（开发环境）
├── manage.py                     # Django管理脚本
├── requirements.txt              # 项目依赖
└── .env                          # 环境变量配置

# 前端目录结构
static/
├── css/                # 样式文件
│   ├── common.css      # 通用样式
│   ├── login.css       # 登录页面样式
│   ├── dashboard.css   # 主页样式
│   └── ...             # 其他模块样式
├── js/                 # JavaScript文件
│   ├── common.js       # 通用工具函数
│   ├── api.js          # API请求封装
│   ├── auth.js         # 认证相关功能
│   ├── charts.js       # 图表绘制功能
│   └── modules/        # 各功能模块脚本
│       ├── login.js    # 登录模块
│       ├── dashboard.js # 主页模块
│       ├── residents.js # 居民管理模块
│       ├── businesses.js # 商户管理模块
│       ├── properties.js # 物业信息模块
│       └── ...         # 其他模块
├── img/                # 图片资源
└── libs/               # 第三方库
    ├── bootstrap/      # Bootstrap框架
    ├── jquery/         # jQuery库
    └── echarts/        # ECharts库
```
