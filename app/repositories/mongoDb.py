from flask import current_app

class InMongoRepository:
    
    
    def __init__(self) -> None:
        self.db = current_app.db
        self.collection = self.db