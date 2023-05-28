"""add phone to patient

Revision ID: b30b55693a90
Revises: 49f6dfaa400d
Create Date: 2023-02-03 10:09:03.347190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b30b55693a90'
down_revision = '49f6dfaa400d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('phone', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patients', 'phone')
    # ### end Alembic commands ###
