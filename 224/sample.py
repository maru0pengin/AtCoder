# def make_combination(input_list):
#     def rec(n):
#         nonlocal S_list
#         nonlocal combinations_list
#         if n == len(input_list):
#             print(S_list)
#             combinations_list.append(list(S_list))
#             return
#         # ①の分岐生成
#         rec(n + 1)
#         # ②の分岐生成
#         S_list[n] = 1
#         rec(n + 1)
#         S_list[n] = 0
#     combinations_list = []
#     S_list = [0 for i in range(len(input_list))]
#     rec(0)
#     return combinations_list


# input_list = [[0, 1], [1, 3], [1, 1], [-1, -1]]
# combibations_list = make_combination(input_list)
# print(combibations_list)

# n=5の時の組み合わせ
def comb(n):
    A = [0]*n
    select(0, A)


def select(i, A):
    if i == n:
        print(A)
        return
    select(i+1, A)
    A[i] = 1  # A[i]を選択
    select(i+1, A)
    A[i] = 0  # A[i]を選択しない


n = 5
comb(n)
