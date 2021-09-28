class SaveSeries: 
    def __init__(self, results):
        self.data = results

    def openFile(self, baseName, name):
        name = '{}_{}_{}'.format(baseName, name, self.data["type"])
        name += ".txt" if self.data["q"] == False else '_q={}.txt'.format(self.data["q"])
        return open(name, "w+")

    def saveA(self,baseName, name="A"):
        file = self.openFile(baseName, name)
        for row in self.data["A"]:
            for result in row:
                file.write('{}, {}\n'.format(str(result[0]), str(result[1])))
        file.close()

    def saveGraphInd(self, baseName, name="graph_indicator"):
        file = self.openFile(baseName, name)
        for graphInd in self.data["graph_indicator"]:
            file.write('{}\n'.format(str(graphInd)))
        file.close()
    
    def saveEdge(self, baseName, name="edge_attributes"):
        file = self.openFile(baseName, name)
        for row in self.data["edge_attributes"]:
            for edge in row:
                file.write('{}\n'.format(str(edge)))
        file.close()
    
    def saveNode(self, baseName, name="node_labels"):
        file = self.openFile(baseName, name)
        for node in self.data["node_labels"]:
            file.write('{}\n'.format(str(node)))
        file.close()


    def saveAllTxt(
    self,
    baseName     =          "output",
    AName        =               "A", 
    graphIndName = "graph_indicator",
    edgeName     = "edge_attributes",
    nodeName     =     "node_labels"
    ):
        if AName != False:
            self.saveA(baseName, AName)
        if graphIndName != False:
            self.saveGraphInd(baseName, graphIndName)
        if edgeName != False and self.data["q"]:
            self.saveEdge(baseName, edgeName)
        if nodeName !=False:
            self.saveNode(baseName, nodeName)
        

