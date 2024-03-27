# SPDX-License-Identifier: BSD-2-Clause

# Copyright (c) 2024 Phil Thompson <phil@riverbankcomputing.com>


from ...specification import DocstringSignature
from ...utils import get_py_struct_name

from ..formatters import fmt_docstring, fmt_docstring_of_overload


def has_member_docstring(bindings, overloads):
    """ Return True if a function/method has a docstring. """

    if not overloads:
        return False

    auto_docstring = False

    # Check for any explicit docstrings and remember if there were any that
    # could be automatically generated.
    for overload in overloads:
        if overload.docstring is not None:
            return True

        if bindings.docstrings:
            auto_docstring = True

    if overloads[0].common.no_arg_parser:
        return False

    return auto_docstring


def member_docstring(sf, spec, bindings, scope, overloads, is_method=False,
        prefix=''):
    """ Generate the docstring for all overloads of a function/method.  Return
    a 2-tuple of the reference to the generated Python struct and True if the
    docstring was entirely automatically generated.
    """

    NEWLINE = '\\n"\n"'

    docstring_ref = get_py_struct_name('doc', scope,
            overloads[0].common.py_name.name, prefix=prefix);
    auto_docstring = True

    # See if all the docstrings are automatically generated.
    all_auto = True
    any_implied = False

    for overload in overloads:
        if overload.docstring is not None:
            all_auto = False

            if overload.docstring.signature is not DocstringSignature.DISCARDED:
                any_implied = True

    # Generate the docstring.
    sf.write(f'PyDoc_STRVAR({docstring_ref}, "')

    is_first = True

    for overload in overloads:
        if not is_first:
            sf.write(NEWLINE)

            # Insert a blank line if any explicit docstring wants to include a
            # signature.  This maintains compatibility with previous versions.
            if any_implied:
                sf.write(NEWLINE)

        if overload.docstring is not None:
            if overload.docstring.signature is DocstringSignature.PREPENDED:
                _member_auto_docstring(sf, spec, bindings, overload, is_method)
                sf.write(NEWLINE)

            sf.write(fmt_docstring(overload.docstring))

            if overload.docstring.signature is DocstringSignature.APPENDED:
                sf.write(NEWLINE)
                _member_auto_docstring(sf, spec, bindings, overload, is_method)

            auto_docstring = False
        elif all_auto or any_implied:
            _member_auto_docstring(sf, spec, bindings, overload, is_method)

        is_first = False

    sf.write('");\n')

    return docstring_ref, auto_docstring


def _member_auto_docstring(sf, spec, bindings, overload, is_method):
    """ Generate the automatic docstring for a function/method. """

    if bindings.docstrings:
        sf.write(
                fmt_docstring_of_overload(spec, overload, is_method=is_method))
