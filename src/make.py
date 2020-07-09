import json_schema_for_humans.generate as mdjs 
import inspect
inspect.signature(mdjs.generate_from_filename)


mdjs.generate_from_filename('../../FedeasAPI/schemas/post.schema.json',
    '../docs/sch/index.md',
    minify=True,
    expand_buttons=True)


