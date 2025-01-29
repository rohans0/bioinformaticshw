def file_even_lines(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for i,line in enumerate(infile):
                if i%2==1:
                    outfile.write(line)
    except IOError as e:
        print(f"error: {e}")

file_even_lines('prob5_in.txt','prob5_out.txt')
