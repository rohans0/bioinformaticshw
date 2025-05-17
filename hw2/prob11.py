import re

# return all substrings of length in string as list
def all_substrings(string:str, length:int) -> list[str]:
    if len(string) < length : return []
    i = 0
    out = []
    while i + length <= len(string):
        out.append(string[i:i+length])
        i+=1

    return out

# return shared_motif from list of strings
def shared_motif(dataset:list[str]) -> str :
    # empty or single element dataset check
    if   len(dataset) <= 0 : return ''
    elif len(dataset) == 1 : return dataset[0]

    # take shortest string out of dataset
    shortest = min(dataset, key=len)
    dataset.remove(shortest)

    # work downward from length of shortest string to 1
    curr_substr_length=len(shortest)
    while curr_substr_length > 0:
        # check every substr at curr length
        for substr in all_substrings(shortest,curr_substr_length):
            # check every string in dataset
            for i in range(0,len(dataset)):
                if dataset[i].find(substr) == -1:
                    break
                # if got to the last one without fail, success
                if i == len(dataset)-1:
                    return substr

        # otherwise decrease the curr substr length
        curr_substr_length-=1

    return ''

import re
def load_data_file(path:str) -> list[str]:
    with open(path) as file:
        string = file.read().replace('\n','')
        list = re.split(r">Rosalind_\d{4}",string)
        list.remove('')
        return list


dataset = load_data_file('12data.txt')

print(f"{shared_motif(dataset)}")
