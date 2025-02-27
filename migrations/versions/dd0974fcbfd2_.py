"""empty message

Revision ID: dd0974fcbfd2
Revises: 780f0cc40ea9
Create Date: 2021-03-19 10:21:33.272362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd0974fcbfd2'
down_revision = '780f0cc40ea9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('new_properties', sa.Column('photo', sa.String(length=255), nullable=True))
    op.drop_column('new_properties', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('new_properties', sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('new_properties', 'photo')
    # ### end Alembic commands ###
