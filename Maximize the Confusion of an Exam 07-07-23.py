class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = 0
        count = 0
        T_offset = 0
        p1 = 0
        p2 = 0
        while p2 < len(answerKey):
            if answerKey[p2] == 'T':
                count += 1
            elif answerKey[p2] == 'F':
                T_offset += 1
                while T_offset > k:
                    if answerKey[p1] == 'F':
                        T_offset -= 1
                    count -= 1
                    p1 += 1
                count += 1
            res = max(res, count)
            p2 += 1
        # res = max(res, count)
        # print("T", res)
        T_offset = 0
        count = 0
        p1 = 0
        p2 = 0
        while p2 < len(answerKey):
            if answerKey[p2] == 'F':
                count += 1
            elif answerKey[p2] == 'T':
                T_offset += 1
                while T_offset > k:
                    if answerKey[p1] == 'T':
                        T_offset -= 1
                    count -= 1
                    p1 += 1
                count += 1
            res = max(res, count)
            p2 += 1
        # res = max(res, count)
        return res



                
