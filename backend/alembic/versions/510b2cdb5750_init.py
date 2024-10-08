"""init

Revision ID: 510b2cdb5750
Revises: 1b6bff106432
Create Date: 2023-12-03 23:53:10.648150

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '510b2cdb5750'
down_revision: Union[str, None] = '1b6bff106432'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cursos_usuario', sa.Column('user_niub', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'cursos_usuario', 'user', ['user_niub'], ['niub'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cursos_usuario', type_='foreignkey')
    op.drop_column('cursos_usuario', 'user_niub')
    # ### end Alembic commands ###
