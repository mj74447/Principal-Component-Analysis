import collections
import string
def main():
    #initialize deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)
    print("Item Count:", str(len(d)))
    for el in d:
        print(el.upper(),end=",")

    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(3)
   # print(d)

#-----------Rotate ----------------------
    print(d)
    d.rotate(10)
    print(d)
if __name__=='__main__':
    main()