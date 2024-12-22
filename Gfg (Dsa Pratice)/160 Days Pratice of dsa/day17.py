#Question : Range Minimum Query
#Link to the question: https://www.geeksforgeeks.org/problems/range-minimum-query/1

import math

def build_segment_tree(idx, l, r, segment_tree, arr):
    if l == r:
        segment_tree[idx] = arr[l]
        return segment_tree[idx]
    
    mid = l + (r - l) // 2
    left_min = build_segment_tree(2 * idx + 1, l, mid, segment_tree, arr)
    right_min = build_segment_tree(2 * idx + 2, mid + 1, r, segment_tree, arr)
    segment_tree[idx] = min(left_min, right_min)
    return segment_tree[idx]

def constructST(arr, n):
    # Allocate memory for segment tree
    height = math.ceil(math.log2(n))
    size = 2 * (2 ** height) - 1
    segment_tree = [float('inf')] * size

    # Build the segment tree
    build_segment_tree(0, 0, n - 1, segment_tree, arr)
    return segment_tree

def query_segment_tree(start, end, idx, l, r, segment_tree):
    # If the range is completely outside the current node range
    if l > end or r < start:
        return float('inf')

    # If the range is completely inside the current node range
    if l >= start and r <= end:
        return segment_tree[idx]

    # If the range is partially inside and outside the current node range
    mid = l + (r - l) // 2
    left_min = query_segment_tree(start, end, 2 * idx + 1, l, mid, segment_tree)
    right_min = query_segment_tree(start, end, 2 * idx + 2, mid + 1, r, segment_tree)
    return min(left_min, right_min)

def RMQ(segment_tree, n, qs, qe):
    return query_segment_tree(qs, qe, 0, 0, n - 1, segment_tree)

