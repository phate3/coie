from jsonschema import Draft7Validator
from json import load

validate(data, schema)

if __name__ == '__main__':

    # with open ('../schemas/definitions/contact') as f:
    #     schema = load(f)

    with open('../schemas/workbook-schema') as f:
        schema = load(f)

    validator = Draft7Validator(schema)

    with open('test_data_json/workbook-payload.json') as p:
        payload = load(p)

    validation_errors = sorted(validator.iter_errors(payload), key=lambda e: e.path)

    errors = []

    for error in validation_errors:
        message = error.message
        if error.path:
            message = "[{}] {}".format(
                ".".join(str(x) for x in error.absolute_path), message
            )

        errors.append(message)
    print(errors)

