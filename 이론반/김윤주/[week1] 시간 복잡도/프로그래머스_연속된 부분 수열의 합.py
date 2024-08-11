def solution(sequence, k):
    start = 0
    end = 0
    total = sequence[0]
    li = []
    
    while True:
        if total < k:
            end += 1
            if end > len(sequence) - 1:
                break
            total += sequence[end]
            
        elif total >= k:
            if total == k:
                li.append((start, end))
            total -= sequence[start]
            start += 1
            
            if start > len(sequence) - 1:
                break

    sorted_list = sorted(li, key=lambda x: x[1] - x[0])
    return sorted_list[0]