import pymysql


class model:
    def __init__(self, h='', u='', p='', dbs=''):
        self.host = h
        self.user = u
        self.password = p
        self.database = dbs

#functions for unique signup and login
    #search mail function for interviewer
    def searchMail(self, mail):
        db = None
        cursor = None
        found = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            if db is not None:
                query = "select * from interviewer where email = %s"
                cursor.execute(query, mail)
                rows = cursor.fetchall()
                if rows is not None and rows is not ():
                    found = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return found

    # search mail function for interviewee
    def searchMail2(self, mail):
        db = None
        cursor = None
        found = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            if db is not None:
                query = "select * from interviewee where email = %s"
                cursor.execute(query, mail)
                rows = cursor.fetchall()
                if rows is not None and rows is not ():
                    found = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return found

    #insertion function for interviewers
    def insertUser(self, temp):
        db = None
        cursor = None
        inserted = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            if db is not None:
                query = "insert into interviewer values(NULL,%s, %s)"
                args = (temp.email, temp.password)
                cursor.execute(query, args)
                db.commit()
                inserted = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return inserted

    # insertion function for interviewees
    def insertUser2(self, temp):
        db = None
        cursor = None
        inserted = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            if db is not None:
                query = "insert into interviewee values(NULL,%s, %s)"
                args = (temp.email, temp.password)
                cursor.execute(query, args)
                db.commit()
                inserted = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return inserted

    #search user function for interviewers
    def searchUser(self, temp):
        db = None
        cursor = None
        found = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            if db is not None:
                query = "select * from interviewer where email = %s and password = %s"
                args = (temp.email, temp.password)
                cursor.execute(query, args)
                rows = cursor.fetchall()
                if rows is not None and rows is not ():
                    found = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return found

    # search user function for interviewees
    def searchUser2(self, temp):
        db = None
        cursor = None
        found = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            if db is not None:
                query = "select * from interviewee where email = %s and password = %s"
                args = (temp.email, temp.password)
                cursor.execute(query, args)
                rows = cursor.fetchall()
                if rows is not None and rows is not ():
                    found = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return found

    def searchInterviewerID(self, temp):
        db = None
        cursor = None
        found = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            if db is not None:
                query = "select id from interviewer where email = %s and password = %s"
                args = (temp.email, temp.password)
                cursor.execute(query, args)
                row = cursor.fetchone()
                found = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            if found:
                return row[0]
            else:
                return None

    def searchIntervieweeID(self, temp):
        db = None
        cursor = None
        found = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            if db is not None:
                query = "select id from interviewee where email = %s and password = %s"
                args = (temp.email, temp.password)
                cursor.execute(query, args)
                row = cursor.fetchone()
                found = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            if found:
                return row[0]
            else:
                return None

    def insertInterviewer(self, temp):
        db = None
        cursor = None
        inserted = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            if db is not None:
                query = "insert into companiesinfo values(%s,%s,%s,%s)"
                args = (temp.name, temp.company, temp.designation, temp.id)
                cursor.execute(query, args)
                db.commit()
                inserted = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return inserted

    def insertInterviewee(self, temp):
        db = None
        cursor = None
        inserted = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            if db is not None:
                query = "insert into studentsinfo(name,subject,cgpa,institute,bio,user_id) values(%s,%s,%s,%s,%s,%s)"
                args = (temp.name, temp.subject, temp.cgpa, temp.institute, temp.bio, temp.id)
                cursor.execute(query, args)
                db.commit()
                inserted = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return inserted

    def uniqueInterviewerEmail(self, mail):
        db = None
        cursor = None
        found = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            if db is not None:
                query = "select * from interviewer where email = %s"
                cursor.execute(query, mail)
                row = cursor.fetchone()
                if row is not None and row is not ():
                    found = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return found

    def uniqueIntervieweeEmail(self, mail):
        db = None
        cursor = None
        found = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            if db is not None:
                query = "select * from interviewee where email = %s"
                cursor.execute(query, mail)
                row = cursor.fetchone()
                if row is not None and row is not ():
                    found = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return found

    #subscribe functions for both interviewers and interviewees
    def subscribe(self, em):
        db = None
        cursor = None
        flag = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            cursor = db.cursor()
            sql = "insert into subscribers values (%s) "
            cursor.execute(sql, em)
            db.commit()
            flag = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return flag

    #insert score
    def insertOs(self, email, score):
        db = None
        cursor = None
        flag = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            cursor = db.cursor()
            sql1 = "select ID from interviewee where email = %s"
            args = email
            cursor.execute(sql1, args)
            result = cursor.fetchone()
            sql = "update studentsinfo set os = %s where user_id = %s"
            arg = (score, result)
            cursor.execute(sql, arg)
            db.commit()
            flag = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return flag

    def checkOS(self, email):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            cursor = db.cursor()
            sql1 = "select ID from interviewee where email = %s"
            args = email
            cursor.execute(sql1, args)
            result = cursor.fetchone()
            sql = "select os from studentsinfo where user_id = %s"
            arg = result
            cursor.execute(sql, arg)
            result2 = cursor.fetchone()
            if result2:
                return result2
            else:
                return None
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()

    def insertDSA(self, email, score):
        db = None
        cursor = None
        flag = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            cursor = db.cursor()
            sql1 = "select ID from interviewee where email = %s"
            args = email
            cursor.execute(sql1, args)
            result = cursor.fetchone()
            sql = "update studentsinfo set dsa = %s where user_id = %s"
            arg = (score, result)
            cursor.execute(sql, arg)
            db.commit()
            flag = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return flag

    def checkDSA(self, email):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            cursor = db.cursor()
            sql1 = "select ID from interviewee where email = %s"
            args = email
            cursor.execute(sql1, args)
            result = cursor.fetchone()
            sql = "select dsa from studentsinfo where user_id = %s"
            arg = result
            cursor.execute(sql, arg)
            result2 = cursor.fetchone()
            if result2:
                return result2
            else:
                return None
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()

    def insertDBS(self, email, score):
        db = None
        cursor = None
        flag = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            cursor = db.cursor()
            sql1 = "select ID from interviewee where email = %s"
            args = email
            cursor.execute(sql1, args)
            result = cursor.fetchone()
            sql = "update studentsinfo set dbs = %s where user_id = %s"
            arg = (score, result)
            cursor.execute(sql, arg)
            db.commit()
            flag = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return flag

    def checkDBS(self, email):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            cursor = db.cursor()
            sql1 = "select ID from interviewee where email = %s"
            args = email
            cursor.execute(sql1, args)
            result = cursor.fetchone()
            sql = "select dbs from studentsinfo where user_id = %s"
            arg = result
            cursor.execute(sql, arg)
            result2 = cursor.fetchone()
            if result2:
                return result2
            else:
                return None
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()

    def insertCN(self, email, score):
        db = None
        cursor = None
        flag = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            cursor = db.cursor()
            sql1 = "select ID from interviewee where email = %s"
            args = email
            cursor.execute(sql1, args)
            result = cursor.fetchone()
            sql = "update studentsinfo set cn = %s where user_id = %s"
            arg = (score, result)
            cursor.execute(sql, arg)
            db.commit()
            flag = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
            return flag

    def checkCN(self, email):
        db = None
        cursor = None
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            cursor = db.cursor()
            sql1 = "select ID from interviewee where email = %s"
            args = email
            cursor.execute(sql1, args)
            result = cursor.fetchone()
            sql = "select cn from studentsinfo where user_id = %s"
            arg = result
            cursor.execute(sql, arg)
            result2 = cursor.fetchone()
            if result2:
                return result2
            else:
                return None
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()

    def deleteInterviewee(self, email):
        db = None
        cursor = None
        flag = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            cursor = db.cursor()
            sql1 = "select ID from interviewee where email = %s"
            args = email
            cursor.execute(sql1, args)
            result = cursor.fetchone()
            sql = "delete from studentsinfo where user_id = %s"
            arg = result
            cursor.execute(sql, arg)
            db.commit()
            sql2 = "delete from interviewee where email = %s"
            cursor.execute(sql2, email)
            db.commit()
            flag = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
                return flag

    def deleteInterviewer(self, email):
        db = None
        cursor = None
        flag = False
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Get cursor object
            cursor = db.cursor()
            sql1 = "select ID from interviewer where email = %s"
            args = email
            cursor.execute(sql1, args)
            result = cursor.fetchone()
            sql = "delete from companiesinfo where user_id = %s"
            arg = result
            cursor.execute(sql, arg)
            db.commit()
            sql2 = "delete from interviewer where email = %s"
            cursor.execute(sql2, email)
            db.commit()
            flag = True
        except Exception as e:
            print(str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if db is not None:
                db.close()
                return flag

  # function to retrieve all interviewees and display their info on cards
    def cards(self):
        db = None
        cursor = None
        rows = None
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            if db is not None:
                query = "Select * from studentsinfo"
                cursor.execute(query)
                rows = cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            if cursor != None:
                cursor.close()
            if db != None:
                db.close()
            return rows

    #for API datatable:
    def fetchData(self):
        mydb = None
        cursor = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = mydb.cursor()
            query = "select * from studentsinfo"
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        except Exception as e:
            print(str(e))
        finally:
            cursor.close()
            mydb.close()

    def getEmail(self,id):
        db = None
        cursor = None
        rows = None
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = db.cursor()
            if db is not None:
                query = "Select email from interviewee where ID = %s"
                cursor.execute(query, id)
                rows = cursor.fetchone()
        except Exception as e:
            print(str(e))
        finally:
            if cursor != None:
                cursor.close()
            if db != None:
                db.close()
            return rows

