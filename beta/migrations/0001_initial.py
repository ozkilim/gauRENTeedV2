# Generated by Django 3.1.6 on 2021-08-04 06:04

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullAddress', models.CharField(blank=True, default='', max_length=2000, unique=True)),
                ('postcode', models.CharField(blank=True, default='', max_length=2000)),
                ('hashId', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=234)),
                ('year', models.CharField(max_length=4)),
                ('charge_id', models.CharField(max_length=234)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('reviewDate', models.DateField(auto_now_add=True)),
                ('timeStamp', models.CharField(blank=True, help_text='Time data was collected', max_length=2000, null=True)),
                ('livingConfirmation', models.BooleanField(blank=True, default=True, help_text='Do you confirm that you live or lived at the property in question?')),
                ('moveIn', models.DateField(null=True)),
                ('moveOut', models.DateField(null=True)),
                ('bedroomNumber', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=3, help_text='How many bedrooms was the house? ', null=True)),
                ('employmentStatus', models.CharField(choices=[('Student', 'Student'), ('Employed', 'Employed'), ('Self-Employed', 'Self-Employed')], default='Student', max_length=2000, null=True)),
                ('reviewerName', models.CharField(max_length=2000, null=True)),
                ('buildingQuality', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='How would you rate the quality of the building (considering mould, pests, cleanliness, damp, etc.)?', null=True)),
                ('buildigComment', models.CharField(blank=True, help_text='Can you explain why you have given it the rating that you have?', max_length=2000, null=True)),
                ('moveInHygene', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='When you moved in, how clean was the property?', null=True)),
                ('moveInHygeneComment', models.CharField(blank=True, help_text='Can you explain why you have given it the rating that you have?', max_length=2000, null=True)),
                ('utilities', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='How would you rate the utilities? (water pressure, heating, insulation etc)', null=True)),
                ('utilitiesComment', models.CharField(blank=True, help_text='Can you explain why you have given it the rating that you have?', max_length=2000, null=True)),
                ('bedroomQuality', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='What is the quality of the bedrooms at the property? (Size, comfort, privacy etc)', null=True)),
                ('bedroomQualityComment', models.CharField(blank=True, help_text='Can you explain why you have given it the rating that you have?', max_length=2000, null=True)),
                ('furnishings', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='If the property was furnished, what is the quality of the furnishings like? (Beds, wardrobes, tables, sofas, etc.)', null=True)),
                ('furnishingsComment', models.CharField(blank=True, help_text='Can you explain why you have given it the rating that you have?', max_length=2000, null=True)),
                ('manageResponsivenes', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='When you have a problem how responsive is the property manager? ', null=True)),
                ('manageResponsivenesComment', models.CharField(blank=True, help_text='Can you explain why you have given them the rating that you have?', max_length=2000, null=True)),
                ('repairQuality', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='When the property manager arranges a repair, the repair is usually...', null=True)),
                ('repairQualityComment', models.CharField(blank=True, help_text='Can you explain why you have given it the rating that you have?', max_length=2000, null=True)),
                ('hiddenExpenses', models.CharField(blank=True, help_text='Were there any hidden expenses at the end of the tenancy? (Cleaning costs, significant deposit reductions, unexpected charges, etc) ', max_length=2000, null=True)),
                ('wantedToKnowBefore', models.CharField(blank=True, help_text='Is there anything else you would have liked to have known about the property manager before you moved in?', max_length=2000, null=True)),
                ('rentMonthly', models.PositiveIntegerField(default=2000, help_text='What is the total monthly rent for the property?', null=True)),
                ('rentGoodDeal', models.BooleanField(default=True, help_text='Do you feel the total monthly rent is a good deal?')),
                ('neighbourhoodDescription', models.CharField(blank=True, help_text='How would you describe the neighbourhood to someone thinking of living there?', max_length=2000, null=True)),
                ('neighbourhoodSafety', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='How safe do you feel in the neighbourhood?', null=True)),
                ('neighbourhoodSafetyComment', models.CharField(blank=True, help_text='Can you explain why you have given it the rating that you have?', max_length=2000, null=True)),
                ('neighbourhoodEnjoyment', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='How much do you enjoy living in this area?', null=True)),
                ('goodPlaceForFriends', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='My house was a good place to have friends over', null=True)),
                ('goodPlaceForDinnerParties', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='My house was a good place to have dinner parties', null=True)),
                ('enjoyedCooking', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='I enjoyed cooking in the kitchen', null=True)),
                ('feltLikeAHome', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='It felt like a home', null=True)),
                ('cosyInWinter', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='It was cosy in the winter', null=True)),
                ('windowView', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='I enjoyed the view out of the windows', null=True)),
                ('neighboursRelationship', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='I had a good relationship with my neighbours', null=True)),
                ('study', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='It was good for studying and focus', null=True)),
                ('easyToSleepAtNight', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='It was easy to sleep at night', null=True)),
                ('feltSafe', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='I felt safe in my house', null=True)),
                ('landlordRelationship', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='I had a good relationship with my landlord / estate agent', null=True)),
                ('hotShower', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='I was able to have a hot shower whenever I wanted', null=True)),
                ('likedMost', models.CharField(blank=True, help_text='What do/did you like most about the property?', max_length=2000, null=True)),
                ('likedLeast', models.CharField(blank=True, help_text='What do/did you like least about the property?', max_length=2000, null=True)),
                ('overallRating', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='Overall, how would you rate this property?', null=True)),
                ('dataConsent', models.BooleanField(default=True, help_text='Are you happy for the data collected during this interview to appear anonymously as a property review on our website?', null=True)),
                ('contactWhenDataPublic', models.BooleanField(default=True, help_text='Would you like to be contacted when this review is made public?', null=True)),
                ('futuePaidWork', models.BooleanField(default=True, help_text='Would you like to hear about future opportunities to work as a paid ambassador for GuaRENTeed?', null=True)),
                ('email', models.CharField(blank=True, help_text='email', max_length=2000, null=True)),
                ('ambassadorPotential', models.BooleanField(default=True, help_text='Would you like to be sent paid opportunities to be a GuaRENTeed ambassador?', null=True)),
                ('whoSentSurvey', models.CharField(blank=True, help_text='Who sent you this survey? (Leave blank if you scanned the QR code on our leaflet)', max_length=2000, null=True)),
                ('maintenanceMoveIn', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='MAINTENANCE/CONDITION: How would you rate the condition of the property when you moved in?', null=True)),
                ('whiteGoods', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='MAINTENANCE/CONDITION: What was the quality of the white goods (dishwasher, washing machine etc)', null=True)),
                ('qualityComments', models.CharField(blank=True, help_text='Any other comment about the quality of property?', max_length=2000, null=True)),
                ('landlordRating', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3, help_text='LANDLORD: Any other comments', null=True)),
                ('landlordComments', models.CharField(blank=True, help_text='LANDLORD: Any other comments', max_length=2000, null=True)),
                ('areaBenefits', models.CharField(blank=True, help_text='What were the benefits of the area?', max_length=2000, null=True)),
                ('areaPerks', models.CharField(blank=True, help_text='Perks of area', max_length=2000, null=True)),
                ('wouldRecommendProperty', models.BooleanField(default=True, help_text='Would you reccomend this property to others? ', null=True)),
                ('property', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='beta.property')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('send_daily_emails', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
