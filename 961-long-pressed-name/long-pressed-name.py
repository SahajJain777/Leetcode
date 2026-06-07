class Solution(object):
    def isLongPressedName(self, name, typed):
        np = 0
        tp = 0

        while tp < len(typed):
            if np < len(name) and typed[tp] == name[np]:
                np += 1
                tp += 1

            elif tp > 0 and typed[tp] == typed[tp - 1]:
                tp += 1

            else:
                return False

        return np == len(name)