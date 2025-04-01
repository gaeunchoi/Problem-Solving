n, m = map(int, input().split())
basket = [i+1 for i in range(n)]

for x in range(m):
    i, j = map(int, input().split())
    reversed_basket = list(reversed(basket[i-1: j]))
    basket[i-1: j] = reversed_basket

for ele in basket:
    print(ele, end = " ")