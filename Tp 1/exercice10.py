def fusioner_dicst(dict1,dict2):
    mydic=dict1.copy()
    for cle,valeur in dict2.items():
        if cle in mydic:
            mydic[cle]+=valeur
        else:
            mydic[cle]=valeur

    return mydic


di1={"one":1,"two":2}
di2={"one":1,"three":3}
reslt=fusioner_dicst(di1,di2)
print(reslt)
