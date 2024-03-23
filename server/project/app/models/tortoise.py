from tortoise import fields

from app.models import enums
from app.models.mixins import AbstractBaseModel, TimestampMixin


class User(TimestampMixin, AbstractBaseModel):
    username = fields.CharField(max_length=255, unique=True)
    email = fields.CharField(max_length=255)
    password_hash = fields.CharField(max_length=255)
    token = fields.CharField(max_length=255, unique=True)
    is_active = fields.BooleanField(default=False)
    notes: fields.ReverseRelation['Note']

    def __str__(self):
        return f'<User #{self.id}: username - {self.username}, active - {self.active} email - {self.email}>'


class Note(TimestampMixin, AbstractBaseModel):
    title = fields.CharField(max_length=150)
    description = fields.TextField(null=True)
    datetime_from = fields.DatetimeField()
    datetime_to = fields.DatetimeField()
    color = fields.IntEnumField(
        enums.NoteColor,
        default=enums.NoteColor.RED
    )
    category = fields.CharEnumField(
        enums.NoteCategory,
        max_length=100,
        default=enums.NoteCategory.PHYSICAL
    )
    #  ForeignKeyField is a virtual field, meaning it has no direct DB backing. Instead it has a field (by default called FKNAME_id (that is, just an _id is appended) that is the actual DB-backing field.
    # It will just contain the Key value of the related table.
    # This is an important detail as it would allow one to assign/read the actual value directly, which could be considered an optimization if the entire foreign object isn’t needed.
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        'models.User',
        on_delete=fields.CASCADE,
        related_name='notes',
    )

    def __str__(self):
        return f'<Note #{self.id}: title: {self.title}, scheduler for {self.datetime_from} till {self.datetime_to}>'
