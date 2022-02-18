f = open("C:/Users/Fede/Downloads/rosalind_deg_2_dataset.txt", "r")
# lista di tutti i collegamenti
listEdge = []
for line in f:
    edge = line.split()
    listEdge.append(edge)

# lista di tutti i vertici ma duplicati
listNode = []
for nodes in listEdge:
    for node in nodes:
        listNode.append(int(node))

# lista di tutti i vertici
listVertex = list(set(listNode))
listVertex.sort()

# lista di tot zeri quanti sono i vertici
listDegreeVertex = [0] * len(listVertex)
for edge in listEdge:
    first = listVertex.index(int(edge[0]))
    second = listVertex.index(int(edge[1]))

    listDegreeVertex[first] += 1
    listDegreeVertex[second] += 1

result = ""
for degree in listDegreeVertex:
    result += str(degree) + " "

print(result)
