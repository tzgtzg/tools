#!/usr/bin/python
# build_native.py
# Build native codes


import sys
import os, os.path
import shutil
import json
from hashlib import md5
from optparse import OptionParser

currentPath = os.getcwd()
splitText='Jigsaw/'

def md5_file(file_extensions=None):
    md5_dict = {}
    
    if file_extensions is None:
        file_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tga']  # 默认支持的图片格式
    else:
        # 确保扩展名以点开头
        file_extensions = [ext if ext.startswith('.') else '.' + ext for ext in file_extensions]
    
    # 递归遍历当前目录下的所有文件
    for root, dirs, files in os.walk(currentPath):
        for file in files:
            # 检查文件扩展名是否在指定格式列表中
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in file_extensions:
                localPath = os.path.join(root, file)
                
                m = md5()
                with open(localPath, 'rb') as a_file:
                    m.update(a_file.read())
                md5str = m.hexdigest()
                print('\n')
                print(localPath)
                print(md5str)
                
                # 将反斜杠转换为正斜杠
                normalized_path = localPath.replace('\\', '/')
                
                # 截取到Jigsaw目录
                jigsaw_index = normalized_path.find(splitText)
                if jigsaw_index != -1:
                    # 保留从Jigsaw开始的部分
                    jigsaw_path = normalized_path[jigsaw_index:]
                else:
                    # 如果没有找到Jigsaw，使用原路径
                    jigsaw_path = normalized_path
                
                # 将文件路径和MD5值添加到字典中
                md5_dict[jigsaw_path] = md5str
    
    # 将MD5字典写入JSON文件
    output_file = os.path.join(currentPath, "md5_hashes.json")
    with open(output_file, 'w') as json_file:
        json.dump(md5_dict, json_file, indent=4)
    
    print(f"\nMD5 hashes saved to: {output_file}")
    print(f"Processed {len(md5_dict)} files")
    return md5_dict


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--filepath", dest="md5file_param", help='md5  file  path', action="append")
    parser.add_option("-o", "--output", dest="output_file", help='output JSON file name', default="md5_hashes.json")
    parser.add_option("-e", "--extensions", dest="file_extensions", help='file extensions to process, separated by comma (e.g., jpg,png,gif)', default="jpg,jpeg,png,gif,bmp,tga")
    
    (opts, args) = parser.parse_args()
    
    # 解析文件扩展名
    extensions = opts.file_extensions.split(',') if opts.file_extensions else None
    
    md5_dict = md5_file(extensions)
    
    print("end    end   end ")
