import xmlschema

schema = xmlschema.XMLSchema('XMLSchema.xsd')


try:
    schema.validate('testXML.xml')
        print('The XML file is valid according to the schema.')
except xmlschema.exceptions.XMLSchemaValidationError:
        print('The XML file is not valid according to the schema.')