from random import randint
sujeto = ["Charli Dmelio", "Goofy", "Obama", "Dave", "Seth"]
verbo = ["se comió","pateó","emborrachó","fumó","quiere"]
objeto = ["una computadora","un sandwich de huevo","un perro","un blunt de weed","una guitarra eletrica"]

while True:
    print(sujeto[randint(0, len(sujeto)-1)]+" "+verbo[randint(0, len(verbo)-1)]+" "+objeto[randint(0, len(objeto)-1)])
    input();