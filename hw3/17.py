def lcs(s1, s2):
    m, n = len(s1), len(s2)

    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        s1 = next(file).strip()
        s2 = next(file).strip()

    output = lcs(s1, s2)
    with open("output.txt", 'w') as file:
        file.write(output)
