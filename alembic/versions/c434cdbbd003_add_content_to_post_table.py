"""add content to post table

Revision ID: c434cdbbd003
Revises: fd2541b17948
Create Date: 2022-06-06 22:27:18.116510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c434cdbbd003'
down_revision = 'fd2541b17948'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
