from jsonschema import Draft7Validator
from json import load
from test_functions.test_data_json.contact_records import contacts

if __name__ == '__main__':

    # with open ('../schemas/definitions/contact') as f:
    #     schema = load(f)

    with open ('../schemas/virtual/contact-extended') as f:
        schema = load(f)

    validator = Draft7Validator(schema)

    with open('./test_data_json/contact_records') as p:
        payload = load(p)

    errors = validator.iter_errors(payload)
    print(list(errors))

