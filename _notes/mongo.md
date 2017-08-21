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
    
## 
    > db.user.find().explain()