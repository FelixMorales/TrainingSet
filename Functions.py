import numpy as np

def Nothing(layer):
    pass

def ProductoPunto(layer):
    parent = layer.node.parents[0]
    
    y = np.zeros(len(parent.objects[0].filters))

    for i in range(len(parent.objects[0].filters)):
        y[i] = Dot((parent.objects[0].filters[i] + parent.objects[0].bias[i]), parent.objects[0].value)

    layer.value = y

def probability(layer):
    parent = layer.node.parents[0]
    sc =  parent.objects[0].value[0] #Preguntar porque y donde el nodo padre tiene un arreglo de valores
    sn = parent.objects[0].value[1]

    if parent.objects[0].label is None or parent.objects[0].label == "c":
        layer.value = np.exp(sc)/(np.exp(sc) + np.exp(sn))
    elif parent.objects[0].label == "n":
        layer.value = (np.exp(sn)/(np.exp(sc) + np.exp(sn)))

def logaritmo(layer):
    parent = layer.node.parents[0]
    layer.value = np.log(parent.objects[0].value)

## f = filter
## v = value
def Dot(f, v):

    y = f * v
    y = y.sum()
    y = y / len(f)

    return y 


def createFilterA(networkObjects):
    filters = []

    for x in range(networkObjects[2]):
        filters.append(np.zeros((networkObjects[0], networkObjects[1], 3), dtype=float))
    
    return filters

def createValueA(networkObjects):
    return np.zeros((networkObjects[0], networkObjects[1], 3), dtype=float)

def createFilterB(networkObjects):
    filters = []
    
    filters.append(np.zeros((networkObjects[0]), dtype=float))
    
    return filters
