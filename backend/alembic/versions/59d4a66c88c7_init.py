"""init

Revision ID: 59d4a66c88c7
Revises: bc2621ddc1d0
Create Date: 2023-12-03 23:32:24.374856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59d4a66c88c7'
down_revision: Union[str, None] = 'bc2621ddc1d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cursos_usuario', 'cursos_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('cursos_usuario_user_niub_fkey', 'cursos_usuario', type_='foreignkey')
    op.drop_column('cursos_usuario', 'user_niub')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cursos_usuario', sa.Column('user_niub', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('cursos_usuario_user_niub_fkey', 'cursos_usuario', 'users', ['user_niub'], ['niub'])
    op.alter_column('cursos_usuario', 'cursos_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
