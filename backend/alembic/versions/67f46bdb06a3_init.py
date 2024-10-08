"""init

Revision ID: 67f46bdb06a3
Revises: 9227216e5695
Create Date: 2023-12-03 22:47:35.827904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67f46bdb06a3'
down_revision: Union[str, None] = '9227216e5695'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_assignaturas_alumnos_id_assignatura'), 'assignaturas_alumnos', ['id_assignatura'], unique=False)
    op.create_index(op.f('ix_assignaturas_alumnos_niub'), 'assignaturas_alumnos', ['niub'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_assignaturas_alumnos_niub'), table_name='assignaturas_alumnos')
    op.drop_index(op.f('ix_assignaturas_alumnos_id_assignatura'), table_name='assignaturas_alumnos')
    # ### end Alembic commands ###
