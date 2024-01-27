class user:
    def __init__(self, a="", b=""):
        self.email = a
        self.password = b


class student:
    def __init__(self, a="", b="", c=0.0, d="", e="", f=0):
        self.name = a
        self.subject = b
        self.cgpa = c
        self.institute = d
        self.bio = e
        self.id = f


class employee:
    def __init__(self, name="", des="", comp="", id=""):
        self.name = name
        self.designation = des
        self.company = comp
        self.id = id