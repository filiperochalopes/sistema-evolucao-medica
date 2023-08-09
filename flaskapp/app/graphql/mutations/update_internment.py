from datetime import datetime

from ariadne import convert_kwargs_to_snake_case

from app.models import Internment, db
from app.serializers import InternmentSchema
from app.graphql import mutation
from app.models import Internment
from app.services.utils.decorators import token_authorization

@mutation.field('updateInternment')
@convert_kwargs_to_snake_case
@token_authorization
def update_internment(_, info, id: int, finished_at: str, current_user: dict, re_open:bool=False):
    internment = db.session.query(Internment).get(id)
    if finished_at:
        internment.finished_at = datetime.fromisoformat(finished_at)
        internment.finished_by = current_user
    if re_open:
        internment.finished_at = False
        internment.finished_by_id = None
    db.session.commit()

    schema = InternmentSchema()
    return schema.dump(internment)
