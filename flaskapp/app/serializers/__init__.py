import sys
from flask_marshmallow import Marshmallow
from app.models import Address, Drug, DrugGroupPreset, Internment, Measure, Patient, User, Cid10, Prescription, Diet, DrugPrescription, NursingActivity, RestingActivity, Evolution, Pending, Allergy, Comorbidity, FluidBalance, FluidBalanceDescription
from marshmallow import fields
from marshmallow_sqlalchemy import fields as sqa_fields

ma = Marshmallow()


def camelcase(s):
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


class CamelCaseSchema(ma.SQLAlchemyAutoSchema):
    """Schema that uses camel-case for its external representation
    and snake-case for its internal representation.
    """

    def on_bind_field(self, field_name, field_obj):

        field_obj.data_key = camelcase(field_obj.data_key or field_name)


class EnumToDictionaryField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return value.name


class ChildValueField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return value.value


class Cid10Schema(CamelCaseSchema):
    class Meta:
        model = Cid10


class DietSchema(CamelCaseSchema):
    class Meta:
        model = Diet


class NursingActivitySchema(CamelCaseSchema):
    class Meta:
        model = NursingActivity


class RestingActivitySchema(CamelCaseSchema):
    class Meta:
        model = RestingActivity


class DrugSchema(CamelCaseSchema):
    kind = EnumToDictionaryField(attribute=('kind'))

    class Meta:
        model = Drug


class DrugPrescriptionSchema(CamelCaseSchema):
    class Meta:
        model = DrugPrescription
        include_fk = True
        include_relationships = True

    drug = sqa_fields.Nested(DrugSchema)


class PrescriptionSchema(CamelCaseSchema):
    class Meta:
        model = Prescription
        include_fk = True
        include_relationships = True

    drug_prescriptions = sqa_fields.RelatedList(
        sqa_fields.Nested(DrugPrescriptionSchema))
    nursing_activities = sqa_fields.RelatedList(
        sqa_fields.Nested(NursingActivitySchema))
    diet = sqa_fields.Nested(DietSchema)
    resting_activity = sqa_fields.Nested(RestingActivitySchema)


class DrugGroupPresetSchema(CamelCaseSchema):
    class Meta:
        model = DrugGroupPreset
        include_fk = True
        include_relationships = True

    drugs = sqa_fields.RelatedList(sqa_fields.Nested(DrugSchema))


class UserSchema(CamelCaseSchema):
    professional_category = EnumToDictionaryField(
        attribute=('professional_category'))
    birthdate = fields.Date(format='%Y-%m-%d')

    class Meta:
        model = User


class AllergySchema(CamelCaseSchema):
    class Meta:
        model = Allergy


class ComorbiditySchema(CamelCaseSchema):
    class Meta:
        model = Comorbidity


class EvolutionSchema(CamelCaseSchema):
    class Meta:
        model = Evolution

    professional = sqa_fields.Nested(UserSchema)


class FluidBalanceDescriptionSchema(CamelCaseSchema):
    class Meta:
        model = FluidBalanceDescription


class FluidBalanceSchema(CamelCaseSchema):
    class Meta:
        model = FluidBalance

    professional = sqa_fields.Nested(UserSchema)
    description = sqa_fields.Nested(FluidBalanceDescriptionSchema)


class EvolutionSchema(CamelCaseSchema):
    class Meta:
        model = Evolution

    professional = sqa_fields.Nested(UserSchema)


class AddressSchema(CamelCaseSchema):
    class Meta:
        model = Address


class PatientSchema(CamelCaseSchema):
    class Meta:
        model = Patient
        include_fk = True

    sex = EnumToDictionaryField(attribute=('sex'))
    age = fields.Str(dump_only=True)
    address = sqa_fields.Nested(AddressSchema)
    allergies = sqa_fields.RelatedList(sqa_fields.Nested(AllergySchema))
    comorbidities = sqa_fields.RelatedList(
        sqa_fields.Nested(ComorbiditySchema))


class Cid10Schema(CamelCaseSchema):
    class Meta:
        model = Cid10


class MeasureSchema(CamelCaseSchema):
    diastolic_blood_pressure = fields.Integer(attribute="diastolic_bp")
    systolic_blood_pressure = fields.Integer(attribute="systolic_bp")
    fetal_cardiac_frequency = fields.Integer(attribute="fetal_cardiac_freq")
    cardiac_frequency = fields.Integer(attribute="cardiac_freq")
    respiratory_frequency = fields.Integer(attribute="respiratory_freq")

    class Meta:
        model = Measure
        exclude = ['diastolic_bp', 'systolic_bp',
                   'fetal_cardiac_freq', 'cardiac_freq', 'respiratory_freq']


class PendingSchema(CamelCaseSchema):
    class Meta:
        model = Pending


class InternmentSchema(CamelCaseSchema):
    class Meta:
        model = Internment
        include_fk = True
        include_relationships = True

    patient = sqa_fields.Nested(PatientSchema)
    cid10 = sqa_fields.Nested(Cid10Schema)
    measures = sqa_fields.RelatedList(sqa_fields.Nested(MeasureSchema))
    evolutions = sqa_fields.RelatedList(sqa_fields.Nested(EvolutionSchema))
    prescriptions = sqa_fields.RelatedList(
        sqa_fields.Nested(PrescriptionSchema))
    pendings = sqa_fields.RelatedList(sqa_fields.Nested(PendingSchema))
    fluid_balance = sqa_fields.RelatedList(
        sqa_fields.Nested(FluidBalanceSchema))
