## Using mongo config file
    - https://docs.mongodb.com/manual/reference/configuration-options/
    - mongod --config /etc/mongod.conf
    - mongod -f /etc/mongod.conf
    
## Create Data
    $python manager.py shell
    >>> from user.models import User
    >>> user = User('ben', 'pwd', 'ben@gmail.com',"ben","huang")
    >>> user.save()
    
    
## Show Index
    > db.user.getIndexes()
    
## Mongo query details
    > db.user.find().explain()
    
## Restart mongo
    Create mongo_restart script
    
    rm -fr ~/data/mongod.lock
    
    mognod -f mongod.conf
    
    chmod 755 mongo_restart
    
## ORM
    ```
    from flask_mongoengine import MongoEngine

    db = MongoEngine()
    
    class User(db.Document):
        username = db.StringField(db_field="u", required=True, unique=True)
        password = db.StringField(db_field="p", required=True)
        email = db.EmailField(db_field="e", required=True, unique=True)
    ```
## Mongo Query
    user = User.objects.filter( username=form.username.data ).first()
    
    
## Relationship models


## 
    from_user = db.ReferenceField(User, db_field='fu', reversed_delete_rule=CASCADE)
    