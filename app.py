from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search/", methods=['GET', 'POST'])
def search():
    connection = sqlite3.connect("hca.db")
    if request.method == 'POST':
        if "searchIn" in request.form:
            SearchData()
            return render_template("home.html")
    return render_template("search.html")


def SearchData():
    connection = sqlite3.connect("hca.db")
    select_query = "SELECT * FROM Patients WHERE UserName=UserName"
    cursor = connection.cursor()
    cursor.execute(select_query)
    data = cursor.fetchall()
    for col in data:
        print("Full Name : ", col[0])
        print("User Name : ", col[1])
        print("Email : ", col[3])
        print("Phone : ", col[4])
        print("Address : ", col[5])
        print("Age : ", col[6])
        print("Height : ", col[7])
        print("Weight :", col[8])
        print("Allergy : ", col[9])
        print("Medical Conditions : ", col[10])
        print("Prescriptions : ", col[11], "\n")


@app.route('/mealprep/', methods=['GET', 'POST'])
def mealprep():
    connection = sqlite3.connect("hca.db")
    if request.method == 'POST':
        if "mealsub" in request.form:
            AddMealOrder(request.form['username'], request.form['paymentnumber'], request.form['expccv'], request.form['breakfastorder'], request.form['breakfastday'],
                         request.form['lunchorder'], request.form['lunchday'], request.form['dinnerorder'], request.form['dinnerday'])
            return render_template("home.html")
    return render_template("mealprep.html")


def AddMealOrder(username, p, eccv, b, bday, l, lday, d, dday):
    connection = sqlite3.connect("hca.db")
    connection.execute('INSERT INTO MealOrders(UserName, CardNumber, ExpCCV, Breakfast, BreakfastDays, Lunch, LunchDays, Dinner, DinnerDays) VALUES(?,?,?,?,?,?,?,?,?)',
                       (username, p, eccv, b, bday, l, lday, d, dday))
    connection.commit()


@app.route('/groceryorder/', methods=['GET', 'POST'])
def groceryorder():
    connection = sqlite3.connect("hca.db")
    if request.method == 'POST':
        if "registerorder" in request.form:
            AddGroceryOrder(
                request.form['username'], request.form['item1'], request.form['item2'], request.form['item3'], request.form['item4'], request.form['item5'], request.form['item6'], request.form['item7'], request.form['item8'])
            return render_template("home.html")
    return render_template("groceryorder.html")


def AddGroceryOrder(username, i1, i2, i3, i4, i5, i6, i7, i8):
    connection = sqlite3.connect("hca.db")
    connection.execute('INSERT INTO GroceryOrders (UserName,Item1,Item2,Item3,Item4,Item5,Item6,Item7,Item8) VALUES(?,?,?,?,?,?,?,?,?)',
                       (username, i1, i2, i3, i4, i5, i6, i7, i8))
    connection.commit()


@app.route('/medicalorder/', methods=['GET', 'POST'])
def medicalorder():
    connection = sqlite3.connect("hca.db")
    if request.method == 'POST':
        if "regmedical" in request.form:
            AddMedicalOrder(request.form['username'], request.form['item1'], request.form['item2'], request.form['item3'],
                            request.form['item4'], request.form['item5'], request.form['item6'], request.form['item7'], request.form['item8'])
            return render_template("home.html")
    return render_template("medicalorder.html")


def AddMedicalOrder(username, i1, i2, i3, i4, i5, i6, i7, i8):
    connection = sqlite3.connect("hca.db")
    connection.execute(
        'INSERT INTO MedicalOrders (UserName, Item1,Item2,Item3,Item4,Item5,Item6,Item7,Item8 ) VALUES(?,?,?,?,?,?,?,?,?)', (username, i1, i2, i3, i4, i5, i6, i7, i8))
    connection.commit()


@app.route('/login/', methods=['GET', 'POST'])
def login():
    connection = sqlite3.connect("hca.db")
    if request.method == 'POST':
        if "logIn" in request.form:
            UserLogIn(request.form['username'], request.form['psw'])
            return render_template("home.html")
    return render_template("login.html")


def UserLogIn(username, Password):
    connection = sqlite3.connect("hca.db")
    if connection.execute('SELECT EXISTS(SELECT * FROM Users WHERE UserName=username)'):
        if connection.execute('SELECT EXISTS(SELECT * FROM Users WHERE Password=Password)'):
            print("Log In Successful")
    else:
        print("Log In Unsuccessful")


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    connection = sqlite3.connect("hca.db")
    if request.method == 'POST':
        if "submit" in request.form:
            RegisterPatient(
                request.form['name'], request.form['username'], request.form['psw'], request.form['email'], request.form['phone'], request.form['address'], request.form['age'], request.form['height'], request.form['weight'], request.form['allergies'], request.form['medicalcondition'], request.form['prescription'],)
            return render_template("home.html")
    return render_template("signup.html")


def RegisterPatient(FullName, username, Password, Email, Phone, Address, Age, Height, Weight, Allergy, MedicalCondition, Prescription):
    connection = sqlite3.connect("hca.db")
    connection.execute(
        'INSERT INTO Patients (Name, UserName, Password, Email, Phone, Address, Age, Height, Weight, Allergy, MedicalConditions, Prescriptions) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', (FullName, username, Password, Email, Phone, Address, Age, Height, Weight, Allergy, MedicalCondition, Prescription))
    connection.execute(
        'INSERT INTO Users(UserName, Password) VALUES(?,?)', (username, Password))
    connection.commit()
