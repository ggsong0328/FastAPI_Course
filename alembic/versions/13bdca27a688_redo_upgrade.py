"""Redo Upgrade

Revision ID: 13bdca27a688
Revises: faed16d6e5ab
Create Date: 2025-07-09 16:56:27.655998

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13bdca27a688'
down_revision: Union[str, None] = 'faed16d6e5ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
