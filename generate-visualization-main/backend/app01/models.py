# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AbnormalCard(models.Model):
    card_id = models.AutoField(primary_key=True)
    owner_type = models.CharField(max_length=50, blank=True, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    c4 = models.CharField(db_column='C4', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    c5 = models.CharField(db_column='C5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c6 = models.CharField(db_column='C6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c7 = models.CharField(db_column='C7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c8 = models.CharField(db_column='C8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c9 = models.CharField(db_column='C9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c10 = models.CharField(db_column='C10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c11 = models.CharField(db_column='C11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'abnormal_card'


class AbnormalFT(models.Model):
    f1 = models.CharField(db_column='F1', max_length=26, blank=True, null=True)  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f3 = models.CharField(db_column='F3', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f4 = models.CharField(db_column='F4', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f5 = models.CharField(db_column='F5', max_length=12, blank=True, null=True)  # Field name made lowercase.
    f6 = models.CharField(db_column='F6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f7 = models.CharField(db_column='F7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f8 = models.CharField(db_column='F8', max_length=4, blank=True, null=True)  # Field name made lowercase.
    f9 = models.CharField(db_column='F9', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f10 = models.DecimalField(db_column='F10', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f11 = models.DecimalField(db_column='F11', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f12 = models.CharField(db_column='F12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f13 = models.CharField(db_column='F13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f14 = models.CharField(db_column='F14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f15 = models.CharField(db_column='F15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f16 = models.CharField(db_column='F16', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f17 = models.CharField(db_column='F17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f18 = models.CharField(db_column='F18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f19 = models.CharField(db_column='F19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f20 = models.CharField(db_column='F20', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f21 = models.CharField(db_column='F21', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f22 = models.CharField(db_column='F22', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f23 = models.CharField(db_column='F23', max_length=2, blank=True, null=True)  # Field name made lowercase.
    f24 = models.CharField(db_column='F24', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f25 = models.CharField(db_column='F25', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f26 = models.CharField(db_column='F26', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f27 = models.CharField(db_column='F27', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f28 = models.CharField(db_column='F28', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f29 = models.CharField(db_column='F29', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f30 = models.CharField(db_column='F30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f31 = models.DateTimeField(db_column='F31', blank=True, null=True)  # Field name made lowercase.
    f32 = models.DateTimeField(db_column='F32', blank=True, null=True)  # Field name made lowercase.
    f33 = models.CharField(db_column='F33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f34 = models.CharField(db_column='F34', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f35 = models.DecimalField(db_column='F35', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f36 = models.CharField(db_column='F36', max_length=4, blank=True, null=True)  # Field name made lowercase.
    f37 = models.DecimalField(db_column='F37', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f38 = models.DecimalField(db_column='F38', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f39 = models.CharField(db_column='F39', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f40 = models.CharField(db_column='F40', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f41 = models.CharField(db_column='F41', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f42 = models.CharField(db_column='F42', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f43 = models.CharField(db_column='F43', max_length=50, blank=True, null=True)  # Field name made lowercase.
    f44 = models.DecimalField(db_column='F44', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f45 = models.CharField(db_column='F45', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'abnormal_f_t'


class AbnormalRelative(models.Model):
    user_id = models.IntegerField()
    gender = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    childlist = models.JSONField(db_column='childList', blank=True, null=True)  # Field name made lowercase.
    f_id = models.IntegerField(blank=True, null=True)
    m_id = models.IntegerField(blank=True, null=True)
    c_id = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'abnormal_relative'


class AbnormalStore(models.Model):
    industry = models.CharField(max_length=50, blank=True, null=True)
    name_field = models.CharField(db_column='name_', max_length=100, blank=True, null=True)  # Field renamed because it ended with '_'.
    rank_field = models.CharField(db_column='rank_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
    consumption_range = models.JSONField(blank=True, null=True)
    opening_hours = models.CharField(max_length=50, blank=True, null=True)
    s1 = models.CharField(db_column='S1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s2 = models.CharField(db_column='S2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s3 = models.CharField(db_column='S3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s4 = models.CharField(db_column='S4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s5 = models.CharField(db_column='S5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s6 = models.CharField(db_column='S6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s7 = models.CharField(db_column='S7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s8 = models.CharField(db_column='S8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s9 = models.CharField(db_column='S9', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s10 = models.CharField(db_column='S10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s11 = models.CharField(db_column='S11', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s12 = models.CharField(db_column='S12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s13 = models.CharField(db_column='S13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s14 = models.CharField(db_column='S14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s15 = models.CharField(db_column='S15', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s16 = models.CharField(db_column='S16', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s17 = models.CharField(db_column='S17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s18 = models.CharField(db_column='S18', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s19 = models.CharField(db_column='S19', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s20 = models.CharField(db_column='S20', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s21 = models.CharField(db_column='S21', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s22 = models.CharField(db_column='S22', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s23 = models.CharField(db_column='S23', max_length=200, blank=True, null=True)  # Field name made lowercase.
    s24 = models.CharField(db_column='S24', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s25 = models.CharField(db_column='S25', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s26 = models.CharField(db_column='S26', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s27 = models.CharField(db_column='S27', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s28 = models.CharField(db_column='S28', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s29 = models.CharField(db_column='S29', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s30 = models.JSONField(db_column='S30', blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'abnormal_store'


class AbnormalTrans(models.Model):
    t1 = models.CharField(db_column='T1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t2 = models.CharField(db_column='T2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t3 = models.CharField(db_column='T3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t4 = models.CharField(db_column='T4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t5 = models.CharField(db_column='T5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t6 = models.CharField(db_column='T6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    t7 = models.CharField(db_column='T7', max_length=5, blank=True, null=True)  # Field name made lowercase.
    t8 = models.CharField(db_column='T8', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t9 = models.CharField(db_column='T9', max_length=6, blank=True, null=True)  # Field name made lowercase.
    t10 = models.CharField(db_column='T10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t11 = models.CharField(db_column='T11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t12 = models.CharField(db_column='T12', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t13 = models.CharField(db_column='T13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t14 = models.CharField(db_column='T14', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t15 = models.CharField(db_column='T15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t16 = models.CharField(db_column='T16', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t17 = models.DecimalField(db_column='T17', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t18 = models.CharField(db_column='T18', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t19 = models.CharField(db_column='T19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t20 = models.CharField(db_column='T20', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t21 = models.CharField(db_column='T21', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t22 = models.CharField(db_column='T22', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t23 = models.CharField(db_column='T23', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t24 = models.CharField(db_column='T24', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t25 = models.CharField(db_column='T25', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t26 = models.CharField(db_column='T26', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t27 = models.CharField(db_column='T27', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t28 = models.CharField(db_column='T28', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t29 = models.CharField(db_column='T29', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t30 = models.CharField(db_column='T30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t31 = models.CharField(db_column='T31', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t32 = models.CharField(db_column='T32', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t33 = models.CharField(db_column='T33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t34 = models.CharField(db_column='T34', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t35 = models.CharField(db_column='T35', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t36 = models.CharField(db_column='T36', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t37 = models.CharField(db_column='T37', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t38 = models.CharField(db_column='T38', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t39 = models.CharField(db_column='T39', max_length=20, blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'abnormal_trans'


class AbnormalUser(models.Model):
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    wage = models.IntegerField(blank=True, null=True)
    card = models.JSONField(blank=True, null=True)
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)
    user_no = models.CharField(unique=True, max_length=100, blank=True, null=True)
    loc_id = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'abnormal_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    owner_type = models.CharField(max_length=50, blank=True, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    c4 = models.CharField(db_column='C4', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    c5 = models.CharField(db_column='C5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c6 = models.CharField(db_column='C6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c7 = models.CharField(db_column='C7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c8 = models.CharField(db_column='C8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c9 = models.CharField(db_column='C9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c10 = models.CharField(db_column='C10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c11 = models.CharField(db_column='C11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'card'


class CreditCard(models.Model):
    card_id = models.AutoField(primary_key=True)
    owner_type = models.CharField(max_length=50, blank=True, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    c4 = models.CharField(db_column='C4', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    c5 = models.CharField(db_column='C5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c6 = models.CharField(db_column='C6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c7 = models.CharField(db_column='C7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c8 = models.CharField(db_column='C8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c9 = models.CharField(db_column='C9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c10 = models.CharField(db_column='C10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c11 = models.CharField(db_column='C11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'credit_card'


class CreditFT(models.Model):
    f1 = models.CharField(db_column='F1', max_length=26, blank=True, null=True)  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f3 = models.CharField(db_column='F3', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f4 = models.CharField(db_column='F4', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f5 = models.CharField(db_column='F5', max_length=12, blank=True, null=True)  # Field name made lowercase.
    f6 = models.CharField(db_column='F6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f7 = models.CharField(db_column='F7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f8 = models.CharField(db_column='F8', max_length=4, blank=True, null=True)  # Field name made lowercase.
    f9 = models.CharField(db_column='F9', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f10 = models.DecimalField(db_column='F10', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f11 = models.DecimalField(db_column='F11', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f12 = models.CharField(db_column='F12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f13 = models.CharField(db_column='F13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f14 = models.CharField(db_column='F14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f15 = models.CharField(db_column='F15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f16 = models.CharField(db_column='F16', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f17 = models.CharField(db_column='F17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f18 = models.CharField(db_column='F18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f19 = models.CharField(db_column='F19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f20 = models.CharField(db_column='F20', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f21 = models.CharField(db_column='F21', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f22 = models.CharField(db_column='F22', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f23 = models.CharField(db_column='F23', max_length=2, blank=True, null=True)  # Field name made lowercase.
    f24 = models.CharField(db_column='F24', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f25 = models.CharField(db_column='F25', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f26 = models.CharField(db_column='F26', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f27 = models.CharField(db_column='F27', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f28 = models.CharField(db_column='F28', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f29 = models.CharField(db_column='F29', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f30 = models.CharField(db_column='F30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f31 = models.DateTimeField(db_column='F31', blank=True, null=True)  # Field name made lowercase.
    f32 = models.DateTimeField(db_column='F32', blank=True, null=True)  # Field name made lowercase.
    f33 = models.CharField(db_column='F33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f34 = models.CharField(db_column='F34', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f35 = models.DecimalField(db_column='F35', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f36 = models.CharField(db_column='F36', max_length=4, blank=True, null=True)  # Field name made lowercase.
    f37 = models.DecimalField(db_column='F37', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f38 = models.DecimalField(db_column='F38', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f39 = models.CharField(db_column='F39', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f40 = models.CharField(db_column='F40', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f41 = models.CharField(db_column='F41', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f42 = models.CharField(db_column='F42', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f43 = models.CharField(db_column='F43', max_length=50, blank=True, null=True)  # Field name made lowercase.
    f44 = models.DecimalField(db_column='F44', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f45 = models.CharField(db_column='F45', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'credit_f_t'


class CreditRelative(models.Model):
    user_id = models.IntegerField()
    gender = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    childlist = models.JSONField(db_column='childList', blank=True, null=True)  # Field name made lowercase.
    f_id = models.IntegerField(blank=True, null=True)
    m_id = models.IntegerField(blank=True, null=True)
    c_id = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'credit_relative'


class CreditStore(models.Model):
    industry = models.CharField(max_length=50, blank=True, null=True)
    name_field = models.CharField(db_column='name_', max_length=100, blank=True, null=True)  # Field renamed because it ended with '_'.
    rank_field = models.CharField(db_column='rank_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
    consumption_range = models.JSONField(blank=True, null=True)
    opening_hours = models.CharField(max_length=50, blank=True, null=True)
    s1 = models.CharField(db_column='S1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s2 = models.CharField(db_column='S2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s3 = models.CharField(db_column='S3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s4 = models.CharField(db_column='S4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s5 = models.CharField(db_column='S5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s6 = models.CharField(db_column='S6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s7 = models.CharField(db_column='S7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s8 = models.CharField(db_column='S8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s9 = models.CharField(db_column='S9', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s10 = models.CharField(db_column='S10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s11 = models.CharField(db_column='S11', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s12 = models.CharField(db_column='S12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s13 = models.CharField(db_column='S13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s14 = models.CharField(db_column='S14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s15 = models.CharField(db_column='S15', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s16 = models.CharField(db_column='S16', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s17 = models.CharField(db_column='S17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s18 = models.CharField(db_column='S18', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s19 = models.CharField(db_column='S19', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s20 = models.CharField(db_column='S20', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s21 = models.CharField(db_column='S21', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s22 = models.CharField(db_column='S22', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s23 = models.CharField(db_column='S23', max_length=200, blank=True, null=True)  # Field name made lowercase.
    s24 = models.CharField(db_column='S24', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s25 = models.CharField(db_column='S25', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s26 = models.CharField(db_column='S26', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s27 = models.CharField(db_column='S27', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s28 = models.CharField(db_column='S28', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s29 = models.CharField(db_column='S29', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s30 = models.JSONField(db_column='S30', blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'credit_store'


class CreditTrans(models.Model):
    t1 = models.CharField(db_column='T1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t2 = models.CharField(db_column='T2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t3 = models.CharField(db_column='T3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t4 = models.CharField(db_column='T4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t5 = models.CharField(db_column='T5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t6 = models.CharField(db_column='T6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    t7 = models.CharField(db_column='T7', max_length=5, blank=True, null=True)  # Field name made lowercase.
    t8 = models.CharField(db_column='T8', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t9 = models.CharField(db_column='T9', max_length=6, blank=True, null=True)  # Field name made lowercase.
    t10 = models.CharField(db_column='T10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t11 = models.CharField(db_column='T11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t12 = models.CharField(db_column='T12', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t13 = models.CharField(db_column='T13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t14 = models.CharField(db_column='T14', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t15 = models.CharField(db_column='T15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t16 = models.CharField(db_column='T16', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t17 = models.DecimalField(db_column='T17', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t18 = models.CharField(db_column='T18', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t19 = models.CharField(db_column='T19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t20 = models.CharField(db_column='T20', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t21 = models.CharField(db_column='T21', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t22 = models.CharField(db_column='T22', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t23 = models.CharField(db_column='T23', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t24 = models.CharField(db_column='T24', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t25 = models.CharField(db_column='T25', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t26 = models.CharField(db_column='T26', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t27 = models.CharField(db_column='T27', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t28 = models.CharField(db_column='T28', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t29 = models.CharField(db_column='T29', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t30 = models.CharField(db_column='T30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t31 = models.CharField(db_column='T31', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t32 = models.CharField(db_column='T32', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t33 = models.CharField(db_column='T33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t34 = models.CharField(db_column='T34', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t35 = models.CharField(db_column='T35', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t36 = models.CharField(db_column='T36', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t37 = models.CharField(db_column='T37', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t38 = models.CharField(db_column='T38', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t39 = models.CharField(db_column='T39', max_length=20, blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'credit_trans'


class CreditUser(models.Model):
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    wage = models.IntegerField(blank=True, null=True)
    card = models.JSONField(blank=True, null=True)
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)
    user_no = models.CharField(unique=True, max_length=100, blank=True, null=True)
    loc_id = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'credit_user'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Enterprise(models.Model):
    socialid = models.CharField(db_column='socialId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=20, blank=True, null=True)
    registerid = models.CharField(db_column='registerId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    represent = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    builttime = models.CharField(db_column='builtTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    regamount = models.CharField(db_column='regAmount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    checktime = models.CharField(db_column='checkTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    reglocate = models.CharField(db_column='regLocate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=10, blank=True, null=True)
    locate = models.CharField(max_length=100, blank=True, null=True)
    busscope = models.CharField(db_column='busScope', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'enterprise'


class FT(models.Model):
    f1 = models.CharField(db_column='F1', max_length=26, blank=True, null=True)  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f3 = models.CharField(db_column='F3', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f4 = models.CharField(db_column='F4', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f5 = models.CharField(db_column='F5', max_length=12, blank=True, null=True)  # Field name made lowercase.
    f6 = models.CharField(db_column='F6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f7 = models.CharField(db_column='F7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f8 = models.CharField(db_column='F8', max_length=4, blank=True, null=True)  # Field name made lowercase.
    f9 = models.CharField(db_column='F9', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f10 = models.DecimalField(db_column='F10', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f11 = models.DecimalField(db_column='F11', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f12 = models.CharField(db_column='F12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f13 = models.CharField(db_column='F13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f14 = models.CharField(db_column='F14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f15 = models.CharField(db_column='F15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f16 = models.CharField(db_column='F16', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f17 = models.CharField(db_column='F17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f18 = models.CharField(db_column='F18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f19 = models.CharField(db_column='F19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f20 = models.CharField(db_column='F20', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f21 = models.CharField(db_column='F21', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f22 = models.CharField(db_column='F22', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f23 = models.CharField(db_column='F23', max_length=2, blank=True, null=True)  # Field name made lowercase.
    f24 = models.CharField(db_column='F24', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f25 = models.CharField(db_column='F25', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f26 = models.CharField(db_column='F26', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f27 = models.CharField(db_column='F27', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f28 = models.CharField(db_column='F28', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f29 = models.CharField(db_column='F29', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f30 = models.CharField(db_column='F30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f31 = models.DateTimeField(db_column='F31', blank=True, null=True)  # Field name made lowercase.
    f32 = models.DateTimeField(db_column='F32', blank=True, null=True)  # Field name made lowercase.
    f33 = models.CharField(db_column='F33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f34 = models.CharField(db_column='F34', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f35 = models.DecimalField(db_column='F35', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f36 = models.CharField(db_column='F36', max_length=4, blank=True, null=True)  # Field name made lowercase.
    f37 = models.DecimalField(db_column='F37', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f38 = models.DecimalField(db_column='F38', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f39 = models.CharField(db_column='F39', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f40 = models.CharField(db_column='F40', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f41 = models.CharField(db_column='F41', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f42 = models.CharField(db_column='F42', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f43 = models.CharField(db_column='F43', max_length=50, blank=True, null=True)  # Field name made lowercase.
    f44 = models.DecimalField(db_column='F44', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f45 = models.CharField(db_column='F45', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'f_t'


class GamblingCard(models.Model):
    card_id = models.AutoField(primary_key=True)
    owner_type = models.CharField(max_length=50, blank=True, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    c4 = models.CharField(db_column='C4', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    c5 = models.CharField(db_column='C5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c6 = models.CharField(db_column='C6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c7 = models.CharField(db_column='C7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c8 = models.CharField(db_column='C8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c9 = models.CharField(db_column='C9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c10 = models.CharField(db_column='C10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c11 = models.CharField(db_column='C11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'gambling_card'


class GamblingFT(models.Model):
    f1 = models.CharField(db_column='F1', max_length=26, blank=True, null=True)  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f3 = models.CharField(db_column='F3', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f4 = models.CharField(db_column='F4', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f5 = models.CharField(db_column='F5', max_length=12, blank=True, null=True)  # Field name made lowercase.
    f6 = models.CharField(db_column='F6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f7 = models.CharField(db_column='F7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f8 = models.CharField(db_column='F8', max_length=4, blank=True, null=True)  # Field name made lowercase.
    f9 = models.CharField(db_column='F9', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f10 = models.DecimalField(db_column='F10', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f11 = models.DecimalField(db_column='F11', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f12 = models.CharField(db_column='F12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f13 = models.CharField(db_column='F13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f14 = models.CharField(db_column='F14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f15 = models.CharField(db_column='F15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f16 = models.CharField(db_column='F16', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f17 = models.CharField(db_column='F17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f18 = models.CharField(db_column='F18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f19 = models.CharField(db_column='F19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f20 = models.CharField(db_column='F20', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f21 = models.CharField(db_column='F21', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f22 = models.CharField(db_column='F22', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f23 = models.CharField(db_column='F23', max_length=2, blank=True, null=True)  # Field name made lowercase.
    f24 = models.CharField(db_column='F24', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f25 = models.CharField(db_column='F25', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f26 = models.CharField(db_column='F26', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f27 = models.CharField(db_column='F27', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f28 = models.CharField(db_column='F28', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f29 = models.CharField(db_column='F29', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f30 = models.CharField(db_column='F30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f31 = models.DateTimeField(db_column='F31', blank=True, null=True)  # Field name made lowercase.
    f32 = models.DateTimeField(db_column='F32', blank=True, null=True)  # Field name made lowercase.
    f33 = models.CharField(db_column='F33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f34 = models.CharField(db_column='F34', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f35 = models.DecimalField(db_column='F35', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f36 = models.CharField(db_column='F36', max_length=4, blank=True, null=True)  # Field name made lowercase.
    f37 = models.DecimalField(db_column='F37', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f38 = models.DecimalField(db_column='F38', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f39 = models.CharField(db_column='F39', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f40 = models.CharField(db_column='F40', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f41 = models.CharField(db_column='F41', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f42 = models.CharField(db_column='F42', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f43 = models.CharField(db_column='F43', max_length=50, blank=True, null=True)  # Field name made lowercase.
    f44 = models.DecimalField(db_column='F44', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f45 = models.CharField(db_column='F45', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'gambling_f_t'


class GamblingRelative(models.Model):
    user_id = models.IntegerField()
    gender = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    childlist = models.JSONField(db_column='childList', blank=True, null=True)  # Field name made lowercase.
    f_id = models.IntegerField(blank=True, null=True)
    m_id = models.IntegerField(blank=True, null=True)
    c_id = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'gambling_relative'


class GamblingStore(models.Model):
    industry = models.CharField(max_length=50, blank=True, null=True)
    name_field = models.CharField(db_column='name_', max_length=100, blank=True, null=True)  # Field renamed because it ended with '_'.
    rank_field = models.CharField(db_column='rank_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
    consumption_range = models.JSONField(blank=True, null=True)
    opening_hours = models.CharField(max_length=50, blank=True, null=True)
    s1 = models.CharField(db_column='S1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s2 = models.CharField(db_column='S2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s3 = models.CharField(db_column='S3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s4 = models.CharField(db_column='S4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s5 = models.CharField(db_column='S5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s6 = models.CharField(db_column='S6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s7 = models.CharField(db_column='S7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s8 = models.CharField(db_column='S8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s9 = models.CharField(db_column='S9', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s10 = models.CharField(db_column='S10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s11 = models.CharField(db_column='S11', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s12 = models.CharField(db_column='S12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s13 = models.CharField(db_column='S13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s14 = models.CharField(db_column='S14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s15 = models.CharField(db_column='S15', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s16 = models.CharField(db_column='S16', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s17 = models.CharField(db_column='S17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s18 = models.CharField(db_column='S18', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s19 = models.CharField(db_column='S19', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s20 = models.CharField(db_column='S20', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s21 = models.CharField(db_column='S21', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s22 = models.CharField(db_column='S22', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s23 = models.CharField(db_column='S23', max_length=200, blank=True, null=True)  # Field name made lowercase.
    s24 = models.CharField(db_column='S24', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s25 = models.CharField(db_column='S25', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s26 = models.CharField(db_column='S26', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s27 = models.CharField(db_column='S27', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s28 = models.CharField(db_column='S28', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s29 = models.CharField(db_column='S29', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s30 = models.JSONField(db_column='S30', blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'gambling_store'


class GamblingTrans(models.Model):
    t1 = models.CharField(db_column='T1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t2 = models.CharField(db_column='T2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t3 = models.CharField(db_column='T3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t4 = models.CharField(db_column='T4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t5 = models.CharField(db_column='T5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t6 = models.CharField(db_column='T6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    t7 = models.CharField(db_column='T7', max_length=5, blank=True, null=True)  # Field name made lowercase.
    t8 = models.CharField(db_column='T8', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t9 = models.CharField(db_column='T9', max_length=6, blank=True, null=True)  # Field name made lowercase.
    t10 = models.CharField(db_column='T10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t11 = models.CharField(db_column='T11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t12 = models.CharField(db_column='T12', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t13 = models.CharField(db_column='T13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t14 = models.CharField(db_column='T14', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t15 = models.CharField(db_column='T15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t16 = models.CharField(db_column='T16', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t17 = models.DecimalField(db_column='T17', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t18 = models.CharField(db_column='T18', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t19 = models.CharField(db_column='T19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t20 = models.CharField(db_column='T20', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t21 = models.CharField(db_column='T21', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t22 = models.CharField(db_column='T22', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t23 = models.CharField(db_column='T23', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t24 = models.CharField(db_column='T24', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t25 = models.CharField(db_column='T25', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t26 = models.CharField(db_column='T26', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t27 = models.CharField(db_column='T27', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t28 = models.CharField(db_column='T28', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t29 = models.CharField(db_column='T29', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t30 = models.CharField(db_column='T30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t31 = models.CharField(db_column='T31', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t32 = models.CharField(db_column='T32', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t33 = models.CharField(db_column='T33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t34 = models.CharField(db_column='T34', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t35 = models.CharField(db_column='T35', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t36 = models.CharField(db_column='T36', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t37 = models.CharField(db_column='T37', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t38 = models.CharField(db_column='T38', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t39 = models.CharField(db_column='T39', max_length=20, blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'gambling_trans'


class GamblingUser(models.Model):
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    wage = models.IntegerField(blank=True, null=True)
    card = models.JSONField(blank=True, null=True)
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)
    user_no = models.CharField(unique=True, max_length=100, blank=True, null=True)
    loc_id = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'gambling_user'


class Login(models.Model):
    role = models.IntegerField()
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        # managed = False
        db_table = 'login'
        unique_together = (('username', 'password'),)


class MarketingCard(models.Model):
    card_id = models.AutoField(primary_key=True)
    owner_type = models.CharField(max_length=50, blank=True, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    c4 = models.CharField(db_column='C4', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    c5 = models.CharField(db_column='C5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c6 = models.CharField(db_column='C6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c7 = models.CharField(db_column='C7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c8 = models.CharField(db_column='C8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c9 = models.CharField(db_column='C9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c10 = models.CharField(db_column='C10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c11 = models.CharField(db_column='C11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'marketing_card'


class MarketingFT(models.Model):
    f1 = models.CharField(db_column='F1', max_length=26, blank=True, null=True)  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f3 = models.CharField(db_column='F3', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f4 = models.CharField(db_column='F4', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f5 = models.CharField(db_column='F5', max_length=12, blank=True, null=True)  # Field name made lowercase.
    f6 = models.CharField(db_column='F6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f7 = models.CharField(db_column='F7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f8 = models.CharField(db_column='F8', max_length=4, blank=True, null=True)  # Field name made lowercase.
    f9 = models.CharField(db_column='F9', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f10 = models.DecimalField(db_column='F10', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f11 = models.DecimalField(db_column='F11', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f12 = models.CharField(db_column='F12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f13 = models.CharField(db_column='F13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f14 = models.CharField(db_column='F14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f15 = models.CharField(db_column='F15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f16 = models.CharField(db_column='F16', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f17 = models.CharField(db_column='F17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f18 = models.CharField(db_column='F18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f19 = models.CharField(db_column='F19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f20 = models.CharField(db_column='F20', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f21 = models.CharField(db_column='F21', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f22 = models.CharField(db_column='F22', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f23 = models.CharField(db_column='F23', max_length=2, blank=True, null=True)  # Field name made lowercase.
    f24 = models.CharField(db_column='F24', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f25 = models.CharField(db_column='F25', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f26 = models.CharField(db_column='F26', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f27 = models.CharField(db_column='F27', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f28 = models.CharField(db_column='F28', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f29 = models.CharField(db_column='F29', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f30 = models.CharField(db_column='F30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f31 = models.DateTimeField(db_column='F31', blank=True, null=True)  # Field name made lowercase.
    f32 = models.DateTimeField(db_column='F32', blank=True, null=True)  # Field name made lowercase.
    f33 = models.CharField(db_column='F33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f34 = models.CharField(db_column='F34', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f35 = models.DecimalField(db_column='F35', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f36 = models.CharField(db_column='F36', max_length=4, blank=True, null=True)  # Field name made lowercase.
    f37 = models.DecimalField(db_column='F37', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f38 = models.DecimalField(db_column='F38', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f39 = models.CharField(db_column='F39', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f40 = models.CharField(db_column='F40', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f41 = models.CharField(db_column='F41', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f42 = models.CharField(db_column='F42', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f43 = models.CharField(db_column='F43', max_length=50, blank=True, null=True)  # Field name made lowercase.
    f44 = models.DecimalField(db_column='F44', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f45 = models.CharField(db_column='F45', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'marketing_f_t'


class MarketingRelative(models.Model):
    user_id = models.IntegerField()
    gender = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    childlist = models.JSONField(db_column='childList', blank=True, null=True)  # Field name made lowercase.
    f_id = models.IntegerField(blank=True, null=True)
    m_id = models.IntegerField(blank=True, null=True)
    c_id = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'marketing_relative'


class MarketingStore(models.Model):
    industry = models.CharField(max_length=50, blank=True, null=True)
    name_field = models.CharField(db_column='name_', max_length=100, blank=True, null=True)  # Field renamed because it ended with '_'.
    rank_field = models.CharField(db_column='rank_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
    consumption_range = models.JSONField(blank=True, null=True)
    opening_hours = models.CharField(max_length=50, blank=True, null=True)
    s1 = models.CharField(db_column='S1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s2 = models.CharField(db_column='S2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s3 = models.CharField(db_column='S3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s4 = models.CharField(db_column='S4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s5 = models.CharField(db_column='S5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s6 = models.CharField(db_column='S6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s7 = models.CharField(db_column='S7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s8 = models.CharField(db_column='S8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s9 = models.CharField(db_column='S9', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s10 = models.CharField(db_column='S10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s11 = models.CharField(db_column='S11', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s12 = models.CharField(db_column='S12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s13 = models.CharField(db_column='S13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s14 = models.CharField(db_column='S14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s15 = models.CharField(db_column='S15', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s16 = models.CharField(db_column='S16', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s17 = models.CharField(db_column='S17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s18 = models.CharField(db_column='S18', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s19 = models.CharField(db_column='S19', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s20 = models.CharField(db_column='S20', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s21 = models.CharField(db_column='S21', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s22 = models.CharField(db_column='S22', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s23 = models.CharField(db_column='S23', max_length=200, blank=True, null=True)  # Field name made lowercase.
    s24 = models.CharField(db_column='S24', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s25 = models.CharField(db_column='S25', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s26 = models.CharField(db_column='S26', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s27 = models.CharField(db_column='S27', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s28 = models.CharField(db_column='S28', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s29 = models.CharField(db_column='S29', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s30 = models.JSONField(db_column='S30', blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'marketing_store'


class MarketingTrans(models.Model):
    t1 = models.CharField(db_column='T1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t2 = models.CharField(db_column='T2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t3 = models.CharField(db_column='T3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t4 = models.CharField(db_column='T4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t5 = models.CharField(db_column='T5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t6 = models.CharField(db_column='T6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    t7 = models.CharField(db_column='T7', max_length=5, blank=True, null=True)  # Field name made lowercase.
    t8 = models.CharField(db_column='T8', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t9 = models.CharField(db_column='T9', max_length=6, blank=True, null=True)  # Field name made lowercase.
    t10 = models.CharField(db_column='T10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t11 = models.CharField(db_column='T11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t12 = models.CharField(db_column='T12', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t13 = models.CharField(db_column='T13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t14 = models.CharField(db_column='T14', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t15 = models.CharField(db_column='T15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t16 = models.CharField(db_column='T16', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t17 = models.DecimalField(db_column='T17', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t18 = models.CharField(db_column='T18', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t19 = models.CharField(db_column='T19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t20 = models.CharField(db_column='T20', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t21 = models.CharField(db_column='T21', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t22 = models.CharField(db_column='T22', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t23 = models.CharField(db_column='T23', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t24 = models.CharField(db_column='T24', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t25 = models.CharField(db_column='T25', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t26 = models.CharField(db_column='T26', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t27 = models.CharField(db_column='T27', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t28 = models.CharField(db_column='T28', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t29 = models.CharField(db_column='T29', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t30 = models.CharField(db_column='T30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t31 = models.CharField(db_column='T31', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t32 = models.CharField(db_column='T32', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t33 = models.CharField(db_column='T33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t34 = models.CharField(db_column='T34', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t35 = models.CharField(db_column='T35', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t36 = models.CharField(db_column='T36', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t37 = models.CharField(db_column='T37', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t38 = models.CharField(db_column='T38', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t39 = models.CharField(db_column='T39', max_length=20, blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'marketing_trans'


class MarketingUser(models.Model):
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    wage = models.IntegerField(blank=True, null=True)
    card = models.JSONField(blank=True, null=True)
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)
    user_no = models.CharField(unique=True, max_length=100, blank=True, null=True)
    loc_id = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'marketing_user'


class Operator(models.Model):
    original_id = models.CharField(db_column='original_ID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    contactor = models.CharField(max_length=200, blank=True, null=True)
    contactor_id = models.CharField(db_column='contactor_ID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mobile_phone_brand = models.CharField(max_length=200, blank=True, null=True)
    mobile_operating_system = models.CharField(max_length=200, blank=True, null=True)
    pv = models.CharField(max_length=200, blank=True, null=True)
    terminal_type = models.CharField(max_length=200, blank=True, null=True)
    video_website = models.CharField(max_length=200, blank=True, null=True)
    shopping_website = models.CharField(max_length=200, blank=True, null=True)
    overseas_taobao_shopping_channel = models.CharField(max_length=200, blank=True, null=True)
    automotive_website = models.CharField(max_length=200, blank=True, null=True)
    real_estate_website = models.CharField(max_length=200, blank=True, null=True)
    travel_website = models.CharField(max_length=200, blank=True, null=True)
    highest_calling = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    city_number = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    day_calling = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    night_calling = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    three_month_calling = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'operator'


class RegisterCard(models.Model):
    card_id = models.AutoField(primary_key=True)
    owner_type = models.CharField(max_length=50, blank=True, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    c4 = models.CharField(db_column='C4', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    c5 = models.CharField(db_column='C5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c6 = models.CharField(db_column='C6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c7 = models.CharField(db_column='C7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c8 = models.CharField(db_column='C8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c9 = models.CharField(db_column='C9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c10 = models.CharField(db_column='C10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c11 = models.CharField(db_column='C11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'register_card'


class RegisterFT(models.Model):
    f1 = models.CharField(db_column='F1', max_length=26, blank=True, null=True)  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f3 = models.CharField(db_column='F3', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f4 = models.CharField(db_column='F4', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f5 = models.CharField(db_column='F5', max_length=12, blank=True, null=True)  # Field name made lowercase.
    f6 = models.CharField(db_column='F6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f7 = models.CharField(db_column='F7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f8 = models.CharField(db_column='F8', max_length=4, blank=True, null=True)  # Field name made lowercase.
    f9 = models.CharField(db_column='F9', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f10 = models.DecimalField(db_column='F10', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f11 = models.DecimalField(db_column='F11', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f12 = models.CharField(db_column='F12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f13 = models.CharField(db_column='F13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f14 = models.CharField(db_column='F14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f15 = models.CharField(db_column='F15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f16 = models.CharField(db_column='F16', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f17 = models.CharField(db_column='F17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f18 = models.CharField(db_column='F18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f19 = models.CharField(db_column='F19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f20 = models.CharField(db_column='F20', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f21 = models.CharField(db_column='F21', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f22 = models.CharField(db_column='F22', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f23 = models.CharField(db_column='F23', max_length=2, blank=True, null=True)  # Field name made lowercase.
    f24 = models.CharField(db_column='F24', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f25 = models.CharField(db_column='F25', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f26 = models.CharField(db_column='F26', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f27 = models.CharField(db_column='F27', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f28 = models.CharField(db_column='F28', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f29 = models.CharField(db_column='F29', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f30 = models.CharField(db_column='F30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f31 = models.DateTimeField(db_column='F31', blank=True, null=True)  # Field name made lowercase.
    f32 = models.DateTimeField(db_column='F32', blank=True, null=True)  # Field name made lowercase.
    f33 = models.CharField(db_column='F33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f34 = models.CharField(db_column='F34', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f35 = models.DecimalField(db_column='F35', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f36 = models.CharField(db_column='F36', max_length=4, blank=True, null=True)  # Field name made lowercase.
    f37 = models.DecimalField(db_column='F37', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f38 = models.DecimalField(db_column='F38', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f39 = models.CharField(db_column='F39', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f40 = models.CharField(db_column='F40', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f41 = models.CharField(db_column='F41', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f42 = models.CharField(db_column='F42', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f43 = models.CharField(db_column='F43', max_length=50, blank=True, null=True)  # Field name made lowercase.
    f44 = models.DecimalField(db_column='F44', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f45 = models.CharField(db_column='F45', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'register_f_t'


class RegisterRelative(models.Model):
    user_id = models.IntegerField()
    gender = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    childlist = models.JSONField(db_column='childList', blank=True, null=True)  # Field name made lowercase.
    f_id = models.IntegerField(blank=True, null=True)
    m_id = models.IntegerField(blank=True, null=True)
    c_id = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'register_relative'


class RegisterStore(models.Model):
    industry = models.CharField(max_length=50, blank=True, null=True)
    name_field = models.CharField(db_column='name_', max_length=100, blank=True, null=True)  # Field renamed because it ended with '_'.
    rank_field = models.CharField(db_column='rank_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
    consumption_range = models.JSONField(blank=True, null=True)
    opening_hours = models.CharField(max_length=50, blank=True, null=True)
    s1 = models.CharField(db_column='S1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s2 = models.CharField(db_column='S2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s3 = models.CharField(db_column='S3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s4 = models.CharField(db_column='S4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s5 = models.CharField(db_column='S5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s6 = models.CharField(db_column='S6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s7 = models.CharField(db_column='S7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s8 = models.CharField(db_column='S8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s9 = models.CharField(db_column='S9', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s10 = models.CharField(db_column='S10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s11 = models.CharField(db_column='S11', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s12 = models.CharField(db_column='S12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s13 = models.CharField(db_column='S13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s14 = models.CharField(db_column='S14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s15 = models.CharField(db_column='S15', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s16 = models.CharField(db_column='S16', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s17 = models.CharField(db_column='S17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s18 = models.CharField(db_column='S18', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s19 = models.CharField(db_column='S19', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s20 = models.CharField(db_column='S20', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s21 = models.CharField(db_column='S21', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s22 = models.CharField(db_column='S22', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s23 = models.CharField(db_column='S23', max_length=200, blank=True, null=True)  # Field name made lowercase.
    s24 = models.CharField(db_column='S24', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s25 = models.CharField(db_column='S25', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s26 = models.CharField(db_column='S26', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s27 = models.CharField(db_column='S27', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s28 = models.CharField(db_column='S28', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s29 = models.CharField(db_column='S29', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s30 = models.JSONField(db_column='S30', blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'register_store'


class RegisterTrans(models.Model):
    t1 = models.CharField(db_column='T1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t2 = models.CharField(db_column='T2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t3 = models.CharField(db_column='T3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t4 = models.CharField(db_column='T4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t5 = models.CharField(db_column='T5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t6 = models.CharField(db_column='T6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    t7 = models.CharField(db_column='T7', max_length=5, blank=True, null=True)  # Field name made lowercase.
    t8 = models.CharField(db_column='T8', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t9 = models.CharField(db_column='T9', max_length=6, blank=True, null=True)  # Field name made lowercase.
    t10 = models.CharField(db_column='T10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t11 = models.CharField(db_column='T11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t12 = models.CharField(db_column='T12', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t13 = models.CharField(db_column='T13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t14 = models.CharField(db_column='T14', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t15 = models.CharField(db_column='T15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t16 = models.CharField(db_column='T16', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t17 = models.DecimalField(db_column='T17', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t18 = models.CharField(db_column='T18', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t19 = models.CharField(db_column='T19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t20 = models.CharField(db_column='T20', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t21 = models.CharField(db_column='T21', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t22 = models.CharField(db_column='T22', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t23 = models.CharField(db_column='T23', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t24 = models.CharField(db_column='T24', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t25 = models.CharField(db_column='T25', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t26 = models.CharField(db_column='T26', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t27 = models.CharField(db_column='T27', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t28 = models.CharField(db_column='T28', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t29 = models.CharField(db_column='T29', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t30 = models.CharField(db_column='T30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t31 = models.CharField(db_column='T31', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t32 = models.CharField(db_column='T32', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t33 = models.CharField(db_column='T33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t34 = models.CharField(db_column='T34', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t35 = models.CharField(db_column='T35', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t36 = models.CharField(db_column='T36', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t37 = models.CharField(db_column='T37', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t38 = models.CharField(db_column='T38', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t39 = models.CharField(db_column='T39', max_length=20, blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'register_trans'


class RegisterUser(models.Model):
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    wage = models.IntegerField(blank=True, null=True)
    card = models.JSONField(blank=True, null=True)
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)
    user_no = models.CharField(unique=True, max_length=100, blank=True, null=True)
    loc_id = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'register_user'


class Relative(models.Model):
    user_id = models.IntegerField()
    gender = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    childlist = models.JSONField(db_column='childList', blank=True, null=True)  # Field name made lowercase.
    f_id = models.IntegerField(blank=True, null=True)
    m_id = models.IntegerField(blank=True, null=True)
    c_id = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'relative'


class Store(models.Model):
    industry = models.CharField(max_length=50, blank=True, null=True)
    name_field = models.CharField(db_column='name_', max_length=100, blank=True, null=True)  # Field renamed because it ended with '_'.
    rank_field = models.CharField(db_column='rank_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
    consumption_range = models.JSONField(blank=True, null=True)
    opening_hours = models.CharField(max_length=50, blank=True, null=True)
    s1 = models.CharField(db_column='S1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s2 = models.CharField(db_column='S2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s3 = models.CharField(db_column='S3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s4 = models.CharField(db_column='S4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s5 = models.CharField(db_column='S5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s6 = models.CharField(db_column='S6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s7 = models.CharField(db_column='S7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s8 = models.CharField(db_column='S8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s9 = models.CharField(db_column='S9', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s10 = models.CharField(db_column='S10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s11 = models.CharField(db_column='S11', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s12 = models.CharField(db_column='S12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s13 = models.CharField(db_column='S13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s14 = models.CharField(db_column='S14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s15 = models.CharField(db_column='S15', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s16 = models.CharField(db_column='S16', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s17 = models.CharField(db_column='S17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s18 = models.CharField(db_column='S18', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s19 = models.CharField(db_column='S19', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s20 = models.CharField(db_column='S20', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s21 = models.CharField(db_column='S21', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s22 = models.CharField(db_column='S22', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s23 = models.CharField(db_column='S23', max_length=200, blank=True, null=True)  # Field name made lowercase.
    s24 = models.CharField(db_column='S24', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s25 = models.CharField(db_column='S25', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s26 = models.CharField(db_column='S26', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s27 = models.CharField(db_column='S27', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s28 = models.CharField(db_column='S28', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s29 = models.CharField(db_column='S29', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s30 = models.JSONField(db_column='S30', blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'store'


class StoreCard(models.Model):
    card_id = models.AutoField(primary_key=True)
    owner_type = models.CharField(max_length=50, blank=True, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    c4 = models.CharField(db_column='C4', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    c5 = models.CharField(db_column='C5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c6 = models.CharField(db_column='C6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c7 = models.CharField(db_column='C7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c8 = models.CharField(db_column='C8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c9 = models.CharField(db_column='C9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c10 = models.CharField(db_column='C10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c11 = models.CharField(db_column='C11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'store_card'


class StoreFT(models.Model):
    f1 = models.CharField(db_column='F1', max_length=26, blank=True, null=True)  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f3 = models.CharField(db_column='F3', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f4 = models.CharField(db_column='F4', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f5 = models.CharField(db_column='F5', max_length=12, blank=True, null=True)  # Field name made lowercase.
    f6 = models.CharField(db_column='F6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f7 = models.CharField(db_column='F7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f8 = models.CharField(db_column='F8', max_length=4, blank=True, null=True)  # Field name made lowercase.
    f9 = models.CharField(db_column='F9', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f10 = models.DecimalField(db_column='F10', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f11 = models.DecimalField(db_column='F11', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f12 = models.CharField(db_column='F12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f13 = models.CharField(db_column='F13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f14 = models.CharField(db_column='F14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f15 = models.CharField(db_column='F15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f16 = models.CharField(db_column='F16', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f17 = models.CharField(db_column='F17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f18 = models.CharField(db_column='F18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f19 = models.CharField(db_column='F19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f20 = models.CharField(db_column='F20', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f21 = models.CharField(db_column='F21', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f22 = models.CharField(db_column='F22', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f23 = models.CharField(db_column='F23', max_length=2, blank=True, null=True)  # Field name made lowercase.
    f24 = models.CharField(db_column='F24', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f25 = models.CharField(db_column='F25', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f26 = models.CharField(db_column='F26', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f27 = models.CharField(db_column='F27', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f28 = models.CharField(db_column='F28', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f29 = models.CharField(db_column='F29', max_length=11, blank=True, null=True)  # Field name made lowercase.
    f30 = models.CharField(db_column='F30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f31 = models.DateTimeField(db_column='F31', blank=True, null=True)  # Field name made lowercase.
    f32 = models.DateTimeField(db_column='F32', blank=True, null=True)  # Field name made lowercase.
    f33 = models.CharField(db_column='F33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    f34 = models.CharField(db_column='F34', max_length=5, blank=True, null=True)  # Field name made lowercase.
    f35 = models.DecimalField(db_column='F35', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f36 = models.CharField(db_column='F36', max_length=4, blank=True, null=True)  # Field name made lowercase.
    f37 = models.DecimalField(db_column='F37', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f38 = models.DecimalField(db_column='F38', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f39 = models.CharField(db_column='F39', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f40 = models.CharField(db_column='F40', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f41 = models.CharField(db_column='F41', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f42 = models.CharField(db_column='F42', max_length=20, blank=True, null=True)  # Field name made lowercase.
    f43 = models.CharField(db_column='F43', max_length=50, blank=True, null=True)  # Field name made lowercase.
    f44 = models.DecimalField(db_column='F44', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    f45 = models.CharField(db_column='F45', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'store_f_t'


class StoreRelative(models.Model):
    user_id = models.IntegerField()
    gender = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    childlist = models.JSONField(db_column='childList', blank=True, null=True)  # Field name made lowercase.
    f_id = models.IntegerField(blank=True, null=True)
    m_id = models.IntegerField(blank=True, null=True)
    c_id = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'store_relative'


class StoreStore(models.Model):
    industry = models.CharField(max_length=50, blank=True, null=True)
    name_field = models.CharField(db_column='name_', max_length=100, blank=True, null=True)  # Field renamed because it ended with '_'.
    rank_field = models.CharField(db_column='rank_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
    consumption_range = models.JSONField(blank=True, null=True)
    opening_hours = models.CharField(max_length=50, blank=True, null=True)
    s1 = models.CharField(db_column='S1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s2 = models.CharField(db_column='S2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s3 = models.CharField(db_column='S3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s4 = models.CharField(db_column='S4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s5 = models.CharField(db_column='S5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s6 = models.CharField(db_column='S6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s7 = models.CharField(db_column='S7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s8 = models.CharField(db_column='S8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s9 = models.CharField(db_column='S9', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s10 = models.CharField(db_column='S10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s11 = models.CharField(db_column='S11', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s12 = models.CharField(db_column='S12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s13 = models.CharField(db_column='S13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s14 = models.CharField(db_column='S14', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s15 = models.CharField(db_column='S15', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s16 = models.CharField(db_column='S16', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s17 = models.CharField(db_column='S17', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s18 = models.CharField(db_column='S18', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s19 = models.CharField(db_column='S19', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s20 = models.CharField(db_column='S20', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s21 = models.CharField(db_column='S21', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s22 = models.CharField(db_column='S22', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s23 = models.CharField(db_column='S23', max_length=200, blank=True, null=True)  # Field name made lowercase.
    s24 = models.CharField(db_column='S24', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s25 = models.CharField(db_column='S25', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s26 = models.CharField(db_column='S26', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s27 = models.CharField(db_column='S27', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s28 = models.CharField(db_column='S28', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s29 = models.CharField(db_column='S29', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s30 = models.JSONField(db_column='S30', blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'store_store'


class StoreTrans(models.Model):
    t1 = models.CharField(db_column='T1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t2 = models.CharField(db_column='T2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t3 = models.CharField(db_column='T3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t4 = models.CharField(db_column='T4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t5 = models.CharField(db_column='T5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t6 = models.CharField(db_column='T6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    t7 = models.CharField(db_column='T7', max_length=5, blank=True, null=True)  # Field name made lowercase.
    t8 = models.CharField(db_column='T8', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t9 = models.CharField(db_column='T9', max_length=6, blank=True, null=True)  # Field name made lowercase.
    t10 = models.CharField(db_column='T10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t11 = models.CharField(db_column='T11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t12 = models.CharField(db_column='T12', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t13 = models.CharField(db_column='T13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t14 = models.CharField(db_column='T14', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t15 = models.CharField(db_column='T15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t16 = models.CharField(db_column='T16', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t17 = models.DecimalField(db_column='T17', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t18 = models.CharField(db_column='T18', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t19 = models.CharField(db_column='T19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t20 = models.CharField(db_column='T20', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t21 = models.CharField(db_column='T21', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t22 = models.CharField(db_column='T22', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t23 = models.CharField(db_column='T23', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t24 = models.CharField(db_column='T24', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t25 = models.CharField(db_column='T25', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t26 = models.CharField(db_column='T26', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t27 = models.CharField(db_column='T27', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t28 = models.CharField(db_column='T28', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t29 = models.CharField(db_column='T29', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t30 = models.CharField(db_column='T30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t31 = models.CharField(db_column='T31', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t32 = models.CharField(db_column='T32', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t33 = models.CharField(db_column='T33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t34 = models.CharField(db_column='T34', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t35 = models.CharField(db_column='T35', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t36 = models.CharField(db_column='T36', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t37 = models.CharField(db_column='T37', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t38 = models.CharField(db_column='T38', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t39 = models.CharField(db_column='T39', max_length=20, blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'store_trans'


class StoreUser(models.Model):
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    wage = models.IntegerField(blank=True, null=True)
    card = models.JSONField(blank=True, null=True)
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)
    user_no = models.CharField(unique=True, max_length=100, blank=True, null=True)
    loc_id = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'store_user'

class Trans(models.Model):
    t1 = models.CharField(db_column='T1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t2 = models.CharField(db_column='T2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t3 = models.CharField(db_column='T3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t4 = models.CharField(db_column='T4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t5 = models.CharField(db_column='T5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t6 = models.CharField(db_column='T6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    t7 = models.CharField(db_column='T7', max_length=5, blank=True, null=True)  # Field name made lowercase.
    t8 = models.CharField(db_column='T8', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t9 = models.CharField(db_column='T9', max_length=6, blank=True, null=True)  # Field name made lowercase.
    t10 = models.CharField(db_column='T10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t11 = models.CharField(db_column='T11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t12 = models.CharField(db_column='T12', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t13 = models.CharField(db_column='T13', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t14 = models.CharField(db_column='T14', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t15 = models.CharField(db_column='T15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t16 = models.CharField(db_column='T16', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t17 = models.DecimalField(db_column='T17', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t18 = models.CharField(db_column='T18', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t19 = models.CharField(db_column='T19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t20 = models.CharField(db_column='T20', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t21 = models.CharField(db_column='T21', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t22 = models.CharField(db_column='T22', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t23 = models.CharField(db_column='T23', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t24 = models.CharField(db_column='T24', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t25 = models.CharField(db_column='T25', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t26 = models.CharField(db_column='T26', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t27 = models.CharField(db_column='T27', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t28 = models.CharField(db_column='T28', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t29 = models.CharField(db_column='T29', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t30 = models.CharField(db_column='T30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t31 = models.CharField(db_column='T31', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t32 = models.CharField(db_column='T32', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t33 = models.CharField(db_column='T33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t34 = models.CharField(db_column='T34', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t35 = models.CharField(db_column='T35', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t36 = models.CharField(db_column='T36', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t37 = models.CharField(db_column='T37', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t38 = models.CharField(db_column='T38', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t39 = models.CharField(db_column='T39', max_length=20, blank=True, null=True)  # Field name made lowercase.
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'trans'


class User(models.Model):
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    wage = models.IntegerField(blank=True, null=True)
    card = models.JSONField(blank=True, null=True)
    abnormal = models.IntegerField(blank=True, null=True)
    abnormal_state = models.JSONField(blank=True, null=True)
    user_no = models.CharField(unique=True, max_length=100, blank=True, null=True)
    loc_id = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'user'

class System_log(models.Model):
    user = models.CharField(max_length=255)
    change = models.CharField(max_length=255)
    time = models.DateTimeField()
    result = models.CharField(max_length=10)

    class Meta:
        # managed = False
        db_table = 'system_log'