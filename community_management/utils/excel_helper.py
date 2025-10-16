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