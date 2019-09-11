import Network as nw
import Functions

def Propagation(layer):

    for parent in layer.node.parents:
        layerParent = parent.objects[0]
        Propagation(layerParent)

    layer.propagate(layer)
 
def BackPropagation(layer):
    
    for kid in layer.node.kids:
        kidLayer = kid.objects[0]
        BackPropagation(kidLayer)

    layer.backPropagate(layer)

x = 3
y = 3
k = 2


objects = Functions.np.full((3), (x, y, k))

network = nw.Network(objects)

print("FILTRO ORIGINAL","\n")
print("FILTROS NODO A")
print(network.nodes[0].objects[0].filters,"\n")
print("FILTROS NODO B")
print(network.nodes[1].objects[0].filters,"\n")

network.assign(Functions.createValueA(network.objects), "c")

print("AGREGANDO NUEVO FILTRO","\n")
Functions.addFilters(network.nodes[0].objects[0])
print("FILTROS NODO A")
print(network.nodes[0].objects[0].filters,"\n")
print("FILTROS NODO B")
print(network.nodes[1].objects[0].filters,"\n")


print("ELIMINANDO ULTIMO FILTRO","\n")
Functions.removeFilters(network.nodes[0].objects[0])
print("FILTROS NODO A")
print(network.nodes[0].objects[0].filters,"\n")
print("FILTROS NODO B")
print(network.nodes[1].objects[0].filters,"\n")




Propagation(network.nodes[4].objects[0])
print("NODE A VALUE= ",network.nodes[0].objects[0].value,"\n")
print("NODE B VALUE= ",network.nodes[1].objects[0].value,"\n")
print("NODE C VALUE= ",network.nodes[2].objects[0].value,"\n")
print("NODE D VALUE= ",network.nodes[3].objects[0].value,"\n")
print("NODE E VALUE= ",network.nodes[4].objects[0].value,"\n")


BackPropagation(network.nodes[0].objects[0])
print("NODE D VALUE_DER= ",network.nodes[3].objects[0].value_der,"\n")
print("NODE C VALUE_DER= ",network.nodes[2].objects[0].value_der,"\n")
print("NODE B VALUE_DER= ",network.nodes[1].objects[0].value_der,"\n")


