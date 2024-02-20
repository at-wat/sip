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

        try:
            return extendable.extension_data[self.name]
        except KeyError:
            pass

        if factory is None:
            return None

        extension_data = factory()
        extendable.extension_data[self.name] = extension_data

        return extension_data

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

    def parse_argument_annotations(self, extendable, annotations):
        """ Parse any argument annotations.  Any annotations dealt with should
        be removed from the dict.
        """

        pass

    def parse_class_annotations(self, extendable, annotations):
        """ Parse any class annotations.  Any annotations dealt with should be
        removed from the dict.
        """

        pass

    def parse_ctor_annotations(self, extendable, annotations):
        """ Parse any ctor annotations.  Any annotations dealt with should be
        removed from the dict.
        """

        pass

    def parse_dtor_annotations(self, extendable, annotations):
        """ Parse any dtor annotations.  Any annotations dealt with should be
        removed from the dict.
        """

        pass

    def parse_enum_annotations(self, extendable, annotations):
        """ Parse any enum annotations.  Any annotations dealt with should be
        removed from the dict.
        """

        pass

    def parse_enum_member_annotations(self, extendable, annotations):
        """ Parse any enum_member annotations.  Any annotations dealt with
        should be removed from the dict.
        """

        pass

    def parse_function_annotations(self, extendable, annotations):
        """ Parse any function annotations.  Any annotations dealt with should
        be removed from the dict.
        """

        pass

    def parse_mapped_type_annotations(self, extendable, annotations):
        """ Parse any mapped type annotations.  Any annotations dealt with
        should be removed from the dict.
        """

        pass

    def parse_namespace_annotations(self, extendable, annotations):
        """ Parse any namespace annotations.  Any annotations dealt with should
        be removed from the dict.
        """

        pass

    def parse_typedef_annotations(self, extendable, annotations):
        """ Parse any typedef annotations.  Any annotations dealt with should
        be removed from the dict.
        """

        pass

    def parse_union_annotations(self, extendable, annotations):
        """ Parse any union annotations.  Any annotations dealt with should be
        removed from the dict.
        """

        pass

    def parse_variable_annotations(self, extendable, annotations):
        """ Parse any variable annotations.  Any annotations dealt with should
        be removed from the dict.
        """

        pass
