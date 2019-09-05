import Network as nw
import Functions

def Propagation(layer):

    for parent in layer.node.parents:
        layerParent = parent.objects[0]
        Propagation(layerParent)

    layer.propagate(layer)
 
def BackPropagation(layer):
    
    for parent in layer.node.parents:
        layerParent = parent.objects[0]
        BackPropagation(layerParent)

    layer.backProgate(layer)

x = 3
y = 1
k = 2



objects = [x, y, k]
network = nw.Network(objects)

'''
print(network.nodes[0].objects[0].filters)
Functions.addFilterNodeA(network.nodes[0].objects[0])
print("AGREGANDO FILTRO NODO A")
print(network.nodes[0].objects[0].filters)
Functions.removeFilterNodeA(network.nodes[0].objects[0])
print("ELIMINANDO FILTRO NODO A")
print(network.nodes[0].objects[0].filters)
'''

Functions.addFilterNodeA(network.nodes[0].objects[0])
Propagation(network.nodes[4].objects[0])
print("NODE A VALUE= ",network.nodes[0].objects[0].value,"\n")
print("NODE B VALUE= ",network.nodes[1].objects[0].value,"\n")
print("NODE C VALUE= ",network.nodes[2].objects[0].value,"\n")
print("NODE D VALUE= ",network.nodes[3].objects[0].value,"\n")
print("NODE E VALUE= ",network.nodes[4].objects[0].value,"\n")
