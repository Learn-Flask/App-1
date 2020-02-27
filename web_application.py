from flask import Flask,url_for,render_template,redirect,request,flash

user_info=[("daniel","1234","guest"),("praveen","1234","Admin")]


app=Flask(__name__)
app.secret_key='danielmuthupandi'


@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/check_user/<username>,<password>/')
def validate_user(username,password):
    global user_info
    for each in user_info:
        if (each[0]==username) and (each[1]==password):
            if each[2]=="guest":
                flash("Guest user found")
                return render_template('guest_page.html')
                flash("Guest page re-direction initiated")
            
            if each[2]=="Admin":
                flash("Admin user found")
                return render_template('admin_page.html')
                flash("Admin page re-direction initiated")

    flash("User not found / Check username and password")
    return render_template('incorrect_user.html')
                

@app.route('/adduser/<username>,<password>,<usertype>')
def add_user(username,password,usertype):
    global user_info
    user_info.append((username,password,usertype))
    flash("new user added into user_info list")
    return render_template('Home.html')

@app.route('/addnewuserinfo',methods=['POST','GET'])
def new_user_info():
    if request.method=='POST':
        newbee_username=request.form['nm']
        newbee_password=request.form['pwd']
        newbee_usertype=request.form['usertype']
        flash("new user details collected")
        return redirect(url_for('add_user',username=newbee_username,password=newbee_password,usertype=newbee_usertype))
    if request.method=='GET':
        newbee_username=request.args.get('nm')
        newbee_password=request.args.get('pwd')
        newbee_usertype=request.args.get('usertype')
        flash("new user details collected")
        return redirect(url_for('add_user',username=newbee_username,password=newbee_password,usertype=newbee_usertype))

@app.route('/New_user_adding')
def new_user_adding():
    flash("new user add process started")
    return render_template('new_user.html')

@app.route('/show_all_users')
def all_users():
    all_users_list=[each[0] for each in user_info]
    return render_template('show_all_user.html',result=all_users_list)

@app.route('/check_login',methods=['POST'])
def login_credential():
    name=request.form['nm']
    password=request.form['pwd']
    flash("Username and password collected")
    return redirect(url_for('validate_user',username=name,password=password))

if __name__=="__main__":
    app.run(debug=True)
