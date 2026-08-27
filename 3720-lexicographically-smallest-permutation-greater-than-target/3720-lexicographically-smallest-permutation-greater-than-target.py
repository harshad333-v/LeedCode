class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for ch in target:
            freq[ord(ch) - ord('a')] -= 1

        for i in range(len(target) - 1, -1, -1):
            idx = ord(target[i]) - ord('a')
            freq[idx] += 1

            if any(x < 0 for x in freq):
                continue

            next_char = -1
            for c in range(idx + 1, 26):
                if freq[c]:
                    next_char = c
                    break

            if next_char == -1:
                continue

            freq[next_char] -= 1
            result = list(target[:i])
            result.append(chr(next_char + ord('a')))

            for c in range(26):
                result.extend(chr(c + ord('a')) * freq[c])

            return ''.join(result)

        return ""

        