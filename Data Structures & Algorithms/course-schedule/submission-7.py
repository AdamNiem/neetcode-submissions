from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # gonna implement the dfs solution
        # idea is to reverse structure of pre_req_map
        
        prereq_map = {i:[] for i in range(numCourses)}

        #populate prereq map
        for crs, prereq in prerequisites:
            prereq_map[crs].append(prereq)

        #if we visit same course twice then thats a cycle
        visited = set()

        def dfs(course):
            if prereq_map[course] == []:
                # this means this course has no pre_reqs
                return True
            if course in visited:
                return False
            
            visited.add(course)

            # visit all pre_reqs for this course
            for pre_req in prereq_map[course]:
                #if the pre_req for current course has no pre_reqs (returns True)
                #then lets remove this pre_req from the current_course as if
                #we completed it already
                if dfs(pre_req):
                    prereq_map[course].remove(pre_req)
                else:
                    return False
            
            visited.remove(course)
            return True

        res = True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return res

        
        