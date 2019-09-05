
# Node.objects[0] = Layer
class Layer():

    def __init__(self, propagate, node, filters=None, value=None, bias=None):
        self.filters = filters
        self.node = node
        self.propagate = propagate
        self.value = value
        self.label = None
        self.bias = bias ## bias = filters
        self.backProgate = None



                
        





