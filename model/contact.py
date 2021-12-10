from sys import maxsize


class Contact:

    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home_phone_number=None, mobile_phone_number=None, work_phone_number=None,
                 fax_number=None, email=None, email2=None, email3=None, homepage=None, birth_day=None,
                 birth_month=None, birth_year=None, anniversary_day=None, anniversary_month=None,
                 anniversary_year=None, address2=None, home_phone_number2=None, notes=None, all_emails=None, all_phones=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone_number = home_phone_number
        self.mobile_phone_number = mobile_phone_number
        self.work_phone_number = work_phone_number
        self.fax_number = fax_number
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.address2 = address2
        self.home_phone_number2 = home_phone_number2
        self.notes = notes
        self.all_emails = all_emails
        self.all_phones = all_phones

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        if self.firstname == other.firstname and self.lastname == other.lastname:
            return self.id is None or other.id is None or self.id == other.id
        else:
            return False

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
