from tkinter import *
import pymysql
import requests


global screen
screen = Tk()

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()


##database connection

connection = pymysql.connect(host='192.168.64.2',
                             user='root',
                             password='pass',
                             db='quizzler',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
if (connection):
    print("connected")
else:
    print("error")

#######################################################################


##Fetching data from API

data = requests.get("https://opentdb.com/api.php?amount=5&type=boolean"
                    ).json()
results = data['results']
results = data['results']

questions = []
answers = []

for i in range(0, 5):
    questions.append(results[i]['question'])
    answers.append(results[i]['correct_answer'])
question_bank = dict(zip(questions, answers))

#######################################################################


# User Registration in database
def register_user():
    try:
        with connection.cursor() as cursor:
            username_info = username.get()
            email_info = email.get()
            password_info = password.get()
            sql = "INSERT INTO `signupdetails` (`uname`, `email`,`psw`) VALUES (%s, %s ,%s)"
            cursor.execute(sql, (username_info, email_info, password_info))
            print("record inserted")
            connection.commit()

    finally:
        connection.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)

    Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()

    #######################################################################

# Register Form
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("500x500")

    global username
    global password
    global email
    global username_entry
    global password_entry
    global email_entry

    username = StringVar()
    password = StringVar()
    email = StringVar()
    Label(screen1, text="Welcome to quizzler").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Email * ").pack()
    email_entry = Entry(screen1, textvariable=email)
    email_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def delete2():
    screen3.destroy()


def delete4():
    screen5.destroy()


#######################################################################

#Checking users answers and result screen
def validate():
    score = []
    value1 = str(var1.get())
    value2 = str(var2.get())
    value3 = str(var3.get())
    value4 = str(var4.get())
    value5 = str(var5.get())

    print(answers[0])
    print(answers[1])
    print(answers[2])
    print(answers[3])
    print(answers[4])

    print("answers")

    if value1 == answers[0]:
        score.append(10)
    else:
        score.append(0)
    print(value1, score)

    if value2 == answers[1]:
        score.append(10)
    else:
        score.append(0)
    print(value2, score)

    if value1 == answers[2]:
        score.append(10)
    else:
        score.append(0)
    print(value3, score)

    if value1 == answers[3]:
        score.append(10)
    else:
        score.append(0)
    print(value4, score)

    if value1 == answers[4]:
        score.append(10)
    else:
        score.append(0)
    print(value5, score)

    sumTotal = 0

    for i in score:
        sumTotal = sumTotal + i

    print(sumTotal)

    screen6.destroy()
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Score")
    screen7.geometry("300x300")
    Label(screen7, text="Your Final Score is :", bg="grey", width="300", height="5", font=("Calibri", 12)).pack()
    Label(screen7, text=sumTotal, bg="grey", height="3", width="300").pack()
    Button(screen7, text="Restart", bg="grey", width="300", height="2", font=("Calibri", 12),
           command=start_quiz).pack()
    Button(screen7, text="Home Page", bg="grey", width="300", height="2", font=("Calibri", 12),
           command=login_sucess).pack()
    del score[0:4]



    #######################################################################

#Quiz main screen
def start_quiz():
    screen3.destroy()


    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Quizzler")
    screen6.geometry("1000x1100")
    Label(screen6, text="Welcome to Quizzler", bg="grey", width="500", height="2", font=("Calibri", 12)).pack()
    trueButton = Button(screen6, text="true")
    falseButton = Button(screen6, text="false")
    Label(screen6, text="").pack()
    Label(screen6, text="").pack()

    questionLabel1 = Label(screen6, text="sample question")
    questionLabel1['text'] = questions[0]
    questionLabel1.pack()
    R1 = Radiobutton(screen6, text="TRUE", value="True", var=var1).pack()
    R2 = Radiobutton(screen6, text="FALSE", value="False", var=var1).pack()

    Label(screen6, text="").pack()

    questionLabel2 = Label(screen6, text="sample question")
    questionLabel2['text'] = questions[1]
    questionLabel2.pack()
    R3 = Radiobutton(screen6, text="TRUE", value="True", variable=var2, ).pack()
    R4 = Radiobutton(screen6, text="FALSE", value="False", variable=var2, ).pack()

    Label(screen6, text="").pack()

    questionLabel3 = Label(screen6, text="sample question")
    questionLabel3['text'] = questions[2]
    questionLabel3.pack()
    R5 = Radiobutton(screen6, text="TRUE", value="True", variable=var3, ).pack()
    R6 = Radiobutton(screen6, text="FALSE", value="False", variable=var3, ).pack()

    Label(screen6, text="").pack()

    questionLabel4 = Label(screen6, text="sample question")
    questionLabel4['text'] = questions[3]
    questionLabel4.pack()
    R7 = Radiobutton(screen6, text="TRUE", value="True", variable=var4, ).pack()
    R8 = Radiobutton(screen6, text="FALSE", value="False", variable=var4, ).pack()

    Label(screen6, text="").pack()

    questionLabel5 = Label(screen6, text="sample question")
    questionLabel5['text'] = questions[4]
    questionLabel5.pack()
    R9 = Radiobutton(screen6, text="TRUE", value="True", variable=var5, ).pack()
    R10 = Radiobutton(screen6, text="FALSE", value="False", variable=var5, ).pack()

    Label(screen6, text="").pack()
    Label(screen6, text="").pack()

    submitButton = Button(screen6, text="Submit", bg="grey", width="500", height="2", font=("Calibri", 12),
                          command=validate).pack()




    #######################################################################

##Home screen
def login_sucess():
    screen2.destroy()
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Quizzler")
    screen3.geometry("500x500")
    Label(screen3, text="Welcome to Quizzler", bg="grey", width="500", height="5", font=("Calibri", 25)).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="SIZZLER FOR YOUR BRAIN").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="START QUIZ").pack()
    Button(screen3, text="LET'S GO", bg="black", width="200", height="2", command=start_quiz).pack()

#######################################################################

#PAsswor or username incorrect

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Login Failure")
    screen5.geometry("300x300")
    Label(screen5, text="Your password or username is inncorrect").pack()
    Label(screen5, text="New User? ").pack()
    Button(screen5, text="Register", command=register).pack()




#######################################################################
#Checking users credentials

def login_verify():
    connection = pymysql.connect(host='192.168.64.2',
                                 user='root',
                                 password='pass',
                                 db='quizzler',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    if (connection):
        print("connected")
    else:
        print("error")

    user_verify = username_verify.get()
    pass_verify = password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    try:
        with connection.cursor() as cursor:

            ul = []
            pl = []
            sql = "select * from signupdetails    "
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                ul.append(i['uname'])
                pl.append(i['psw'])
            print("yes")
            data = dict(zip(ul, pl))
            if user_verify in data.keys():
                pswc = data[user_verify]
                if pswc == pass_verify:
                    print("yes1")
                    login_sucess()
                else:
                    print("no")
                    user_not_found()
            else:
                user_not_found()




    finally:
        connection.close()







#######################################################################

##Login UI
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


#######################################################################

#mainscreen UI
def main_screen():
    screen.geometry("300x250")
    screen.title("Quizzler")
    Label(text="Quizzler", bg="grey", width="300", height="2", font=("Calibri", 15)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()
