from flask import Flask, request, render_template


from model import model1
app = Flask(__name__)

# MySQL Configuration
# mydb =  mysql.connector.connect(host="localhost", user="root", passwd="nopassword")
# mycursor = mydb.cursor()
# mycursor.execute("USE medihelp")

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/submiter', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        user_name = request.form.get('username')
        password = request.form.get('password')
        
        # Use a parameterized query to avoid SQL injection
        # mycursor.execute("SELECT password FROM authenticator WHERE user_name = %s", (user_name,))
        # data = mycursor.fetchall()
        
        if model1.authentication(user_name,password)==True:
            return render_template('home.html')
        else:
            return render_template('index.html', data="Invalid credentials")
@app.route('/form1',methods=['GET','POST'])
def form123():
    return render_template('form1.html')
@app.route('/form2',methods=['GET','POST'])
def form456():
    return render_template('form2.html')
@app.route('/form3',methods=['GET','POST'])
def form789():
    return render_template('form3.html')
@app.route('/submit2',methods=['GET','POST'])
def submition2():
    name = request.form.get('name')
    age = request.form.get('age')
    cause = request.form.get('cause')
    doctor = request.form.get('doc')

    ticket = model1.appointment(name,age,cause,doctor)
    return render_template('form1.html',data=ticket)
@app.route('/upload_location',methods=['GET','POST'])
def upload_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    print(latitude,longitude)

    ans = model1.apiing(latitude,longitude)
    print(ans)
    return render_template('form2.html',data2=ans)


if __name__ == '__main__':
    app.run(debug=True)
