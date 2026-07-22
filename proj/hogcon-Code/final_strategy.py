"""
    This file contains your final_strategy that will be submitted to the contest.

    You can only depend on "general-purpose" libraries - do not import or open any
    contest-specific files, like other Python or text files. All contest logic must
    be in this file.

    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""

PLAYER_NAME = '头顶尖尖的'  # Change this line!


def final_strategy(score, opponent_score):
    if score>opponent_score:
        return 6
    else:
        return 7

