from app.graphql import query
from ariadne import convert_kwargs_to_snake_case
from app.models import db, Cid10
from sqlalchemy import or_

# TODO Criar depois priorização para que apareçam primeiro em ordem os cids mais utilizados
@query.field("cid10")
@convert_kwargs_to_snake_case
def cid10(*_, query:str='', per_page:int=25, page:int=1):   
    # return db.session.paginate(db.session.query(Cid10).all())
    return db.session.query(Cid10).filter(or_(Cid10.description.like(f"%{query}%"),Cid10.code.like(f"%{query}%"))).order_by(Cid10.code).paginate(page=page, per_page=per_page)