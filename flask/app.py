from pickle import TRUE
from flask import Flask, render_template, request, flash,redirect, url_for, session
import mysql.connector as mysql
import re
from werkzeug.security import generate_password_hash, check_password_hash
from func import predict_label
from datetime import datetime

#database connection
conn = mysql.connect(host='localhost', database = 'projectdrone', user='root', password = 'root')
cur = conn.cursor()

app = Flask(__name__)
app.secret_key ="abcde"

#################################################general route################################################################

@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/classify")
def classify():
    return render_template("users/classify.html", id = session['id'])

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/shipping")
def shipping():
    return render_template("shipping.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/returnpolicy")
def returnpolicy():
    return render_template("returnpolicy.html")

@app.route("/portal")
def portal():
    
    cur.execute("SELECT * FROM info ORDER BY info_id DESC")
    info = cur.fetchall()
    
    return render_template("portal.html", info = info)

@app.route("/logout", methods = ['GET', 'POST'])
def logout():
    
    session.clear()
    return redirect(url_for('main'))

@app.route("/contact",methods = ['GET', 'POST'])
def contact():
    
    msg = ''
    if request.method == 'POST'  and'name' in request.form and 'email' in request.form and 'topic' in request.form and 'comment' in request.form:
        name = request.form['name']
        email = request.form['email']
        topic = request.form['topic']
        comment = request.form['comment']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cur.execute('INSERT INTO contact VALUES (NULL, %s, %s, %s, %s, %s)', (name ,email, topic, comment, timestamp ))
        conn.commit()
        msg = 'Message Submitted!'
    return render_template("contact.html", msg=msg)


########################################################admin####################################################################

#auth
@app.route("/admin_login", methods = ['GET', 'POST'])
def admin_login():
    
    msg = ''
    if request.method == 'POST' and  'email' in request.form and 'pass' in request.form:
        email = request.form['email']
        pwd = request.form['pass']
        cur= conn.cursor()
        cur.execute('SELECT * FROM admin WHERE email = %s AND pass = %s', (email, pwd))
        admin = cur.fetchone()
        if admin:
            session['loggedin'] = True
            session['admin_id'] = admin[0]
            session['email'] = admin[2]
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect email or password !'
    return render_template('admin/login.html', msg = msg)

@app.route("/admin_register", methods = ['GET', 'POST'])
def admin_register():
    msg = ''
    if request.method == 'POST'  and'uname' in request.form and 'pass' in request.form and 'email' in request.form :
        uname = request.form['uname']
        pwd = request.form['pass']
        email = request.form['email']
        cur.execute('SELECT * FROM admin WHERE uname = %s', (uname, ))
        account = cur.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', uname):
            msg = 'Username must contain only characters and numbers !'
        elif not uname or not pwd or not email:
            msg = 'Please fill out the form !'
        else:
            cur.execute('INSERT INTO admin VALUES (NULL, %s, %s, %s)', (email, uname, pwd ))
            conn.commit()
            msg = 'Account Created!'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('admin/register.html', msg = msg)

#info function
@app.route("/addinfo", methods = ['GET', 'POST'])
def addinfo():
    
    msg=''
    cur.execute("SELECT * FROM info ORDER BY info_id DESC") 
    info = cur.fetchall() 
    
    if request.method == 'POST' and'num' in request.form and 'info_image' in request.files and 'description' in request.form and 'info_topic' in request.form and 'title' in request.form:
        num = request.form['num']        
        info_image = request.files['info_image']
        description = request.form['description']
        info_topic = request.form['info_topic']
        title = request.form['title']
        img_path = "static/image/" + info_image.filename	
        info_image.save(img_path)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("INSERT INTO info VALUES (NULL, %s, %s,%s,%s,%s, %s)", (num, title,img_path, description, info_topic, timestamp ))
        conn.commit()
        
        msg ='Posted Successfully'  
        cur.execute("SELECT * FROM info ORDER BY info_id DESC") 
        info = cur.fetchall()  
 
    return render_template("admin/editinfo.html", info=info,  id = session['admin_id'], msg =msg)

@app.route('/deleteinfo/<string:id>', methods =['GET'])
def deleteinfo(id):
    cur.execute("DELETE FROM info WHERE info_id= {0}".format(id))
    conn.commit()
    flash('Data Deleted Successfully')
    
    return redirect(url_for('addinfo'))

@app.route('/editinfo', methods =['POST'])
def editinfo():
    
    if request.method == 'POST':
        info_id= request.form['id']
        num = request.form['num']        
        info_image = request.files['info_image']
        description = request.form['description']
        info_topic = request.form['info_topic']
        title = request.form['title']
        img_path = "static/image/" + info_image.filename	
        info_image.save(img_path)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        cur.execute("UPDATE info set num=%s, title=%s, image=%s, description=%s, info_topic=%s , timestamp_post=%s WHERE info_id= %s", (num, title,img_path, description, info_topic, timestamp, info_id,))
        conn.commit()
        
        flash('Data Updated Successfully')
        return redirect(url_for('addinfo'))
    
#data function
@app.route("/data")
def data():
    cur.execute('SELECT c.id , c.image, c.result, c.timestamp, u.email FROM dat as c, users as u WHERE u.id = c.user_id')
    disease = cur.fetchall()
    return render_template("admin/data.html", disease=disease, id = session['admin_id'])

@app.route('/admin_deletedata/<string:id>', methods =['GET'])
def admin_deletedata(id):
    cur.execute("DELETE FROM dat WHERE id= {0}".format(id))
    conn.commit()
    flash('Data Deleted Successfully')
    
    return redirect(url_for('data'))

@app.route('/editdata', methods =['POST'])
def editdata():
    
    if request.method == 'POST':
        id= request.form['id']
        result =request.form['result']     
        cur.execute("UPDATE dat set result=%s WHERE id= %s", (result,id,))
        conn.commit()
        
        flash('Data Updated Successfully')
        return redirect(url_for('data'))

#user function

@app.route("/userlist")
def userlist():
    cur.execute('SELECT * FROM users')
    userlist = cur.fetchall()
    return render_template("admin/userlist.html",userlist=userlist, id = session['admin_id'])

@app.route('/deleteuser/<string:id>', methods =['GET'])
def deleteuser(id):
    cur.execute("DELETE FROM users WHERE id= {0}".format(id))
    conn.commit()
    flash('Data Deleted Successfully')
    
    return redirect(url_for('userlist'))

@app.route('/edituser', methods =['POST'])
def edituser():
    
    if request.method == 'POST' and  'email' in request.form and 'uname' in request.form:
        id= request.form['id']
        uname = request.form['uname']
        email = request.form['email']
        
        cur.execute("UPDATE users set email=%s, uname=%s WHERE id= %s", (email, uname,id,))
        conn.commit()
        
        flash('Data Updated Successfully')
        return redirect(url_for('userlist'))



#query function

@app.route("/query")
def query():
    cur.execute('SELECT * FROM contact')
    query = cur.fetchall()
    return render_template("admin/query.html",query=query, id = session['admin_id'])

@app.route('/deletequery/<string:id>', methods =['GET'])
def deletequery(id):
    cur.execute("DELETE FROM contact WHERE id= {0}".format(id))
    conn.commit()
    flash('Data Deleted Successfully')
    
    return redirect(url_for('query'))

@app.route("/adminprofile")
def adminprofile():
    id = session['admin_id']
    cur.execute("SELECT * FROM admin where admin_id= %s",(id,))
    admin = cur.fetchall()
        
    return render_template("admin/profile.html", id = session['admin_id'], admin=admin)



#################################################################user################################################################

#auth

@app.route("/profile")
def profile():
    id = session['id']
    cur.execute("SELECT * FROM users where id= %s",(id,))
    user = cur.fetchall()
        
    return render_template("users/profile.html", id = session['id'], user=user)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and  'email' in request.form and 'pwd' in request.form:
        email = request.form['email']
        pwd = request.form['pwd']
        cur.execute('SELECT * FROM users WHERE email = %s AND pwd = %s', (email, pwd))
        user = cur.fetchone()
        if user:
            session['loggedin'] = True
            session['id'] = user[0]
            session['email'] = user[2]
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect email or password !'
    return render_template('users/login.html', msg = msg)
 
@app.route("/register", methods = ['GET', 'POST'])
def register():
    msg = ''

    if request.method == 'POST'  and'uname' in request.form and 'pwd' in request.form and 'email' in request.form :
        uname = request.form['uname']
        pwd = request.form['pwd']
        email = request.form['email']
        cur.execute('SELECT * FROM users WHERE uname = %s', (uname, ))
        account = cur.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', uname):
            msg = 'Username must contain only characters and numbers !'
        elif not uname or not pwd or not email:
            msg = 'Please fill out the form !'
        else:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cur.execute('INSERT INTO users VALUES (NULL, %s, %s, %s, %s)', (email, uname, pwd, timestamp ))
            conn.commit()
            msg = 'Account Created!'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('users/register.html', msg = msg)

#classify history
@app.route("/hist")   
def display():
    id = session['id']
    cur.execute('SELECT * FROM dat WHERE user_id = %s ORDER BY timestamp DESC ', (id, ))
    data = cur.fetchall()
    
    return render_template("users/hist.html", data = data, id = session['id'])

@app.route('/delete/<string:id>', methods =['GET'])
def delete(id):
    cur.execute("DELETE FROM dat WHERE id= {0}".format(id))
    conn.commit()
    flash('Data Deleted Successfully')
    
    return redirect(url_for('display'))

#classify function
@app.route("/submit", methods = ['GET', 'POST']) # get image and produce output
def get_output():
    
    # get image and save it in a folder
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = "static/uploaded_img/" + img.filename	
        img.save(img_path)

        p = str(predict_label(img_path)) #predict the image
        
        if conn.is_connected():
            id = session['id']
            
            sql = "INSERT INTO dat(user_id,image,result) VALUES (%s,%s,%s)"
            cur.execute(sql, (id,img_path, p))
            print("Record inserted")
            conn.commit()        
        
        return render_template("users/classify.html", prediction = p, img_path = img_path, id = session['id'])


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)

