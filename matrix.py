def matrix_chain_multiplication(dim):
    n = len(dim) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dim[i] * dim[k + 1] * dim[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k
        for i in range(len(m)):
            print(m[i])
        print('\n')
        for i in range(len(s)):
            print(s[i])
        print('\n')
    def build_parenthesis_string(s, i, j):
        if i == j:
            return f"A{i+1}"
        else:
            return "(" + build_parenthesis_string(s, i, s[i][j]) + build_parenthesis_string(s, s[i][j] + 1, j) + ")"
    optimal_parenthesis = build_parenthesis_string(s, 0, n - 1)

    return optimal_parenthesis, m[0][n - 1]

matrix = [40, 20, 30, 10, 30]
optimal_parenthesis, optimal_cost = matrix_chain_multiplication(matrix)
print("Optimal parenthesization:", optimal_parenthesis)
print("Optimal cost of parenthesization:", optimal_cost)

