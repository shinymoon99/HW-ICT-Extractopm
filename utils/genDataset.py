def combine_txt_files(input_files, output_file):
    # Example usage:
    # input_files = ['click_SL.txt', 'create_SL.txt', 'configure_SL.txt','view_SL.txt']
    # path_to_dir = './datasets/selected_4/'
    # input_files = [path_to_dir+x for x in input_files]
    # output_file = './datasets/selected_4/first_v/train.txt'
    # combine_txt_files(input_files, output_file)
    try:
        with open(output_file, 'w') as output:
            for input_file in input_files:
                with open(input_file, 'r') as input:
                    output.write(input.read())
                output.write("\n")
        print(f"Combined {len(input_files)} files into {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")




if __name__=="__main__":
    input_files = ['click_SL.txt', 'create_SL.txt', 'configure_SL.txt','view_SL.txt']
    path_to_dir = './datasets/selected_4/'
    input_files = [path_to_dir+x for x in input_files]
    output_file = './datasets/selected_4/first_v/train.txt'
    combine_txt_files(input_files, output_file)