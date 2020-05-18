from sqlalchemy import create_engine,Column,String,Integer,ForeignKey,Boolean,Float,Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker ,relationship
import sqlite3

Base=declarative_base()

engine=create_engine("sqlite:///database.db", echo=True)
Session=sessionmaker(bind=engine)
session=Session()

class MCQ(Base):
    __tablename__='MCQ'
    id=Column('id',Integer,primary_key=True)
    Question=Column('Question',String,nullable=False)
    first_Choice=Column('first_Choice',String,nullable=False)
    second_Choice = Column('second_Choice', String, nullable=False)
    third_Choice = Column('third_Choice', String, nullable=False)
    fourth_Choice = Column('fourth_Choice', String, nullable=False)
    answer=Column('answer',String,nullable=False)
    mark=Column('mark',Float,nullable=False)
    Quiz_id = Column(Integer, ForeignKey('Quiz.id'))

    def __init__(self,id,Question,first_choice,second_choice,third_choice,fourth_choice,answer,mark,Quiz_id):
        self.id=id
        self.Question=Question
        self.first_Choice=first_choice
        self.second_Choice=second_choice
        self.third_Choice=third_choice
        self.fourth_Choice=fourth_choice
        self.answer=answer
        self.mark=mark
        self.Quiz_id=Quiz_id

class TrueOrFalse(Base):
    __tablename__='TrueOrFalse'
    id=Column('id',Integer,primary_key=True)
    Question=Column('Question',String,nullable=False)
    answer=Column('answer',Boolean,nullable=False)
    mark = Column('mark', Float, nullable=False)
    Quiz_id = Column(Integer, ForeignKey('Quiz.id'))

    def __init__(self, id, Question, answer, mark, Quiz_id):
        self.id = id
        self.Question = Question
        self.answer = answer
        self.mark = mark
        self.Quiz_id = Quiz_id

class Essay_Question(Base):
    __tablename__='Essay_Question'
    id=Column('id',Integer,primary_key=True)
    Question=Column('Question',String,nullable=False)
    answer=Column('answer',String,nullable=False)
    mark = Column('mark', Float, nullable=False)
    Quiz_id = Column(Integer, ForeignKey('Quiz.id'))

    def __init__(self, id, Question, answer, mark, Quiz_id):
        self.id = id
        self.Question = Question
        self.answer = answer
        self.mark = mark
        self.Quiz_id = Quiz_id

class Integer_Question(Base):
    __tablename__='Integer_Question'
    id=Column('id',Integer,primary_key=True)
    Question=Column('Question',String,nullable=False)
    answer=Column('answer',Integer,nullable=False)
    mark = Column('mark', Float, nullable=False)
    Quiz_id = Column(Integer, ForeignKey('Quiz.id'))

    def __init__(self, id, Question, answer, mark, Quiz_id):
        self.id = id
        self.Question = Question
        self.answer = answer
        self.mark = mark
        self.Quiz_id = Quiz_id

class Float_Question(Base):
    __tablename__=' Float_Question'
    id=Column('id',Integer,primary_key=True)
    Question=Column('Question',String,nullable=False)
    answer=Column('answer',Float,nullable=False)
    mark = Column('mark', Float, nullable=False)
    Quiz_id = Column(Integer, ForeignKey('Quiz.id'))

    def __init__(self, id, Question, answer, mark, Quiz_id):
        self.id = id
        self.Question = Question
        self.answer = answer
        self.mark = mark
        self.Quiz_id = Quiz_id

class Quiz(Base):
    __tablename__ = 'Quiz'
    id = Column( Integer,primary_key=True)
    Time=Column(Time, nullable=False)
    Mcq =relationship("MCQ", backref='Quiz')
    TrueOrFalse=relationship(" TrueOrFalse",backref='Quiz')
    Essay_Question=relationship("Essay_Question",backref='Quiz')
    Integer_Question = relationship("Integer_Question", backref='Quiz')
    Float_Question = relationship("Float_Question", backref='Quiz')

Base.metadata.create_all(bind=engine)

MCq=MCQ(1,'how old are you','1','2','3','4','3',2)

session.add(MCq)
session.commit()
session.close()
