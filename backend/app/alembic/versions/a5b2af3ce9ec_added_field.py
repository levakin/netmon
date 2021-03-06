"""Added field

Revision ID: a5b2af3ce9ec
Revises: ad6931f0a372
Create Date: 2020-06-02 09:54:23.961337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5b2af3ce9ec'
down_revision = 'ad6931f0a372'
branch_labels = None
depends_on = None


def upgrade():
# ### commands auto generated by Alembic - please adjust! ###
    op.add_column('machine', sa.Column('last_online_timestamp', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_machine_last_online_timestamp'), 'machine', ['last_online_timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
# ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_machine_last_online_timestamp'), table_name='machine')
    op.drop_column('machine', 'last_online_timestamp')
    # ### end Alembic commands ###
