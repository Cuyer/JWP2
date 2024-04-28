from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.sql import select

engine = create_engine('sqlite:///census.sqlite', echo=True)
meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer),
    Column('grade', Float)
)


meta.create_all(engine)

ins = students.insert().values(name='Maciej', age=19, grade=4.0)
ins2 = students.insert().values(name='Paweł', age=20, grade=3.0)
ins3 = students.insert().values(name='Jacek', age=19, grade=5.0)
sel = students.select()
with engine.connect() as conn:
    conn.execute(ins)
    conn.execute(ins2)
    conn.execute(ins3)

    result = conn.execute(sel)

    for select_result in result:
        print(select_result)