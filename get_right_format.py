import json
key_map = {"start":"arguments_start_index","end":"arguments_end_index","role":"role","text":"argument","alias":"alias"}
def convert2dueeArgu(arguments):
    new_arguments = []
    for argu in arguments:
        t_argu = {key_map[key]:value for key,value in argu.items()}
        t_argu["alias"] = []
        new_arguments.append(t_argu)
    return new_arguments
# read from complex_data
origin_data = []
with open("complex_data_label_event_20230811.json",encoding="utf-8") as f1:
    origin_data = json.load(f1)

target = []

for sentence in origin_data:
    sentence_dict = {}
    sentence_dict["text"] = sentence["text"]
    
            #     "event_type": "组织关系-裁员",
            # "trigger": "裁员",
            # "trigger_start_index": 15,
            # "arguments": [
    t_arguments = sentence["event_list"]
    t_arguments = convert2dueeArgu(t_arguments)
    t_trigger = sentence["trigger"]
    t_trigger_index = sentence["start"]
    t_event_type = '-'.join(sentence["event_class"])
    t_class = sentence["event_class"][0]
    
    event = {"event_type":t_event_type,"trigger":t_trigger,"trigger_start_index":t_trigger_index,"arguments":t_arguments,"class":t_class}

    sentence_dict["event_list"] = []
    sentence_dict["event_list"].append(event)
    target.append(sentence_dict)
# write to formatted
with open("./formatted_event_data.json","w",encoding="utf-8") as f2:
    json.dump(target,f2,ensure_ascii=False)
