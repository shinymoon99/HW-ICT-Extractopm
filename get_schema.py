import json
with open("./datasets/selected_5r/ICT_all_formatted.json",encoding="utf-8") as f:
    sentences = json.load(f)
# schema for each event_type
# content type   {event_type:role_set}
event_schema = {}
for sentence in sentences:
    for event in sentence["event_list"]:
        event_type = event["event_type"].split("-")[1]
        class_all = ""
        e_type = event_type
        if e_type not in event_schema:
            event_schema[e_type] = set()
        for arg in event["arguments"]:
            event_schema[e_type].add(arg["role"])
print(event_schema)
final_schema_list =[]
for event_type,roles in event_schema.items():
    role_list = []
    class_all = event_type
    classes = event_type
    for role in roles:
        role_list.append({"role":role})
    if event_type in ['配置','点击','选择','查看','创建']:
        final_schema_list.append({"event_type":event_type,"role_list":role_list,"class":classes})
sorted_list = sorted(final_schema_list, key=lambda x: x['event_type'])
print(final_schema_list)
with open("./datasets/selected_5r/ICT_schema.json","w",encoding="utf-8") as f1:
    for schema in final_schema_list:
        f1.write(str(schema).replace("'", '"'))
        f1.write("\n")