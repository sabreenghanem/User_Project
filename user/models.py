
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime, Enum, Float, Text



Base=declarative_base()


class CountryCodeLookup(Base):
   __tablename__="country_code_lookup"
   id=Column(Integer,primary_key=True)
   iso=Column(String(45))
   name=Column(String(45))
   nice_name=Column(String(45))
   iso3=Column(String(45))
   number_code=Column(Integer)
   phone_code=Column(Integer)
   flag=Column(String(45))
   created=Column(DateTime, default=datetime.datetime.now)
   updated=Column(DateTime,onupdate=datetime.datetime.now)
   user=relationship('User',back_populates='country_code_lookup')
 # def __repr__(self):
	 # return "<CountryCodeLookup(name='%s',nice_name='%s')>"%(self.name,self.nice_name)


class User(Base):
   __tablename__="user"
   id=Column(Integer,primary_key=True)
   first_name=Column(String(45))
   surname=Column(String(45))
   email=Column(String(45))
   date_of_birth=Column(DateTime)
   phone=Column(String(45))
   gender=Column(Enum('male','female'))
   password=Column(String(45))
   country_code_lookup_id=Column(Integer,ForeignKey('country_code_lookup.id'))
   country_code_lookup=relationship('CountryCodeLookup',back_populates='user')
   user_general_info=relationship('UserGeneralInfo',back_populates='user')
	# def __repr__(self):
	# 	return "<User(first_name='%s',surname='%s')>"%(self.first_name,self.surname)


class UserGeneralInfo(Base):
   __tablename__="user_general_info"
   id=Column(Integer,primary_key=True)
   hight=Column(Float)
   weight=Column(Float)
   marital_status=Column(Enum('Married','single','divorced','widowed'))
   registered_treatment=Column(Text)
   created=Column(DateTime)
   updated=Column(DateTime,onupdate=datetime.datetime.now)
   user_id=Column(Integer,ForeignKey('user.id'))
   user=relationship('User',back_populates='user_general_info')
