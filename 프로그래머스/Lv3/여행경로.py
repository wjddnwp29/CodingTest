t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
g = dict()
for (a,b) in t:
    if a not in g:
        g[a] = []
    g[a].append([b,False])
    
for k in g:
    g[k].sort()

arr = []
def dfs(node):
    arr.append(node)
    if len(arr) == len(t) + 1:
        return True
    if node in g:
        for i in g[node]:
            if i[1] == False:
                i[1] = True
                if dfs(i[0]):
                    return True
                i[1] = False
dfs("ICN")
print(arr)
            
            