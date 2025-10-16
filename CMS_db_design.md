# 社区信息管理系统数据库设计文档

## 一、数据库概述

本数据库设计文档详细描述了社区信息管理系统的数据库结构、表定义、字段说明、关系模型及相关技术规范。数据库设计遵循第三范式（3NF）原则，确保数据的完整性、一致性和可扩展性。

## 二、数据库环境

- **数据库系统**：MySQL 8.0
- **字符集**：UTF-8
- **排序规则**：utf8mb4_unicode_ci (MySQL) / utf8mb4 (PostgreSQL)

## 三、数据库结构设计

### 3.1 整体架构

系统数据库包含以下核心表：
- 居民身份信息表（residents）
- 楼房信息表（buildings）
- 小区信息表（communities）
- 单元信息表（units）
- 楼栋信息表（apartments）
- 户号信息表（house_numbers）
- 平房信息表（bungalows）
- 胡同信息表（hutong）
- 组别信息表（groups）
- 物业信息表（properties）
- 物业管理表（property_managers）
- 商户信息表（merchants）
- 行业信息表（industries）
- 街道信息表（streets）
- 低保户信息表（low_income_residents）
- 五保户信息表（five_guarantees_residents）
- 残疾人信息表（disabled_residents）
- 特扶户信息表（special_needs_residents）
- 死亡户信息表（deceased_residents）
- 重点对象信息表（special_objects）
- 管理员信息表（admins）
- 民族表（ethnicities）
- 权限组表（roles）

## 四、表结构详细设计

### 4.1 居民身份信息表（residents）

**表功能**：存储居民的身份信息，包括姓名、性别、出生日期、联系电话、身份证号等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 居民唯一标识 |
| name | VARCHAR | 50 | 否 | 否 | | 居民姓名 |
| id_card | VARCHAR | 18 | 否 | 否 | UNIQUE | 身份证号（唯一） |
| gender | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 性别（0男，1女） |
| birth_date | DATE | | 否 | 否 | | 出生日期 |
| ethnicity_id | INT | 11 | 否 | 否 | FOREIGN KEY (ethnicity_id) REFERENCES ethnicities(id) | 民族ID |
| political_affiliation | TINYINT | 2 | 否 | 否 | DEFAULT 0 | 政治面貌（0群众/1中共党员/2共青团员/3中国国民党革命委员会/4中国民主同盟/5中国民主建国会/6中国民主促进会/7中国农工民主党/8中国致公党/9九三学社/10台湾民主自治同盟）|
| household_address | VARCHAR | 255 | 否 | 否 | | 户籍地址 |
| phone_number | VARCHAR | 20 | 否 | 否 | | 联系方式 |
| marital_status | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 婚姻状况（0未婚/1已婚/2离异/3丧偶）|
| education_level | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 学历（0文盲/1小学/2初中/3高中/4大专/5本科/6研究生） |
| population_type | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 人口类型（0常住人口, 1非常住人口）| 
| residential_type | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 住宅类型（0楼房/1平房）|
| own_house | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 是否自有房（0是，1否）|
| is_low_income | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 是否低保户（0否，1是） |
| is_beneficiary | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 是否五保户（0否，1是） |
| is_disabled | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 是否残疾（0否，1是） |
| is_special_support | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 是否特扶人口（0否，1是） |
| is_key_person | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 是否重点对象（0否，1是） |
| is_deceased | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 是否死亡（0否，1是） |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 唯一索引：id_card
- 索引：name, ethnicity, political_affiliation, population_type, residential_type, marital_status, education_level

### 4.2 楼房信息表（buildings）

**表功能**：存储楼房的详细信息，包括居民id、小区ID、单元ID、户号ID等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 楼房唯一标识 |
| resident_id | INT | 11 | 否 | 否 | FOREIGN KEY (resident_id) REFERENCES residents(id) | 居民ID |
| building_number | INT | 5 | 否 | 否 | | 楼房号 |
| house_number_id | INT | 11 | 否 | 否 | FOREIGN KEY (house_number_id) REFERENCES house_numbers(id) | 户号ID |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：resident_id, house_number_id

### 4.4 单元信息表（units）

**表功能**：存储单元的详细信息，包括单元号、小区ID等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 单元唯一标识 |
| apartment_id | INT | 11 | 否 | 否 | FOREIGN KEY (apartment_id) REFERENCES apartments(id) | 楼栋ID |
| unit_number | TINYINT | 1 | 否 | 否 | | 单元号 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：community_id, unit_number

### 4.5 楼栋信息表（apartments）

**表功能**：存储楼栋的详细信息，包括楼栋号、单元ID等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 楼栋唯一标识 |
| community_id | INT | 11 | 否 | 否 | FOREIGN KEY (community_id) REFERENCES communities(id) | 小区ID |
| apartment_number | TINYINT | 2 | 否 | 否 | | 楼栋号 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：community_id, apartment_number

### 4.6 小区信息表（communities）

**表功能**：存储小区的详细信息，包括小区名称、所属组别等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 小区唯一标识 |
| community_name | VARCHAR | 255 | 否 | 否 | UNIQUE | 小区名称（唯一） |
| group_id | INT | 11 | 否 | 否 | FOREIGN KEY (group_id) REFERENCES groups(id) | 所属组别ID |
| community_number | VARCHAR | 50 | 否 | 否 | | 小区号 |
| has_property | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 是否有物业（0否，1是） |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：community_name, group_id, has_property

### 4.7 平房信息表（bungalows）

**表功能**：存储平房的详细信息，包括平房号、胡同ID等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 平房唯一标识 |
| resident_id | INT | 11 | 否 | 否 | FOREIGN KEY (resident_id) REFERENCES residents(id) | 居民ID |
| bungalow_number | VARCHAR | 50 | 否 | 否 | | 平房号 |
| hutong_id | INT | 11 | 否 | 否 | FOREIGN KEY (hutong_id) REFERENCES hutong(id) | 胡同ID |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：resident_id, bungalow_number

### 4.8 胡同信息表（hutong）

**表功能**：存储胡同的详细信息，包括胡同号、小区ID等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 胡同唯一标识 |
| hutong_name | VARCHAR | 255 | 否 | 否 | UNIQUE | 胡同名称（唯一） |
| group_id | INT | 11 | 否 | 否 | FOREIGN KEY (group_id) REFERENCES groups(id) | 所属组别ID |
| hutong_number | VARCHAR | 50 | 否 | 否 | | 胡同号 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：hutong_name, group_id, hutong_number

### 4.9 组别信息表（groups）

**表功能**：存储组别信息，包括组别号等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 组别唯一标识 |
| group_number | VARCHAR | 50 | 否 | 否 | UNIQUE | 组别号（唯一） |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：group_number

### 4.10 物业信息表（properties）

**表功能**：存储物业的详细信息，包括物业类型、物业地址等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 物业唯一标识 |
| property_name | VARCHAR | 255 | 否 | 否 | UNIQUE | 物业名称（唯一） |
| property_address | VARCHAR | 255 | 否 | 否 | | 物业地址 |
| property_owner | VARCHAR | 255 | 否 | 否 | | 物业负责人 |
| property_contact_phone | VARCHAR | 20 | 否 | 否 | | 物业联系电话 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：property_name, property_owner, property_contact_phone

### 4.11 物业管理表（property_managers）

**表功能**：存储物业经理的详细信息，包括物业经理ID、物业ID等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 物业管理唯一标识 |
| property_id | INT | 11 | 否 | 否 | FOREIGN KEY (property_id) REFERENCES properties(id) | 物业ID |
| community_id | INT | 11 | 否 | 否 | FOREIGN KEY (community_id) REFERENCES communities(id) | 所属小区ID（唯一） |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：property_id, community_id

### 4.12 商户信息表（merchants）

**表功能**：存储社区商户的详细信息

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 商户唯一标识 |
| merchants_name | VARCHAR | 100 | 否 | 否 | | 商户名称 |
| credit_code | VARCHAR | 18 | 否 | 否 | UNIQUE | 统一社会信用代码（唯一） |
| license_number | VARCHAR | 50 | 否 | 否 | | 营业执照编号 |
| legal_person_name | VARCHAR | 50 | 否 | 否 | | 法人代表姓名 |
| legal_person_id | VARCHAR | 18 | 否 | 否 | | 法人代表身份证号 |
| phone_number | VARCHAR | 20 | 否 | 是 | | 联系电话 |
| address | VARCHAR | 255 | 否 | 否 | | 地址 |
| business_scope | TEXT | | 否 | 是 | | 经营范围 |
| industry_id | INT | 11 | 否 | 否 | FOREIGN KEY (industries.id) | 所属行业ID |
| streets_id | INT | 11 | 否 | 否 | FOREIGN KEY (streets.id) | 所属街道ID |
| establishment_date | DATE | | 否 | 否 | | 成立日期 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 唯一索引：credit_code
- 普通索引：business_name, license_number, legal_person, streets_id, industry_id

### 4.13 行业信息表（industries）

**表功能**：存储行业信息，包括行业ID、行业名称等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 行业唯一标识 |
| industry_name | VARCHAR | 100 | 否 | 否 | UNIQUE | 行业名称（唯一） |
| industry_code | VARCHAR | 50 | 否 | 否 | UNIQUE | 行业代码（唯一） |

**索引**：
- 主键索引：id
- 索引：industry_name, industry_code

### 4.14 街道信息表（streets）

**表功能**：存储街道信息，包括街道ID、街道名称等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 街道唯一标识 |
| street_name | VARCHAR | 100 | 否 | 否 | UNIQUE | 街道名称（唯一） |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：street_name

### 4.15 低保户信息表（low_income_residents）

**表功能**：存储低保户的详细信息

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 低保户唯一标识 |
| resident_id | INT | 11 | 否 | 否 | FOREIGN KEY (residents.id) | 居民ID |
| authentication_date | DATETIME | | 否 | 否 | | 认证日期 |
| bank_account_number | VARCHAR | 50 | 否 | 否 | UNIQUE | 银行卡号（唯一） |
| bank_account_name | VARCHAR | 100 | 否 | 否 | | 银行卡账户名称 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：resident_id

### 4.16 五保户信息表（five_guarantees_residents）

**表功能**：存储五保户的详细信息

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 五保户唯一标识 |
| resident_id | INT | 11 | 否 | 否 | FOREIGN KEY (residents.id) | 居民ID |
| authentication_date | DATETIME | | 否 | 否 | | 认证日期 |
| bank_account_number | VARCHAR | 50 | 否 | 否 | UNIQUE | 银行卡号（唯一） |
| bank_account_name | VARCHAR | 100 | 否 | 否 | | 银行卡账户名称 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：resident_id

### 4.17 残疾人信息表（disabled_residents）

**表功能**：存储残疾人的详细信息

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 残疾人唯一标识 |
| resident_id | INT | 11 | 否 | 否 | FOREIGN KEY (residents.id) | 居民ID |
| authentication_date | DATETIME | | 否 | 否 | | 认证日期 |
| bank_account_number | VARCHAR | 50 | 否 | 否 | UNIQUE | 银行卡号（唯一） |
| bank_account_name | VARCHAR | 100 | 否 | 否 | | 银行卡账户名称 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：resident_id

### 4.18 特扶户信息表（special_needs_residents）

**表功能**：存储特扶户的详细信息

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 特扶户唯一标识 |
| resident_id | INT | 11 | 否 | 否 | FOREIGN KEY (residents.id) | 居民ID |
| authentication_date | DATETIME | | 否 | 否 | | 认证日期 |
| bank_account_number | VARCHAR | 50 | 否 | 否 | UNIQUE | 银行卡号（唯一） |
| bank_account_name | VARCHAR | 100 | 否 | 否 | | 银行卡账户名称 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：resident_id

### 4.19 死亡户信息表（deceased_residents）

**表功能**：存储死亡户的详细信息

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 死亡户唯一标识 |
| resident_id | INT | 11 | 否 | 否 | FOREIGN KEY (residents.id) | 居民ID |
| deceased_date | DATETIME | | 否 | 否 | | 死亡日期 |
| deceased_place | VARCHAR | 100 | 否 | 否 | | 死亡地点 |
| deceased_reason | VARCHAR | 255 | 否 | 否 | | 死亡原因 |
| deceased_contact_name | VARCHAR | 100 | 否 | 否 | | 联系人姓名 |
| deceased_contact_phone | VARCHAR | 20 | 否 | 否 | | 联系人电话 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：resident_id

### 4.20 重点对象信息表（special_objects）

**表功能**：存储重点对象的详细信息

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 重点对象唯一标识 |
| resident_id | INT | 11 | 否 | 否 | FOREIGN KEY (residents.id) | 居民ID |
| object_type | TINYINT | 1 | 否 | 否 | | 对象类型（0信访, 1新疆, 2西藏） |
| object_name | VARCHAR | 100 | 否 | 否 | | 对象姓名 |
| object_contact_phone | VARCHAR | 20 | 否 | 否 | | 对象联系电话 |
| object_address | VARCHAR | 255 | 否 | 否 | | 对象住址 |
| object_responsible_name | VARCHAR | 100 | 否 | 否 | | 负责人姓名 |
| object_responsible_phone | VARCHAR | 20 | 否 | 否 | | 负责人联系电话 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：resident_id

### 4.21 管理员信息表（admins）

**表功能**：存储系统管理员的账户信息

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 管理员唯一标识 |
| username | VARCHAR | 50 | 否 | 否 | UNIQUE | 用户名（唯一） |
| password_hash | VARCHAR | 255 | 否 | 否 | | 密码哈希值（加密存储） |
| real_name | VARCHAR | 50 | 否 | 否 | | 真实姓名 |
| phone_number | VARCHAR | 20 | 否 | 否 | | 联系电话 |
| role_id | INT | 11 | 否 | 否 | FOREIGN KEY (roles.id) | 角色ID |
| status | TINYINT | 1 | 否 | 否 | DEFAULT 1 | 状态（0禁用，1启用） |
| create_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 创建时间 |
| last_login_time | DATETIME | | 否 | 是 | | 最后登录时间 |

**索引**：
- 主键索引：id
- 索引：username

### 4.22 民族表（ethnicities）

**表功能**：存储民族信息

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 民族唯一标识 |
| name | VARCHAR | 50 | 否 | 否 | UNIQUE | 民族名称（唯一） |

**索引**：
- 主键索引：id
- 索引：name

### 4.23 权限组表（roles）

**表功能**：存储系统权限组信息

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 权限组唯一标识 |
| name | VARCHAR | 50 | 否 | 否 | UNIQUE | 权限组名称（唯一） |
| description | VARCHAR | 255 | 否 | 是 | | 权限组描述 |

**索引**：
- 主键索引：id
- 索引：name

### 4.24 户号信息表（house_numbers）

**表功能**：存储户号的详细信息

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 户号唯一标识 |
| unit_id | INT | 11 | 否 | 否 | FOREIGN KEY (units.id) | 单元ID |
| house_number | VARCHAR | 20 | 否 | 否 | | 户号 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：unit_id

## 五、数据关系模型

### 5.1详细关系说明

#### 居民身份信息表（residents）
- 与民族表（ethnicities）：一对多关系，一个居民对应一个民族，一个民族可对应多个居民，通过 `ethnicity_id` 关联。

#### 楼房信息表（buildings）
- 与居民身份信息表（residents）：一对多关系，一个居民可对应一套楼房，一套楼房对应多个居民，通过 `resident_id` 关联。
- 与单元信息表（units）：一对多关系，一套楼房对应一个单元，一个单元可对应多套楼房，通过 `unit_id` 关联。

#### 单元信息表（units）
- 与楼栋信息表（apartments）：一对多关系，一个单元对应一个楼栋，一个楼栋可对应多个单元，通过 `apartment_id` 关联。

#### 楼栋信息表（apartments）
- 与小区信息表（communities）：一对多关系，一个楼栋对应一个小区，一个小区可对应多个楼栋，通过 `community_id` 关联。

#### 小区信息表（communities）
- 与组别信息表（groups）：一对多关系，一个小区对应一个组别，一个组别可对应多个小区，通过 `group_id` 关联。

#### 平房信息表（bungalows）
- 与居民身份信息表（residents）：一对多关系，一个居民可对应一套平房，一套平房对应多个居民，通过 `resident_id` 关联。
- 与胡同信息表（hutong）：一对多关系，一套平房对应一个胡同，一个胡同可对应多套平房，通过 `hutong_id` 关联。

#### 胡同信息表（hutong）
- 与组别信息表（groups）：一对多关系，一个胡同对应一个组别，一个组别可对应多个胡同，通过 `group_id` 关联。

#### 物业管理表（property_managers）
- 与物业信息表（properties）：一对多关系，一个物业管理记录对应一个物业，一个物业可对应多个物业管理记录，通过 `property_id` 关联。
- 与小区信息表（communities）：一对一关系，一个物业管理记录仅对应一个小区，一个小区仅对应一个物业管理记录，通过 `community_id` 关联。

#### 商户信息表（merchants）
- 与行业信息表（industries）：一对多关系，一个商户对应一个行业，一个行业可对应多个商户，通过 `industry_id` 关联。
- 与街道信息表（streets）：一对多关系，一个商户对应一条街道，一条街道可对应多个商户，通过 `streets_id` 关联。

#### 低保户信息表（low_income_residents）、五保户信息表（five_guarantees_residents）、残疾人信息表（disabled_residents）、特扶户信息表（special_needs_residents）、死亡户信息表（deceased_residents）、重点对象信息表（special_objects）
- 均与居民身份信息表（residents）：一对多关系，对应表中的一条记录对应一个居民，一个居民可对应零条或一条对应表记录，通过 `resident_id` 关联。

#### 管理员信息表（admins）
- 与权限组表（roles）：一对多关系，一个管理员可对应一个权限组，一个权限组可对应多个管理员，通过中间表 `admin_roles` 关联。

### 5.2 数据完整性约束

- **实体完整性**：所有表都有主键，确保每条记录的唯一性
- **参照完整性**：通过外键约束维护表之间的引用关系
- **域完整性**：通过数据类型、长度、NOT NULL、DEFAULT等约束确保数据的有效性
- **用户定义完整性**：通过UNIQUE、CHECK等约束实现特定业务规则