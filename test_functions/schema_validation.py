from jsonschema import Draft7Validator
from json import load
from test_functions.test_data_json.contact_records import contacts

if __name__ == '__main__':

    with open ('../schemas/virtual/contact.json') as f:
        schema = load(f)

    validator = Draft7Validator(schema)

    for ob in contacts:
        errors = validator.iter_errors(ob)
        print(list(errors))

