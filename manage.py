import Network as nw

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

x = 2
y = 2
k = 2


objects = [x, y, k]
network = nw.Network(objects)

##Propagation(network.nodes[0].objects[0])
Propagation(network.nodes[1].objects[0])
print(network.nodes[1].objects[0].value)