import json
with open("./formatted_event_data.json",encoding="utf-8") as f:
    sentences = json.load(f)
# schema for each event_type
# content type   {event_type:role_set}
event_schema = {}
for sentence in sentences:
    for event in sentence["event_list"]:
        e_type = event["event_type"]
        if e_type not in event_schema:
            event_schema[e_type] = set()
        for arg in event["arguments"]:
            event_schema[e_type].add(arg["role"])
print(event_schema)
final_schema_list =[]
for event_type,roles in event_schema.items():
    role_list = []
    class_all = event_type.split("-")
    classes = class_all[0]
    for role in roles:
        role_list.append({"role":role})
    final_schema_list.append({"event_type":event_type,"role_list":role_list,"class":classes})
print(final_schema_list)
with open("ICT_schema.json","w",encoding="utf-8") as f1:
    for schema in final_schema_list:
        f1.write(str(schema).replace("'", '"'))
        f1.write("\n")