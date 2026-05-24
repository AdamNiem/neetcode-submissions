from collections import deque

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors if neighbors else []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # create adjacency list
        pre_map = {i:[] for i in range(numCourses)}
        in_degrees = [0 for i in range(numCourses)]

        # now we populate the adjacency list
        for crs, pre_req in prerequisites:
            pre_map[pre_req].append(crs)
            in_degrees[crs] += 1

        # for each course we take its pre_map and 
        # need to dfs or bfs until we reach node with no preReqs
        # and if we hit the same course twice then we know we stuck in a loop
        queue = deque() #start from course

        #start bfs from nodes with in_degree 0 aka no preReqs
        #must loop through all courses because could be disconnected graph(s)
        for course in range(numCourses):
            if in_degrees[course] == 0:
                queue.append(course)

        finished = 0

        while queue:
            course_id = queue.popleft()
            
            # get all courses this course is a pre req for
            # then append those courses to queue and decrement their in_degree
            # since we imagine the current course as "completed" and 
            # removed from graph
            finished += 1
            for subsequent_crs in pre_map[course_id]:
                in_degrees[subsequent_crs] -= 1
                #only explore courses which we already have pre req for
                if in_degrees[subsequent_crs] == 0:
                    queue.append(subsequent_crs)

        # assuming no cycles then we should be able to visit every course
        # so finished == numCourses if true

        return finished == numCourses

        