from ts2g import save, calculate, read

# export files in .txt
def save(result, name):
    return save.SaveSeries(result).saveAllTxt(name)


def qg(data, q):
    return calculate.Calculate(data).qg(q)


def hg(data):
    return calculate.Calculate(data).hg()


def vg(data):
    return calculate.Calculate(data).vg()


def importData(fileName):
    return read.ReadSeries(fileName).dataInList()
