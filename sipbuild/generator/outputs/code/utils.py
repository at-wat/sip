# SPDX-License-Identifier: BSD-2-Clause

# Copyright (c) 2024 Phil Thompson <phil@riverbankcomputing.com>


from ...specification import ArgumentType, CodeBlock, WrappedEnum

from ..formatters import fmt_class_as_scoped_name


def abi_supports_array(spec):
    """ Return True if the ABI supports sip.array. """

    return spec.abi_version >= (13, 4) or (spec.abi_version >= (12, 11) and spec.abi_version < (13, 0))


def cached_name_ref(cached_name, as_nr=False):
    """ Return a reference to a cached name. """

    prefix = 'sipNameNr_' if as_nr else 'sipName_'

    return prefix + get_normalised_cached_name(cached_name)


def get_gto_name(wrapped_object):
    """ Return the name of the generated type object for a wrapped object. """

    fq_cpp_name = wrapped_object.fq_cpp_name if isinstance(wrapped_object, WrappedEnum) else wrapped_object.iface_file.fq_cpp_name

    return 'sipType_' + fq_cpp_name.as_word


def get_normalised_cached_name(cached_name):
    """ Return the normalised form of a cached name. """

    # If the name seems to be a template then just use the offset to ensure
    # that it is unique.
    if '<' in cached_name.name:
        return str(cached_name.offset)

    # Handle C++ and Python scopes.
    return cached_name.name.replace(':', '_').replace('.', '_')


def is_string(type):
    """ Check if a type is a string rather than a char type. """

    nr_derefs = len(type.derefs)

    if type.is_out and not type.is_reference:
        nr_derefs -= 1

    return nr_derefs > 0


def is_used_in_code(code, s):
    """ Return True if a string is used in code. """

    # The code may be a list of code blocks or an optional code block.
    if code is None:
        return False

    if isinstance(code, CodeBlock):
        code = [code]

    for cb in code:
        if s in cb.text:
            return True

    return False


def scoped_class_name(spec, klass):
    """ Return a scoped class name as a string.  Protected classes have to be
    explicitly scoped.
    """

    return fmt_class_as_scoped_name(spec, klass, scope=klass.iface_file)


def type_needs_user_state(type):
    """ Return True if a type needs user state to be provided. """

    return type.type is ArgumentType.MAPPED and type.definition.needs_user_state


def use_in_code(code, s, spec=None):
    """ Return the string to use depending on whether it is used in some code
    and optionally if the bindings are for C.
    """

    # Always use the string for C bindings.
    if spec is not None and spec.c_bindings:
        return s

    return s if is_used_in_code(code, s) else ''
