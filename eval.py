from utils.eval_edge import find_best_matching
from utils.util import convertDUEE2eval,evaluate,read_json_file_line_by_line
# read gold and test data
gold_data = read_json_file_line_by_line("./datasets/ICT_v2/ICT_test_new1.json")
test_data = read_json_file_line_by_line("./datasets/ICT_v2/ICT_test_pred1.json")
eval_gold = []
eval_pred = []
for g,t in zip(gold_data,test_data):
    eg=convertDUEE2eval(g)
    ep=convertDUEE2eval(t)
    eval_gold.append(eg)
    eval_pred.append(ep)
# use evaluate function to calculate
ep,e_f1, e_pr, e_rc, a_f1, a_pr, a_rc =evaluate(eval_gold,eval_pred)
print(ep,a_pr,e_rc,a_rc)