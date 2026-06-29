class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # len1 = len(word1)
        # len2 = len(word2)

        # ptr1 = 0
        # ptr2 = 0

        # merged = []

        # word = 1
        # while ptr1<len1 and ptr2<len2:
        #     if word == 1:
        #         merged.append(word1[ptr1])
        #         ptr1 += 1
        #         word = 2
        #     else:
        #         merged.append(word2[ptr2])
        #         ptr2 += 1
        #         word = 1

        # while ptr1<len1:
        #     merged.append(word1[ptr1])
        #     ptr1 += 1

        # while ptr2<len2:
        #     merged.append(word2[ptr2])
        #     ptr2 += 1

        # return ''.join(merged)

        result = []
        shorter_length = min(len(word1), len(word2))

        # Step 1: interleave characters while both strings still have letters
        for i in range(shorter_length):
            result.append(word1[i])
            result.append(word2[i])

        # Step 2: append whatever is left over from the longer string
        # (only ONE of these two lines will actually add anything)
        result.append(word1[shorter_length:])
        result.append(word2[shorter_length:])

        return ''.join(result)


            
        