def two_sum(ls: List[int], target: int) -> bool:
    hash_map = {}
    for l in ls:
        if (target-l) in hash_map:
            return True
        hash_map[l] = l
    return False