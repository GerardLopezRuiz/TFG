"""init

Revision ID: c74ef58ec700
Revises: 8adc0f34e6dc
Create Date: 2023-12-28 17:47:26.775191

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c74ef58ec700'
down_revision: Union[str, None] = '8adc0f34e6dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'practicas', ['nom'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'practicas', type_='unique')
    # ### end Alembic commands ###
