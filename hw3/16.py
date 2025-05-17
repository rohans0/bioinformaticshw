def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            if line.startswith('>'):
                continue
            else:
                sequence += line.strip()
        if sequence:
            sequences.append(sequence)
    return sequences

def spell_string(input) -> str:
    if input is None : return ''
    out = input[0]

    for str in input[1:]:
        if str is None:
            return ''
        out += str[-1]
        print(out)

    return out


if __name__ == "__main__":
    input = []
    with open("input.txt", 'r') as file:
        for line in file:
            input.append(line.strip())

    print(input)

    output = spell_string(input)
    with open("output.txt", 'w') as file:
        file.write(output)
