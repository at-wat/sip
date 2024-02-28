# SPDX-License-Identifier: BSD-2-Clause

# Copyright (c) 2024 Phil Thompson <phil@riverbankcomputing.com>


from .outputs.formatters import (fmt_argument_as_cpp_type, fmt_docstring,
        fmt_docstring_of_overload)
from .parser import (InvalidAnnotation, validate_boolean, validate_integer,
        validate_string_list, validate_string)
from .specification import DocstringSignature


class BuildSystemExtension:
    """ The base class for a build system extension. """

    def __init__(self, name, bindings, spec):
        """ Initialise the extension. """

        self.name = name
        self.bindings = bindings

        self._spec = spec

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

    @staticmethod
    def parse_boolean_annotation(name, raw_value, location):
        """ Parse and return the valid value of a boolean annotation. """

        pm, p, symbol = location

        try:
            value = validate_boolean(pm, p, symbol, name, raw_value)
        except InvalidAnnotation as e:
            pm.parser_error(p, symbol, str(e))
            value = e.use

        return value

    @staticmethod
    def parse_integer_annotation(name, raw_value, location):
        """ Parse and return the valid value of an integer annotation. """

        pm, p, symbol = location

        try:
            value = validate_integer(pm, p, symbol, name, raw_value,
                    optional=False)
        except InvalidAnnotation as e:
            pm.parser_error(p, symbol, str(e))
            value = e.use

        return value

    @staticmethod
    def parse_string_annotation(name, raw_value, location):
        """ Parse and return the valid value of a string annotation. """

        pm, p, symbol = location

        try:
            value = validate_string(pm, p, symbol, name, raw_value)
        except InvalidAnnotation as e:
            pm.parser_error(p, symbol, str(e))
            value = e.use

        return value

    @staticmethod
    def parse_string_list_annotation(name, raw_value, location):
        """ Parse and return the valid value of a string list annotation. """

        pm, p, symbol = location

        try:
            value = validate_string_list(pm, p, symbol, name, raw_value)
        except InvalidAnnotation as e:
            pm.parser_error(p, symbol, str(e))
            value = e.use

        return value

    @staticmethod
    def parsing_error(error_message, location):
        """ Register a parsing error at a particular location. """

        pm, p, symbol = location

        pm.parser_error(p, symbol, error_message)

    def query_argument_cpp_decl(self, argument, scope, strip=0):
        """ Returns the C++ declaration of an argument within a specific scope.
        If the name of the argument type contains scopes then 'strip' specifies
        the number of leading scopes to be removed.  If it is -1 then only the
        leading global scope is removed.
        """

        return fmt_argument_as_cpp_type(self._spec, argument,
                scope=scope.iface_file, strip=strip)

    @staticmethod
    def query_argument_is_optional(argument):
        """ Returns True if the argument is optional. """

        return argument.default_value is not None

    def query_function_default_docstring(self, function):
        """ Return the function's default (ie. automatically generated)
        docstring.
        """

        return fmt_docstring_of_overload(self._spec, function)

    @staticmethod
    def query_function_default_docstring_is_appended(self):
        """ Returns True the function's default (ie. automatically generated)
        docstring should be appended.
        """

        return function.docstring.signature is DocstringSignature.APPENDED

    @staticmethod
    def query_function_default_docstring_is_prepended():
        """ Returns True the function's default (ie. automatically generated)
        docstring should be prepended.
        """

        return function.docstring.signature is DocstringSignature.PREPENDED

    @staticmethod
    def query_function_docstring(function):
        """ Return the function's docstring or None if it doesn't have one. """

        return None if function.docstring is None else fmt_docstring(function.docstring)

    @staticmethod
    def query_class_cpp_name(klass):
        """ Return the fully qualified C++ name of a class. """

        return klass.iface_file.fq_cpp_name.as_cpp

    @staticmethod
    def query_class_function_group_pymethoddef_reference(klass, group_nr):
        """ Return a reference to a PyMethod structure that handles a group of
        overloaded class functions.
        """

        return f'&methods_{klass.iface_file.fq_cpp_name.as_word}[{group_nr}]'

    @staticmethod
    def query_class_function_groups(klass):
        """ Return a sequence of the class's function groups.  A function group
        is a sequence of overloaded functions with the same C++ name.
        """

        groups = {}

        for overload in klass.overloads:
            overload_list = groups.setdefault(overload.common.py_name.name, [])
            overload_list.append(overload)

        # The order is important as the index can be used to reference a
        # particular group.
        return [groups[m.py_name.name] for m in klass.members]

    @staticmethod
    def query_class_is_subclass(klass, module_name, class_name):
        """ Return True if a class with the given name is the same as, or is a
        subclass of the class.
        """

        for klass in klass.mro:
            if klass.iface_file.module.fq_py_name.name == module_name and klass.py_name.name == class_name:
                return True

        return False

    @staticmethod
    def query_function_cpp_arguments(function):
        """ Return a sequence of the C++ arguments of a function. """

        return function.cpp_signature.args

    @staticmethod
    def query_function_cpp_name(function):
        """ Return the C++ name of a function. """

        return function.cpp_name

    # The rest of the class are the stubs to be re-implemented by sub-classes.

    def append_class_extension_code(self, klass, name, code):
        """ Append code fragments that implements a class extension data
        structure.
        """

        pass

    def append_mapped_type_extension_code(self, mapped_type, name, code):
        """ Append code fragments that implements a mapped type extension data
        structure.
        """

        pass

    def append_sip_api_h_code(self, code):
        """ Append code fragments to be included in all generated sipAPI*.h
        files.
        """

        pass

    def complete_class_definition(self, klass):
        """ Complete the definition of a class. """

        pass

    def complete_function_parse(self, function, scope):
        """ Complete the parsing of a (possibly scoped) function. """

        pass

    def get_class_access_specifier_keywords(self):
        """ Return a sequence of class action specifier keywords to be
        recognised by the parser.
        """

        return ()

    def get_function_keywords(self):
        """ Return a sequence of function keywords to be recognised by the
        parser.
        """

        return ()

    def parse_argument_annotation(self, argument, name, raw_value, location):
        """ Parse an argument annotation.  Return True if it was parsed. """

        return False

    def parse_class_access_specifier(self, klass, primary, secondary):
        """ Parse a primary and optional secondary class access specifier.  If
        it was parsed return the C++ standard access specifier (ie. 'public',
        'protected' or 'private') to use, otherwise return None.
        """

        return None

    def parse_class_annotation(self, klass, name, raw_value, location):
        """ Parse a class annotation.  Return True if it was parsed. """

        return False

    def parse_ctor_annotation(self, ctor, name, raw_value, location):
        """ Parse a ctor annotation.  Return True if it was parsed. """

        return False

    def parse_dtor_annotation(self, dtor, name, raw_value, location):
        """ Parse a dtor annotation.  Return True if it was parsed. """

        return False

    def parse_enum_annotation(self, enum, name, raw_value, location):
        """ Parse an enum annotation.  Return True if it was parsed. """

        return False

    def parse_enum_member_annotation(self, enum_member, name, raw_value,
            location):
        """ Parse an enum member annotation.  Return True if it was parsed. """

        return False

    def parse_function_annotation(self, function, name, raw_value, location):
        """ Parse a function annotation.  Return True if it was parsed. """

        return False

    def parse_function_keyword(self, function, keyword):
        """ Parse a function keyword.  Return True if it was parsed. """

        return False

    def parse_mapped_type_annotation(self, mapped_type, name, raw_value,
            location):
        """ Parse a mapped type annotation.  Return True if it was parsed. """

        return False

    def parse_namespace_annotation(self, namespace, name, raw_value,
            location):
        """ Parse a namespace annotation.  Return True if it was parsed. """

        return False

    def parse_typedef_annotation(self, typedef, name, raw_value, location):
        """ Parse a typedef annotation.  Return True if it was parsed. """

        return False

    def parse_union_annotation(self, union, name, raw_value, location):
        """ Parse a union annotation.  Return True if it was parsed. """

        return False

    def parse_variable_annotation(self, variable, name, raw_value, location):
        """ Parse a variable annotation.  Return True if it was parsed. """

        return False
