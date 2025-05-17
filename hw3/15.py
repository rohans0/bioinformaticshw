import itertools

def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                    sequence = ''
            else:
                sequence += line.strip()
        if sequence:
            sequences.append(sequence)
    return sequences

def overlap(a, b):
    start = 0
    while True:
        start = a.find(b[:3], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

def shortest_superstring(reads):
    while len(reads) > 1:
        max_overlap = -1
        a, b = None, None

        for pair in itertools.permutations(reads, 2):
            current_overlap = overlap(pair[0], pair[1])
            if current_overlap > max_overlap:
                max_overlap = current_overlap
                a, b = pair

        reads.remove(a)
        reads.remove(b)
        reads.append(a + b[max_overlap:])
    return reads[0]

if __name__ == "__main__":
    file_path = "input.txt"
    reads = read_fasta(file_path)

    result = shortest_superstring(reads)
    with open("output.txt", 'w') as file:
        file.write(result)
