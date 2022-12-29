import pickle

importedpickle = open('drop1','rb')
NEW = pickle.load(importedpickle)
importedpickle.close()

print(len(NEW))
OLD=NEW
importtopickle = open('drop1','wb')
pickle.dump(NEW[5:],importtopickle)
importtopickle.close()   

importedpickle = open('drop1','rb')
NEW = pickle.load(importedpickle)
importedpickle.close()

print(len(NEW))



def notin(x,list):
    index=1
    for i in list:
        if i.lower().__contains__(x.lower()):
            index*=0
        else:
            pass
    return index!=0        


NEW.sort()
OLD.sort()         
NEW_ListofNames = [x[0] for x in NEW]
new_entries = [x for x in OLD if notin(x[0],NEW_ListofNames)==True]
print(new_entries)
