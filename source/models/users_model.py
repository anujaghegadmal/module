from flask import make_response
import psycopg2 
from psycopg2.extras import RealDictCursor

class users_model:
    def __init__(self):
        self.con=psycopg2.connect(dbname="e_learning",user="postgres",host="localhost",password="anujagr98",port=5432)
        self.con.set_session(autocommit=True)
        self.cursor=self.con.cursor(cursor_factory=RealDictCursor)

    def add_user_model(self,data):
        try:
            self.cursor.execute("insert into users(name,email,phone_no,password,role,status) values('"+data["name"]+"','"+data["email"]+"','"+data["phone_no"]+"','"+data["password"]+"','"+data["role"]+"','a')")
            return make_response({"status_message":"USER CREATED"},200)

        except Exception as e:
            return make_response({"Error":"Contact developer"},500)

    def list_user_model(self):
        try:
            self.cursor.execute("select * from users_v")
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"status_message":"EXECUTED","payload":fetched_data},200)
        
        except Exception as e:
            return make_response({"Error":"Contact developer"},500)

    def update_user_model(self):
        try:
            return make_response({"status_message":"USER UPDATED"},200)

        except Exception as e:
            return make_response({"Error":"Contact developer"},500)

    def delete_user_model(self,user_id):
        try:
            # update query to update status=d
            self.cursor.execute("update users set status='d' where id="+user_id)
            return make_response({"status_message":"USER DELETED"},200)
        
        except Exception as e:
            return make_response({"Error":"Contact developer"},500)

    # 2nd call
    def single_user_details_model(self,user_id):
        try:
            self.cursor.execute("select * from users_v where id="+user_id)
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"status_message":"EXECUTED"},200)
        
        except Exception as e:
            return make_response({"Error":"Contact developer"},500)