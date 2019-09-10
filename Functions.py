import numpy as np
import random

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
    sc =  parent.objects[0].value[0] 
    sn = parent.objects[0].value[1]

    if parent.objects[0].label is None or parent.objects[0].label == "c":
        layer.value = np.exp(sc)/(np.exp(sc) + np.exp(sn))
    elif parent.objects[0].label == "n":
        layer.value = (np.exp(sn)/(np.exp(sc) + np.exp(sn)))

def logaritmo(layer):
    parent = layer.node.parents[0]
    layer.value = np.log(parent.objects[0].value)*-1

def probability_der(layer):
    layer.value_der = (1/layer.value)*-1

def c_filter_der(layer):
    kid = layer.node.kids[0]
    p = kid.objects[0].value
    sc = layer.value[0] 
    sn = layer.value[1]

    filter_der = np.zeros(2, dtype=float)

    if kid.objects[0].label == "c":
        filter_der[0] = p - (p*p)
        filter_der[1] = (-(p*p)*np.exp(sn))/np.exp(sc)
    else:
        filter_der[0] = (-(p*p)*np.exp(sc))/np.exp(sn)
        filter_der[1] = p - (p*p)
    
    layer.value_der = filter_der*kid.objects[0].value_der

## f = filter
## v = value
def Dot(f, v):

    y = f * v
    y = y.sum()
    y = y / len(f)

    return y 



def removeFilterNodeA(layer):
    del layer.filters[len(layer.filters) - 1]
    del layer.bias[len(layer.bias) - 1] 

    
def addFilters(layer):
        
    addFilterNodeA(layer)
    addFilterNodeB(layer.node.kids[0].objects[0])

def addFilterNodeA(layerNodeA):

    if layerNodeA.filters is not None and len(layerNodeA.filters) > 0:

            # Obtengo la estructura del tensor del filtro original y lo convierto a lista mutable
            filterShape = list(layerNodeA.filters.shape)
            
            # Aumento la cantidad de filtros (Valor de K)
            filterShape[0] += 1
            
            # Creo los nuevos filtros partiendo de los valores existentes del filtro anterior y la nueva estructura

            newFilter = np.zeros(tuple(filterShape), dtype=float)

            for i in range(len(layerNodeA.filters)):
                newFilter[i] = layerNodeA.filters[i]

            # Creo los nuevos valores random para el nuevo filtro K + 1.
            newFilter[len(newFilter) - 1] = np.random.rand(*layerNodeA.filters.shape[1:])
            
            # Repito el proceso para el Bias
            newBias = np.zeros(tuple(filterShape), dtype=float)

            for i in range(len(layerNodeA.bias)):
                newBias[i] = layerNodeA.bias[i]

            newBias[len(newBias) - 1] = np.random.rand(*layerNodeA.filters.shape[1:])

            layerNodeA.filters = newFilter
            layerNodeA.bias = newBias

def addFilterNodeB(layerNodeB):

    if layerNodeB.filters[0] is not None and len(layerNodeB.filters[0]) > 0:

        filterShape = list(layerNodeB.filters[0].shape)
        filterShape[0] += 1

        newFilter1 = np.zeros(tuple(filterShape), dtype=float)

        for i in range(len(layerNodeB.filters[0])):
            newFilter1[i] = layerNodeB.filters[0][i]
        
        newFilter1[len(newFilter1) - 1] = random.uniform(0, 1)

        newFilter2 = np.zeros(tuple(filterShape), dtype=float)

        for i in range(len(layerNodeB.filters[1])):
            newFilter2[i] = layerNodeB.filters[1][i]
        
        newFilter2[len(newFilter2) - 1] = random.uniform(0, 1)

        layerNodeB.filters = np.zeros((2, filterShape[0]), dtype=float)

        layerNodeB.filters[0] = newFilter1
        layerNodeB.filters[1] = newFilter2


        newBias1 = np.zeros(tuple(filterShape), dtype=float)

        for i in range(len(layerNodeB.bias[0])):
            newBias1[i] = layerNodeB.bias[0][i]
        
        newBias1[len(newBias1) - 1] = random.uniform(0, 1)

        newBias2 = np.zeros(tuple(filterShape), dtype=float)

        for i in range(len(layerNodeB.bias[1])):
            newBias2[i] = layerNodeB.bias[1][i]
        
        newBias2[len(newBias2) - 1] = random.uniform(0, 1)

        layerNodeB.bias = np.zeros((2, filterShape[0]), dtype=float)
        
        layerNodeB.bias[0] = newBias1
        layerNodeB.bias[1] = newBias2


def createFilterA(networkObjects):

    filters = np.random.rand(networkObjects[2],networkObjects[0], networkObjects[1], 3)
    return filters

def createValueA(networkObjects):

    return np.random.rand(networkObjects[0], networkObjects[1], 3)

def createFilterB(networkObjects):

    filters = np.random.rand(2, networkObjects[2])

    return filters
