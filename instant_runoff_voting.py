"""
Solution for "Instant Runoff Voting" kata:
https://www.codewars.com/kata/52996b5c99fdcb5f20000004/train/python
"""


def count_votes(voters):
    candidates = dict()

    for voter in voters:
        if len(voter):
            vote = voter[0]
            if vote in candidates:
                candidates[vote] += 1
            else:
                candidates[vote] = 1

    return candidates


def get_top_candidate(candidates):
    sorted_candidates = sorted(candidates.iteritems(), key=lambda x: x[1], reverse=True)
    return sorted_candidates[0]


def get_tie_candidate(candidates):
    sorted_candidates = sorted(candidates.iteritems(), key=lambda x: x[1])
    return sorted_candidates[0]


def get_tie_candidates(candidates):
    return [x for x in candidates.iteritems() if x[1] == get_tie_candidate(candidates)[1]]


def remove_tie_candidates(candidates, voters):
    tie_candidates = get_tie_candidates(candidates)

    for tie_candidate in tie_candidates:
        for voter in voters:
            voter.remove(tie_candidate[0])


def check_winner(candidate, total_votes):
    return candidate[1] > total_votes / 2


def runoff(voters):
    total_voters = len(voters)

    while any(voters):
        candidates = count_votes(voters)
        top = get_top_candidate(candidates)
        if check_winner(top, total_voters):
            return top[0]
        else:
            remove_tie_candidates(candidates, voters)

    return None


voters = [["dem", "ind", "rep"],
          ["rep", "ind", "dem"],
          ["ind", "dem", "rep"],
          ["ind", "rep", "dem"]]
#
print(runoff(voters))  # "ind"

voters = [["a", "c", "d", "e", "b"],
         ["e", "b", "d", "c", "a"],
         ["d", "e", "c", "a", "b"],
         ["c", "e", "d", "b", "a"],
         ["b", "e", "a", "c", "d"]]

print(runoff(voters))  # None

# failed test
# [
#     ['a', 'c', 'b', 'd', 'e'],
#     ['d', 'c', 'a', 'b', 'e'],
#     ['e', 'b', 'd', 'a', 'c'],
#     ['e', 'a', 'b', 'c', 'd'],
#     ['b', 'c', 'e', 'a', 'd']
# ]
