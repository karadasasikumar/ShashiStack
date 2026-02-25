class Profile:
    def __init__(self,username):
       self.follower=0
       self.username=username
    def follow(self):
        print("someone followed you")
        self.follower+=1
    def update_username(self,nun):
        self.username=nun
p1=Profile("sasi")#oldusername
p1.follow()#follow method call
print(p1.follower)#update follower count
p1.update_username("sashi")#updateusrname
print(p1.username)
