from rest_framework import serializers
from candidate.models import Candidatedirectory
from django.db import models
from django.core.validators import EmailValidator,MinValueValidator, MaxValueValidator, RegexValidator
class CandidatedirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatedirectory
        fields = '__all__'

class PersonalSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()])
    contact_no_primary = serializers.DecimalField(max_digits=10,decimal_places=0,allow_null=True,required=False,
        validators=[RegexValidator(r'^\d{10}$', message="Mobile number must be a 10-digit number.")]
    )
    contact_no_alternate = serializers.DecimalField(max_digits=10,decimal_places=0,allow_null=True,required=False,
        validators=[RegexValidator(r'^\d{10}$', message="Alternate mobile number must be a 10-digit number.")]
    )
    class Meta:
        model = Candidatedirectory
        fields = (
            'first_name',
            'last_name',
            'email',
            'dob',
            'gender',
            'marital_status',
            'contact_no_primary',
            'contact_no_alternate',
            'address_line',
            'city',
            'pincode',
        )

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatedirectory
        fields = (
            'education_level',
            'education_qualification',
            'education_specialization',
            'education_specialization_other',
            'education_institution',
            'education_institution_other',
        )

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatedirectory
        fields = (
            'years_of_experience',
            'current_employer',
            'current_designation',
        )

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatedirectory
        fields = (
            'persona',
            'job_position',
            'role',
            'event',
            'referred_by',
            'referred_by_other',
            'experience_level',
            'source',
            'source_type',
            'current_monthly_salary',
            'expected_monthly_salary',
            'notice_period',
            'reason_for_change',
            'photo_path',
            'resume_path',
            'recruiter_alert',
            'screening_mode',
            'geo_location',
        )

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatedirectory
        fields = (
            'created_date',
            'created_by',
            'modified_date',
            'modified_by',
            'status',
            'login_time',
            'logout_time',
            'ip_address'
        )
