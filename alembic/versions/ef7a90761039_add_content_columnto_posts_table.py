"""add content columnto posts table

Revision ID: ef7a90761039
Revises: 5eec24b3dc6e
Create Date: 2025-07-09 16:36:03.396034

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef7a90761039'
down_revision: Union[str, None] = '5eec24b3dc6e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
