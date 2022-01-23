from jsonschema import Draft7Validator
from json import load

if __name__ == '__main__':

    # with open ('../schemas/definitions/contact') as f:
    #     schema = load(f)

    with open('../schemas/workbook-schema.json') as f:
        schema = load(f)

    validator = Draft7Validator(schema)

    with open('test_data_json/workbook-payload.json') as p:
        payload = load(p)

    errors = validator.iter_errors(payload)
    print(list(errors))

