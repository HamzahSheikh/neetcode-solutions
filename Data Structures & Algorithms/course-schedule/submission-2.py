class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            courses[course].append(prereq)
        
        seen = set()
        def courseSequencePossible(course) -> bool:
            
            if course in seen:
                return False
            
            if courses[course] == []:
                return True

            seen.add(course)

            for prereq in courses[course]:
                if not courseSequencePossible(prereq):
                    return False
        
            seen.remove(course)

            return True


        for course in courses:
            if not courseSequencePossible(course):
                return False

        return True

            



                