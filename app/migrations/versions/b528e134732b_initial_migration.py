"""Initial migration

Revision ID: b528e134732b
Revises: 
Create Date: 2023-05-12 20:27:44.228061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b528e134732b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('couriers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('regions', sa.ARRAY(sa.Integer()), nullable=False),
    sa.Column('working_hours', sa.ARRAY(sa.String()), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('assignments',
    sa.Column('courier_id', sa.Integer(), nullable=False),
    sa.Column('time', sa.String(), nullable=False),
    sa.Column('order_id', sa.ARRAY(sa.Integer()), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['courier_id'], ['couriers.id'], ),
    sa.PrimaryKeyConstraint('courier_id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('region', sa.Integer(), nullable=False),
    sa.Column('time', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('complition_time', sa.String(), nullable=True),
    sa.Column('courier_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['courier_id'], ['couriers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('assignments')
    op.drop_table('couriers')
    # ### end Alembic commands ###
