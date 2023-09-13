import json
import os
def write_dicts_to_files(dict_list, output_dir):  
    for i, dict_ in enumerate(dict_list):  
        # 创建文件名  
        file_name = f'dict_{i}.json'  
        file_path = os.path.join(output_dir, file_name)  
          
        # 将字典写入JSON文件  
        with open(file_path, 'w',encoding="utf-8") as f:  
            json.dump(dict_, f,ensure_ascii=False)
with open("./datasets/selected_5/ICT_all_formatted.json",encoding="utf-8") as f:
    a = json.load(f)
data_type = {}
for sentence in a:
    event_type =  sentence["event_list"][0]["event_type"]
    if event_type not in data_type:
        data_type[event_type] = []
        data_type[event_type].append(sentence)        
    else:
        data_type[event_type].append(sentence)
dict_lists = [v for k,v in data_type.items() if k in ['配置','点击','选择','指定','使能']]
write_dicts_to_files(dict_lists,"./output/selected_5/")