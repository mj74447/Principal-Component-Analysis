from enum import Enum, unique,auto
@unique #duplicate values now will lead to errors .prior to this duplicate value is acceptable
class Fruit(Enum):
    A=1
    B=2
    C=auto()#automatic increment in C.
def main():
    print(Fruit.A.name,Fruit.A.value)
    print(Fruit.B.name,Fruit.B.value)
    print(Fruit.C.name,Fruit.C.value)
if __name__ == '__main__':#basic python
    main()