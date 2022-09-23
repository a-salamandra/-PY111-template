from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    stairway.append(0)

    for i in range(len(stairway)-3,-1,-1):
        stairway[i] = min(stairway[i] + stairway[i+1], stairway[i] + stairway[i+2])

    print(stairway)
    return min(stairway[0], stairway[1])
