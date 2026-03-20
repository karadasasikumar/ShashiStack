# create a class movie and instance object hero,director,ticket price,lang,collections has to be updated
# language has to be dubbed thiz movie


class Movie:
    lang="Telugu"
    def __init__(self,hero,director,tp):
        self.director=director
        self.hero=hero
        self.tp=tp
    def collection(self,tickets):
        return self.tp*tickets
    def dub(self,new_lang):
        self.lang=new_lang
sahoo=Movie("prabhas","sujeeth",350)
sahoo.collection(6000000)
sahoo.lang
sahoo.dub("hindi")
sahoo.lang
print(sahoo.lang)














































