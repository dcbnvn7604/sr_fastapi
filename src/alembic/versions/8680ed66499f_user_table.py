"""user table

Revision ID: 8680ed66499f
Revises: 
Create Date: 2023-10-24 03:03:54.228855

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8680ed66499f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(30), unique=True),
        sa.Column('password', sa.String(60), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('user')
