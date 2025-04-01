# A[p...r]을 오름차순 정렬
def merge_sort(A, p, r):
    if p < r and cnt <= K:
        q = (p + r) // 2
        merge_sort(A, p, q);
        merge_sort(A, q+1, r);
        merge(A, p, q, r);

# A[p...q]와 A[q+1...r]을 병합하여 A[p...r]을 오름차순 정렬된 상태로 만든다
# A[p...q]와 A[q+1...r]은 이미 오름차순 정렬 완료
def merge(A, p, q, r):
    global cnt, result

    i, j = p, q+1
    tmp = []

    while i <= q and j <= r:
        if A[i]  <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:
        tmp.append(A[i])
        i += 1

    while j <= r:
        tmp.append(A[j])
        j += 1

    i, t = p, 0;
    while i <= r:
        A[i] = tmp[t]
        cnt += 1

        if cnt == K:
            result = A[i]
            break;
        i, t = i+1, t+1

A, K = map(int, input().split())
nums = list(map(int, input().split()))
cnt, result = 0, -1
merge_sort(nums, 0, A-1)
print(result)