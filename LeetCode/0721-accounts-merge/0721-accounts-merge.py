class DisjointSet:
    def __init__(self, emails: List[Tuple[str, str]]):
        self.n = len(emails)
        self.size = {e: 1 for e in emails}
        self.parent = {e: e for e in emails}
    
    def find(self, node: Tuple[str, str]) -> Tuple[str, str]:
        par = self.parent[node]
        if par == node:
            return node
        else:
            res = self.find(par)
            self.parent[node] = res
            return res

    def union(self, node1: Tuple[str, str], node2: Tuple[str, str]):
        node1 = self.find(node1)
        node2 = self.find(node2)
        if node1 != node2:
            if self.size[node1] >= self.size[node2]:
                self.parent[node2] = node1
                self.size[node1] += self.size[node2]
            else:
                self.parent[node1] = node2
                self.size[node2] += self.size[node1]
    
    def roots(self) -> List[Tuple[str, str]]:
        rootList = []
        for par in self.parent:
            if self.parent[par] == par:
                rootList.append(par)
        return rootList

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = set()
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                emails.add((email, name))
    
        dset = DisjointSet(emails)
        for account in accounts:
            name = account[0]
            emailList = account[1:]
            for i in range(len(emailList) - 1):
                node1 = (emailList[i], name)
                node2 = (emailList[i+1], name)
                dset.union(node1, node2)
        
        rootList = dset.roots()
        modAcc = {root: [] for root in rootList}
        for node in dset.parent:
            root = dset.find(node)
            modAcc[root].append(node)
        
        res = []
        for emailList in modAcc.values():
            resEmailList = []
            for email, name in emailList:
                resEmailList.append(email)
            resEmailList = sorted(resEmailList)
            res.append([name] + resEmailList)
        
        return res