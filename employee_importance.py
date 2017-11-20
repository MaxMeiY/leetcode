"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # Be careful of this.
        # This is WRONG. If in doubt, try it.
         #id_importance, id_sub = [(employee.importance, employee.subordinates) for employee in employees if employee.id == id]
        for employee in employees:
            if employee.id == id:
                id_importance, id_sub = employee.importance, employee.subordinates
        rest = sum(self.getImportance(employees, ID) for ID in id_sub)

        return id_importance + rest
