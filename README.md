# 社区信息管理系统

## 项目简介

社区信息管理系统是一款基于Python 3.11开发的综合性管理平台，旨在帮助社区管理人员高效管理居民、商户及物业信息，并提供全面的统计分析功能，以优化社区服务质量。

## 系统架构

系统采用经典的三层架构设计，结合前后端分离模式：

1. **表示层（前端）**：提供用户界面，负责数据展示和用户交互
   - 基于HTML5/CSS3/JavaScript构建Web界面
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

## 功能模块设计

### 1. 登录模块
- 用户身份验证与登录
- 权限验证
- 会话管理

### 2. 主页信息统计展示功能
- 展示社区各类统计数据（人口总数、商户总数等）
- 时间维度统计：
  - 新增人口数（年/月/日）
  - 新增商户数（年/月/日）
  - 新增死亡人口数及死亡人口总数（年/月/日）
  - 新增残疾人数及残疾人总数（年/月/日）
  - 新增特扶人口数及特扶人口总数（年/月/日）
  - 新增低保户数及低保户总数（年/月/日）
  - 新增五保户数及五保户总数（年/月/日）
- 图表可视化展示（柱状图、折线图等）

### 3. 居民信息管理模块
#### 3.3.1 居民信息录入功能
- 录入新居民的详细信息
- 数据验证和存储

#### 3.3.2 居民信息变更功能
- 修改已存在居民的信息
- 数据查询、验证和更新

#### 3.3.3 居民信息查询功能
- 根据条件查询居民信息
- 支持条件筛选和分页

#### 3.3.4 居民信息删除功能
- 删除已存在居民的信息
- 确认机制和安全保障

### 4. 商户信息管理模块
#### 4.4.1 商户信息录入功能
- 录入新商户的详细信息
- 数据验证和存储

#### 4.4.2 商户信息变更功能
- 修改已存在商户的信息
- 数据查询、验证和更新

#### 4.4.3 商户信息查询功能
- 根据条件查询商户信息
- 支持条件筛选和分页

#### 4.4.4 商户信息删除功能
- 删除已存在商户的信息
- 确认机制和安全保障

### 5. 物业信息管理模块
#### 5.5.1 物业信息录入功能
- 录入新物业的详细信息
- 数据验证和存储

#### 5.5.2 物业信息变更功能
- 修改已存在物业的信息
- 数据查询、验证和更新

#### 5.5.3 物业信息查询功能
- 根据条件查询物业信息
- 支持条件筛选和分页

#### 5.5.4 物业信息删除功能
- 删除已存在物业的信息
- 确认机制和安全保障

### 6. 统计分析模块
- 各类数据统计、报表生成
- 数据可视化支持

### 7. 系统管理模块
- 用户管理、角色权限管理
- 系统配置、数据备份恢复

### 8. 基础数据维护模块
- 小区、单元、户、组别、户号、街道、行业等基础数据的管理

详见`CMS_design.md`

## 数据库设计

系统数据库采用MySQL 8.0，遵循关系型数据库设计原则，确保数据的完整性、一致性和可扩展性。主要表结构包括：
- **居民信息表（residents）**：存储居民基本信息，包括姓名、身份证号、联系方式等
- **楼房信息表（buildings）**：存储楼房基本信息
- **小区信息表（communities）**：存储小区基本信息
- **单元信息表（units）**：存储单元基本信息
- **房屋信息表（houses）**：存储房屋基本信息
- **平房信息表（flats）**：存储平房基本信息
- **胡同信息表（alleys）**：存储胡同基本信息
- **门牌号信息表（house_numbers）**：存储门牌号基本信息
- **组别信息表（groups）**：存储组别基本信息
- **物业信息表（properties）**：存储物业基本信息
- **物业管理表（property_managers）**：存储物业与小区的管理关系
- **商户信息表（merchants）**：存储商户基本信息
- **行业信息表（industries）**：存储行业基本信息
- **街道信息表（streets）**：存储街道基本信息
- **低保户信息表（low_income_residents）**：存储低保户相关信息
- **五保户信息表（five_guarantee_residents）**：存储五保户相关信息
- **残疾人信息表（disabled_residents）**：存储残疾人相关信息
- **特扶户信息表（special_support_residents）**：存储特扶户相关信息
- **死亡户信息表（deceased_residents）**：存储死亡人员相关信息
- **重点对象信息表（special_objects）**：存储重点关注对象相关信息
- **管理员信息表（admins）**：存储系统管理员信息
- **民族表（ethnicities）**：存储民族基本信息
- **权限组表（roles）**：存储权限组信息

表间关系：
- **居民信息表** 与 **民族表**：多对一关系
- **居民信息表** 与 **房屋信息表/平房信息表**：多对一关系
- **房屋信息表** 与 **单元信息表**：多对一关系
- **单元信息表** 与 **楼房信息表**：多对一关系
- **楼房信息表** 与 **小区信息表**：多对一关系
- **小区信息表** 与 **组别信息表**：多对一关系
- **平房信息表** 与 **胡同信息表**：多对一关系
- **胡同信息表** 与 **组别信息表**：多对一关系
- **商户信息表** 与 **街道信息表**：多对一关系
- **商户信息表** 与 **行业信息表**：多对一关系
- **物业管理表** 与 **物业信息表**：多对一关系
- **物业管理表** 与 **小区信息表**：多对一关系
- **管理员信息表** 与 **权限组表**：多对一关系

详见`CMS_db_design.md`

## 技术栈选择

### 后端技术
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

5. **数据库**：MySQL 8.0（统一使用，包括开发和生产环境）
   - 高性能，适合生产环境，支持大数据量
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

### 前端技术
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

### 开发与部署工具
1. **版本控制**：Git
2. **代码编辑器/IDE**：PyCharm、Visual Studio Code

详见`CMS_technical.md`、`CMS_frontend_technical.md`和`CMS_backend_technical.md`

## 项目结构

```
community_management/
├── community_management/  # 项目配置目录
│   ├── __init__.py        # 项目初始化
│   ├── settings.py        # 项目设置
│   ├── urls.py            # 主URL配置
│   ├── wsgi.py            # WSGI配置
│   └── asgi.py            # ASGI配置
├── residents/             # 居民管理应用
│   ├── __init__.py
│   ├── admin.py           # Django管理后台
│   ├── apps.py            # 应用配置
│   ├── models.py          # 居民模型
│   ├── serializers.py     # DRF序列化器
│   ├── views.py           # Django视图
│   ├── viewsets.py        # DRF视图集
│   ├── urls.py            # 应用URL配置
│   ├── services/          # 业务服务
│   │   └── __init__.py
│   └── utils/             # 工具函数
│       └── __init__.py
├── businesses/            # 商户管理应用
│   ├── __init__.py
│   ├── admin.py           # Django管理后台
│   ├── apps.py            # 应用配置
│   ├── models.py          # 商户模型
│   ├── serializers.py     # DRF序列化器
│   ├── views.py           # Django视图
│   ├── viewsets.py        # DRF视图集
│   ├── urls.py            # 应用URL配置
│   ├── services/          # 业务服务
│   │   └── __init__.py
│   └── utils/             # 工具函数
│       └── __init__.py
├── authentication/        # 认证应用
│   ├── __init__.py
│   ├── admin.py           # Django管理后台
│   ├── apps.py            # 应用配置
│   ├── models.py          # 认证相关模型
│   ├── serializers.py     # DRF序列化器
│   ├── views.py           # Django视图
│   ├── viewsets.py        # DRF视图集
│   ├── urls.py            # 应用URL配置
│   ├── services/          # 认证服务
│   │   └── __init__.py
│   └── utils/             # 认证工具
│       └── __init__.py
├── statistics/            # 统计应用
│   ├── __init__.py
│   ├── admin.py           # Django管理后台
│   ├── apps.py            # 应用配置
│   ├── models.py          # 统计相关模型
│   ├── serializers.py     # DRF序列化器
│   ├── views.py           # Django视图
│   ├── viewsets.py        # DRF视图集
│   ├── urls.py            # 应用URL配置
│   ├── services/          # 统计服务
│   │   └── __init__.py
│   └── utils/             # 统计工具
│       └── __init__.py
├── utils/                 # 通用工具
│   ├── __init__.py
│   ├── excel_helper.py    # Excel处理工具
│   └── common.py          # 通用工具函数
├── static/                # 静态资源
│   ├── css/               # 样式文件
│   ├── js/                # JavaScript文件
│   ├── img/               # 图片资源
│   └── libs/              # 第三方库
├── templates/             # HTML模板
├── media/                 # 媒体文件
├── manage.py              # Django管理脚本
├── requirements.txt       # 项目依赖
└── .env                   # 环境变量配置
```

## 安装与配置

### 开发环境配置

1. **安装Python 3.11**
   - 从[Python官网](https://www.python.org/downloads/)下载并安装Python 3.11
   - 确保将Python添加到系统环境变量

2. **安装MySQL 8.0**
   - 从[MySQL官网](https://dev.mysql.com/downloads/mysql/)下载并安装MySQL 8.0
   - 创建数据库和用户，设置适当的权限

3. **创建虚拟环境**
   ```bash
   python -m venv .venv
   ```

4. **激活虚拟环境**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

5. **安装项目依赖**
   ```bash
   pip install -r requirements.txt
   ```

6. **配置环境变量**
   创建`.env`文件，添加以下配置：
   ```
   SECRET_KEY=your-secret-key
   DB_NAME=community_management
   DB_USER=root
   DB_PASSWORD=password
   DB_HOST=localhost
   DB_PORT=3306
   DEBUG=True
   ```

7. **运行数据库迁移**
   ```bash
   python manage.py migrate
   ```

8. **创建超级用户（可选）**
   ```bash
   python manage.py createsuperuser
   ```

9. **运行开发服务器**
   ```bash
   python manage.py runserver
   ```

10. **访问系统**
    打开浏览器，访问：`http://localhost:8000`

### 生产环境配置

1. **配置MySQL数据库**
   - 安装MySQL 8.0
   - 创建数据库和用户
   - 授予必要的权限

2. **配置环境变量**
   创建`.env`文件，添加以下配置：
   ```
   SECRET_KEY=your-secret-key
   DB_NAME=community_management
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   DB_PORT=3306
   DEBUG=False
   ALLOWED_HOSTS=your-domain.com,www.your-domain.com
   ```

3. **运行数据库迁移**
   ```bash
   python manage.py migrate
   ```

4. **收集静态文件**
   ```bash
   python manage.py collectstatic
   ```

5. **使用Gunicorn作为WSGI服务器**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 "community_management.wsgi:application"
   ```

6. **配置Nginx作为反向代理**
   设置Nginx配置文件，将请求转发到Gunicorn

7. **配置HTTPS**
   使用SSL证书配置HTTPS访问

8. **配置系统服务**
   将Gunicorn配置为系统服务，确保系统重启后自动启动

### 容器化部署（可选）

项目支持Docker容器化部署，详细步骤请参考相关容器化部署文档。

## 登录信息

默认管理员账号：
- 用户名：admin
- 密码：password

**注意**：首次登录后，请及时修改管理员密码。

## 功能特点

1. **全面的信息管理**：支持居民、商户、物业等各类信息的录入、查询、更新和删除
2. **强大的统计分析**：提供多维度的数据统计和可视化图表展示
3. **安全可靠**：采用Django Simple JWT双Token认证机制、密码加密存储等多重安全机制
4. **用户友好**：界面简洁直观，操作便捷
5. **响应式设计**：基于Bootstrap 5.2+实现响应式布局，适配不同屏幕尺寸的设备
6. **数据导入导出**：支持批量数据导入导出，提高工作效率
7. **系统管理**：支持用户管理、角色权限管理、系统配置、数据备份恢复等功能
8. **前后端分离**：采用Django REST Framework构建RESTful API，实现前后端完全分离
9. **统一数据库**：采用MySQL 8.0作为统一数据库，保证数据一致性和可扩展性
10. **高级查询**：支持复杂条件查询、分页和排序功能

## 系统要求

### 硬件要求
- 处理器：Intel Core i3及以上
- 内存：4GB及以上
- 硬盘空间：10GB及以上可用空间

### 软件要求
- **操作系统**：Windows 7/10/11、Linux、macOS
- **开发环境**：Python 3.11、MySQL 8.0
- **浏览器支持**：
  - Google Chrome（最新两个稳定版本）
  - Mozilla Firefox（最新两个稳定版本）
  - Apple Safari（最新两个稳定版本）
  - Microsoft Edge（最新两个稳定版本）
- **数据库**：MySQL 8.0（字符集：UTF-8，排序规则：utf8mb4_unicode_ci）

## 联系方式

如有问题或建议，请联系项目负责人：

- 邮箱：[example@email.com]
- 电话：[联系方式]
