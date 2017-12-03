class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people_dict, height, res = {}, [], []
        for index in range(len(people)):
            i = people[index]
            if i[0] in people_dict:
                people_dict[i[0]].append((i[1], index))
            else:
                people_dict[i[0]] = [(i[1], index)]
                height.append(i[0])
        height.sort()
        for i in height[::-1]:
            people_dict[i].sort()
            for j in people_dict[i]:
                res.insert(j[0], people[j[1]])

        return res
            