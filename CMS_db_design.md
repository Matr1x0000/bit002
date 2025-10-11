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
- 户号信息表（house_numbers）
- 平房信息表（bungalows）
- 胡同信息表（streets）
- 组别信息表（groups）
- 物业信息表（properties）
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
| population_type | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 人口类型（0常住人口, 1非常住人口）| 
| household_address | VARCHAR | 255 | 否 | 否 | | 户籍地址 |
| residential_type | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 住宅类型（0楼房/1平房）|
| own_house | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 是否自有房（0是，1否）|
| phone_number | VARCHAR | 20 | 否 | 否 | | 联系方式 |
| marital_status | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 婚姻状况（0未婚/1已婚/2离异/3丧偶）|
| education_level | TINYINT | 1 | 否 | 否 | DEFAULT 0 | 学历（0文盲/1小学/2初中/3高中/4大专/5本科/6研究生） |
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
| house_number_id | INT | 11 | 否 | 否 | FOREIGN KEY (house_number_id) REFERENCES house_numbers(id) | 户号ID |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：resident_id, house_number_id

### 4.3 户号信息表（house_numbers）

**表功能**：存储户号的详细信息，包括户号、单元ID等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 户号唯一标识 |
| unit_id | INT | 11 | 否 | 否 | FOREIGN KEY (unit_id) REFERENCES units(id) | 单元ID |
| house_number | VARCHAR | 50 | 否 | 否 | | 户号 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：unit_id, house_number

### 4.4 单元信息表（units）

**表功能**：存储单元的详细信息，包括单元号、小区ID等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 单元唯一标识 |
| community_id | INT | 11 | 否 | 否 | FOREIGN KEY (community_id) REFERENCES communities(id) | 小区ID |
| unit_number | VARCHAR | 50 | 否 | 否 | | 单元号 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：community_id, unit_number

### 4.5 小区信息表（communities）

**表功能**：存储小区的详细信息，包括小区名称、所属组别等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 小区唯一标识 |
| community_name | VARCHAR | 255 | 否 | 否 | | 小区名称 |
| group_id | INT | 11 | 否 | 否 | FOREIGN KEY (group_id) REFERENCES groups(id) | 所属组别ID |
| group_number | VARCHAR | 50 | 否 | 否 | | 组别号 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：community_name, group_id

### 4.6 平房信息表（bungalows）

**表功能**：存储平房的详细信息，包括平房号、胡同ID等。

| 字段名 | 数据类型 | 长度 | 是否主键 | 是否可为空 | 约束条件 | 描述 |
|-------|---------|------|---------|---------|---------|------|
| id | INT | 11 | 是 | 否 | AUTO_INCREMENT | 平房唯一标识 |
| resident_id | INT | 11 | 否 | 否 | FOREIGN KEY (resident_id) REFERENCES residents(id) | 居民ID |
| bungalow_number | VARCHAR | 50 | 否 | 否 | | 平房号 |
| street_id | INT | 11 | 否 | 否 | FOREIGN KEY (street_id) REFERENCES streets(id) | 胡同ID |
| street_number | VARCHAR | 50 | 否 | 否 | | 胡同号 |
| registration_date | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP | 登记日期 |
| last_update_time | DATETIME | | 否 | 否 | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | 最后更新时间 |

**索引**：
- 主键索引：id
- 索引：resident_id, bungalow_number

