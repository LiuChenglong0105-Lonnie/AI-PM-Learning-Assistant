import json
import os

# 定义文件路径
input_file = '/Users/liuchenglong/Documents/AI/AipmStudyApp/questions&answers.json'
output_file = '/Users/liuchenglong/Documents/AI/AipmStudyApp/questions&answers_processed.json'

def process_json_file():
    try:
        # 检查文件是否存在
        if not os.path.exists(input_file):
            print(f"错误: 文件 '{input_file}' 不存在。")
            return
        
        # 读取JSON文件
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # 检查数据格式是否正确
        if not isinstance(data, list):
            print("错误: JSON数据不是一个列表格式。")
            return
        
        # 统计处理的条目数量
        processed_count = 0
        total_count = len(data)
        
        # 处理每个条目
        for item in data:
            if 'answer' in item and isinstance(item['answer'], str):
                # 检查answer字段内容是否以###开头
                if item['answer'].startswith('### '):
                    # 删除开头的### 
                    item['answer'] = item['answer'][4:]
                    processed_count += 1
        
        # 保存处理后的JSON文件
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"处理完成！")
        print(f"总共处理了 {total_count} 个条目")
        print(f"其中 {processed_count} 个条目的answer字段开头有###并已被删除")
        print(f"处理后的文件已保存至: {output_file}")
        
    except json.JSONDecodeError:
        print("错误: JSON文件格式不正确，无法解析。")
    except Exception as e:
        print(f"处理文件时发生错误: {str(e)}")

if __name__ == '__main__':
    process_json_file()