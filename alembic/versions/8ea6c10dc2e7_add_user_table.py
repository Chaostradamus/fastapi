"""add user table

Revision ID: 8ea6c10dc2e7
Revises: c434cdbbd003
Create Date: 2022-06-06 22:33:31.298725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ea6c10dc2e7'
down_revision = 'c434cdbbd003'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
        server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'))
    
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
