import sys
from app.graphql import query
from app.models import Internment, db, Patient
from app.serializers import InternmentSchema

@query.field("internment")
def internment(*_, id:int):
    schema = InternmentSchema()
    return schema.dump(db.session.query(Internment).get(id))


@query.field("internments")
def internments(*_, active=True, cns=None):
    # Query de todas as internações
    query = db.session.query(Internment)
    if active == True:
        # Filtra por todos aqueles que não tem finished_at preenchidos
        query = query.filter(Internment.finished_at.is_(None))
    elif active == False:
        # Filtra por todos aqueles que já encerraram
        query = query.filter(Internment.finished_at.is_not(None))
    if cns is not None:
        # Caso tenha cns, filtra pelos internamentos que pertencem apenas ao paciente em questão
        query = query.filter(Internment.patient.has(Patient.cns == cns))

    schema = InternmentSchema(many=True)
    print(schema.dump(query.all()), file=sys.stderr)
    return schema.dump(query.all())
