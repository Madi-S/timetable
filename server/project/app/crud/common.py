# TODO: create common base crud operations


async def post(class_model, payload):
    obj = class_model(**payload)
    await obj.save()
    return obj.id
