from model.contact import Contact
from model.group import Group
import random


def test_remove_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    group = random.choice(db.get_group_list())
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='new_contact'))
    if len(db.get_contacts_in_group(group)) == 0:
        contact = random.choice(db.get_contacts_not_in_group(group))
        app.contact.add_to_group(contact, group)
    else:
        contact = random.choice(db.get_contacts_in_group(group))
    app.contact.remove_from_group(contact, group)
    assert contact not in db.get_contacts_in_group(group)
