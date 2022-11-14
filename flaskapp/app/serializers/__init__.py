from flask_marshmallow import Marshmallow
from app.models import Drug, DrugGroupPreset, Internment, Patient, User, Cid10, Prescription, Diet, DrugPrescription, NursingActivity, RestingActivity, Evolution
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


class EnumToDictionary(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return value.name

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
    kind = EnumToDictionary(attribute=('kind'))

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

    drug_prescriptions = sqa_fields.RelatedList(sqa_fields.Nested(DrugPrescriptionSchema))
    nursing_activities = sqa_fields.RelatedList(sqa_fields.Nested(NursingActivitySchema))
    diet = sqa_fields.Nested(DietSchema)
    resting_activity = sqa_fields.Nested(RestingActivitySchema)


class EvolutionSchema(CamelCaseSchema):
    class Meta:
        model = Evolution

class DrugGroupPresetSchema(CamelCaseSchema):
    class Meta:
        model = DrugGroupPreset
        include_fk = True
        include_relationships = True

    drugs = sqa_fields.RelatedList(sqa_fields.Nested(DrugSchema))


class UserSchema(CamelCaseSchema):
    professional_category = EnumToDictionary(
        attribute=('professional_category'))
    birthday = fields.Date(format='%Y-%m-%d')

    class Meta:
        model = User
        include_fk = True


class PatientSchema(CamelCaseSchema):
    sex = EnumToDictionary(attribute=('sex'))

    class Meta:
        model = Patient
        include_fk = True


class InternmentSchema(CamelCaseSchema):
    class Meta:
        model = Internment
        include_fk = True
