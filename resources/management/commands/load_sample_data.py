from django.core.management.base import BaseCommand
from resources.models import Resource, Provider, Tag

class Command(BaseCommand):
    help = "Loads sample data into the database"

    def handle(self, *args, **kwargs):
        
        # Create Providers
        provider1, _ = Provider.objects.get_or_create(name="Calvert Homeschool", defaults={"description": "Curriculum for K-5th grade", "link": "https://www.calverthomeschool.com/", "phone": "1-888-487-4652", "email": "example@email.com"})
        provider2, _ = Provider.objects.get_or_create(name="Khan Academy", defaults={"description": "Free online courses", "link": "https://www.khanacademy.org/", "phone": "1-650-646-8123", "email": "example@email.com" })
        provider3, _ = Provider.objects.get_or_create(name="Codecademy", defaults={"description": "Learn to code online", "link": "https://www.codecademy.com/", "phone": "1-917-210-1251"})
        provider4, _ = Provider.objects.get_or_create(name="Coursera", defaults={"description": "Online courses from top universities", "link": "https://www.coursera.org/", "phone": "1-650-331-3170"})
        provider5, _ = Provider.objects.get_or_create(name="Udemy", defaults={"description": "Online courses for adults", "link": "https://www.udemy.com/", "phone": "1-415-813-6590"})

        # Create Tags
        tag1, _ = Tag.objects.get_or_create(name="christian")
        tag2, _ = Tag.objects.get_or_create(name="online")
        tag3, _ = Tag.objects.get_or_create(name="free")
        tag4, _ = Tag.objects.get_or_create(name="math")
        tag5, _ = Tag.objects.get_or_create(name="science")
        tag6, _ = Tag.objects.get_or_create(name="history")
        tag7, _ = Tag.objects.get_or_create(name="language")
        tag8, _ = Tag.objects.get_or_create(name="art")
        tag9, _ = Tag.objects.get_or_create(name="music")

        # Create Resources
        resource1, _ = Resource.objects.get_or_create(
            title="Preschool Math, Phonics & Electives Set",
            defaults={
                "resource_type": "curriculum",
                "description": "Encourage early math skills, prepare your child for reading success, and encourage discovery learning and create meaningful learning experiences with Calvert’s Preschool Math, Phonics and Electives Set. Hands-on activities and engaging lessons are easy to teach and fun to learn, making this preschool program a favorite of both kids and parents. These flexible courses easily can be adapted to a variety of daily schedules and program objectives. Each set features a student book with colorful, hands-on lessons, as well as a teacher’s guide stuffed with answer keys, lesson plans, and tips to enrich your child’s learning. Each set also includes a separate resource book with full-color pages of practice to reinforce foundational concepts.",
                "link": "https://www.calverthomeschool.com/product/preschool-math-phonics-set/",
                "provider": provider1,
            }
        )
        resource1.tags.add(tag2, tag2)

        resource2, _ = Resource.objects.get_or_create(
            title="Math Boook for 5th Graders",
            defaults={
                "resource_type": "book",
                "description": "Sample resource two",
                "provider": provider2,
            }
        )
        resource2.tags.add(tag3, tag4)

        self.stdout.write(self.style.SUCCESS("Sample data loaded successfully."))
