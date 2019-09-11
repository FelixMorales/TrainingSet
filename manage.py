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

network.assign(Functions.createValueA(network.objects), "c")

Functions.addFilters(network.nodes[0].objects[0])

Functions.removeFilters(network.nodes[0].objects[0])

print("############################# PROPAGATION #############################", "\n", "\n")
Propagation(network.nodes[4].objects[0])
print("NODE A VALUE= ",network.nodes[0].objects[0].value,"\n")
print("NODE B VALUE= ",network.nodes[1].objects[0].value,"\n")
print("NODE C VALUE= ",network.nodes[2].objects[0].value,"\n")
print("NODE D VALUE= ",network.nodes[3].objects[0].value,"\n")
print("NODE E VALUE= ",network.nodes[4].objects[0].value,"\n")


print("############################# BACK-PROPAGATION #############################", "\n", "\n")

BackPropagation(network.nodes[0].objects[0])
print("NODE D VALUE_DER= ",network.nodes[3].objects[0].value_der,"\n")
print("NODE C VALUE_DER= ",network.nodes[2].objects[0].value_der,"\n")
print("NODE B VALUE_DER= ",network.nodes[1].objects[0].value_der,"\n")

print("############################# ACUMULATE #############################", "\n", "\n")

print("NODE B VALUE_DER_TOTAL= ",network.nodes[1].objects[0].value_der_total,"\n")
print("NODE B BIAS_DER_TOTAL= ",network.nodes[1].objects[0].bias_der_total,"\n")
print("NODE B FILTER_DER_TOTAL= ",network.nodes[1].objects[0].filter_der_total,"\n")
print("ACUMULATE(2)", "\n")
network.Acumulate_der(2)
print("NODE B VALUE_DER_TOTAL= ",network.nodes[1].objects[0].value_der_total,"\n")
print("NODE B BIAS_DER_TOTAL= ",network.nodes[1].objects[0].bias_der_total,"\n")
print("NODE B FILTER_DER_TOTAL= ",network.nodes[1].objects[0].filter_der_total,"\n")
print("ACUMULATE(2)", "\n")
network.Acumulate_der(2)
print("NODE B VALUE_DER_TOTAL= ",network.nodes[1].objects[0].value_der_total,"\n")
print("NODE B BIAS_DER_TOTAL= ",network.nodes[1].objects[0].bias_der_total,"\n")
print("NODE B FILTER_DER_TOTAL= ",network.nodes[1].objects[0].filter_der_total,"\n")

print("############################# REGULARIZE #############################", "\n", "\n")

print("1st Regularize")
network.Regularize_der()
print("NODE B BIAS_DER_TOTAL= ",network.nodes[1].objects[0].bias_der_total,"\n")
print("NODE B FILTER_DER_TOTAL= ",network.nodes[1].objects[0].filter_der_total,"\n")

print("2nd Regularize")
network.Regularize_der()
print("NODE B BIAS_DER_TOTAL= ",network.nodes[1].objects[0].bias_der_total,"\n")
print("NODE B FILTER_DER_TOTAL= ",network.nodes[1].objects[0].filter_der_total,"\n")

print("############################# RESET DER #############################", "\n", "\n")

network.Reset_der()
print("NODE B VALUE_DER= ",network.nodes[1].objects[0].value_der,"\n")
print("NODE B BIAS_DER= ",network.nodes[1].objects[0].bias_der,"\n")
print("NODE B FILTER_DER= ",network.nodes[1].objects[0].filter_der,"\n")

print("############################# RESET DER TOTAL #############################", "\n", "\n")

network.Reset_der_total()
print("NODE B VALUE_DER_TOTAL= ",network.nodes[1].objects[0].value_der_total,"\n")
print("NODE B BIAS_DER_TOTAL= ",network.nodes[1].objects[0].bias_der_total,"\n")
print("NODE B FILTER_DER_TOTAL= ",network.nodes[1].objects[0].filter_der_total,"\n")