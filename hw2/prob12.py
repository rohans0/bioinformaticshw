import re
def load_data_file(path:str) -> list[str]:
    with open(path) as file:
        string = file.read().replace('\n','')
        list = re.split(r">Rosalind_\d{4}",string)
        list.remove('')
        return list

def motif_finding()

dataset = load_data_file('12data.txt')

print(dataset)


