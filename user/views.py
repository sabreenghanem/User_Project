
from _mysql import connection

from django.shortcuts import render
from sqlalchemy import exists

from user import session
from user.models import UserGeneralInfo, User, CountryCodeLookup

from django.shortcuts import render
from user.models import UserGeneralInfo,User,CountryCodeLookup
from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from user.schemas import UserGeneralInfoSchema,UserSchema,CountrCodeLookupSchema




class CountryCodeLookupsViewSet (viewsets.ViewSet):


    def list(self,request,format=None):

        countries = session.query(CountryCodeLookup).all()
        countries_schema = CountrCodeLookupSchema(many=True)
        dump_data= countries_schema.dump(countries).data
        return Response(dump_data)




class UserViewSet(viewsets.ModelViewSet):


     def list(self, request, format=None):

         users = session.query(User).all()
         user_schema=UserSchema(many=True)
         return Response(user_schema.dump(users).data)


     def get_object(self,pk):
         try:

             user=session.query(User).filter_by(id=pk)
             return user
         except User.DoesNotExist:
             raise Http404

     def retrieve(self, request, pk,format=None):
         user=self.get_object(pk)
         user_schema=UserSchema(many=True)
         return Response(user_schema.dump(user).data)


     def create(self, request, format=None):

         content = request.data

         user = User(first_name = content.get("first_name"), surname = content.get("surname"), email= content.get("email"), date_of_birth = content.get("date_of_birth"), phone = content.get("phone"),country_code_lookup_id=content.get("country_code_lookup"), gender = content.get("gender"), password = content.get("password") )

         session.add(user)
         session.commit()
         if session.query(exists().where(User.id == user.id)).scalar():
           user_schema=UserSchema()
           return Response(user_schema.dump(user).data, status=status.HTTP_201_CREATED)


     def update(self, request, pk, format=None):


          content = request.data
          user =session.query(User).filter_by(id=pk).first()

          if content.get("first_name") != None:
              user.first_name = content.get("first_name")

          if content.get("surname") != None:
              user.surname = content.get("surname")

          if content.get("email") != None:
              user.email = content.get("email")
          if content.get("date_of_birth") != None:
              user.date_of_birth = content.get("date_of_birth")
          if content.get("phone") != None:
              user.phone = content.get("phone")
          if content.get("country_code_lookup") != None:
              user.country_code_lookup = session.query(CountryCodeLookup).filter_by(id=content.get("country_code_lookup"))
          if content.get("gender") != None:
              user.gender = content.get("gender")
          if content.get("password") != None:
              user.password = content.get("password")

          session.commit()
          return Response(status=status.HTTP_200_OK)


     def destroy(self, request, pk,format=None):

         user=self.get_object(pk)
         user.delete()
         session.commit()
         return Response(status=status.HTTP_204_NO_CONTENT)

class UserGeneralInfoViewSet(viewsets.ModelViewSet):


         def list(self, request, user_pk):

              general_info=session.query(UserGeneralInfo).filter_by(user_id=user_pk)
              general_info_schema=UserGeneralInfoSchema(many=True)
              return Response(general_info_schema.dump(general_info).data)

         def retrieve(self, request, pk, user_pk):

              general_info=session.query(UserGeneralInfo).filter_by(id=pk,user_id=user_pk)
              general_info_schema = UserGeneralInfoSchema(many=True)
              return Response(general_info_schema.dump(general_info).data)

         def update(self, request, pk, user_pk, format=None):


              user_info = session.query(UserGeneralInfo).filter_by(id=pk,user_id=user_pk).first()
              content = request.data

              if content.get("user") != None:
                  user_info.user = session.query(User).filter_by(id=content.get("user"))

              if content.get("hight") != None:
                  user_info.hight = content.get("hight")

              if content.get("weight") != None:
                  user_info.weight = content.get("weight")
              if content.get("marital_status") != None:
                  user_info.marital_status = content.get("marital_status")
              if content.get("registered_treatment") != None:
                  user_info.registered_treatment = content.get("registered_treatment")

              session.commit()
              return Response(status=status.HTTP_200_OK)




















