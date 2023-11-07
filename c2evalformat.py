import json
import re
def removeQuotes(texts):
    output_texts  = []
    for t in texts:
        modified_t = re.sub(r"<([^>]+)>","",t)
        output_texts.append(modified_t)
    return output_texts
def extract_labels(input_text, source_text):
    label_pattern = r'<([^>]+)>(.*?)</\1>'
    label_matches = re.finditer(label_pattern, input_text)

    label_positions = {}
    
    for match in label_matches:
        label_type = match.group(1)
        label_content = match.group(2)
        start_index = source_text.find(label_content)
        end_index = start_index + len(label_content)
        
        if label_type in label_positions:
            label_positions[label_type].append((start_index, end_index))
        else:
            label_positions[label_type] = [(start_index, end_index)]
    
    return label_positions

# input_text = "<条件>在批量配置LDP Keychain认证或LDP MD5认证后</条件>，<操作>指定LDP对等体 **ifname=10.1.1.1** 不进行认证</操作>。"
# source_text = "在批量配置LDP Keychain认证或LDP MD5认证后，指定LDP对等体 **10.1.1.1** 不进行认证。"

# label_positions = extract_labels(input_text, source_text)
# print(label_positions)

def extract_label_positions(input_text, source_text):
    label_pattern = r'<([^>]+)>(.*?)(</\1>)'
    temp_text = input_text
    label_positions = {}
    # 找到第一个命中pattern直到没有为止
    match = re.search(label_pattern,temp_text)
    while(match!=None):
        label_type = match.group(1)
        label_content = match.group(2)
        start,end = (match.start(2)-len(label_type)-2,match.end(2)-len(label_type)-2)
        temp_text = temp_text[:match.start(1)-1]+label_content+temp_text[match.end(3):]
        if source_text[start:end]==label_content:
            # 用标签类型更新位置字典
            if label_type in label_positions:
                label_positions[label_type].append((start, end))
            else:
                label_positions[label_type] = [(start, end)]        
        match = re.search(label_pattern,temp_text)
    return label_positions    
    # 获取pattern位置，文本在源文本位置，删除pattern，修改temp_text
def build_data(text,label_locs,event_type):
    """
    :param label_locs = {"l":[[],[]]}
    :return 
    """
    t2l = {"l":"位置","o":"对象","i":"影响","t":"触发词","c":"内容"}
    trigger_index  = label_locs["t"][0]
    trigger_span = text[trigger_index[0]:trigger_index[1]]
    trigger_start_index = label_locs["t"][0][0]
    event = {"event_type":event_type,"trigger":trigger_span,"trigger_start_index":trigger_start_index}
    data = {"text":text,"id":1,"event_list":[]}
    arguments = []
    for k,v in label_locs.items():
        if k=='t':
            pass
        else:
            for index in v:
                argument = {}
                start,end =index[0],index[1]
                argument= {"argument_start_index":start,"argument_end_index":end,"role":t2l[k],"argument":text[start:end],"alias":[]}
                arguments.append(argument)
    event["arguments"]=arguments
    data["event_list"].append(event)
    return data
datas = []
inputtexts = []
labelposes = []

names = ["点选","配置","查看","创建"]
file_names = ["click","configure","view","create"]
for i in range(4):
    format_dataset = []
    with open(f"./datasets/selected_4/test_txt/{file_names[i]}_SL_test.txt","r",encoding="utf-8") as f:
        inputtexts =f.readlines()

    sourcetexts = removeQuotes(inputtexts)
    e_type = names[i]
    for itext,s in zip(inputtexts,sourcetexts):
        label_pos  =extract_labels(itext,s)
        labelposes.append(label_pos)
        output_data =build_data(s,label_pos,e_type)
        format_dataset.append(output_data)
    with open(f"./datasets/selected_4/test_json/{file_names[i]}.json","w") as f1:
        json.dump(format_dataset,f1)
