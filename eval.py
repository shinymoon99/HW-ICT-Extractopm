from utils.eval_edge import find_best_matching
from utils.util import convertDUEE2eval,evaluate,read_json_file_line_by_line
def remove_elements_by_indices(input_list, indices_to_remove):
    # Example usage:
# my_list = [10, 20, 30, 40, 50]
# indices_to_remove = [1, 3]  # Indices of elements to remove

# result_list = remove_elements_by_indices(my_list, indices_to_remove)
# print(result_list)  # The updated list with elements removed based on indices
    # Create a new list that excludes elements at the specified indices
    output_list = [element for index, element in enumerate(input_list) if index not in indices_to_remove]
    return output_list

nums = [19,20,30]

# read gold and test data
gold_data = read_json_file_line_by_line("./datasets/ICT_v3/evaltest/test.json")
test_data = read_json_file_line_by_line("./datasets/ICT_v3/test_pred2.json")
gold_data = remove_elements_by_indices(gold_data,nums)
test_data = remove_elements_by_indices(test_data,nums)

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