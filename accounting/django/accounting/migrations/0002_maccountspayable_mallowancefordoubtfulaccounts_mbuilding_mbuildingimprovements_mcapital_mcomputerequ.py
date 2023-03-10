# Generated by Django 3.2.9 on 2021-12-22 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MAccountsPayable',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('valueLoaned', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valuePayed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dateOpened', models.DateField(null=True)),
                ('dateClosed', models.DateField(null=True)),
                ('dueDate', models.DateField(null=True)),
                ('customerID', models.IntegerField()),
                ('receiptID', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Accounts Payable',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MAllowanceForDoubtfulAccounts',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customerID', models.IntegerField()),
                ('receiptID', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Allowance For Doubtful Accounts',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MBuilding',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchaseDate', models.DateField(null=True)),
                ('depreciationLife', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receiptID', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Building',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MBuildingImprovements',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchaseDate', models.DateField()),
                ('depreciationLife', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receiptID', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Building Improvements',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MCapital',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('transactionDate', models.DateField()),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customerID', models.IntegerField()),
                ('receiptID', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Capital',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MComputerEquipment',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchaseDate', models.DateField()),
                ('depreciationLife', models.DecimalField(decimal_places=2, max_digits=5)),
                ('receiptID', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Computer Equipment',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MCustomWork',
            fields=[
                ('snid', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pcIn', models.IntegerField(choices=[(0, 'Out'), (1, 'In')], default=0, null=True, verbose_name='In')),
                ('pcOut', models.IntegerField(choices=[(0, 'Out'), (1, 'In')], default=0, null=True, verbose_name='Out')),
                ('mfgDate', models.DateField()),
                ('image', models.ImageField(upload_to='custom/')),
                ('invoiceID', models.IntegerField(null=True)),
                ('customerID', models.IntegerField(null=True)),
                ('employeeID', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Custom Work',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MDeliveryExpense',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customerID', models.IntegerField()),
                ('receiptID', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Delivery Expense',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MDrawings',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('transactionDate', models.DateField()),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customerID', models.IntegerField()),
                ('receiptID', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Drawings',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MLandImprovements',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchaseDate', models.DateField()),
                ('receiptID', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Land Improvements',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MMachineryEquipment',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchaseDate', models.DateField()),
                ('depreciationLife', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receiptID', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Machinery & Equipment',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MOfficeEquipment',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchaseDate', models.DateField()),
                ('depreciationLife', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receiptID', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Office Equipment',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MProductionWork',
            fields=[
                ('snid', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('model', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=500)),
                ('msrp', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
                ('wholesale', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
                ('inchesPerUnit', models.IntegerField()),
                ('image', models.ImageField(upload_to='prodo/')),
                ('qrcode', models.ImageField(upload_to='prodo/qrcodes/')),
                ('squareLink', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Production Work',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MPrototypes',
            fields=[
                ('snid', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=25)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='proto/')),
            ],
            options={
                'verbose_name_plural': 'Prototypes',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MRawMaterials',
            fields=[
                ('snid', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('category', models.CharField(choices=[('Clear', 'Clear'), ('Color', 'Color'), ('Joint', 'Joint'), ('Dichro', 'Dichro'), ('Opal', 'Opal')], default='Clear', help_text='Choose a Category...', max_length=10)),
                ('make', models.CharField(default='Pyrex', help_text='The Brand of Glass.', max_length=30)),
                ('model', models.CharField(choices=[('Tube', 'Tube'), ('Rod', 'Rod'), ('Frit', 'Frit'), ('Sheets', 'Sheets'), ('Strips', 'Strips'), ('Image', 'Image'), ('Shaped', 'Shaped'), ('Tumbled/Polished', 'Tumbled/Polished'), ('Crushed/Rough', 'Crushed/Rough'), ('Sample', 'Sample')], default='Tube', help_text='Choose the Model...', max_length=20)),
                ('diameter', models.DecimalField(decimal_places=2, default='0.00', help_text='Outer Diameter of the Tube.', max_digits=10, null=True)),
                ('thickness', models.DecimalField(decimal_places=2, default='0.00', help_text='Thickness of the Tube.', max_digits=10, null=True)),
                ('inchesPerUnit', models.IntegerField(help_text='Break the Tube into 1/4s.', null=True)),
                ('inchesPerPc', models.IntegerField(help_text='Full length of the Item.', null=True)),
                ('pcsPerCs', models.IntegerField(help_text='Total Items in a Case.', null=True)),
                ('oz', models.IntegerField(help_text='Total Ounces of Frit.', null=True)),
            ],
            options={
                'verbose_name_plural': 'Raw Materials',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MRentExpense',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('payDate', models.DateField()),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customerID', models.IntegerField()),
                ('receiptID', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Rent Expense',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MSalaryExpense',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('payPerHour', models.DecimalField(decimal_places=2, max_digits=10)),
                ('totalHours', models.DecimalField(decimal_places=2, max_digits=10)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Salary Expense',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MSalesRevenue',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('saleDate', models.DateField()),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customerID', models.IntegerField()),
                ('receiptID', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Sales Revenue',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MShopEquipment',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchaseDate', models.DateField()),
                ('depreciationLife', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receiptID', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Shop Equipment',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MStoreEquipment',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchaseDate', models.DateField()),
                ('depreciationLife', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receiptID', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Store Equipment',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MStoreInventory',
            fields=[
                ('snid', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('msrp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unitsPerCs', models.IntegerField()),
                ('image', models.ImageField(upload_to='catalog/')),
            ],
            options={
                'verbose_name_plural': 'Store Inventory',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MSuppliesExpense',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchaseDate', models.DateField()),
                ('customerID', models.IntegerField()),
                ('receiptID', models.IntegerField()),
                ('accountID', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Supplies Expense',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MTravelExpense',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('purchaseDate', models.DateField()),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customerID', models.IntegerField()),
                ('receiptID', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Travel Expense',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MUnearnedSalesRevenue',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('owed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customerID', models.IntegerField()),
                ('receiptID', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Unearned Sales Revenue',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MUtilitiesExpense',
            fields=[
                ('timestamp', models.DateField(auto_now_add=True)),
                ('snid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('billDate', models.DateField()),
                ('dueDate', models.DateField()),
                ('customerID', models.IntegerField()),
                ('receiptID', models.IntegerField()),
                ('accountID', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Utilities Expense',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MsiOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=50)),
                ('unitsOut', models.IntegerField()),
                ('snid', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounting.mstoreinventory')),
            ],
            options={
                'verbose_name_plural': 'SI Out',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MsiIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=50)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchaseDate', models.DateField()),
                ('unitsIn', models.IntegerField()),
                ('invoiceID', models.CharField(max_length=50)),
                ('snid', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounting.mstoreinventory')),
            ],
            options={
                'verbose_name_plural': 'SI In',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MrmOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('units', models.IntegerField()),
                ('waste', models.IntegerField()),
                ('rnd', models.IntegerField()),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounting.mrawmaterials')),
            ],
            options={
                'verbose_name_plural': 'RM Out',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='MrmIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pcsIn', models.IntegerField()),
                ('invoiceID', models.CharField(max_length=100)),
                ('purchaseDate', models.DateField()),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounting.mrawmaterials')),
            ],
            options={
                'verbose_name_plural': 'RM In',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='MpwOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('unitsOut', models.IntegerField()),
                ('snid', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounting.mproductionwork')),
            ],
            options={
                'verbose_name_plural': 'PW Out',
                'ordering': ['snid'],
            },
        ),
        migrations.CreateModel(
            name='MpwIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('unitsIn', models.IntegerField()),
                ('snid', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounting.mproductionwork')),
            ],
            options={
                'verbose_name_plural': 'PW In',
                'ordering': ['snid'],
            },
        ),
    ]
