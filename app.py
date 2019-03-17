from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import mysql.connector


app = Flask(__name__)
api = Api(app)
cnx = mysql.connector.connect(user="root", database="anima")
cursor = cnx.cursor()



# SQL DB:
#   ID int(10)
#   user_id int(10)
#   progress_id int(10)


class  User(Resource):
    
    def get(self, user_id):
        
        query = (
            "SELECT progress_id FROM user_progress "
            "WHERE  user_id = {}".format(user_id)
        )

        cursor.execute(query)
        records = cursor.fetchall()
        
        if(len(records) == 0):
            return {
                'status_code': 404,
                'status': 'User Not Found',
            }

        elif(len(records) == 1):
            return {
                'status_code': 200,
                'status': 'Sucssess',
                'progress_id': records[0][0]
            }

        return 'error'

    def delete(self,  user_id):
        query = (
            "DELETE FROM `user_progress` "
            "WHERE `user_id` = {}".format(user_id)
        )

        cursor.execute(query)
        cnx.commit()

        return {
            'status_code': 201,
            'status': 'User Deleted'
        }

class ForPut(Resource):   
    def put(self, user_id, user_progress):
        query = (
            "SELECT user_id FROM user_progress "
            "WHERE  user_id = {}".format(user_id)
        )



        cursor.execute(query)
        records = cursor.fetchall()
                    
        if(len(records) == 0):

  
            add_user = (
                "INSERT INTO `user_progress`"
                "(`user_id`, `progress_id`) "
                "VALUES ( '%s', '%s')"
            )

            cursor.execute(add_user, (user_id, user_progress))
            cnx.commit()

            return {
                'status': 201,
                'status': 'Progress Created'
            }


        elif(len(records) == 1): 
            
            add_progress = (
                "UPDATE `user_progress` "
                "SET `progress_id` = %s "
                "WHERE `user_id` = %s"
            )
            
            cursor.execute(add_progress, (user_progress, user_id))
            cnx.commit()

            return {
                'status': 201,
                'status': 'Progress Updated'
            }

        return 'error'



api.add_resource(User   , "/user/<int:user_id>")
api.add_resource(ForPut, "/put/<int:user_id>/<int:user_progress>")

app.run()
