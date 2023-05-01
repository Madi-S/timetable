from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

import enums

'''
One user -> many notes
User gets his/her timetable by user_id
'''


class User(models.Model):
    id = fields.IntField(pk=True)

    notes: fields.ReverseRelation['Note']

    def __str__(self):
        return f'<UserDB object: id={self.id}>'


class Note(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    created_at = fields.DatetimeField(auto_now_add=True)
    color = fields.CharEnumField(enums.Color, max_length=100)
    description = fields.TextField(max_length=1000)
    # TODO: define method to be parsed later
    datetime = fields.CharField(max_length=100)

    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        'models.User', related_name='notes', to_field='id'
    )

    def __str__(self):
        return f'<NoteDB object: id={self.id} title={self.title} user_id={self.user.id}>'
