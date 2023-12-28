"""init

Revision ID: c1d2366a1a3f
Revises: bc87f3b36813
Create Date: 2023-12-28 17:19:13.909494

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1d2366a1a3f'
down_revision: Union[str, None] = 'bc87f3b36813'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('practicas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('curs', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(), nullable=False),
    sa.Column('descripcio', sa.String(), nullable=True),
    sa.Column('idiomaP', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['curs'], ['cursos.id'], ),
    sa.PrimaryKeyConstraint('id', 'nom')
    )
    op.create_index(op.f('ix_practicas_id'), 'practicas', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_practicas_id'), table_name='practicas')
    op.drop_table('practicas')
    # ### end Alembic commands ###
