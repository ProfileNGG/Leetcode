class Solution(object):
    def wordPattern(self, pattern, word_str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = word_str.split(" ")
        if len(pattern) != len(words):
            return False

		# use two dictionaries, mapping character / string with index
        pattern_map, word_map = {}, {}
        for i in range(len(pattern)):
            if pattern_map.get(pattern[i], -1) != word_map.get(words[i], -1):
                return False
            pattern_map[pattern[i]] = word_map[words[i]] = i

        return True