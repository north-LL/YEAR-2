from guizero import App, Window, PushButton, Text, CheckBox, ListBox, TextBox, ButtonGroup, Picture, Combo, Box, info
import sqlite3
import os
import os.path
# Define the DDL SQL 
sql = """
CREATE TABLE "user" (
	"userID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"username"	TEXT,
	"userpword"	TEXT,
	'userfirstname' TEXT,
	'usersurname' TEXT,
	'useremail' TEXT
);
CREATE TABLE 'reviews' (
	'reviewID' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'reviewtest' TEXT,
	'userID' INTEGER,
	FOREIGN KEY(userID) REFERENCES user(userID)
);
insert into user (username, userpword, userfirstname, usersurname, useremail) values ('joe', 'joeiscool', 'joe', 'fanshaw', 'joefanshaw@email.com');
insert into reviews (reviewtest) values ('This place was great ****/*****');
"""
#
# global database name
#
database_file = 'reviews.db'
# Delete the database
# in case it already exists
#
if os.path.exists(database_file):
  os.remove(database_file)
#
# Connect to the database
#
conn = sqlite3.connect(database_file)
# Get a cursor pointing to the database
cursor = conn.cursor()
# Create the tables
cursor.executescript(sql)
# Commit to save everything
conn.commit()
#Queries the database using the database parameter as the database
#to query and the query parameter as the actual query to issue
# for SELECT
#
def query_database(database, query):
	Lconn = sqlite3.connect(database)
	cur = Lconn.cursor()			# use a local cursor
	cur.execute(query)
	rows = cur.fetchall()
	cur.close()
	return rows
#
#
#Executes the sql statement to INSERT and UPDATE rows
#
def execute_sql(database, sql_statement, params=()):
    with sqlite3.connect(database) as conn:
        cur = conn.cursor()
        cur.execute(sql_statement, params)
        conn.commit()
    return cur.lastrowid
#
# NAVIGATION
#
def open_signup():
	#This removes all the text that was in the text boxes
	app.hide()
	signup_txtbox1.clear()
	signup_txtbox2.clear()
	signup_txtbox3.clear()
	signup_txtbox4.clear()
	signup_txtbox5.clear()
	signup_window.show()
#
def close_signup():
	#This makes sure that the signup window isnt visible straight away
	app.show()
	signup_window.hide()
#
def	create_user_validation():
	#This makes sure that the create user has been validated
	signup_username = signup_txtbox1.value
	signup_password = signup_txtbox2.value
	signup_firstname = signup_txtbox3.value
	signup_surname = signup_txtbox4.value
	signup_email = signup_txtbox5.value
	
	if signup_username.isalpha() == False:
		info('Error','Username cannot contain numbers or special characters')
	elif signup_firstname.isalpha() == False:
		info('Error','Username cannot contain numbers or special characters')
	elif signup_surname.isalpha() == False:
		info('Error','Username cannot contain numbers or special characters')
	elif '@' not in signup_email:
		info('Error','Email must contain the @ symbol')
	else:
		create_user()
#
def create_user():
	query = 'INSERT INTO user (username, userpword, userfirstname, usersurname, useremail) VALUES (?, ?, ?, ?, ?)'
	execute_sql(database_file, query, (signup_txtbox1.value, signup_txtbox2.value, signup_txtbox3.value, signup_txtbox4.value, signup_txtbox5.value))
	info('Sucess','user created')
	close_signup()
#
def back_button():
	signup_window.hide()
	review.hide()
	usertextbox.clear()
	pwtextbox.clear()
	app.show()
#
# login sql
#
def login_user():  #### TEST WITH 'or 1 = 1; -- 
	global user_LoggedIn ## variable needed to know who logged in ##
	if usertextbox.value == "":
		info("Error", "You must enter a valid username")
	elif pwtextbox.value == "":
		info("Error", "You must enter a password")
	else:
		sqlselect= "SELECT * FROM user WHERE username = '"+usertextbox.value+"'"
		rows = query_database(database_file, sqlselect)
		if len(rows)== 0:
			info('Error', 'Error')
		else:
			sqlselect= "SELECT * FROM user WHERE userpword = '"+pwtextbox.value+"'"
			rows = query_database(database_file, sqlselect)
			if len(rows)== 0:
				info('Error','Error')
			else:
				app.hide()
				review.show()
#
#
#
#################################
# LOGIN                         #
#################################
app = App(title='Review Central', height=400)
blanktext = Text(app, text='                                   ')
toptext = Text(app, text='    Welcome to Review Central     ')
blanktext = Text(app, text='                                   ')
box1 = Box(app, layout='grid')
#
blanktext = Text(box1, text='      ',grid=[1,0])
text1 = Text(box1, text='Enter Username:', align='left', grid=[0,0])
usertextbox = TextBox(box1, hide_text=False, align='left',grid=[2,0], width=25)
#
blanktext = Text(box1, text='      ',grid=[1,1])
text2 = Text(box1, text='Enter Password:', align='left', grid=[0,1])
pwtextbox = TextBox(box1, hide_text=True, align='left',grid=[2,1], width=25)
#
box2 = Box(app, layout='grid')
loginbutton = PushButton(box2, text='login', command=login_user, grid=[0,0])
signupbutton = PushButton(box2, text='Sign Up', command=open_signup, grid=[0,1])
#
box3 = Box(app, width='fill', align='bottom')
exitbutton = PushButton(box3, text='Exit', command=exit, align='left')
#
##############################
# SIGN UP                    #
##############################
signup_window=Window(app, title="Sign Up")
signup_window.hide()
signup_exit_box = Box(signup_window, width="fill", align="top")
signup_exit_button = PushButton(signup_exit_box, text="Cancel", align="left", command=close_signup)
signup_toptxt1 = Text(signup_window, text="                                   ")
signup_toptxt2 = Text(signup_window, text="      Please Enter Details         ", size=15)
signup_toptxt3 = Text(signup_window, text="                                   ")

signup_box1 = Box(signup_window, layout="grid")

signup_blanktxt1 = Text(signup_box1, text="            ", grid=[1,0])
signup_txt1 = Text(signup_box1, text="Enter Username", align="left", grid=[0,0])
signup_txtbox1 = TextBox(signup_box1, hide_text=False, align="left", grid=[2,0], width=20)

signup_blanktxt2 = Text(signup_box1, text="            ", grid=[1,1])
signup_txt2 = Text(signup_box1, text="Enter Password", align="left", grid=[0,1])
signup_txtbox2 = TextBox(signup_box1, hide_text=True, align="left", grid=[2,1], width=20)

signup_blanktxt3 = Text(signup_box1, text="            ", grid=[1,2])
signup_txt3 = Text(signup_box1, text="Enter First Name", align="left", grid=[0,2])
signup_txtbox3 = TextBox(signup_box1, hide_text=False, align="left", grid=[2,2], width=20)

signup_blanktxt4 = Text(signup_box1, text="            ", grid=[1,3])
signup_txt4 = Text(signup_box1, text="Enter Surname", align="left", grid=[0,3])
signup_txtbox4 = TextBox(signup_box1, hide_text=False, align="left", grid=[2,3], width=20)

signup_blanktxt5 = Text(signup_box1, text="            ", grid=[1,4])
signup_txt5 = Text(signup_box1, text="Enter Email", align="left", grid=[0,4])
signup_txtbox5 = TextBox(signup_box1, hide_text=False, align="left", grid=[2,4], width=20)

signup_box2 = Box(signup_window, layout="grid")
signup_window_button = PushButton(signup_box2, text="Sign Up", command=create_user_validation, grid=[0,0])
#
#										 
#
###############################
# REVIEW WINDOW               #
###############################
review = Window(app, 'Please Write a Review')
review.hide()
blanktext = Text(review, text='                                ')
toptext1 = Text(review, text='  Please Write a Review        ')
blanktext = Text(review, text='                                ')
box4 = Box(review, layout='grid')
#
box4 = Box(review, width='fill', align='bottom')
exitbutton = PushButton(box4, text='Exit', command=exit, align='left')
reviewtextbox = TextBox(review, width='fill', height='fill', multiline=True)
backbutton = PushButton(box4, text='Back', command=back_button, align='left')
#
#
#
#
app.display()
