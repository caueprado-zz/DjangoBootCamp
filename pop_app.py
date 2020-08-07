import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evolution.settings')

import django
django.setup()

import random
from evolution_app.models import Topic, AccessRecord, Webpage, User
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        webpg.save()
        acc_rec = AccessRecord.objects.get_or_create(webpage=webpg, name=fake_name, date=fake_date)[0]
        acc_rec.save()

        username = fakegen.name()
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        address = fakegen.address()
        phone = fakegen.phone_number()
        # password = fakegen.words(6)
        password = fakegen.sha256()
        email = fakegen.safe_email()

        user = User.objects.get_or_create(first_name=first_name, last_name=last_name, username=username, email= email, password=password, address=address, phone=phone)


if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("complete")