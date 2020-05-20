"""Initial Migration

Revision ID: 1641d785cef3
Revises: 29d608733294
Create Date: 2020-05-14 11:49:45.007337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1641d785cef3'
down_revision = '29d608733294'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('donate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('donate')
    # ### end Alembic commands ###
