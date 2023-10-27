def binary_search_best(ls: List[int], k:int) -> int:
    """Binary search function to return the closest if exact value is not found
    Runtime complexity : O(log N)
    Space complexity : O(1)
    Parameters
    ----------
    ls : List[int]
        Input list of int 
    k : int
        Int to search

    Returns
    -------
    int
        Index of equal or closest element to k in ls
    """
    lo, hi = 0, len(ls)-1
    best = lo
    while lo <= hi:
        mid = lo + (hi-lo)//2
        if ls[mid] < k:
            lo = mid+1
        elif ls[mid] > k:
            hi = mid - 1
        else:
            best = mid
            break
    if abs(ls[best]-k) < abs(ls[mid]-k):
        best = mid
    return best