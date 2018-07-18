from marshmallow_sqlalchemy import ModelSchema


from .models import User,UserGeneralInfo,CountryCodeLookup

class UserSchema(ModelSchema):
    class Meta:
        model = User



class UserGeneralInfoSchema(ModelSchema):
    class Meta:
        model = UserGeneralInfo


class CountrCodeLookupSchema(ModelSchema):
    class Meta:
        model = CountryCodeLookup