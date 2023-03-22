from lxml import etree

xml_file = 'testXML.xml'
xsd_file = 'XMLSchema.xsd'


def validate_xml(xml_file, xsd_file):
    with open(xsd_file, 'r') as f:
        xsd = etree.parse(f)

    with open(xml_file, 'r') as f:
        xml = etree.parse(f)

    schema = etree.XMLSchema(xsd)

    is_valid = schema.validate(xml)

    return is_valid


is_valid = validate_xml(xml_file, xsd_file)

if is_valid:
    print('The file is valid.')
else:
    print('The file is not valid.')
