from storage_format_class import Defualt_formating
"""
    artificially introduced false data into a piece of software (Mock File Example).
"""


class XmlDataClass(Defualt_formating):
    def dump(self, dict_data: dict):
        # python dictionary object
        '''
            {
                key: value
            }

             → Converting it to XML File → <key> value </key>
        '''

        # Return XML
        raise NotImplementedError("Mock")

    def load(self, serialized_data):
        # Input → XML format.
        '''
        Loading data
       '''
        raise NotImplementedError("MOCK")

    def data_format_type(self):
        return "XML Format"
