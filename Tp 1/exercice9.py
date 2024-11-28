def analyse_texte(texte):
    mydic={
        "nombre de mot":0,
        "nombre de carac":0,
    }
    for i in texte:
        mydic["nombre de mot"]=len(texte.split())
        mydic["nombre de carac"]=len(texte.replace(" ",""))

    return mydic


texte="je suis mohamed abassari"
print(analyse_texte(texte))
