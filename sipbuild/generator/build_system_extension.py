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

    def parse_boolean_annotation(self, name, annotations, location):
        """ Parse and return the value of a boolean annotation or False if it
        wasn't specified.
        """

        from .parser import InvalidAnnotation, validate_boolean

        try:
            value = annotations.pop(name)
        except KeyError:
            return False

        pm, p, symbol = location

        try:
            value = validate_boolean(pm, p, symbol, name, value)
        except InvalidAnnotation as e:
            pm.parser_error(p, symbol, str(e))
            value = False

        return value

    def parse_integer_annotation(self, name, annotations, location):
        """ Parse and return the value of an integer annotation or 0 if it
        wasn't specified.
        """

        from .parser import InvalidAnnotation, validate_integer

        try:
            value = annotations.pop(name)
        except KeyError:
            return 0

        pm, p, symbol = location

        try:
            value = validate_integer(pm, p, symbol, name, value)
        except InvalidAnnotation as e:
            pm.parser_error(p, symbol, str(e))
            value = 0

        return value

    def parse_string_annotation(self, name, annotations, location):
        """ Parse and return the value of a string annotation or None if it
        wasn't specified.
        """

        from .parser import InvalidAnnotation, validate_string

        try:
            value = annotations.pop(name)
        except KeyError:
            return None

        pm, p, symbol = location

        try:
            value = validate_string(pm, p, symbol, name, value)
        except InvalidAnnotation as e:
            pm.parser_error(p, symbol, str(e))
            value = None

        return value

    def parse_string_list_annotation(self, name, annotations, location):
        """ Parse and return the value of a string list annotation or None if
        it wasn't specified.
        """

        from .parser import InvalidAnnotation, validate_string_list

        try:
            value = annotations.pop(name)
        except KeyError:
            return None

        pm, p, symbol = location

        try:
            value = validate_string_list(pm, p, symbol, name, value)
        except InvalidAnnotation as e:
            pm.parser_error(p, symbol, str(e))
            value = None

        return value

    # The rest of the class are the stubs to be re-implemented by sub-classes.

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

    def parse_argument_annotations(self, extendable, annotations, location):
        """ Parse any argument annotations.  Any annotations dealt with should
        be removed from the dict.
        """

        pass

    def parse_class_annotations(self, extendable, annotations, location):
        """ Parse any class annotations.  Any annotations dealt with should be
        removed from the dict.
        """

        pass

    def parse_ctor_annotations(self, extendable, annotations, location):
        """ Parse any ctor annotations.  Any annotations dealt with should be
        removed from the dict.
        """

        pass

    def parse_dtor_annotations(self, extendable, annotations, location):
        """ Parse any dtor annotations.  Any annotations dealt with should be
        removed from the dict.
        """

        pass

    def parse_enum_annotations(self, extendable, annotations, location):
        """ Parse any enum annotations.  Any annotations dealt with should be
        removed from the dict.
        """

        pass

    def parse_enum_member_annotations(self, extendable, annotations, location):
        """ Parse any enum_member annotations.  Any annotations dealt with
        should be removed from the dict.
        """

        pass

    def parse_function_annotations(self, extendable, annotations, location):
        """ Parse any function annotations.  Any annotations dealt with should
        be removed from the dict.
        """

        pass

    def parse_mapped_type_annotations(self, extendable, annotations, location):
        """ Parse any mapped type annotations.  Any annotations dealt with
        should be removed from the dict.
        """

        pass

    def parse_namespace_annotations(self, extendable, annotations, location):
        """ Parse any namespace annotations.  Any annotations dealt with should
        be removed from the dict.
        """

        pass

    def parse_typedef_annotations(self, extendable, annotations, location):
        """ Parse any typedef annotations.  Any annotations dealt with should
        be removed from the dict.
        """

        pass

    def parse_union_annotations(self, extendable, annotations, location):
        """ Parse any union annotations.  Any annotations dealt with should be
        removed from the dict.
        """

        pass

    def parse_variable_annotations(self, extendable, annotations, location):
        """ Parse any variable annotations.  Any annotations dealt with should
        be removed from the dict.
        """

        pass
