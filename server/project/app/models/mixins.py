from tortoise import models, fields


class TimestampMixin():
    modified_at = fields.DatetimeField(null=True, auto_now=True)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)


class AbstractBaseModel(models.Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True
