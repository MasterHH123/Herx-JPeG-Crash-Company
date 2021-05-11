from random import randint
name = ["Charli Dmelio", "Goofy", "Obama", "Dave", "Seth"]
verb = ["ate","kicked","drank","smoked","wants"]
object = ["a computer","an egg sandwich","a dog","a blunt of weed","an eletric guitar"]

while True:
    print(name[randint(0, len(name)-1)]+" "+verb[randint(0, len(verb)-1)]+" "+object[randint(0, len(object)-1)])
    input()
