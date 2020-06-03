"""processes

Revision ID: 7f778a2c60ed
Revises: a5b2af3ce9ec
Create Date: 2020-06-03 17:00:32.903763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f778a2c60ed'
down_revision = 'a5b2af3ce9ec'
branch_labels = None
depends_on = None


def upgrade():
# ### commands auto generated by Alembic - please adjust! ###
    op.create_table('machineprocess',
    sa.Column('machine_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('path', sa.String(), nullable=True),
    sa.Column('hash', sa.String(), nullable=True),
    sa.Column('is_hash_same', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['machine_id'], ['machine.id'], ),
    sa.PrimaryKeyConstraint('machine_id', 'id')
    )
    op.create_index(op.f('ix_machineprocess_id'), 'machineprocess', ['id'], unique=False)
    op.create_index(op.f('ix_machineprocess_is_hash_same'), 'machineprocess', ['is_hash_same'], unique=False)
    op.create_index(op.f('ix_machineprocess_name'), 'machineprocess', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
# ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_machineprocess_name'), table_name='machineprocess')
    op.drop_index(op.f('ix_machineprocess_is_hash_same'), table_name='machineprocess')
    op.drop_index(op.f('ix_machineprocess_id'), table_name='machineprocess')
    op.drop_table('machineprocess')
    # ### end Alembic commands ###