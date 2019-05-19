from django.db import migrations
from uttar.models import Topic


class Migration(migrations.Migration):

    dependencies = [
        ('uttar', '0001_initial'),
    ]
    
    def insertData(apps, schema_editor):
        Login = apps.get_model('uttar', 'Topic')
        br = Topic(name = "Programming")
        br.save()
        br = Topic(name = "Maths")
        br.save()
        br = Topic(name = "English")
        br.save()
        br = Topic(name = "GK")
        br.save()
        br = Topic(name = "Aptitude")
        br.save()
        br = Topic(name = "Other")
        br.save()


    operations = [
        migrations.RunPython(insertData),
    ]