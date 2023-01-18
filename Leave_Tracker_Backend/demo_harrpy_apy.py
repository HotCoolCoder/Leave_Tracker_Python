from calendar import month
# from crypt import methods
# from crypt import methods
import string
from tokenize import String
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request,render_template,jsonify
from datetime import datetime
from sqlalchemy import text
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@' + 'DESKTOP-T3T90T0\\SQLEXPRESS' + '/' + 'weekly_status' + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
db = SQLAlchemy(app)
cors = CORS()
cors.init_app(app)

# class Contacts(db.Model):
#     # sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80),primary_key = True, nullable=False)
#     phone_num = db.Column(db.String(12), nullable=False)
#     msg = db.Column(db.String(120), nullable=False)
#     # date = db.Column(db.String(12), nullable=True)
#     email = db.Column(db.String(20), nullable=False)
#     def to_json(self):
#         return {
#             'name': self.name,
#             'email': self.email,
#             'phone_num': self.phone_num,
#             'message': self.msg
#         }
    # def __init__(self, name, phone_num, msg,email):
    #     self.name = name
    #     self.phone_num = phone_num
    #     self.msg = msg
    #     self.email = email

# class Attendance(db.Model):
#     Emp_Id = db.Column(db.String(10),primary_key = True, nullable=False)
#     Emp_name = db.Column(db.String(10), nullable=False)
#     Month = db.Column(db.String(10), nullable=False)
#     Present_count = db.Column(db.Integer(), nullable=False)
#     Absent_count = db.Column(db.Integer(), nullable=False)
#     def to_json(self):
#         return {
#             'Emp_Id': self.Emp_Id,
#             'Emp_name': self.Emp_name,
#             'Month':self.Month,
#             'Present_count': self.Present_count,
#             'Absent_count': self.Absent_count
#         }

class demo_weekly_status(db.Model):
    Fiscal_Month = db.Column(db.String(100), nullable=False)
    Week = db.Column(db.String(100),primary_key = True, nullable=False)
    Area = db.Column(db.String(100), nullable=False)
    Project = db.Column(db.String(100), nullable=False)
    Team_Member_Name = db.Column(db.String(100),primary_key = True, nullable=False)
    Test_Lead = db.Column(db.String(100), nullable=False)
    User_Story =  db.Column(db.String(100), nullable=False)
    Analysis_Hours = db.Column(db.String(100), nullable=False)
    # Test_Script_num = db.Column(db.String(100), nullable=False)
    Test_Script_Hours =db.Column(db.String(100), nullable=False)
    # Test_Execution_num = db.Column(db.String(100), nullable=False)
    Test_Execution_Hours =db.Column(db.String(100), nullable=False)
    Support_Hours =db.Column(db.String(100), nullable=False)
    Defect = db.Column(db.String(100), nullable=False)
    Calls_Status_Updates_hours = db.Column(db.String(100), nullable=False)
    KT_Learnings_VideoRecording_Documentation_Hours = db.Column(db.String(100), nullable=False)
    Support_Tickets_Raised_Hours = db.Column(db.String(10), nullable=False)
    Notes =db.Column(db.String(10), nullable=False)
    def to_json(self):
        return {
            'Fiscal_Month': self.Fiscal_Month,
            'Week': self.Week,
            'Area':self.Area,
            'Project': self.Project,
            'Team_Member_Name': self.Team_Member_Name,
            'Test_Lead': self.Test_Lead,
            'User_Story': self.User_Story,
            'Analysis_Hours':self.Analysis_Hours,
            # 'Test_Script_num': self.Test_Script_num,
            'Test_Script_Hours': self.Test_Script_Hours,
            # 'Test_Execution_num': self.Test_Execution_num,
            'Test_Execution_Hours': self.Test_Execution_Hours,
            'Support_Hours':self.Support_Hours,
            'Defect': self.Defect,
            'Calls_Status_Updates_hours': self.Calls_Status_Updates_hours,
            'KT_Learnings_VideoRecording_Documentation_Hours': self.KT_Learnings_VideoRecording_Documentation_Hours,
            'Support_Tickets_Raised_Hours': self.Support_Tickets_Raised_Hours,
            'Notes':self.Notes,
        }

    def chart_data_to_json(self):
        return {
            'Week': self.Week,
            'Team_Member_Name': self.Team_Member_Name,
            'Analysis_Hours':self.Analysis_Hours,
            'Test_Script_Hours': self.Test_Script_Hours,
            'Test_Execution_Hours': self.Test_Execution_Hours,
            'Support_Hours':self.Support_Hours,
            'Defect': self.Defect,
            'Calls_Status_Updates_hours': self.Calls_Status_Updates_hours,
            'KT_Learnings_VideoRecording_Documentation_Hours': self.KT_Learnings_VideoRecording_Documentation_Hours,
            'Support_Tickets_Raised_Hours': self.Support_Tickets_Raised_Hours,
        }



# @app.route("/contacts/<string:month>", methods = ['GET','POST'])
# def contact(month:str,Emp_name:str):
#     if(request.method=='POST'):
#         '''Add entry to the database'''
#         name = 'Paritosh'
#         email = 'paritosh@gmail.com'
#         phone = '7483758373'
#         message = 'initial commit to the DB'
#         entry = Contacts(name=name, phone_num = phone, msg = message, email = email )
#         db.session.add(entry)
#         db.session.commit()
#         return request.method
#     # return render_template('contact.html')
#     else:
#         # entry = Contacts()
#         # month = request.args.get()
#         books = Contacts.query.filter_by(name = month)
#         # connection = db.session.connection()
#         # books = connection.execute( text("select * from Contacts where name = '1'") )
#         return jsonify([book.to_json() for book in books])
#         # return jsonify(books)
#         # return render_template('month.html', book = books)

# @app.route('/try/<string:month>' , methods = ['GET'])
# def tryy(month:str):
#     if(request.method == 'GET'):
#         # entry = Attendance()
#         # if(emp_name =='All'):
#         #     result = Attendance.query.filter(Month = month)
#         #     return jsonify([book.to_json() for book in result])
#         # else:
#         result = Attendance.query.filter_by(Month = month, )
#         return jsonify([book.to_json() for book in result])
            
@app.route('/weekly/<area>', methods = ['GET','POST'])
def weekly_status(area:str):
    if(request.method == 'GET'):
        print(request.method)
        result = demo_weekly_status.query.filter_by(Area = area,)
        # result = demo_weekly_status.query.all()
        return jsonify([res.to_json() for res in result])

@app.route('/chart/<name>',methods = ['GET','POST'])
@app.route('/chart/<name>/<week>',methods = ['GET','POST'])
def chart(name:str,week:str='None'):
    if(request.method == 'GET'):
        if(week =='None'):
            result = demo_weekly_status.query.filter_by(Team_Member_Name = name,)
            return jsonify([res.chart_data_to_json() for res in result])
            # return type(chart_data)
        else:
            data = demo_weekly_status.query.filter_by(Team_Member_Name = name,Week = week,)
            return jsonify([res.chart_data_to_json() for res in data])
            # return type(chart_data)
        

app.run(debug=True)