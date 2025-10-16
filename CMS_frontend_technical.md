# 社区信息管理系统前端技术文档

## 一、前端系统概述

本系统前端部分负责提供用户界面，实现数据展示和用户交互，是社区信息管理系统的重要组成部分。前端采用现代化Web技术栈构建，确保界面美观、交互友好、响应迅速，并支持跨浏览器兼容。前端通过HTTP/HTTPS协议与后端Django REST Framework提供的RESTful API进行通信，实现前后端分离的系统架构。

## 二、前端技术栈

### 2.1 基础技术
- **HTML5**：构建页面结构和语义化内容
- **CSS3**：实现页面样式和视觉效果
- **JavaScript (ES6+)**：实现页面交互和数据处理

### 2.2 UI框架
- **Bootstrap 5.2+**：提供响应式布局和丰富的UI组件
  - 响应式设计，适配不同屏幕尺寸
  - 丰富的UI组件库
  - 现代化的视觉设计

### 2.3 数据可视化
- **ECharts 5.4+**：强大的图表库，支持多种图表类型
  - 支持柱状图、折线图、饼图、雷达图等多种图表类型
  - 交互式数据展示
  - 性能优化，支持大数据量展示

### 2.4 前端交互
- **jQuery 3.6+**：简化DOM操作和AJAX请求
  - 简化DOM操作
  - 提供AJAX支持
  - 跨浏览器兼容性

## 三、前端架构设计

### 3.1 整体架构

前端采用经典的三层架构设计，结合组件化开发模式：

1. **展示层**：HTML模板和CSS样式，负责页面渲染
2. **控制层**：JavaScript脚本，处理用户交互和业务逻辑
3. **数据层**：AJAX请求和数据处理，与后端API通信

### 3.2 目录结构

```
app/static/
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
│       └── ...         # 其他模块
├── img/                # 图片资源
└── libs/               # 第三方库
    ├── bootstrap/      # Bootstrap框架
    ├── jquery/         # jQuery库
    └── echarts/        # ECharts库
templates/
├── login.html          # 登录页面模板
├── dashboard.html      # 主页模板
├── residents/
│   ├── list.html       # 居民列表页面
│   ├── add.html        # 添加居民页面
│   └── edit.html       # 编辑居民页面
├── businesses/
│   ├── list.html       # 商户列表页面
│   ├── add.html        # 添加商户页面
│   └── edit.html       # 编辑商户页面
└── ...                 # 其他页面模板
```

## 四、前端模块详细设计

### 4.1 登录模块

#### 4.1.1 功能描述
实现系统用户的身份验证与登录，是用户访问系统的入口。与后端Django Simple JWT认证机制紧密集成，实现安全的用户认证流程。

#### 4.1.2 页面设计
- 登录表单：包含用户名和密码输入框
- 登录按钮：提交登录信息
- 错误提示：显示登录失败原因

#### 4.1.3 交互流程
1. 用户访问登录页面
2. 用户输入用户名和密码
3. 前端进行基本验证（非空检查）
4. 前端发送POST请求到后端Django Simple JWT的/token/接口
5. 后端验证用户凭据，返回JWT Token（access token和refresh token）
6. 认证成功后，前端存储Token并跳转到主页
7. 认证失败则显示错误信息

#### 4.1.4 核心代码结构
```javascript
// 登录表单提交处理 - 与后端Django Simple JWT认证机制保持一致
$("#login-form").submit(function(e) {
    e.preventDefault();
    const username = $("#username").val();
    const password = $("#password").val();
    
    // 基本验证
    if (!username || !password) {
        showError("用户名和密码不能为空");
        return;
    }
    
    // 发送登录请求 - 与后端Django Simple JWT的/token/接口对应
    apiPost('/token/', {username, password})
        .then(function(response) {
            // 存储access token和refresh token
            setTokens(response.access, response.refresh);
            // 跳转到主页
            window.location.href = '/dashboard';
        })
        .catch(function(xhr) {
            const errorMsg = xhr.responseJSON?.detail || '登录失败，请检查用户名和密码';
            showError(errorMsg);
        });
});

// 检查用户是否已登录 - 与后端Django Simple JWT认证机制保持一致
function checkLoginStatus() {
    const accessToken = getAccessToken();
    
    // 如果没有Token，跳转到登录页面
    if (!accessToken) {
        window.location.href = '/login';
        return;
    }
    
    // 检查Token是否过期
    if (isTokenExpired(accessToken)) {
        // 尝试刷新Token
        refreshAccessToken().catch(() => {
            // 刷新失败，跳转到登录页面
            window.location.href = '/login';
        });
    }
}

// 登出功能
function logout() {
    // 清除Token
    removeTokens();
    
    // 跳转到登录页面
    window.location.href = '/login';
}
```

### 4.2 主页模块

#### 4.2.1 功能描述
展示社区各类统计数据，提供数据概览和快捷操作入口。

#### 4.2.2 页面设计
- 数据概览区：显示人口总数、商户总数等关键指标
- 图表展示区：使用ECharts展示各类统计图表
  - 新增人口趋势图（柱状图/折线图）
  - 人口结构分布图（饼图）
  - 商户行业分布图（饼图）
- 快捷操作区：提供常用功能的快速访问入口
- 最新动态区：显示系统最新消息或数据更新记录

#### 4.2.3 交互流程
1. 用户登录成功后进入主页
2. 前端向后端请求各类统计数据
3. 后端返回数据后，前端更新页面数据和图表
4. 用户可以点击快捷操作按钮进入相应功能模块

#### 4.2.4 核心代码结构
```javascript
// 初始化主页数据
function initDashboard() {
    // 请求统计数据
    $.ajax({
        url: '/api/statistics/overview',
        type: 'GET',
        headers: { 'Authorization': 'Bearer ' + getToken() },
        success: function(data) {
            // 更新数据概览
            updateOverviewData(data);
            // 渲染各类图表
            renderPopulationTrendChart(data.population_trend);
            renderPopulationStructureChart(data.population_structure);
            renderBusinessIndustryChart(data.business_industry);
        }
    });
}

// 渲染人口趋势图
function renderPopulationTrendChart(data) {
    const chartDom = document.getElementById('population-trend-chart');
    const myChart = echarts.init(chartDom);
    
    const option = {
        title: { text: '人口趋势统计' },
        tooltip: { trigger: 'axis' },
        xAxis: { type: 'category', data: data.xAxis },
        yAxis: { type: 'value' },
        series: [
            {
                name: '新增人口',
                type: 'bar',
                data: data.new_population
            },
            {
                name: '总人口',
                type: 'line',
                data: data.total_population
            }
        ]
    };
    
    myChart.setOption(option);
    
    // 响应式调整
    window.addEventListener('resize', function() {
        myChart.resize();
    });
}
```

### 4.3 居民信息管理模块

#### 4.3.1 功能描述
居民信息管理模块允许管理员查看、添加、编辑和删除居民信息，支持按姓名、身份证号、地址等条件进行筛选和搜索。与后端Django REST Framework的Resident模型保持一致，支持特殊人群（低保户、五保户、残疾人、特扶户、死亡户、重点对象）的标记和管理。

#### 4.3.2 页面设计
- **居民列表页**：显示所有居民信息，支持分页、筛选和搜索，与后端/api/residents接口交互
- **居民详情页**：显示居民详细信息，包括基本信息、家庭信息、特殊人群标记等，与后端/api/residents/{id}接口交互
- **添加/编辑居民页**：表单页面，用于添加或编辑居民信息，字段与后端Resident模型保持一致

#### 4.3.3 交互流程
1. 用户进入居民信息列表页
2. 系统加载居民数据并显示在表格中，与后端/api/residents接口交互
3. 用户可以使用筛选条件和搜索框查找特定居民，支持多条件组合查询和特殊人群筛选
4. 用户点击查看按钮查看居民详情，与后端/api/residents/{id}接口交互
5. 用户点击添加按钮进入添加居民页面
6. 用户填写居民信息并提交，与后端/api/residents接口交互
7. 系统保存居民信息并返回居民列表页
8. 用户点击编辑按钮进入编辑居民页面
9. 用户修改居民信息并提交，与后端/api/residents/{id}接口交互
10. 系统更新居民信息并返回居民列表页
11. 用户点击删除按钮删除居民信息
12. 系统提示确认删除，确认后与后端/api/residents/{id}接口交互删除居民信息并更新列表

#### 4.3.4 核心代码结构

```javascript
// 居民列表页代码 - 与后端Resident模型保持一致
function loadResidentList() {
    // 获取筛选条件
    const filters = getFilters();
    
    // 发送API请求获取居民列表 - 与后端/api/residents接口对应
    apiGet('/residents', filters)
        .then(data => {
            // 渲染居民列表
            renderResidentList(data);
        })
        .catch(error => {
            console.error('Failed to load resident list:', error);
            showErrorMessage('加载居民列表失败');
        });
}

// 添加居民 - 与后端Resident模型保持一致
function addResident(residentData) {
    apiPost('/residents', residentData)
        .then(() => {
            showSuccessMessage('添加居民成功');
            // 返回居民列表页
            window.location.href = '/residents';
        })
        .catch(error => {
            console.error('Failed to add resident:', error);
            showErrorMessage('添加居民失败');
        });
}

// 编辑居民 - 与后端Resident模型保持一致
function updateResident(id, residentData) {
    apiPut(`/residents/${id}`, residentData)
        .then(() => {
            showSuccessMessage('更新居民成功');
            // 返回居民列表页
            window.location.href = '/residents';
        })
        .catch(error => {
            console.error('Failed to update resident:', error);
            showErrorMessage('更新居民失败');
        });
}

// 删除居民 - 与后端Resident模型保持一致
function deleteResident(id) {
    if (confirm('确定要删除这个居民吗？')) {
        apiDelete(`/residents/${id}`)
            .then(() => {
                showSuccessMessage('删除居民成功');
                // 重新加载居民列表
                loadResidentList();
            })
            .catch(error => {
                console.error('Failed to delete resident:', error);
                showErrorMessage('删除居民失败');
            });
    }
}
```

### 4.4 商户信息管理模块

#### 4.4.1 功能描述
商户信息管理模块允许管理员查看、添加、编辑和删除商户信息，支持按商户名称、行业类型、注册日期等条件进行筛选和搜索。与后端Django REST Framework的Business模型保持一致。

#### 4.4.2 页面设计
- **商户列表页**：显示所有商户信息，支持分页、筛选和搜索
- **商户详情页**：显示商户详细信息，包括基本信息、联系人信息、经营信息等
- **添加/编辑商户页**：表单页面，用于添加或编辑商户信息，字段与后端Business模型保持一致

#### 4.4.3 交互流程
1. 用户进入商户信息列表页
2. 系统加载商户数据并显示在表格中，与后端/api/businesses接口交互
3. 用户可以使用筛选条件和搜索框查找特定商户，支持多条件组合查询
4. 用户点击查看按钮查看商户详情，与后端/api/businesses/{id}接口交互
5. 用户点击添加按钮进入添加商户页面
6. 用户填写商户信息并提交，与后端/api/businesses接口交互
7. 系统保存商户信息并返回商户列表页
8. 用户点击编辑按钮进入编辑商户页面
9. 用户修改商户信息并提交，与后端/api/businesses/{id}接口交互
10. 系统更新商户信息并返回商户列表页
11. 用户点击删除按钮删除商户信息
12. 系统提示确认删除，确认后与后端/api/businesses/{id}接口交互删除商户信息并更新列表

#### 4.4.4 核心代码结构

```javascript
// 商户列表页代码 - 与后端Business模型保持一致
function loadBusinessList() {
    // 获取筛选条件
    const filters = getFilters();
    
    // 发送API请求获取商户列表 - 与后端/api/businesses接口对应
    apiGet('/businesses', filters)
        .then(data => {
            // 渲染商户列表
            renderBusinessList(data);
        })
        .catch(error => {
            console.error('Failed to load business list:', error);
            showErrorMessage('加载商户列表失败');
        });
}

// 添加商户 - 与后端Business模型保持一致
function addBusiness(businessData) {
    apiPost('/businesses', businessData)
        .then(() => {
            showSuccessMessage('添加商户成功');
            // 返回商户列表页
            window.location.href = '/businesses';
        })
        .catch(error => {
            console.error('Failed to add business:', error);
            showErrorMessage('添加商户失败');
        });
}

// 编辑商户 - 与后端Business模型保持一致
function updateBusiness(id, businessData) {
    apiPut(`/businesses/${id}`, businessData)
        .then(() => {
            showSuccessMessage('更新商户成功');
            // 返回商户列表页
            window.location.href = '/businesses';
        })
        .catch(error => {
            console.error('Failed to update business:', error);
            showErrorMessage('更新商户失败');
        });
}

// 删除商户 - 与后端Business模型保持一致
function deleteBusiness(id) {
    if (confirm('确定要删除这个商户吗？')) {
        apiDelete(`/businesses/${id}`)
            .then(() => {
                showSuccessMessage('删除商户成功');
                // 重新加载商户列表
                loadBusinessList();
            })
            .catch(error => {
                console.error('Failed to delete business:', error);
                showErrorMessage('删除商户失败');
            });
    }
}
```

### 4.5 物业信息管理模块

#### 4.5.1 功能描述
物业信息管理模块允许管理员查看、添加、编辑和删除物业信息，支持按物业名称、地址、负责人等条件进行筛选和搜索。与后端Django REST Framework的Property和PropertyManager模型保持一致。

#### 4.5.2 页面设计
- **物业列表页**：显示所有物业信息，支持分页、筛选和搜索，与后端/api/properties接口交互
- **物业详情页**：显示物业详细信息，包括基本信息、管理人员信息、联系方式等，与后端/api/properties/{id}接口交互
- **添加/编辑物业页**：表单页面，用于添加或编辑物业信息，字段与后端Property模型保持一致
- **物业管理员管理**：允许管理物业管理员信息，与后端PropertyManager模型保持一致

#### 4.5.3 交互流程
1. 用户进入物业信息列表页
2. 系统加载物业数据并显示在表格中，与后端/api/properties接口交互
3. 用户可以使用筛选条件和搜索框查找特定物业，支持多条件组合查询
4. 用户点击查看按钮查看物业详情，与后端/api/properties/{id}接口交互
5. 用户点击添加按钮进入添加物业页面
6. 用户填写物业信息并提交，与后端/api/properties接口交互
7. 系统保存物业信息并返回物业列表页
8. 用户点击编辑按钮进入编辑物业页面
9. 用户修改物业信息并提交，与后端/api/properties/{id}接口交互
10. 系统更新物业信息并返回物业列表页
11. 用户点击删除按钮删除物业信息
12. 系统提示确认删除，确认后与后端/api/properties/{id}接口交互删除物业信息并更新列表

#### 4.5.4 核心代码结构

```javascript
// 物业列表页代码 - 与后端Property模型保持一致
function loadPropertyList() {
    // 获取筛选条件
    const filters = getFilters();
    
    // 发送API请求获取物业列表 - 与后端/api/properties接口对应
    apiGet('/properties', filters)
        .then(data => {
            // 渲染物业列表
            renderPropertyList(data);
        })
        .catch(error => {
            console.error('Failed to load property list:', error);
            showErrorMessage('加载物业列表失败');
        });
}

// 添加物业 - 与后端Property模型保持一致
function addProperty(propertyData) {
    apiPost('/properties', propertyData)
        .then(() => {
            showSuccessMessage('添加物业成功');
            // 返回物业列表页
            window.location.href = '/properties';
        })
        .catch(error => {
            console.error('Failed to add property:', error);
            showErrorMessage('添加物业失败');
        });
}

// 编辑物业 - 与后端Property模型保持一致
function updateProperty(id, propertyData) {
    apiPut(`/properties/${id}`, propertyData)
        .then(() => {
            showSuccessMessage('更新物业成功');
            // 返回物业列表页
            window.location.href = '/properties';
        })
        .catch(error => {
            console.error('Failed to update property:', error);
            showErrorMessage('更新物业失败');
        });
}

// 删除物业 - 与后端Property模型保持一致
function deleteProperty(id) {
    if (confirm('确定要删除这个物业吗？')) {
        apiDelete(`/properties/${id}`)
            .then(() => {
                showSuccessMessage('删除物业成功');
                // 重新加载物业列表
                loadPropertyList();
            })
            .catch(error => {
                console.error('Failed to delete property:', error);
                showErrorMessage('删除物业失败');
            });
    }
}

// 管理物业管理员 - 与后端PropertyManager模型保持一致
function loadPropertyManagers(propertyId) {
    apiGet(`/properties/${propertyId}/managers`)
        .then(data => {
            renderPropertyManagers(data);
        })
        .catch(error => {
            console.error('Failed to load property managers:', error);
            showErrorMessage('加载物业管理员失败');
        });
}

function addPropertyManager(propertyId, managerData) {
    apiPost(`/properties/${propertyId}/managers`, managerData)
        .then(() => {
            showSuccessMessage('添加物业管理员成功');
            loadPropertyManagers(propertyId);
        })
        .catch(error => {
            console.error('Failed to add property manager:', error);
            showErrorMessage('添加物业管理员失败');
        });
}
```

### 4.6 统计分析模块

#### 4.6.1 功能描述
提供各类数据统计和分析功能，以图表形式展示分析结果。

#### 4.6.2 页面设计
- 人口统计分析：人口结构、人口趋势、特殊人群分布等
- 商户统计分析：商户行业分布、商户数量趋势等
- 综合统计报表：各类综合统计数据报表

#### 4.6.3 交互流程
1. 用户进入统计分析页面
2. 前端请求各类统计数据
3. 后端返回数据后，前端使用ECharts渲染各类图表
4. 用户可以选择不同的统计维度和时间范围进行数据筛选

#### 4.6.4 核心代码结构
```javascript
// 初始化统计分析页面
function initStatistics() {
    // 获取统计参数
    const params = getStatisticsParams();
    
    // 请求统计数据
    $.ajax({
        url: '/api/statistics/detailed',
        type: 'GET',
        headers: { 'Authorization': 'Bearer ' + getToken() },
        data: params,
        success: function(data) {
            // 渲染各类统计图表
            renderPopulationStructureChart(data.population_structure);
            renderBusinessIndustryChart(data.business_industry);
            renderSpecialPopulationChart(data.special_population);
        }
    });
}

// 渲染特殊人群分布图
function renderSpecialPopulationChart(data) {
    const chartDom = document.getElementById('special-population-chart');
    const myChart = echarts.init(chartDom);
    
    const option = {
        title: { text: '特殊人群分布' },
        tooltip: { trigger: 'item' },
        legend: { orient: 'vertical', left: 'left' },
        series: [
            {
                name: '特殊人群',
                type: 'pie',
                radius: '50%',
                data: [
                    { value: data.disabled, name: '残疾人' },
                    { value: data.elderly, name: '高龄老人' },
                    { value: data.special_support, name: '特扶人口' },
                    { value: data.low_income, name: '低保户' }
                ]
            }
        ]
    };
    
    myChart.setOption(option);
}
```

### 4.7 系统管理模块

#### 4.7.1 功能描述
实现系统用户管理、系统配置和数据备份恢复等功能。

#### 4.7.2 页面设计
- 用户管理界面：显示系统用户列表，支持添加、编辑、删除用户
- 系统配置界面：提供系统各项配置选项
- 数据备份恢复界面：提供数据备份和恢复功能

#### 4.7.3 交互流程
1. 用户进入系统管理页面
2. 前端请求系统相关数据
3. 后端返回数据后，前端渲染相关界面
4. 用户可以进行用户管理、系统配置、数据备份恢复等操作

## 五、前端组件设计

### 5.1 通用组件
- **导航组件**：系统菜单和导航栏
- **侧边栏组件**：功能模块导航菜单
- **面包屑组件**：当前页面路径显示
- **分页组件**：数据列表分页控制
- **搜索框组件**：数据搜索功能
- **表单组件**：通用表单元素和验证
- **提示框组件**：成功/错误/警告提示
- **确认框组件**：操作确认对话框

### 5.2 业务组件
- **居民信息卡片**：展示居民核心信息
- **商户信息卡片**：展示商户核心信息
- **物业信息卡片**：展示物业核心信息
- **统计图表组件**：各类数据统计图表
- **数据导入导出组件**：数据批量导入导出功能

## 六、前端API交互设计

### 6.1 API请求封装
前端对所有API请求进行统一封装，处理请求参数、请求头、响应数据和错误处理等，确保与后端Django REST Framework提供的RESTful API接口保持一致。

```javascript
// API请求封装
const API_BASE_URL = '/api';

// GET请求 - 与Django REST Framework列表和详情接口对应
function apiGet(endpoint, params = {}) {
    return $.ajax({
        url: `${API_BASE_URL}${endpoint}`,
        type: 'GET',
        data: params,
        beforeSend: function(xhr) {
            // 添加认证token
            const accessToken = getAccessToken();
            if (accessToken) {
                xhr.setRequestHeader('Authorization', `Bearer ${accessToken}`);
            }
        }
    }).fail(function(xhr) {
        handleApiError(xhr);
    });
}

// POST请求 - 与Django REST Framework创建接口对应
function apiPost(endpoint, data = {}) {
    return $.ajax({
        url: `${API_BASE_URL}${endpoint}`,
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json',
        beforeSend: function(xhr) {
            // 添加认证token
            const accessToken = getAccessToken();
            if (accessToken) {
                xhr.setRequestHeader('Authorization', `Bearer ${accessToken}`);
            }
        }
    }).fail(function(xhr) {
        handleApiError(xhr);
    });
}

// PUT请求 - 与Django REST Framework更新接口对应
function apiPut(endpoint, data = {}) {
    return $.ajax({
        url: `${API_BASE_URL}${endpoint}`,
        type: 'PUT',
        data: JSON.stringify(data),
        contentType: 'application/json',
        beforeSend: function(xhr) {
            // 添加认证token
            const accessToken = getAccessToken();
            if (accessToken) {
                xhr.setRequestHeader('Authorization', `Bearer ${accessToken}`);
            }
        }
    }).fail(function(xhr) {
        handleApiError(xhr);
    });
}

// PATCH请求 - 与Django REST Framework部分更新接口对应
function apiPatch(endpoint, data = {}) {
    return $.ajax({
        url: `${API_BASE_URL}${endpoint}`,
        type: 'PATCH',
        data: JSON.stringify(data),
        contentType: 'application/json',
        beforeSend: function(xhr) {
            // 添加认证token
            const accessToken = getAccessToken();
            if (accessToken) {
                xhr.setRequestHeader('Authorization', `Bearer ${accessToken}`);
            }
        }
    }).fail(function(xhr) {
        handleApiError(xhr);
    });
}

// DELETE请求 - 与Django REST Framework删除接口对应
function apiDelete(endpoint) {
    return $.ajax({
        url: `${API_BASE_URL}${endpoint}`,
        type: 'DELETE',
        beforeSend: function(xhr) {
            // 添加认证token
            const accessToken = getAccessToken();
            if (accessToken) {
                xhr.setRequestHeader('Authorization', `Bearer ${accessToken}`);
            }
        }
    }).fail(function(xhr) {
        handleApiError(xhr);
    });
}

// 文件上传 - 与Django REST Framework文件上传接口对应
function apiUpload(endpoint, formData) {
    return $.ajax({
        url: `${API_BASE_URL}${endpoint}`,
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        beforeSend: function(xhr) {
            // 添加认证token
            const accessToken = getAccessToken();
            if (accessToken) {
                xhr.setRequestHeader('Authorization', `Bearer ${accessToken}`);
            }
        }
    }).fail(function(xhr) {
        handleApiError(xhr);
    });
}

// 错误处理 - 与Django REST Framework错误响应格式保持一致
function handleApiError(xhr) {
    if (xhr.status === 401) {
        // 认证失败，与后端Simple JWT认证机制配合
        if (isTokenExpired(getAccessToken())) {
            // 尝试刷新Token
            refreshAccessToken().then(() => {
                // 刷新成功后可以选择重试请求
            });
        } else {
            // Token无效或未授权，跳转到登录页面
            removeTokens();
            window.location.href = '/login';
        }
    } else if (xhr.status === 403) {
        // 权限不足，与后端Django REST Framework权限类保持一致
        alert('您没有权限执行此操作');
    } else if (xhr.status === 404) {
        // 资源不存在
        alert('请求的资源不存在');
    } else if (xhr.status === 400) {
        // 请求参数错误，与后端Django REST Framework序列化器验证错误格式保持一致
        try {
            const errorData = JSON.parse(xhr.responseText);
            let errorMessage = '请求参数错误：';
            for (const field in errorData) {
                if (errorData.hasOwnProperty(field)) {
                    errorMessage += `\n${field}: ${errorData[field].join(', ')}`;
                }
            }
            alert(errorMessage);
        } catch (e) {
            alert('请求参数错误，请检查输入');
        }
    } else if (xhr.status === 500) {
        // 服务器错误
        alert('服务器内部错误，请稍后再试');
    } else {
        // 其他错误
        alert('请求失败，请稍后再试');
    }
}```

### 6.2 认证与授权
前端认证与授权机制与后端Django Simple JWT认证系统紧密集成，确保系统安全访问。

#### 6.2.1 JWT Token管理
- **Token获取**：用户登录成功后从后端Django Simple JWT接口获取JWT Token（access token和refresh token）
- **Token存储**：将Token安全存储在localStorage中
- **Token过期处理**：实现基于Django Simple JWT的Token自动刷新机制，当access token即将过期时，使用refresh token获取新的access token
- **Token清除**：用户登出时清除localStorage中的Token

```javascript
// Token管理
function getAccessToken() {
    return localStorage.getItem('access_token');
}

function getRefreshToken() {
    return localStorage.getItem('refresh_token');
}

function setTokens(accessToken, refreshToken) {
    localStorage.setItem('access_token', accessToken);
    localStorage.setItem('refresh_token', refreshToken);
}

function removeTokens() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
}

// 检查Token是否过期
function isTokenExpired(token) {
    try {
        const decoded = jwt_decode(token);
        return decoded.exp < Date.now() / 1000;
    } catch (e) {
        return true;
    }
}

// 刷新Token
function refreshAccessToken() {
    const refreshToken = getRefreshToken();
    if (!refreshToken) {
        removeTokens();
        window.location.href = '/login';
        return Promise.reject('No refresh token available');
    }
    
    return $.ajax({
        url: '/api/token/refresh/',
        type: 'POST',
        data: JSON.stringify({refresh: refreshToken}),
        contentType: 'application/json'
    }).then(response => {
        setTokens(response.access, refreshToken);
        return response.access;
    }).catch(() => {
        removeTokens();
        window.location.href = '/login';
        throw new Error('Failed to refresh token');
    });
}

// 拦截器：处理认证失败和Token刷新
function setupAuthInterceptor() {
    let refreshing = false;
    let refreshQueue = [];
    
    $(document).ajaxSend(function(event, xhr) {
        // 添加认证头
        const accessToken = getAccessToken();
        if (accessToken) {
            xhr.setRequestHeader('Authorization', 'Bearer ' + accessToken);
        }
    });
    
    $(document).ajaxError(function(event, xhr) {
        if (xhr.status === 401) {
            const request = event.target;
            const accessToken = getAccessToken();
            
            // 如果没有Token或者Token未过期，直接跳转到登录页面
            if (!accessToken || !isTokenExpired(accessToken)) {
                removeTokens();
                window.location.href = '/login';
                return;
            }
            
            // 处理Token刷新
            if (!refreshing) {
                refreshing = true;
                
                refreshAccessToken().then(newToken => {
                    refreshing = false;
                    
                    // 重试队列中的请求
                    refreshQueue.forEach(callback => callback(newToken));
                    refreshQueue = [];
                }).catch(() => {
                    refreshing = false;
                    refreshQueue = [];
                });
            }
            
            // 将当前请求加入队列等待重试
            return new Promise((resolve, reject) => {
                refreshQueue.push((newToken) => {
                    // 重新设置请求头
                    request.setRequestHeader('Authorization', 'Bearer ' + newToken);
                    
                    // 重新发送请求
                    $.ajax({
                        url: request.url,
                        type: request.method,
                        headers: { 'Authorization': 'Bearer ' + newToken },
                        data: request.data,
                        contentType: request.contentType
                    }).then(resolve).catch(reject);
                });
            });
        }
    });
}
```

#### 6.2.2 用户角色与权限管理
- **角色识别**：通过Token解析用户角色信息
- **动态路由**：根据用户角色动态生成可访问的路由
- **权限验证**：在组件级别实现细粒度的权限验证，与后端基于角色的访问控制（RBAC）保持一致

```javascript
// 用户角色与权限管理
function getUserRole() {
    const token = getAccessToken();
    if (token) {
        try {
            const decoded = jwt_decode(token);
            return decoded.role;
        } catch (e) {
            return null;
        }
    }
    return null;
}

function hasPermission(permission) {
    const token = getAccessToken();
    if (token) {
        try {
            const decoded = jwt_decode(token);
            return decoded.permissions && decoded.permissions.includes(permission);
        } catch (e) {
            return false;
        }
    }
    return false;
}

function canAccessRoute(route) {
    // 公开路由无需验证
    if (route.public) {
        return true;
    }
    
    // 检查登录状态
    const token = getAccessToken();
    if (!token || isTokenExpired(token)) {
        return false;
    }
    
    // 检查角色和权限
    const userRole = getUserRole();
    const requiredRoles = route.requiredRoles || [];
    const requiredPermissions = route.requiredPermissions || [];
    
    // 角色检查
    if (requiredRoles.length > 0 && !requiredRoles.includes(userRole)) {
        return false;
    }
    
    // 权限检查
    for (const permission of requiredPermissions) {
        if (!hasPermission(permission)) {
            return false;
        }
    }
    
    return true;
}

## 七、前端数据流向

### 7.1 数据输入流程
1. 用户通过前端界面输入数据
2. 前端进行客户端验证
3. 前端将数据以JSON格式发送到后端Django REST Framework API
4. 后端Django REST Framework视图接收数据，通过序列化器进行服务端验证和数据转换
5. 后端通过Django ORM将验证通过的数据持久化到MySQL数据库
6. 后端返回操作结果给前端
7. 前端根据返回结果更新界面和显示提示信息

### 7.2 数据查询流程
1. 用户在前端界面发起数据查询请求
2. 前端构造请求参数，携带JWT Token
3. 前端发送GET请求到后端Django REST Framework API
4. 后端Django REST Framework通过Simple JWT验证Token合法性并解析查询条件
5. 后端通过Django ORM查询集(QuerySet)从MySQL数据库查询数据
6. 后端序列化器将查询结果序列化为JSON格式并返回
7. 前端接收数据，渲染界面或更新图表

### 7.3 数据更新流程
1. 用户在前端填写表单或编辑数据
2. 前端进行数据验证
3. 前端构造数据对象，携带JWT Token
4. 前端发送POST/PUT请求到后端Django REST Framework API
5. 后端Django REST Framework通过Simple JWT验证Token合法性
6. 后端序列化器解析请求数据，执行数据验证
7. 后端通过Django ORM执行数据存储或更新操作
8. 后端返回更新结果
9. 前端根据返回结果更新界面和显示提示信息

## 八、前端性能优化

### 8.1 资源优化
- **资源压缩**：压缩CSS和JavaScript文件
- **资源合并**：合并多个CSS和JavaScript文件
- **资源缓存**：设置合理的缓存策略
- **CDN加速**：使用CDN分发静态资源

### 8.2 页面加载优化
- **懒加载**：图片和非首屏内容懒加载
- **按需加载**：组件和功能按需加载
- **预加载**：关键资源预加载
- **减少HTTP请求**：合并请求，使用HTTP/2

### 8.3 渲染优化
- **DOM优化**：减少DOM操作，使用虚拟DOM
- **CSS优化**：避免重排重绘，使用CSS动画
- **JavaScript优化**：减少阻塞，使用异步加载
- **Web Workers**：将耗时操作移至后台线程

### 8.4 数据处理优化
- **前端缓存**：缓存不常变化的数据
- **分页加载**：大数据量分页加载
- **数据预取**：预取可能需要的数据
- **数据压缩**：传输时使用数据压缩

## 九、前端安全机制

前端安全机制与后端Django安全体系紧密配合，共同构建完整的系统安全防护。

### 9.1 防止XSS攻击
- **输入验证**：对用户输入进行严格验证，与后端Django Forms和ModelForms验证形成双重保障
- **输出编码**：对输出到页面的内容进行HTML编码
- **内容安全策略(CSP)**：配置CSP策略，与后端Django security middleware协同工作
- **XSS过滤器**：实现XSS过滤功能

### 9.2 防止CSRF攻击
- **CSRF Token**：使用Django内置的CSRF Token验证机制，自动包含在表单和AJAX请求中
- **SameSite Cookie**：与后端同步设置Cookie的SameSite属性
- **Origin检查**：验证请求的Origin和Referer，与后端Django安全配置保持一致

### 9.3 数据安全
- **敏感数据加密**：敏感数据在前端加密后传输，与后端Django的加密功能配合使用
- **安全存储**：使用localStorage安全存储JWT Token等信息，配合后端Simple JWT认证机制
- **数据脱敏**：在前端展示时对敏感数据进行脱敏处理

### 9.4 安全访问控制
- **前端路由守卫**：实现路由级别的访问控制，与后端Django REST Framework的权限类协同工作
- **组件级权限控制**：实现组件级别的权限控制，与后端基于角色的访问控制（RBAC）保持一致
- **操作日志记录**：记录用户的关键操作日志，与后端Django admin日志记录功能互补

## 十、浏览器兼容性要求

### 10.1 主流浏览器支持
- Google Chrome（最新两个稳定版本）
- Mozilla Firefox（最新两个稳定版本）
- Apple Safari（最新两个稳定版本）
- Microsoft Edge（最新两个稳定版本）

### 10.2 兼容性保障措施
- 使用Babel转译ES6+代码
- 使用Autoprefixer处理CSS前缀
- 使用Polyfill补充浏览器缺失功能
- 定期进行浏览器兼容性测试

## 十一、前端开发规范

### 11.1 代码规范
- **HTML规范**：语义化标签，合理嵌套，统一缩进
- **CSS规范**：使用BEM命名法，避免内联样式，合理使用CSS变量
- **JavaScript规范**：使用ES6+语法，遵循模块化开发，使用ESLint进行代码检查

### 11.2 目录规范
- 按功能模块组织代码结构
- 公共组件和工具函数统一管理
- 静态资源分类存放

### 11.3 命名规范
- 文件名：小写字母，使用连字符(-)分隔
- 变量名：小驼峰命名法
- 函数名：小驼峰命名法，动词+名词
- 类名：大驼峰命名法

### 11.4 注释规范
- 为重要函数和组件添加JSDoc注释
- 为复杂逻辑添加行内注释
- 为文件添加文件头注释

### 11.5 版本控制规范
- 使用Git进行版本控制
- 遵循分支管理策略
- 提交信息清晰明了

## 十二、前端部署说明

前端部署应与后端Django系统部署协同进行，确保前后端集成顺畅。

### 12.1 开发环境部署
1. **安装依赖**：确保Node.js环境正确安装后，使用npm install命令安装项目依赖
2. **配置开发环境**：设置开发环境变量，配置与后端Django开发服务器的连接参数
3. **启动开发服务器**：使用npm run dev命令启动前端开发服务器
4. **访问应用**：在浏览器中访问前端应用，确保能正确连接到后端Django开发服务器

### 12.2 生产环境部署
1. **构建应用**：使用npm run build命令构建生产版本
2. **配置生产环境**：设置生产环境变量，指向生产环境的Django REST Framework API端点
3. **部署到服务器**：将构建后的文件部署到Web服务器静态文件目录
4. **配置Web服务器**：配置Nginx等Web服务器，与后端Django应用部署在同一服务器或通过负载均衡连接
5. **设置HTTPS**：配置SSL证书，启用HTTPS访问，与后端Django应用的HTTPS配置保持一致

### 12.3 Nginx配置示例

```nginx
server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name example.com;
    root /path/to/frontend/dist;
    index index.html;
    
    # SSL配置
    ssl_certificate /path/to/ssl/certificate.crt;
    ssl_certificate_key /path/to/ssl/private.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers off;
    
    location / {
        try_files $uri $uri/ /index.html;
    }
    
    # 代理API请求到Django REST Framework
    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # 静态资源优化
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
    
    # 缓存配置
    location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
        expires 30d;
        add_header Cache-Control "public, max-age=2592000";
    }
}
```

### 12.4 Docker部署集成

前端应用可与后端Django应用一起使用Docker容器化部署，通过Docker Compose编排服务。建议将前端静态文件构建后放入Nginx容器，与Django应用容器通过网络连接，实现完整的容器化部署方案。

### 12.5 性能监控与优化
- 配置前端性能监控工具
- 定期分析性能数据
- 根据性能分析结果进行优化