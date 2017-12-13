class Solution(object):

    mapped = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
            
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def inner(inner_digits):
            if not inner_digits:
                return ""

            combos = []
            letters = self.mapped[inner_digits[0]]
            if len(inner_digits) == 1:
                return [[x] for x in letters]

            for letter in letters:
                for inner_combo in inner(inner_digits[1:]):
                    inner_combo.insert(0, letter)
                    combos.append(inner_combo)

            return combos

        return ["".join(x) for x in inner(digits)]
