from marshmallow import Schema, fields

## Model Without Relationships

class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

## Model Relationships

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

class TagSchema(PlainTagSchema):
    # NOTE: ERROR IN TUTORIAL SINCE POST ROUTE INCLUDES STORE_ID
    # store_id = fields.Int(required=True, load_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)
    
