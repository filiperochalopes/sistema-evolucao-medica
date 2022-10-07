from app import ma
from app.models import Cid10


class Cid10Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cid10
