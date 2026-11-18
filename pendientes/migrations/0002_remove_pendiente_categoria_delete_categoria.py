from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("pendientes", "0001_initial")]
    operations = [
        migrations.RemoveField(model_name="pendiente", name="categoria"),
        migrations.DeleteModel(name="Categoria"),
    ]
