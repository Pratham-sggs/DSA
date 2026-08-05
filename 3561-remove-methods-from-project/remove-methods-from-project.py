class Solution:
    def all_suspicious(self, graph, suspicious_set, idx):
        if idx in suspicious_set:
            return
        suspicious_set.add(idx)
        for i in graph[idx]:
            self.all_suspicious(graph, suspicious_set, i)
        return
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = []
        for i in range(n):
            graph.append([])
        for u, v in invocations:
            graph[u].append(v)
        suspicious_set = set()
        self.all_suspicious(graph, suspicious_set, k)
        if len(suspicious_set) == n:
            return []
        ans = []
        for i in range(n):
            if i not in suspicious_set:
                for k in graph[i]:
                    if k in suspicious_set:
                        return [i for i in range(n)]
                else:
                    ans.append(i)
        return ans
            