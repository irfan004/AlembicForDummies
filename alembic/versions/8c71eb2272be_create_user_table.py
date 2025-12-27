"""create user table

Revision ID: 8c71eb2272be
Revises: 
Create Date: 2025-12-28 10:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

# --- THESE ARE THE MANDATORY VARIABLES ---
revision = '8c71eb2272be'  # This must match the start of your filename
down_revision = None       # This is None because it's your first migration
branch_labels = None
depends_on = None
# ----------------------------------------

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )

def downgrade():
    op.drop_table('users')