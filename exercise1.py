def merge(xs, ys):
    i = j = 0
    result = []

    while i < len(xs) and j < len(ys):
        if xs[i] < ys[j]:
            result.append(xs[i])
            i += 1
        else:
            result.append(ys[j])
            j += 1

    result.extend(xs[i:])
    result.extend(ys[j:])

    return result 


def msort(xs):
    mid  = len(xs) // 2

    if len(xs) <= 1:
        return xs
    
    left_half = msort(xs[:mid])
    right_half = msort(xs[mid:])

    return merge(left_half, right_half)

# print(msort([7, 3, 1, 2, 4, 5, 6, 3, 2, 5, 6, 1]))