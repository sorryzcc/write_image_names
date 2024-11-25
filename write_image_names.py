import os

# 指定图片文件夹路径
image_folder = './images'

# 获取文件夹中的所有图片文件名称
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# 指定输出文本文件路径
output_file = 'image_names.txt'

# 将图片名称写入文本文件
with open(output_file, 'w') as file:
    for image_name in image_files:
        file.write(image_name + '\n')

print(f"图片名称已成功写入 {output_file}")