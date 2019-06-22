from flask_login import UserMixin

 

class User(UserMixin):
    def __init__(self, id,email,nom,prenom):
        self.id = id
        self.email = email
        self.nom = nom
        self.prenom = prenom


class UserHelper:
    def __init__(self, users) : 
         self.users = users
    
    def getUserById(self,id) :
        retour = None
        for u in self.users : 
            if u.id == int(id) :
                retour = u
        return self.users[0]
    
    def getUserByEmail(self,email) : 
        retour = None
        for u in self.users : 
            if u.email == email :
                retour = u
        return retour

    


Users = [User(1,'sdelporte@gmail.com','delporte','sebastien') , User(2,'test@gmail.com','test','test'), User(3,'test2@gmail.com','test2','test2')]