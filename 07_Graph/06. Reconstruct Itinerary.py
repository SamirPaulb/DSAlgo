# https://leetcode.com/problems/reconstruct-itinerary/

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        # Create a graph for each airport and keep list of airport reachable from it
        for src, dst in tickets:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]

        for src in graph.keys():
            graph[src].sort(reverse=True)
            # Sort children list in descending order so that we can pop last element 
            # instead of pop out first element which is costly operation
        stack = []
        res = []
        stack.append("JFK")
        # Start with JFK as starting airport and keep adding the next child to traverse 
        # for the last airport at the top of the stack. If we reach to an airport from where 
        # we can't go further then add it to the result. This airport should be the last to go 
        # since we can't go anywhere from here. That's why we return the reverse of the result
        # After this backtrack to the top airport in the stack and continue to traaverse it's children

        while len(stack) > 0:
            elem = stack[-1]
            if elem in graph and len(graph[elem]) > 0: 
                # Check if elem in graph as there may be a case when there is no out edge from an airport 
                # In that case it won't be present as a key in graph
                stack.append(graph[elem].pop())
            else:
                res.append(stack.pop())
                # If there is no further children to traverse then add that airport to res
                # This airport should be the last to go since we can't anywhere from this
                # That's why we return the reverse of the result
        return res[::-1]
