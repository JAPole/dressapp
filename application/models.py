from application import db


class topid (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typeoftop = db.Column(db.String(40), nullable=False)
    colouroftop = db.Column(db.String(40), nullable=False)
    solidorNot = db.Column(db.Boolean)

    
    outfittop = db.relationship ('outfitid', backref='stylisttop', lazy=True)

  
    #__repr__ prints to the screen
    
    def __repr__(self):
        return ''.join([
            'User: ', self.first_name, ' ', self.last_name, '\r\n',
            'Title: ', self.title, '\r\n', self.content
            ])


class bottomid (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typeoftop = db.Column(db.String(40), nullable=False)
    colouroftop = db.Column(db.String(40), nullable=False)

    outfitbottom = db.relationship ('outfitid', backref='stylistbottom', lazy=True)



class outfitid (db.Model):
    outfittopid = db.Column(db.Integer, db.ForeignKey('top.id'), nullable=False)
    outfitbottomid = db.Column(db.Integer, db.ForeignKey('bottom.id'), nullable=False)


    id = db.Column(db.Integer, primary_key=True) #
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    
    
    
    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n',
        'Email: ', self.email], '\r\n',
        'Name: ', self.first_name, ' ', self.last_name
        )



