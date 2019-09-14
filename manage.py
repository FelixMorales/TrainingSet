import Network as nw
import Functions

Functions.decimal.getcontext().prec = 10

def generateData(data, objects, n):
    
        circulo = []
        circulo.append(Functions.np.zeros((objects[0], objects[1], 3), dtype=object))
        circulo.append("c")

        data.append(circulo)

        for i in range(objects[0]//2):
            for j in range(objects[1]):
                circulo[0][i][j] = [Functions.decimal.Decimal(255),Functions.decimal.Decimal(255),Functions.decimal.Decimal(255)]

        for i in range(objects[0]//2, objects[0]):
            for j in range(objects[1]):
                circulo[0][i][j] = [Functions.decimal.Decimal(1),Functions.decimal.Decimal(1),Functions.decimal.Decimal(1)]

        for i in range(n-1):
            imagenRandom = []
            imagenRandom.append(generateImageRandom(objects))
            imagenRandom.append("n")

            data.append(imagenRandom)


def generateImageRandom(objects):
    image = Functions.np.zeros((objects[0], objects[1], 3), dtype=object)

    
    for i in range(objects[0]):
        for j in range(objects[1]):
            image[i,j] = [Functions.decimal.Decimal(Functions.random.randint(1, 255)), 
                Functions.decimal.Decimal(Functions.random.randint(1, 255)), 
                Functions.decimal.Decimal(Functions.random.randint(1, 255))]
    
    return image

x = 3
y = 2
k = 10


objects = Functions.np.full((3), (x, y, k))

network = nw.Network(objects)
data = []

generateData(data, objects, 500)

network.Training(data)
'''
print("############################# PROPAGATION #############################", "\n", "\n")
Functions.Propagation(network.nodes[4].objects[0])
print("NODE A VALUE= ",network.nodes[0].objects[0].value,"\n")
print("NODE B VALUE= ",network.nodes[1].objects[0].value,"\n")
print("NODE C VALUE= ",network.nodes[2].objects[0].value,"\n")
print("NODE D VALUE= ",network.nodes[3].objects[0].value,"\n")
print("NODE E VALUE= ",network.nodes[4].objects[0].value,"\n")


print("############################# BACK-PROPAGATION #############################", "\n", "\n")

Functions.BackPropagation(network.nodes[0].objects[0])
print("NODE D VALUE_DER= ",network.nodes[3].objects[0].value_der,"\n")
print("NODE C VALUE_DER= ",network.nodes[2].objects[0].value_der,"\n")
print("NODE B VALUE_DER= ",network.nodes[1].objects[0].value_der,"\n")
'''