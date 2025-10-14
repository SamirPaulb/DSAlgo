# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/description/

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)  # Important: Assign large jobs first
        worker = [0] * k
        self.ans = sum(jobs)  # Worst case: all jobs on one worker

        def dfs(i):
            if i == len(jobs):
                self.ans = min(self.ans, max(worker))
                return

            visited = set()
            for j in range(k):
                if worker[j] in visited:
                    # Multiple workers can have the same workload, and assigning a job to any of them would result in equivalent recursive states.
                    # So, if two workers have the same current total time, there's no need to try both — trying one of them is enough.
                    continue
                if worker[j] + jobs[i] >= self.ans:
                    continue  # Prune: worse than best found so far

                visited.add(worker[j])
                worker[j] += jobs[i]

                dfs(i + 1)

                worker[j] -= jobs[i]

        dfs(0)
        return self.ans
