## Unit Testing
    - Automated
    - Independent
    - Consistent and repeatable
    - Maintainable
    
## Implements
    create main tests.py to call other tests.py
    
## Overwrite coning in Unit test
    ```
     return create_app(
            MONGODB_SETTINGS={'DB': self.db_name},
            TESTING=True,
            WTF_CSRF_ENABLED=False,
            SECRET_KEY='mySecret'
        )
     ```