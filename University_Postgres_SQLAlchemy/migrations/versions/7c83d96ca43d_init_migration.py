"""init migration

Revision ID: 7c83d96ca43d
Revises: 
Create Date: 2023-05-13 17:31:46.019438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c83d96ca43d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('professors',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=75), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('professor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['professor_id'], ['professors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('marks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('mark', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('professor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['professor_id'], ['professors.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('marks')
    op.drop_table('subjects')
    op.drop_table('students')
    op.drop_table('professors')
    op.drop_table('groups')
    # ### end Alembic commands ###
