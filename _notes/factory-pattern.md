## Project structure
    ```
    /manager.py
    /app.py
    /settings.py
    ```
    
    
## Run
    $python manager.py run
    
## Create Data
    $python manager.py shell
    >>> from user.models import User
    >>> user = User('ben', 'pwd', 'ben@gmail.com',"ben","huang")
    >>> user.save()