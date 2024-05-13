from marshmallow_jsonapi import Schema, fields


class SessionSchema(Schema):
    id = fields.Str(dump_only=True)
    assigned_time = fields.Integer()
    user = fields.Relationship(
        type_="user",
        schema="UserSchema",
    )

    class Meta:
        type_ = "session"

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str()
    isActive = fields.Boolean()

    class Meta:
        type_ = "user"
