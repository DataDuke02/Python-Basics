def ArrayChallenge(strArr):
    # __define-ocg__ checking whether a valid binary tree can be formed

    parent_map = {}
    varFiltersCg = {}
    varOcg = set()

    for pair in strArr:
        pair = pair.strip("()")
        child, parent = map(int, pair.split(","))

        # A child cannot have more than one parent
        if child in parent_map:
            return "false"

        parent_map[child] = parent

        # Count children for each parent
        if parent not in varFiltersCg:
            varFiltersCg[parent] = 0

        varFiltersCg[parent] += 1

        # A parent cannot have more than two children
        if varFiltersCg[parent] > 2:
            return "false"

        varOcg.add(child)
        varOcg.add(parent)

    # Find the root nodes
    roots = varOcg - set(parent_map.keys())

    # There must be exactly one root
    if len(roots) != 1:
        return "false"

    return "true"


# Example
print(ArrayChallenge(["(1,2)", "(2,4)", "(7,2)"]))
