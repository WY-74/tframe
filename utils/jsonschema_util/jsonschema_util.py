import json
from genson import SchemaBuilder
from jsonschema.validators import validate
from conftest import LOGGER


class JsonSchemaUtil:
    @classmethod
    def generate_jsonschema(cls, obj, by_file: str | None = None):
        builder = SchemaBuilder()
        builder.add_object(obj)
        schema = builder.to_schema()
        LOGGER.info(f"Json Schema: {schema}")
        if by_file:
            LOGGER.info("Generate json schema with file")
            with open(by_file, "w") as f:
                json.dump(schema, f)
            return
        return schema

    @classmethod
    def validate_jsonschema(cls, obj, schema: str | None = None, by_file: str | None = None):
        if not schema and not by_file:
            LOGGER.warning("No Json Schema is generated and no file is passed in")

        if by_file:
            LOGGER.info("Validate json schema with file")
            with open(by_file) as f:
                schema = json.load(f)
        try:
            validate(instance=obj, schema=schema)
            return True
        except Exception:
            return False
