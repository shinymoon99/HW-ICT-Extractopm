import json

with open("datasets\ICT_all_formatted.json",encoding="utf-8") as f:
    data =json.load(f)
eventtype_cnt = {}
for sentence in data:
    etype =sentence["event_list"][0]["event_type"]
    if etype not in eventtype_cnt:
        eventtype_cnt[etype]=1
    else:
        eventtype_cnt[etype]+=1
# Sorting the dictionary by values in ascending order
sorted_dict = dict(sorted(eventtype_cnt.items(), key=lambda item: item[1],reverse=True))

print(sorted_dict)
with open("data_count.json","w",encoding="utf-8") as f1:
    json.dump(sorted_dict,f1,ensure_ascii=False)