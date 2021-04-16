"""empty message

Revision ID: 1a7867213793
Revises: bcb6f210abb1
Create Date: 2021-04-16 06:39:36.537860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a7867213793'
down_revision = 'bcb6f210abb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('name', table_name='children')
    op.drop_index('name', table_name='parent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('name', 'parent', ['name'], unique=True)
    op.create_index('name', 'children', ['name'], unique=True)
    # ### end Alembic commands ###