"""add email and bio

Revision ID: 748fb240bb45
Revises: 8c71eb2272be
Create Date: 2025-12-28 00:36:38.125414

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '748fb240bb45'
down_revision: Union[str, Sequence[str], None] = '8c71eb2272be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('users', sa.Column('email', sa.String(100), unique=True))
    op.add_column('users', sa.Column('bio', sa.Text()))

def downgrade():
    op.drop_column('users', 'bio')
    op.drop_column('users', 'email')
