from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from model import model
from classes import user, student, employee
from flask_session import Session
import random
import smtplib
obj = model("localhost", "root", "1234", "jobcode")
app = Flask(__name__, static_folder="static")
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
Session(app)
app.secret_key = "bsjvhusdhg5565645"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USERNAME = 'deebaumar02@gmail.com'
EMAIL_PASSWORD = 'mdeszqmjqumqgmjx'
#dsa answers
correct_answers_dsa1 = {
            'Q1': '2',
            'Q2': '3',
            'Q3': '2',
            'Q4': '1',
            'Q5': '4',
            'Q6': '1',
            'Q7': '4',
            'Q8': '3',
            'Q9': '4',
            'Q10': '1',
        }
correct_answers_dsa2 = {
            'Q1': '2',
            'Q2': '4',
            'Q3': '1',
            'Q4': '2',
            'Q5': '3',
            'Q6': '4',
            'Q7': '3',
            'Q8': '4',
            'Q9': '3',
            'Q10': '1',
        }
#dbs answers:
correct_answers_dbs1 = {
    'Q1': '3',
    'Q2': '3',
    'Q3': '3',
    'Q4': '2',
    'Q5': '1',
    'Q6': '3',
    'Q7': '4',
    'Q8': '2',
    'Q9': '2',
    'Q10': '1',
}
correct_answers_dbs2 = {
    'Q1': '2',
    'Q2': '3',
    'Q3': '3',
    'Q4': '2',
    'Q5': '4',
    'Q6': '1',
    'Q7': '4',
    'Q8': '3',
    'Q9': '1',
    'Q10': '2',
}
#os answers
correct_answers_os1 = {
            'Q1': '4',
            'Q2': '2',
            'Q3': '1',
            'Q4': '4',
            'Q5': '1',
            'Q6': '2',
            'Q7': '1',
            'Q8': '2',
            'Q9': '3',
            'Q10': '1',
        }
correct_answers_os2 = {
            'Q1': '3',
            'Q2': '2',
            'Q3': '1',
            'Q4': '2',
            'Q5': '2',
            'Q6': '4',
            'Q7': '2',
            'Q8': '3',
            'Q9': '2',
            'Q10': '2',
        }

#cn answers
correct_answers_cn = {
            'Q1': '4',
            'Q2': '3',
            'Q3': '4',
            'Q4': '1',
            'Q5': '1',
            'Q6': '1',
            'Q7': '3',
            'Q8': '1',
            'Q9': '1',
            'Q10': '1',
        }


@app.route("/")
def root():
    if session.get("id") is None and session.get("id2") is None:
        return render_template("index.html")
    else:
        return render_template("index2.html")


@app.route("/login/form")
def loginForm():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    try:
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]
        u1 = user(email, password)
        if role == "interviewer":
            if obj.searchUser(u1):
                session["id"] = obj.searchInterviewerID(u1)
                session["email"] = email
                return render_template("index2.html")
            elif obj.searchMail(email) is True and obj.searchUser(u1) is False:
                message = 'Incorrect password entered!'
                return render_template("login.html", msg2=message)
            else:
                message = 'No such user exists. TRY AGAIN'
                return render_template("login.html", msg=message)
        else:
            if obj.searchUser2(u1):
                session["id2"] = obj.searchIntervieweeID(u1)
                session["email"] = email
                return render_template("index2.html")
            elif obj.searchMail2(email) is True and obj.searchUser2(u1) is False:
                message = 'Incorrect password entered!'
                return render_template("login.html", msg2=message)
            else:
                message = 'No such user exists. TRY AGAIN'
                return render_template("login.html", msg=message)
    except Exception as e:
        print(str(e))


@app.route("/signup/form")
def signupForm():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup():
    try:
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]
        u1 = user(email, password)
        if role == "interviewer":
            if obj.uniqueIntervieweeEmail(email):
                message = "Sorry you can't signup as an Interviewer with this account!"
                return render_template("signup.html", msg=message)
            elif obj.searchMail(email) is True:
                message = "This account already exists!"
                return render_template("signup.html", msg=message)
            elif len(password) < 8:
                message = "Password should be 8 characters long."
                return render_template("signup.html", msg2=message)
            elif obj.insertUser(u1):
                session["id"] = obj.searchInterviewerID(u1)
                session["email"] = email
                return render_template("InterviewerSignup.html")
        elif role == "interviewee":
            if obj.uniqueInterviewerEmail(email):
                message = "Sorry you can't signup as an Interviewee with this account!"
                return render_template("signup.html", msg=message)
            elif obj.searchMail2(email) is True:
                message = "This account already exists!"
                return render_template("signup.html", msg=message)
            elif len(password) < 8:
                message = "Password should be 8 characters long."
                return render_template("signup.html", msg2=message)
            elif obj.insertUser2(u1):
                session["id2"] = obj.searchIntervieweeID(u1)
                return render_template("IntervieweeSignup.html")
    except Exception as e:
        print(str(e))


@app.route("/data/interviewer", methods=['POST'])
def interviewer():
    try:
        name = request.form["name"]
        comp = request.form["company"]
        des = request.form["designation"]
        id_ = session["id"]
        print(name, des, comp, id_)
        emp = employee(name, des, comp, id_)
        if obj.insertInterviewer(emp):
            return render_template("index.html")
        else:
            message = "Signup Failed! TRY AGAIN"
            return render_template("signup.html", msg=message)
    except Exception as e:
        print(str(e))


@app.route("/data/interviewee", methods=['POST'])
def interviewee():
    try:
        name = request.form["name"]
        subj = request.form["major"]
        cgpa = request.form["cgpa"]
        uni = request.form["institute"]
        bio = request.form["bio"]
        id_ = session["id2"]
        print(name, subj, cgpa, uni, bio, id_)
        emp = student(name, subj, cgpa, uni, bio, id_)
        if obj.insertInterviewee(emp):
            return render_template("index.html")
        else:
            message = "Signup Failed! TRY AGAIN"
            return render_template("signup.html", msg=message)
    except Exception as e:
        print(str(e))


@app.route("/about")
def about():
    if session.get("id") is None and session.get("id2") is None:
        return render_template("about.html")
    else:
        return render_template("about2.html")


@app.route("/competition")
def competition():
    if session.get("id") is None and session.get("id2") is None:
        return render_template("competition.html")
    else:
        return render_template("competition2.html")


@app.route("/contact")
def contact():
    if session.get("id") is None and session.get("id2") is None:
        return render_template("contact.html")
    else:
        return render_template("contact2.html")


# the feedback will be added to database
@app.route('/feedback', methods=['POST'])
def feedback():
    try:
        if request.method == 'POST':
            feed = request.form['feedback']
            with open('feedback.txt', 'a') as file:
                file.write(feed + '\n')
            msg = "Thank you for your feedback!"
            return render_template("contact.html", msg=msg)
        else:
            render_template("contact.html")
    except Exception as e:
        print(str(e))
        return render_template("contact.html")


@app.route("/interviews")
def interviews():
    if session.get("id") is None and session.get("id2") is None:
        return render_template("interviews.html")
    else:
        if session.get("id2") is not None:
            return render_template("services2.html", msg='Access Denied')
        if session.get("id") is None:
            return render_template("login.html", msg='First Login here!')
        else:
            interviewers = obj.cards()
            return render_template("interviews2.html", interviewees=interviewers)


@app.route("/optimization")
def optimization():
    if session.get("id") is None and session.get("id2") is None:
        return render_template("optimization.html")
    else:
        return render_template("optimization2.html")


@app.route("/safety")
def safety():
    if session.get("id") is None and session.get("id2") is None:
        return render_template("safety.html")
    else:
        return render_template("safety2.html")


@app.route("/security")
def security():
    if session.get("id") is None and session.get("id2") is None:
        return render_template("security.html")
    else:
        return render_template("security2.html")


@app.route("/services")
def services():
    if session.get("id") is None and session.get("id2") is None:
        return render_template("services.html")
    else:
        return render_template("services2.html")


@app.route('/dbs')
def dbs():
    email = session.get("email")
    score = obj.checkDBS(email)
    subject = "Database Systems"
    if session.get("id2") is None:
        return render_template("login.html", msg='First Login here!')
    else:
        if score[0] is not None:
            return render_template("result.html", subject=subject, score=score[0])
        else:
            dbs = ['dbs1.html', 'dbs2.html']
            testno = random.randint(0, 1)
            session['dbstest'] = dbs[testno]
            if testno == 0:
                return render_template("dbs1.html")
            else:
                return render_template("dbs2.html")


@app.route('/dbstest', methods=['GET', 'POST'])
def quiz3():
    email = session.get("email")
    if session.get("id2") is not None:
        if request.method == 'POST':
            # Get user answers from the form
            user_answers = {}
            test_attempted = session['dbstest']
            if test_attempted == "dbs1.html":
                user_answers = {key: request.form.get(key) for key in correct_answers_dbs1.keys()}
                correct_answers = correct_answers_dbs1
            elif test_attempted == "dbs2.html":
                user_answers = {key: request.form.get(key) for key in correct_answers_dbs2.keys()}
                correct_answers = correct_answers_dbs2
            # Calculate the score
            score = sum(1 for key, value in user_answers.items() if value == correct_answers[key])
            session["score"] = score
            subject = "Database Management Systems"
            obj.insertDBS(email, score)
            # Store the score in the session
            return render_template("result.html", subject=subject, score=score)

        # Render the quiz template if it's a GET request
        return render_template("dbs2.html")


@app.route('/os')
def os():
    email = session.get("email")
    score = obj.checkOS(email)
    subject = "Operating System"
    if session.get("id2") is None:
        return render_template("login.html", msg='First Login here!')
    else:
        if score[0] is not None:
            return render_template("result.html", subject=subject, score=score[0])
        else:
            os = ['os1.html', 'os2.html']
            testno = random.randint(0, 1)
            session['ostest'] = os[testno]
            if testno == 0:
                return render_template("os1.html")
            else:
                return render_template("os2.html")


@app.route('/ostest', methods=['GET', 'POST'])
def quiz():
    email = session.get("email")
    print(email)
    if session.get("id2") is not None:
        if request.method == 'POST':
            # Get user answers from the form
            score = obj.checkOS(email)
            user_answers = {}
            test_attempted = session['ostest']
            if test_attempted == "os1.html":
                user_answers = {key: request.form.get(key) for key in correct_answers_os1.keys()}
                correct_answers = correct_answers_os1
            elif test_attempted == "os2.html":
                user_answers = {key: request.form.get(key) for key in correct_answers_os2.keys()}
                correct_answers = correct_answers_os2
            # Calculate the score
            score = sum(1 for key, value in user_answers.items() if value == correct_answers[key])
            session["score"] = score
            subject = "Operating Systems"
            obj.insertOs(email, score)
            # Store the score in the session
            return render_template("result.html", subject=subject, score=score)
    # Render the quiz template if it's a GET request
    return render_template("dsa1.html")


@app.route("/result")
def res():
    return render_template("result.html")


@app.route('/dsa')
def dsa():
    email = session.get("email")
    score = obj.checkDSA(email)
    subject = "Data Structures and Algorithms"
    if session.get("id2") is None:
        return render_template("login.html", msg='First Login here!')
    else:
        if score[0] is not None:
            return render_template("result.html", subject=subject, score=score[0])
        else:
            dsa = ['dsa1.html', 'dsa2.html']
            testno = random.randint(0, 1)
            session['dsatest'] = dsa[testno]
            if testno == 0:
                return render_template("dsa1.html")
            else:
                return render_template("dsa2.html")


@app.route('/dsatest', methods=['GET', 'POST'])
def quiz2():
    email = session.get("email")
    if session.get("id2") is not None:
        if request.method == 'POST':
            # Get user answers from the form
            user_answers = {}
            test_attempted = session['dsatest']
            if test_attempted == "dsa1.html":
                user_answers = {key: request.form.get(key) for key in correct_answers_dsa1.keys()}
                correct_answers = correct_answers_dsa1
            elif test_attempted == "dsa2.html":
                user_answers = {key: request.form.get(key) for key in correct_answers_dsa2.keys()}
                correct_answers = correct_answers_dsa2
            # Calculate the score
            score = sum(1 for key, value in user_answers.items() if value == correct_answers[key])
            session["score"] = score
            subject = "Data Structures"
            obj.insertDSA(email, score)
            # Store the score in the session
            return render_template("result.html", subject=subject, score=score)

        # Render the quiz template if it's a GET request
        return render_template("dsa1.html")


@app.route('/cn')
def cn():
    email = session.get("email")
    score = obj.checkCN(email)
    subject = "Computer Networks"
    if session.get("id2") is None:
        return render_template("login.html", msg='First Login here!')
    else:
        if score[0] is not None:
            return render_template("result.html", subject=subject, score=score[0])
        else:
            return render_template("CN.html")


@app.route('/cntest', methods=['GET','POST'])
def quizzz():
    email = session.get("email")
    if session.get("id2") is not None:
        if request.method == 'POST':
            # Get user answers from the form
            user_answers = {}
            user_answers = {key: request.form.get(key) for key in correct_answers_cn.keys()}
            correct_answers = correct_answers_cn
            score = sum(1 for key, value in user_answers.items() if value == correct_answers[key])
            session["score"] = score
            subject = "Computer Networks"
            obj.insertCN(email, score)
            # Store the score in the session
            return render_template("result.html", subject=subject, score=score)

        # Render the quiz template if it's a GET request
        return render_template("CN.html")


# the subscribers will be added to database for updates
@app.route('/subscribe', methods=['POST'])
def subs():
    try:
        em = request.form["email"]
        if em:
            print(em)
            if obj.subscribe(em):
                return render_template("index.html")

        return render_template("contact.html")

    except Exception as e:
        print(e)
        return render_template("index.html")


@app.route("/test")
def test():
    if session.get("id") is not None:
        return render_template("services2.html", msg='Access Denied')
    if session.get("id2") is None:
        return render_template("login.html", msg='First Login here!')
    else:
        return render_template("test2.html")


@app.route("/connect", methods=["GET"])
def connect():
    interviewee_id = request.args.get('interviewee_id')
    if interviewee_id:
        interviewee_email = obj.getEmail(interviewee_id)
        print( interviewee_email[0])
        # Send the email to the interviewee's email address
        if interviewee_email[0]:
            send_email(interviewee_email[0])
            return render_template("email.html", msg='Email sent successfully!')
        else:
            return render_template("email.html", msg='Interviewee not found!')
    else:
        return "Invalid request. Please provide an interviewee_id."


def send_email(email):
    subject = "Interview Invitation"
    body = "Dear candidate, you have been invited for an interview. Be prepared. Your interview will start at 4:00 pm today."
    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(EMAIL_USERNAME, email, message)

        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


#api datatable
@app.route("/datatable")
def table():
    if session.get("id") is None and session.get("id2") is not None:
        return render_template("login.html", msg='First Login as an interviewer here')
    if session.get("id2") is not None:
        return render_template("services2.html", msg='Access Denied')
    else:
        return render_template("datatable.html")


@app.route("/api/data")
def get_data():
    data_list = []
    data = obj.fetchData()
    for i in data:
        row = {"name": i[0], "subject": i[1], "cgpa": i[2], "institute": i[3], "bio": i[4]}
        data_list.append(row)
    return jsonify(data_list)


#api datatable
@app.route("/meeting")
def meet():
    if session.get("id") is None and session.get("id2") is not None:
        return render_template("login.html", msg='First Login as an interviewer here')
    if session.get("id2") is not None:
        return render_template("services2.html", msg='Access Denied')
    else:
        return render_template("meeting.html")


@app.route("/delete")
def delete():
    email = session.get("email")
    if session.get("id") is not None:
        obj.deleteInterviewer(email)
        return render_template("login.html")
    elif session.get("id2") is not None:
        obj.deleteInterviewee(email)
        return render_template("login.html")
    else:
        return render_template("index.html")


@app.route("/logout")
def logout():
    try:
        session.clear()
        return render_template("index.html")
    except Exception as e:
        return render_template("login.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True, port=8001)
