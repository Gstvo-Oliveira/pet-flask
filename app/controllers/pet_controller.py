from flask import request
from http import HTTPStatus
from app.repositories.mongoDb import InMongoRepository
from bson import ObjectId


class PetController:


    def list_pets(self):
        pets = InMongoRepository().db.pet.find()

        pets_list = []

        for pet in pets:
            pets_list.append(pet)

        return pets_list

    def create_pet(self):
        pet_data:dict = request.get_json()

        id = ObjectId()
        
        pet_data['_id'] = str(id)
        pet = InMongoRepository().db.pet.insert_one(pet_data)

        return pet_data, HTTPStatus.CREATED


    def retrieve_pet(self ,pet_id):
        pet =  InMongoRepository().db.pet.find_one({'_id': pet_id})
    
        
        if not pet:
            return {"error": "pet not found"}, HTTPStatus.NOT_FOUND

        return pet    


    def update_pet(self, pet_id):
        pet_data:dict = request.get_json()
        pet = InMongoRepository().db.pet.find_one_and_update(
            {'_id': pet_id}, 

            update = {
                "$set":
            {
                'name': pet_data['name'], 
                'type': pet_data['type']
                }}, 

            return_document=True)
        
        
        if not pet:
            return {"error": "pet not found"}, HTTPStatus.NOT_FOUND


        return pet, HTTPStatus.CREATED


    def delete_pet(self, pet_id):
        pet = InMongoRepository().db.pet.find_one_and_delete( 
            {'_id': pet_id}
        )
        
        if not pet:
            return {"error": "pet not found"}, HTTPStatus.NOT_FOUND      

        return pet, HTTPStatus.NO_CONTENT