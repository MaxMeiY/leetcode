class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        mapping = {}
        for path in paths:
            data = path.split()
            root = data[0]
            for file in data[1:]:
                name, _, content = file.partition('(')
                if content[:-1] in mapping:
                    mapping[content[:-1]].append(root+'/'+name)
                else:
                    mapping[content[:-1]] = [root+'/'+name]
        return [mapping[i] for i in mapping if len(mapping[i]) > 1]
