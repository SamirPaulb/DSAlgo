# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# https://www.youtube.com/watch?v=1XkMFNvkouo

import collections

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        res = 2**31  # Initialize result with a large number (acts like infinity)

        # Try starting BFS from every node (since we can start anywhere)
        for i in range(n):
            # Bitmask to represent which nodes have been visited so far.
            # Each bit corresponds to a node. Start with only the i-th node visited.
            curPathState = 1 << i

            # Queue will store tuples of (current node, visited mask, path length)
            q = collections.deque([(i, curPathState, 0)])

            # 'visited' keeps track of (node, mask) pairs we've already explored
            # to avoid revisiting the same state and causing redundant BFS steps.
            visited = set()

            ans = 2**n  # Local minimum path length for this starting node

            # Standard BFS traversal
            while q:
                curNode, curPathState, pathLen = q.popleft()

                # If we've visited all nodes (mask == 111... for n bits)
                if curPathState == (1 << n) - 1:
                    ans = min(ans, pathLen)
                    continue  # We found one complete path; continue checking others (optional)

                # Skip if this state was already processed
                if (curNode, curPathState) in visited:
                    continue
                visited.add((curNode, curPathState))

                # Explore all connected neighbors
                for childNode in graph[curNode]:
                    # Update the bitmask to mark the neighbor as visited
                    childPathState = curPathState | (1 << childNode)
                    # Push new state into the queue with increased path length
                    q.append((childNode, childPathState, pathLen + 1))

            # Keep the shortest overall path found among all starting nodes
            res = min(res, ans)

        return res


# Time Complexity: O(n × 2^n)
# Space Complexity: O(n × 2^n)
