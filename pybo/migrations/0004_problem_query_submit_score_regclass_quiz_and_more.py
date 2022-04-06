# Generated by Django 4.0.3 on 2022-04-04 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_alter_users_id_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Statement', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Difficulty', models.FloatField(default=0.0)),
                ('Query', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('AcceptRate', models.FloatField(default=0.0)),
                ('ProblemID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.problem')),
                ('UserName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.users')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Score', models.IntegerField(default=0)),
                ('ProblemID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.problem')),
                ('StudentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.users')),
            ],
        ),
        migrations.CreateModel(
            name='RegClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.class')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.users')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('StartDateTime', models.DateTimeField()),
                ('EndDateTime', models.DateTimeField()),
                ('ClassID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.class')),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='Query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.query'),
        ),
    ]