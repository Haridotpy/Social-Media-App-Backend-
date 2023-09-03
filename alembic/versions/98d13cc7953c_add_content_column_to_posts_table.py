"""add content column to posts table

Revision ID: 98d13cc7953c
Revises: 6d3b896ab0c1
Create Date: 2023-09-03 10:55:21.622137

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98d13cc7953c'
down_revision: Union[str, None] = '6d3b896ab0c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
