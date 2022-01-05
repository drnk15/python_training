from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db):
    # check that at least 1 group exist
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    # select random group
    group = random.choice(db.get_group_list())
    # select contact not in group; if not any - create new contact
    if len(db.get_contacts_not_in_group(group)) > 0:
        contact = random.choice(db.get_contacts_not_in_group(group))
    else:
        app.contact.create(Contact(firstname='new_contact'))
        contact = db.get_contacts_not_in_group(group)[0]
    # add contact to the group
    app.contact.add_to_group(contact, group)
    # check that contact is in group
    assert contact in db.get_contacts_in_group(group)


