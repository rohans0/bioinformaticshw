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

scoring_matrix_str = """
 4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
 0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
-2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
-1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
-2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
 0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
-2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
-1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
-1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
-1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
-1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
-2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
-1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
-1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
-1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
 1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
 0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
 0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
-3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
-2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7
"""
amino_acids = ' A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y'.split()
scoring_matrix = []
for line in scoring_matrix_str.split('\n'):
    if line.strip() == '': continue
    scoring_matrix.append([int(x) for x in line.split()])

def get_score_matrix(aa1, aa2) -> int:
    i = amino_acids.index(aa1.upper())
    j = amino_acids.index(aa2.upper())
    return int(scoring_matrix[i][j])

gap_penalty = -5
def align_sequences(s1, s2):
    m, n = len(s1), len(s2)

    # initialization
    table = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        table[i][0] = table[i - 1][0] + gap_penalty
    for j in range(1, n + 1):
        table[0][j] = table[0][j - 1] + gap_penalty

    # filling in table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match  = table[i - 1][j - 1]    + get_score_matrix(s1[i - 1], s2[j - 1])
            delete = table[i - 1][j]        + gap_penalty
            insert = table[i][j - 1]        + gap_penalty

            table[i][j] = max(match, delete, insert)

    return table[m][n]


if __name__ == "__main__":
    input = read_fasta('input.txt')
    print("input:   ", input)

    output = align_sequences(input[0], input[1])
    with open("output.txt", 'w') as file:
        file.write(str(output))
    print("output:  ", output)
