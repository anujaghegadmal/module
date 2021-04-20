from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor

class enrollments_model:
    def __init__(self):
        self.con=psycopg2.connect(dbname="e_learning",user="postgres",host="localhost",password="anujagr98",port=5432)
        self.con.set_session(autocommit=True)
        self.cursor=self.con.cursor(cursor_factory=RealDictCursor)

    def add_enrollment_model(self,data):
        try:
            print(data)
            self.cursor.execute("insert into enrollments(created_by,course_id,user_id,status) values('"+data["created_by"]+"','"+data["course_id"]+"','"+data["user_id"]+"','a')")
            return make_response({"status_message":"ENROLLED SUCCESSFULLY"},200)

        except Exception as e:
            return make_response({"Error":"Contact developer"},500)


    def list_enrollment_model(self):
        try:
            self.cursor.execute("select * from enrollments")
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"status_message":"EXECUTED"},200)

        except Exception as e:
            return make_response({"Error":"Contact developer"},500)


    def update_enrollment_model(self):
        try:
            return make_response({"status_message":"ENROLLMENT UPDATED"},200)

        except Exception as e:
            return make_response({"Error":"Contact developer"},500)

    def delete_enrollment_model(self,id):
        try:
            return make_response({"status_message":"ENROLLMENT DELETED SUCCESSFULLY"},200)

        except Exception as e:
            return make_response({"Error":"Contact developer"},500)

    def my_enrollments_model(self,user_id):
        print(user_id )
        self.cursor.execute("select * from my_enrollments_v where created_by="+user_id)
        fetched_data=self.cursor.fetchall()
        print(fetched_data)
        return make_response({"status_message":"THESES ARE ALL YOUR ENROLLMENTS"},200)