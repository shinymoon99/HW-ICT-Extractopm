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
def write_combineddicts_to_files(dict_lists, output_dir):  
    combined_dict_list = []
    for d in dict_lists:
        combined_dict_list.extend(d)
    # 创建文件名  
    file_name = f'ICT_all_formatted.json'  
    file_path = os.path.join(output_dir, file_name)  
        
    # 将字典写入JSON文件  
    with open(file_path, 'w',encoding="utf-8") as f:  
        json.dump(combined_dict_list, f,ensure_ascii=False)
with open("./datasets/ICT_all_formatted.json",encoding="utf-8") as f:
    a = json.load(f)
data_type = {}
for sentence in a:
    event_type =  sentence["event_list"][0]["event_type"].split("-")[1]
    if event_type not in data_type:
        data_type[event_type] = []
        data_type[event_type].append(sentence)        
    else:
        data_type[event_type].append(sentence)
dict_lists = [v for k,v in data_type.items() if k in ['配置','点击','选择','查看','创建']]
#dict_lists = [v for k,v in data_type.items()]
event_of_class = []
for dict_list in dict_lists:
    event_of_class.append(set())
    for event in dict_list:
        event_of_class[-1].add(event["event_list"][0]["event_type"])
print(event_of_class)
with open("./output/class_events.txt","w") as f:
    for event_class in event_of_class:
        f.write(str(event_class))
        f.write("\n")   
#write_dicts_to_files(dict_lists,"./output/all_class/")
write_combineddicts_to_files(dict_lists,"./datasets/selected_5r/")