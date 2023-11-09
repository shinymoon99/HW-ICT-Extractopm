import os
import json
from utils.eval_edge import find_best_matching
def combine_json_files_in_folder(folder_path):
    combined_data = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    combined_data.extend(data)

    return combined_data

def json_to_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as json_file, open(output_file, 'w') as output:
            data = json.load(json_file)
            for item in data:
                output.write(json.dumps(item) + '\n')
        print(f"Conversion complete. Lines written to {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")
def read_json_file_line_by_line(filename):  
    data_list = []  
    with open(filename, 'r') as file:  
        for line in file:  
            # 将每行的json对象转换为Python字典，并添加到列表中  
            data = json.loads(line)  
            data_list.append(data)  
    return data_list  
def convertDUEE2eval(data):
    # eval data [(事件类型,对应文本)]
    eval_data = []
    for event in data["event_list"]:
        eval_event = []
        for argument in event["arguments"]:
            eval_argu = (event["event_type"],argument["role"],argument["argument"])
            eval_event.append(eval_argu)
        # trigger
        eval_event.append((event["event_type"],"触发词",event["trigger"]))
        eval_data.append(eval_event)
    return eval_data
class DedupList(list):
    """定义去重的list
    """
    def append(self, x):
        if x not in self:
            super(DedupList, self).append(x)
def evaluate(golds, preds,threshold=0):
    """评估函数，计算f1、precision、recall
    """
    ex, ey, ez = 1e-10, 1e-10, 1e-10  # 事件级别
    ep, en= 1e-10,0
    ep_sum = 1e-10
    ax, ay, az = 1e-10, 1e-10, 1e-10  # 论元级别
    
    for gold_events,pred_events in zip(golds,preds): 
        # 事件级别
        R, T = DedupList(), DedupList()
        for event in pred_events:
            if any([argu[1] == u'触发词' for argu in event]):
                R.append(list(sorted(event)))
        for event in gold_events:
            T.append(list(sorted(event)))
        for event in R:
            if event in T:
                ex += 1
        
        ey += len(R)
        ez += len(T)
        # 事件级别precision
        num,ep_single =find_best_matching(pred_events,gold_events)
        ep_sum=ep_sum+ep_single
        en=en+num
        # 论元级别
        R, T = DedupList(), DedupList()
        for event in pred_events:
            for argu in event:
                if argu[1] != u'触发词':
                    R.append(argu)
        for event in gold_events:
            for argu in event:
                if argu[1] != u'触发词':
                    T.append(argu)
        for argu in R:
            if argu in T:
                ax += 1
        ay += len(R)
        az += len(T)
    ep = ep_sum/en
    e_f1, e_pr, e_rc = 2 * ex / (ey + ez), ex / ey, ex / ez
    a_f1, a_pr, a_rc = 2 * ax / (ay + az), ax / ay, ax / az
    return ep,e_f1, e_pr, e_rc, a_f1, a_pr, a_rc

# Usage example
# input_file = 'input.json'
# output_file = 'output.txt'
# json_to_lines(input_file, output_file)

# Example usage:
# input_folder = "./path_to_folder_containing_json_files"
# combined_data = combine_json_files_in_folder(input_folder)

# Now combined_data is a list containing all dictionaries from the JSON files in the specified folder.
