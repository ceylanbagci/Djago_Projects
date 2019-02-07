import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_site.settings')

import django
# Import settings
django.setup()

import random
from library_app.models import Customer,Book
from faker import Faker

fake = Faker()

for i in range(20):
    fake_id = fake.itin()
    fake_name = fake.name()
    fake_email = fake.email()
    fake_address = fake.address()
    c = Customer.objects.create(customer_id = fake_id, customer_name_surname=fake_name, customer_mail = fake_email, customer_adress = fake_address)
    c.save()

for i in range(20):
    bookList= ["Wolf Of The Land",
    "Mouse Without Hope",
    "Bandits Of Hell",
    "Horses Of Tomorrow",
    "Descendants And Descendants",
    "Warriors And Hunters",
    "Goal Without Fear",
    "Will With Sins",
    "Hunted By Eternity",
    "Bathing In The Shadows","Queen Of Heaven",
    "Thief Of The Sea",
    "Robots Of The Frontline",
    "Gods Without Hope",
    "Butchers And Heroes",
    "Serpents And Gods",
    "Root Of Darkness",
    "Birth Of Wind",
    "Walking Dreams",
    "Signs Of The Abyss"
    ]
    book_auth = fake.name()
    book_isbn = fake.isbn10(separator="-")
    book_pub_d = fake.date_between(start_date="-30y", end_date="today")
    b = Book.objects.create(book_title = bookList[i],book_author = book_auth, book_isbn_no = book_isbn, book_pub_date = book_pub_d)
    b.save()


#topics = ['Search','Social','Marketplace','News','Games']

# def add_topic():
#     t = Customer.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t
#
#
#
# def populate(N=5):
#     '''
#     Create N Entries of Dates Accessed
#     '''
#
#     for entry in range(N):
#
#         # Get Topic for Entry
#         top = add_topic()
#
#         # Create Fake Data for entry
#         fake_url = fakegen.url()
#         fake_date = fakegen.date()
#         fake_name = fakegen.company()
#
#         # Create new Webpage Entry
#         webpg = Customer.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
#
#         # Create Fake Access Record for that page
#         # Could add more of these if you wanted...
#         accRec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
#
#
# if __name__ == '__main__':
#     print("Populating the databases...Please Wait")
#     populate(20)
#     print('Populating Complete')
