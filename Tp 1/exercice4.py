def compte_occurences(list) :
    mydic={}
    for i in list:
        if i in mydic:
            mydic[i]+=1
        else:
            mydic[i]=1
    return mydic

list=["mohamed","abdellah","abdelghani","mohamed"]
res=compte_occurences(list)
print(res)