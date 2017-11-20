class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        all_cap = True
        all_not_cap = True
        first_cap = True
        rest_lower = True

        if word[0].islower():
            first_cap = False
            all_cap = False

        for w in word[1:]:
            if w.islower():
                all_cap = False
            else:
                all_not_cap = False
                rest_lower = False
        return all_cap or all_not_cap or (first_cap and len(word) > 1 and rest_lower)