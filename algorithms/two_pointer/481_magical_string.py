'''
link: https://leetcode.com/problems/magical-string/description/?envType=problem-list-v2&envId=dsa-recursion-maze-two-pointers
'''

# time: O(n) space: O(n)
# time analysis: we generate the magical string until it reaches length n, which takes O(n)
# space analysis: we store the magical string in a list, which can grow up to O(n) in size
def magicalString(n: int) -> int:

    # [1] The starting values are always fixed: 1, 2, 2
    #     These 3 elements are self-evident initial values confirmed by the rule itself
    s = [1, 2, 2]

    # [2] head: pointer that 'reads' s (determines how many to add next)
    #     Starts at index 2 (3rd element) — first two (1, 2) are already written
    head = 2

    # [3] num: the next number to append (either 1 or 2, alternating)
    #     At the initial state, the next number to add is 1
    num = 1

    # [4] Keep expanding s using itself until length reaches n
    while len(s) < n:

        count = s[head]          # [5] Value at head = how many times to append num
        s.extend([num] * count)  # [6] Append num exactly count times
        num = 3 - num            # [7] Toggle between 1 and 2: 3-1=2, 3-2=1
        head += 1                # [8] Advance head to read the next count

    # [9] Slice the first n elements and count the number of 1s
    return s[:n].count(1)