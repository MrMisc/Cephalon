import pickle
importedpickle = open('n1','rb')
NEW = pickle.load(importedpickle)
importedpickle.close()

importedpickle = open('n2','rb')
OLD = pickle.load(importedpickle)
importedpickle.close()

for x in NEW:
    print(x.split('\n')[0])

print("vs")

for y in OLD:
    print(y.split('\n')[0])


print("#####")
print("And then the difference with the set method is...")
print("#####")

#Remove the stupid duplicates
NEW_=[]
OLD_=[]
NEW_= [x for x in NEW if x.split('\n')[0] not in NEW_]
OLD_= [x for x in OLD if x.split('\n')[0] not in OLD_]

print(len(OLD_))
print(len(NEW_))
#This time the entry NEW is actually the newer set
NEW_.sort()
OLD_.sort()

for i in range(len(NEW_)):
    print(OLD_[i].split('\n')[0])
    print(OLD_[i]==NEW_[i])
    print(NEW_[i].split('\n')[0])
    print("++++++++++")
    print(OLD_[i].split('\n')[0]==NEW_[i].split('\n')[0])
    print("##############")
    

new_entries = set(NEW_).difference(set(OLD_))
print(len(new_entries))


def notin(x,list):
    index=1
    for i in list:
        if i.lower().__contains__(x.lower()):
            index*=0
        else:
            pass
    return index!=0


new_entries2 = [x for x in NEW_ if notin(x.split('\n')[0],OLD_)==True]

for x in new_entries2:
    print(x.split('\n')[0])

print(len(new_entries))
print(len(new_entries2))




#Little trick


importedpickle = open('n1','rb')
NEW = pickle.load(importedpickle)
importedpickle.close()

print(NEW[:5])
NEWnew = NEW[2:]
print(NEWnew[:5])

importtopickle = open('n1','wb')
pickle.dump(NEWnew,importtopickle)
importtopickle.close()