from sklearn.externals.array_api_compat.dask.array.linalg import vector_norm


class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)


    def  __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'


v1=Vector(1,2)
v2=Vector(3,4)
v3=v1+v2

print(v3)