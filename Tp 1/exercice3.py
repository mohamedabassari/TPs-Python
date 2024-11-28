def intersection(ensemble1,ensemble2):
    res = ensemble1 & ensemble2
    return res

ensemble1={1,3,5,7}
ensemble2={1,4,5,9}

resul = intersection(ensemble1,ensemble2)

print(resul)