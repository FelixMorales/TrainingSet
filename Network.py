import Node as nd
import Layer as ly
import Functions

class Network:

    def __init__(self, objects):
        # objects [x, y, k]
        # x -> dimension x
        # y -> dimension y
        # k -> cantidad filtros
        self.objects = objects
        self.nodes = []
        self.__createStructure()

    def __createStructure(self):
        nodes = []

        nodes.append(nd.Node())
        nodes.append(nd.Node())
        nodes.append(nd.Node())
        nodes.append(nd.Node())
        nodes.append(nd.Node())

        nodes[0].kids.append(nodes[1])
        nodes[1].kids.append(nodes[2])
        nodes[2].kids.append(nodes[3])
        nodes[3].kids.append(nodes[4])

        nodes[1].parents.append(nodes[0])
        nodes[2].parents.append(nodes[1])
        nodes[3].parents.append(nodes[2])
        nodes[4].parents.append(nodes[3])


        self.nodes = nodes 
        self.__assignLayers()

    def __assignLayers(self):

        self.nodes[0].objects.append(ly.Layer(propagate=Functions.Nothing, node=self.nodes[0], 
                            filters=Functions.createFilterA(self.objects), value=Functions.createValueA(self.objects),
                            bias=Functions.createValueA(self.objects), backPropagate=Functions.a_filter_der))

        self.nodes[1].objects.append(ly.Layer(propagate=Functions.ProductoPunto, node=self.nodes[1], 
                           filters=Functions.createFilterB(self.objects), 
                           bias=None, backPropagate=Functions.b_filter_der))

        self.nodes[2].objects.append(ly.Layer(propagate=Functions.ProductoPunto, node=self.nodes[2],backPropagate=Functions.c_filter_der))
        self.nodes[3].objects.append(ly.Layer(propagate=Functions.probability, node=self.nodes[3], backPropagate=Functions.probability_der))
        self.nodes[4].objects.append(ly.Layer(propagate=Functions.logaritmo, node=self.nodes[4], backPropagate=Functions.Nothing))

    def assign(self, x, label=None):
        self.nodes[0].objects[0].value = x
        self.nodes[3].objects[0].label = label

    
    def Acumulate_der(self, l):

        for node in self.nodes:
            layer = node.objects[0]

            if layer.value_der is not None and layer.value_der_total is not None:
                layer.value_der_total = (layer.value_der_total + layer.value_der) / l

            if layer.bias_der is not None and layer.bias_der_total is not None:
                layer.bias_der_total = (layer.bias_der_total + layer.bias_der) / l
            
            if layer.filter_der is not None and layer.filter_der_total is not None:
                layer.filter_der_total = (layer.filter_der_total + layer.filter_der) / l
    
    def Regularize_der(self):
        
        for node in self.nodes:
            layer = node.objects[0]

            if layer.bias is not None and layer.bias_der_total is not None:
                layer.bias_der_total = layer.bias_der_total + layer.bias
            
            if layer.filters is not None and layer.filter_der_total is not None:
                layer.filter_der_total = layer.filter_der_total + layer.filters

    def Reset_der(self):

        for node in self.nodes:
            layer = node.objects[0]

            if layer.value_der is not None:
                layer.value_der = layer.value_der * 0

            if layer.bias_der is not None:
                layer.bias_der = layer.bias_der * 0
            
            if layer.filter_der is not None:
                layer.filter_der = layer.filter_der * 0

    def Reset_der_total(self):

        for node in self.nodes:
            layer = node.objects[0]

            if layer.value_der_total is not None:
                layer.value_der_total = layer.value_der_total * 0

            if layer.bias_der_total is not None:
                layer.bias_der_total = layer.bias_der_total * 0
            
            if layer.filter_der_total is not None:
                layer.filter_der_total = layer.filter_der_total * 0
