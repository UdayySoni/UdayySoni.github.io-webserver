from flask import Flask, render_template , url_for, request , redirect
import csv

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return render_template('index.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# create database with .txt file
def database_writer(data):
   with open('database.txt' , mode='a') as database:
      Name  = data["Name"]
      Email = data["Email"]
      Message = data["Message"]
      file = database.write(f'\n Name : {Name}, \n E-mail : {Email}, \n Comment : {Message}')
      
# create database with .csv file
# def to_csv_writer(data):
#    with open('database.csv' , mode='a') as database2:
#       Name  = data["Name"]
#       Email = data["Email"]
#       Message = data["Message"]
#       csv_writer = csv.writer(database2 , delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)  
#       csv_writer.writerow([Name , Email , Message])




@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method == 'POST':
     data = request.form.to_dict()
     database_writer(data)
     return redirect('thankyou.html#contact')
  else:
     return 'Something went wrong at our side , please try again'


@app.route("/www.linkedin.com/in/Udaysoni10846652", methods=["GET"])
def redirect_external():
    return redirect("http://www.linkedin.com/in/Udaysoni10846652", code=302)
