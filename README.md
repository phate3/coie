# COie 
## A national information exchange model for geospatial assets

> geospatial: of or relating to the relative position of things on the earth's surface


Definitions for the contractual construction / built environment 
information exchanges relating to physical real world assets.

(This schema has been developed with respect to BS1192:4, ISO 19650 and any UK annexes)


## Features
- Describe your existing data format(s).
- Provides clear human- and machine- readable documentation.
- Validates data which is useful for:
    - Automated testing.
    - Ensuring quality of client submitted data.
    - ✨Magic ✨


### Why use COie with JSON?: 
> ###  COie is primarily about data understanding and interoperability. 

These things become difficult when there are many data resources, constructed and used by many developers or data analysts. COie can help when those problems emerge, by providing:

> - Meaningful data names and machine-readable documentation
> - Global identifiers for data components
> - Self-describing data
> - Reuse of community-agreed data definitions



##### COie-CORE

The primary definitions will be defined using Json, Json-LD and Jsonschema


Example workbook schema: https://www.coie.uk/schema/workbook-schema

`json-schema does not fully support unique item properties check. AJV has an implementation of uniqueItemProperties.`

```
- workbook-schema
    [Validation] All named data sets (sheets) are required (even if empty)
    - Instruction
        -   [TBC]
    - Contact 
        - [Validation] Primary keys in array must be unique
        - [Validation] Each item conforms to contact schema
    - Extent 
        - [Validation] Can only be 1 item in length
    - Region 
        - [Validation] Primary keys in array must be unique
        - [Validation] Each item conforms to region schema
    - Feature 
        - [Validation] Primary keys in array must be unique
        - [Validation] Each item conforms to feature schema
    - Zone
        - [Validation] Primary keys in array must be unique
        - [Validation] Each item conforms to zone schema
    - Type
        - [Validation] Primary keys in array must be unique
        - [Validation] Each item conforms to type schema
    - Component
        - [Validation] Primary keys in array must be unique
        - [Validation] Each item conforms to component schema

```

Provides the base schema that forms the minimum technical requirement for an information exchange between two contracted parties (in the built environment, where the contract topic is about physical built assets)

Using jsonschema as a base we set out the object that form the exchange model described by BS1192:4.

Then including "title" tags and following we can generate a form:

https://jsonform.github.io/jsonform/playground/

`paste the code from above into the form website, you will now have generated a "COie Contact record"`


#### COie-definitions:

Provide the ability to specify, procure, deliver and assure data in a single unambiguous, open format and interoperable language.

The sample below is a machine readible (and fairly human readable) schema which enables the communication of the "shape" the data payload must adhere to. 

* You can see it includes a set of properties (you might know these as excel "headings")
* You can see that each property has a description, an example value and 
* where possible validation rules for further "pattern" control 
    * `"pattern": "^\\S+@\\S+$"` enables both front-end and back-end to check that the value provided is in basic email format (not to RFC)
    
Here is the General Email Regex (RFC 5322 Official Standard)
 
```(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])```

Example COie contact schema definition, with a single file you can state the shape of the object and implement basic validation (non semantic analysis):


```
{
  "schema": {
    "$id": "https://www.COie.uk/schema/contact.json",
    "title": "Contact",
    "description": "A contact in the information exchange",
    "type": "object",
    "properties": {
      "email": {
        "title": "Email",
        "description": "The unique email for a contact on a contract / project",
        "type": "string",
        "example": "email@home.com",
        "pattern": "^\\S+@\\S+$"
      },
      "category": {
        "title": "Category",
        "description": "https://www.thenbs.com/-/media/uk/files/xls/uniclass/2021-04/uniclass2015_ro_v1_5.xlsx code best describing contact",
        "type": "string",
        "enum": ["Ro_1", "Ro_2", "Ro_3"],
        "example": "Ro_10:Management roles"
      },
      "company": {
        "title": "Company",
        "description": "Organisation that the contact record represents",
        "type": "string",
        "example": "acme ltd"
      },
      "phone": {
        "title": "Phone",
        "description": "Organisation that the contact record represents",
        "type": "string",
        "example": "+44 (0) 1234 222 333"
      }
    },
    "required": [ "email" , "category", "company", "phone"]
  }
  }
```   



# ALL WORK IN PROGRESS

[possible use cases]
* https://better.engineering/jsonschema2db/
* https://jsonforms.io/
* 

##### COie-Exchange Requirements 
Provides extensiblity required to extend COie-CORE to suit a specific purpose. 


Areas of Interest / Context:

* Automating contracts for construction - NEC/JCT
    * Specification of requirements
    * Procurement of requirements
    * Delivery of data (supporting information exchange)
    * Assurance of data (supporting information exchange)   
    
* Automating project information management - (RIBA/BSRIA/?)
    * information exchange and control points
    * Data delivery assurance and validation

ORGANISED BY:
* DEFINITIONS
* EXCHANGE MODEL
* EXCHANGE MODEL REQUIREMENTS

```
Deliverable schema:

- unique ID is by name. 
    - 19650 regex pattern can be worked out for minimum validation
    - complex validation possible but might need a parsed name into segments for comparison to lists. 
 

```
