from django.db import migrations


def create_site(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    custom_domain = "tst-proxy-conn-3-3.botics.io"

    site_params = {
        "name": "Tst proxy conn 3",
    }
    if custom_domain:
        site_params["domain"] = custom_domain

    Site.objects.update_or_create(defaults=site_params, id=1)


class Migration(migrations.Migration):
    dependencies = [
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RunPython(create_site),
    ]
