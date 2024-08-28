
import yaml
import jsonschema

# Compared to JSON, YAML is easier to author.
# Validation is applied to data structures, not to serialisations.

def get_schema(path: str = "schema.yaml") -> dict: # {{{
    '''Return the schema which must sit alongside this file.
    '''
    with open(path) as fd:
        return yaml.safe_load(fd)
# }}} def get_schema

def get_data(path: str) -> dict: # {{{
    '''Return data from a JSON object.
    '''
    with open(path) as fd:
        return yaml.safe_load(fd)
# }}} def get_data

if __name__ == "__main__":
    schema = get_schema()
    print(schema)
    dataA = get_data("testcases/valid/1.yaml")
    print(dataA)
    jsonschema.validate(instance=dataA, schema=schema)
