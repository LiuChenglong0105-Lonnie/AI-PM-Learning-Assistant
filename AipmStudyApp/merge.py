import json
import os

# 定义文件路径
merged_file1 = '/Users/liuchenglong/Documents/AI/AipmStudyApp/merged_ai_answers.json'
merged_file2 = '/Users/liuchenglong/Documents/AI/AipmStudyApp/merged_ai_answers1.json'
target_file = '/Users/liuchenglong/Documents/AI/AipmStudyApp/questions&answers.json'

# 统一的timestamp和starred值
统一时间戳 = '2025-08-16 16:54:00'
统一收藏状态 = False

def process_entry(entry):
    """处理单个条目，保留指定字段，添加新字段，处理category"""
    # 保留需要的字段
    processed_entry = {
        'id': entry.get('id'),
        'category': entry.get('category'),
        'question': entry.get('question'),
        'answer': entry.get('answer')
    }
    
    # 处理category，如果以"AI "开头，删除"AI "
    if processed_entry['category'] and processed_entry['category'].startswith('AI '):
        processed_entry['category'] = processed_entry['category'][3:]
    
    # 添加新字段
    processed_entry['timestamp'] = 统一时间戳
    processed_entry['starred'] = 统一收藏状态
    
    return processed_entry

def main():
    try:
        # 读取源文件
        with open(merged_file1, 'r', encoding='utf-8') as f1, \
             open(merged_file2, 'r', encoding='utf-8') as f2, \
             open(target_file, 'r', encoding='utf-8') as ft:
            
            data1 = json.load(f1)
            data2 = json.load(f2)
            target_data = json.load(ft)
        
        # 处理所有条目
        processed_entries = []
        for entry in data1 + data2:
            processed_entries.append(process_entry(entry))
        
        # 检查是否有重复的id
        existing_ids = {item['id'] for item in target_data}
        new_entries = [item for item in processed_entries if item['id'] not in existing_ids]
        
        # 添加新条目到目标数据
        updated_data = target_data + new_entries
        
        # 写回目标文件
        with open(target_file, 'w', encoding='utf-8') as ft:
            json.dump(updated_data, ft, ensure_ascii=False, indent=2)
        
        print(f"处理完成！成功将 {len(new_entries)} 条新内容添加到 {target_file}")
        print(f"总条目数：{len(updated_data)}")
        
    except Exception as e:
        print(f"处理过程中出错：{e}")

if __name__ == "__main__":
    main()