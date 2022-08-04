#you need to add a list of words to compare with to complete this spellchecker (it's possible to just paste it in the ''):
dictionary = 'word list'.split()

def levenshtein(a, b):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    matrix = [[0] * (len(b) + 1) for _ in range(2)]
    for j in range(len(b) + 1):
        matrix[0][j] = j
    for i in range(1, len(a) + 1):
        matrix[1][0] = i
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                matrix[1][j] = matrix[0][j - 1]
            else:
                matrix[1][j] = min(matrix[0][j-1], matrix[0][j], matrix[1][j-1]) + 1
        matrix[0] = matrix[1].copy()
    else:
        return matrix[1][j]

numrecords = 10
def add_to_list(entry, best):
    best.append(entry)
    best.sort(key=lambda x: x[1])
    best = best[:numrecords]
    return best

def main():
    word = input("What word do you want to check? ")
    best = []
    for entry in dictionary:
        best = add_to_list((entry, levenshtein(word, entry)), best)

    for answer, distance in best:
        print(word, '-', answer + ':', distance)
    

if __name__ == "__main__":
    main()
