l=[]
def read(l):
    print(l)
def insert(l):
    e=int(input("Enter a element :"))
    l.append(e)
def remove(l):
    i=int(input("Enter the index to remove :"))
    l.pop(i)
while True:
    print('''1)Print the given list.
2)Insert an element in a list.
3)Delete a element from a list.
4)Exit.''')
    ch=int(input("Enter your choice :"))
    if ch==1:
        read(l)
    elif ch==2:
        insert(l)
    elif ch==3:
        remove(l)
    elif ch==4:
        break
    else:
        print("wrong choice...")
        
