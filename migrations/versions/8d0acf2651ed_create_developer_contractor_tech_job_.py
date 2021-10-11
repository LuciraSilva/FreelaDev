"""create developer, contractor, tech, job, developers_techs tables

Revision ID: 8d0acf2651ed
Revises: 
Create Date: 2021-10-11 10:04:24.206041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d0acf2651ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contractors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('cnpj', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cnpj'),
    sa.UniqueConstraint('email')
    )
    op.create_table('developers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('birthdate', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('difficulty_level', sa.String(), nullable=False),
    sa.Column('expiration_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('progress', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('techs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('developers_techs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('developer_id', sa.Integer(), nullable=True),
    sa.Column('tech_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['developer_id'], ['developers.id'], ),
    sa.ForeignKeyConstraint(['tech_id'], ['techs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('developers_techs')
    op.drop_table('techs')
    op.drop_table('jobs')
    op.drop_table('developers')
    op.drop_table('contractors')
    # ### end Alembic commands ###