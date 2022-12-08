from flask_marshmallow import Marshmallow
from app.models import Internment, Patient, User, Cid10
from marshmallow import fields

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


class Cid10Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cid10

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
