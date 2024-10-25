# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        srt_words = sorted(folder)
        output = []
        i = 0
        while i < len(srt_words):
            w = srt_words[i]
            output.append(w)
            j = i + 1
            while j < len(srt_words):
                ww = srt_words[j]
                if ww.startswith(w) and len(w) < len(ww) and ww[len(w)] == '/':
                    del srt_words[j]
                else:
                    j += 1
            i += 1
        return output