class Solution:
    def groupStrings(self, strings):
        groups = {}

        for s in strings:
            key = []

            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1])) % 26
                key.append(diff)

            key = tuple(key)

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())
