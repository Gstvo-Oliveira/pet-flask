from flask import Flask
from app.controllers import pet_controller
def pet_routes(app: Flask):

    app.get('/pets')(pet_controller.list_pets)
    app.post('/pets')(pet_controller.create_pet)
    app.get('/pets/<pet_id>')(pet_controller.retrieve_pet)
    app.patch('/pet/<pet_id>')(pet_controller.update_pet)   
    app.delete('/pet/<pet_id>')(pet_controller.delete_pet)
