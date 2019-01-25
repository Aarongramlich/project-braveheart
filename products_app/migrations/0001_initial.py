# Generated by Django 2.1.5 on 2019-01-10 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=256)),
                ('website', models.URLField(max_length=2000, null=True)),
                ('primary_request_method', models.CharField(choices=[('email', 'Email'), ('api', 'API'), ('phone', 'Phone'), ('mail', 'Physical Mail'), ('webform', 'Webform'), ('portal', 'Portal')], max_length=256, null=True)),
                ('secondary_request_method', models.CharField(choices=[('email', 'Email'), ('api', 'API'), ('phone', 'Phone'), ('mail', 'Physical Mail'), ('webform', 'Webform'), ('portal', 'Portal')], max_length=256, null=True)),
                ('industry', models.CharField(choices=[('aerospace', 'Aerospace'), ('agriculture', 'Agriculture'), ('pharmaceutical', 'Pharmaceutical'), ('software', 'Software'), ('hardware', 'Hardware'), ('construction', 'Construction'), ('defense', 'Defense'), ('education', 'Education'), ('energy', 'Energy'), ('entertainment', 'Entertainment'), ('financial_services', 'Financial Services'), ('food', 'Food'), ('healthcare', 'Healthcare'), ('hospitality', 'Hospitality'), ('information', 'Information'), ('manufacturing', 'Manufacturing'), ('automotive', 'Automotive'), ('broadcasting', 'Broadcasting'), ('film', 'Film'), ('music', 'Music'), ('news', 'News'), ('publishing', 'Publishing'), ('internet', 'Internet'), ('transportation', 'Transporation'), ('services', 'Services')], max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='companies',
            name='packages',
            field=models.ManyToManyField(to='products_app.ProductPackage'),
        ),
    ]