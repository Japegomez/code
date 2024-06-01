import uuid
from marshmallow_jsonapi import Schema, fields


class SessionSchema(Schema):
    id = fields.UUID(required=True, default=lambda: str(uuid.uuid4()))
    assigned_time = fields.Integer()
    user = fields.Relationship(
        type_="user",
        schema="UserSchema",
    )

    class Meta:
        type_ = "session"

class UserSchema(Schema):
    id = fields.UUID(required=True, default=lambda: str(uuid.uuid4()))
    name = fields.Str()
    isActive = fields.Boolean()

    class Meta:
        type_ = "user"


class MeasurementSchema(Schema):
    id = fields.UUID(required=True, default=lambda: str(uuid.uuid4()))
    current = fields.List(fields.Float(), required=True)
    voltage = fields.List(fields.Float(), required=True)

    class Meta:
        type_ = 'measurements'

class ImageSchema(Schema):
    id = fields.UUID(required=True, default=lambda: str(uuid.uuid4()))
    image = fields.Str(required=True)

    class Meta:
        type_ = 'image'