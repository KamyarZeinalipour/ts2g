class Calculate():
    # data must be in python list
    def __init__(self, data):
        self.data = data
        self.last = 0

    def hgInRow(self, rowNum):
        result = []
        row = self.data[rowNum-1]
        rowLen = len(row)
        for i in range(1, rowLen):
            alpha = 1
            # save somthing in the row!
            result.append([i+self.last, i+1+self.last])
            result.append([i+1+self.last, i+self.last])

            for j in range(2, rowLen-i+1):
                criterio = row[i+alpha-1]
                pendiente = row[i+j-1]
                if (criterio >= row[i-1]):
                    break
                elif (criterio < pendiente):
                    result.append([i+self.last, i+j+self.last])
                    result.append([i+j+self.last, i+self.last])
                    alpha = j
        self.last = max(max(result))
        return result

    def vgInRow(self, rowNum):
        result = []
        row = self.data[rowNum-1]
        rowLen = len(row)
        for i in range(1, rowLen):
            # save somthing in the row!
            result.append([i+self.last, i+1+self.last])
            result.append([i+1+self.last, i+self.last])

            criterio = row[i+1-1] - row[i-1]

            for j in range(2, rowLen-i+1):

                pendiente = (row[i+j-1] - row[i-1]) / j

                if(criterio < pendiente):
                    result.append([i+self.last, i+j+self.last])
                    result.append([i+j+self.last, i+self.last])

                    criterio = pendiente
        self.last = max(max(result))
        return result

    def qgInRow(self, rowNum, q):
        result = []
        graphInd = []
        row = self.data[rowNum-1]
        rowLen = len(row)
        Q = []
        v = [i for i in row]
        vStOrdQuantiles = []
        vQuantiles = [0 for i in range(0, rowLen)]
        MA = [[0 for i in range(0, q)] for j in range(0, q)]
        W = [[0 for i in range(0, q)] for j in range(0, q)]
        sum = 0

        for j in range(0, rowLen):
            for i in range(0, rowLen-1):
                if v[i] > v[i+1]:
                    v[i], v[i+1] = v[i+1], v[i]

        for i in range(0, q+1):
            Q += [int(((rowLen*i)/q))]

        for i in range(0, q):
            for j in range(Q[i], Q[i+1]):
                vStOrdQuantiles += [[v[j], i+1]]

        for j in range(0, rowLen):
            for i in range(0, rowLen):
                if(row[j] == vStOrdQuantiles[i][0]):
                    vQuantiles[j] = int(vStOrdQuantiles[i][1]-1)
                    vStOrdQuantiles[i][0] = 1000000000000
                    break

        for i in range(0, rowLen - 1):
            MA[vQuantiles[i]][vQuantiles[i+1]] = MA[vQuantiles[i]][vQuantiles[i+1]]+1

        for i in range(0, q):
            sum = 0
            for j in range(0, q):
                sum += MA[i][j]
            for j in range(0, q):
                W[i][j] = MA[i][j]/sum

        for i in range(0, q):
            for j in range(0, q):
                if W[i][j] != 0:
                    result.append([i+1+self.last, j+1+self.last])
                    graphInd.append(W[i][j])
        self.last = max(max(result))
        return result, graphInd
    
    def graphInd(self, q=False):
        graphIndList = []
        if q != False:
            for i in range(0, len(self.data)):
                for j in range(0, q):
                    graphIndList.append(i+1)
        else:
            for i in range(0, len(self.data)):
                for j in range(0, len(self.data[i])):
                    graphIndList.append(i+1)
        return graphIndList

    def nodeLabels(self, q=False):
        nodeLabelsList = []
        if q != False:
            for row in self.data:
                for i in range(0, q):
                    nodeLabelsList.append(i+1)
        else:
            for row in self.data:
                for i in range(0, len(row)):
                    nodeLabelsList.append(i+1)
        
        return nodeLabelsList

    def hg(self):
        result = []
        for i in range(1, len(self.data)+1):
            result.append(self.hgInRow(i))
        return {
            "A": result,
            "graph_indicator": self.graphInd(),
            "node_labels": self.nodeLabels(),
            "q": False,
            "type": "hg"
        }
    
    def vg(self):
        result = []
        for i in range(1, len(self.data)+1):
            result.append(self.vgInRow(i))
        return {
            "A": result,
            "graph_indicator": self.graphInd(),
            "node_labels": self.nodeLabels(),
            "q": False,
            "type": "vg"
        }


    def qg(self, q):
        result = []
        edgeAttr = []
        for i in range(1, len(self.data)+1):
            res = self.qgInRow(i, q)
            result.append(res[0])
            edgeAttr.append(res[1])
        return {
            "A": result,
            "graph_indicator": self.graphInd(q),
            "node_labels": self.nodeLabels(q),
            "edge_attributes": edgeAttr,
            "q": q,
            "type": "qg"
        }


