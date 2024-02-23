# SPDX-License-Identifier: BSD-2-Clause

# Copyright (c) 2024 Phil Thompson <phil@riverbankcomputing.com>


class BuildSystemExtension:
    """ The base class for a build system extension. """

    def __init__(self, name, project):
        """ Initialise the extension. """

        self.name = name
        self.project = project

    def get_extension_data(self, extendable, factory=None):
        """ Return the build system extension-specific extension data for an
        extendeable object, optionally creating it if necessary.
        """

        if extendable.extension_data is None:
            if factory is None:
                return None

            extendable.extension_data = {}
        else:
            try:
                return extendable.extension_data[self.name]
            except KeyError:
                pass

            if factory is None:
                return None

        extension_data = factory()
        extendable.extension_data[self.name] = extension_data

        return extension_data

    def parse_boolean_annotation(self, name, raw_value, location):
        """ Parse and return the valid value of a boolean annotation. """

        from .parser import InvalidAnnotation, validate_boolean

        pm, p, symbol = location

        try:
            value = validate_boolean(pm, p, symbol, name, raw_value)
        except InvalidAnnotation as e:
            pm.parser_error(p, symbol, str(e))
            value = e.use

        return value

    def parse_integer_annotation(self, name, raw_value, location):
        """ Parse and return the valid value of an integer annotation. """

        from .parser import InvalidAnnotation, validate_integer

        pm, p, symbol = location

        try:
            value = validate_integer(pm, p, symbol, name, raw_value)
        except InvalidAnnotation as e:
            pm.parser_error(p, symbol, str(e))
            value = e.use

        return value

    def parse_string_annotation(self, name, raw_value, location):
        """ Parse and return the valid value of a string annotation. """

        from .parser import InvalidAnnotation, validate_string

        pm, p, symbol = location

        try:
            value = validate_string(pm, p, symbol, name, raw_value)
        except InvalidAnnotation as e:
            pm.parser_error(p, symbol, str(e))
            value = e.use

        return value

    def parse_string_list_annotation(self, name, raw_value, location):
        """ Parse and return the valid value of a string list annotation. """

        from .parser import InvalidAnnotation, validate_string_list

        pm, p, symbol = location

        try:
            value = validate_string_list(pm, p, symbol, name, raw_value)
        except InvalidAnnotation as e:
            pm.parser_error(p, symbol, str(e))
            value = e.use

        return value

    # The rest of the class are the stubs to be re-implemented by sub-classes.

    def append_class_extension_code(self, extendable, name, code):
        """ Append code fragments that implements a class extension data
        structure.
        """

        pass

    def append_mapped_type_extension_code(self, extendable, name, code):
        """ Append code fragments that implements a mapped type extension data
        structure.
        """

        pass

    def append_sip_api_h_code(self, code):
        """ Append code fragments to be included in all generated sipAPI*.h
        files.
        """

        pass

    def parse_argument_annotation(self, extendable, name, raw_value, location):
        """ Parse an argument annotation.  Return True if it was parsed. """

        pass

    def parse_class_annotation(self, extendable, name, raw_value, location):
        """ Parse a class annotation.  Return True if it was parsed. """

        pass

    def parse_ctor_annotation(self, extendable, name, raw_value, location):
        """ Parse a ctor annotation.  Return True if it was parsed. """

        pass

    def parse_dtor_annotation(self, extendable, name, raw_value, location):
        """ Parse a dtor annotation.  Return True if it was parsed. """

        pass

    def parse_enum_annotation(self, extendable, name, raw_value, location):
        """ Parse an enum annotation.  Return True if it was parsed. """

        pass

    def parse_enum_member_annotation(self, extendable, name, raw_value,
            location):
        """ Parse an enum member annotation.  Return True if it was parsed. """

        pass

    def parse_function_annotation(self, extendable, name, raw_value, location):
        """ Parse a function annotation.  Return True if it was parsed. """

        pass

    def parse_mapped_type_annotation(self, extendable, name, raw_value,
            location):
        """ Parse a mapped type annotation.  Return True if it was parsed. """

        pass

    def parse_namespace_annotation(self, extendable, name, raw_value,
            location):
        """ Parse a namespace annotation.  Return True if it was parsed. """

        pass

    def parse_typedef_annotation(self, extendable, name, raw_value, location):
        """ Parse a typedef annotation.  Return True if it was parsed. """

        pass

    def parse_union_annotation(self, extendable, name, raw_value, location):
        """ Parse a union annotation.  Return True if it was parsed. """

        pass

    def parse_variable_annotation(self, extendable, name, raw_value, location):
        """ Parse a variable annotation.  Return True if it was parsed. """

        pass
