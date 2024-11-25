import os
from openpyxl import Workbook
from openpyxl.drawing.image import Image

# 指定图片文件夹路径
image_folder = './images'

# 获取文件夹中的所有图片文件名称
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# 创建一个新的Excel工作簿
wb = Workbook()
ws = wb.active

# 设置表头
ws.append(['图片名称', '图片'])

# 将图片插入到Excel表格的每一行
for idx, image_name in enumerate(image_files, start=1):
    # 插入图片名称
    ws.cell(row=idx + 1, column=1, value=image_name)
    
    # 加载图片
    img_path = os.path.join(image_folder, image_name)
    img = Image(img_path)
    
    # 调整图片大小（可选）
    img.width = 100
    img.height = 100
    
    # 插入图片
    img_anchor = f'B{idx + 1}'  # 图片插入到B列
    ws.add_image(img, img_anchor)
    
    # 设置行高
    ws.row_dimensions[idx + 1].height = 100

# 保存Excel工作簿
output_file = 'images_with_names.xlsx'
wb.save(output_file)

print(f"图片已成功插入到 {output_file}")