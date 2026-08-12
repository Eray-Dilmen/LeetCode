class Solution(object):
    def longestCommonPrefix(self, strs):
        cm_pref = ''
        for i in range(len(strs[0])):
            is_common = True
            for j in range(len(strs) - 1):
                if i < len(strs[j]) and i < len(strs[j + 1]) and strs[j][i] == strs[j + 1][i]:
                    continue
                else:
                    is_common = False
                    break

            if is_common:
                cm_pref += strs[0][i]
            else:
                break

        return cm_pref