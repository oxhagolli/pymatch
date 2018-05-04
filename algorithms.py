"""
Author: Orens Xhagolli
"""


def gale_shapley(preferences):
    """
    Get a stable matching M.
    :param preferences: tuple of 2 nxn matrices that contain preferences for each side
    :return: A stable matching in form of a list of tuples (m, w)
    """
    men = [None for _ in range(len(preferences[0]))]
    women = men[:]
    while None in men:
        m_index = men.index(None)
        w_index = preferences[0][m_index].pop(0)
        if women[w_index] is None:
            men[m_index] = w_index
            women[w_index] = m_index
        else:
            if preferences[1][w_index].index(m_index) < preferences[1][w_index].index(women[w_index]):
                men[women[w_index]] = None
                men[m_index] = w_index
                women[w_index] = m_index
    return list(enumerate(men))


print(gale_shapley([[[0, 1, 2, 3, 4], [1, 2, 3, 0, 4], [2, 3, 0, 1, 4], [3, 0, 1, 2, 4], [0, 1, 2, 3, 4]],
                    [[1, 2, 3, 4, 0], [2, 3, 4, 0, 1], [3, 4, 0, 1, 2], [4, 0, 1, 2, 3], [0, 1, 2, 3, 4]]]))
