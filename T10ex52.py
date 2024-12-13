def indexParaula(paraula):
    l = ["gorra", "camiseta", "calcetines", "Joan"]
    try:
        index = l.index(paraula)
        return index
    except ValueError:
        return -1
    
print(indexParaula("camiseta"))
print(indexParaula("calcetines"))
    