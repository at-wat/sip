# SPDX-License-Identifier: BSD-2-Clause

# Copyright (c) 2024 Phil Thompson <phil@riverbankcomputing.com>


from enum import auto, Enum


class EventType(Enum):
    """ The event types. """

    # Parse argument annotations.  The extendable specification object is an
    # argument.  The handler argument is a dict of annotations.  Any
    # annotations dealt with by the handler should be removed from the dict.
    PARSE_ARGUMENT_ANNOTATIONS = auto()

    # Parse class annotations.  The extendable specification object is a
    # class.  The handler argument is a dict of annotations.  Any annotations
    # dealt with by the handler should be removed from the dict.
    PARSE_CLASS_ANNOTATIONS = auto()

    # Parse ctor annotations.  The extendable specification object is a ctor.
    # The handler argument is a dict of annotations.  Any annotations dealt
    # with by the handler should be removed from the dict.
    PARSE_CTOR_ANNOTATIONS = auto()

    # Parse dtor annotations.  The extendable specification object is a dtor.
    # The handler argument is a dict of annotations.  Any annotations dealt
    # with by the handler should be removed from the dict.
    PARSE_DTOR_ANNOTATIONS = auto()

    # Parse enum annotations.  The extendable specification object is an enum.
    # The handler argument is a dict of annotations.  Any annotations dealt
    # with by the handler should be removed from the dict.
    PARSE_ENUM_ANNOTATIONS = auto()

    # Parse enum member annotations.  The extendable specification object is an
    # enum member.  The handler argument is a dict of annotations.  Any
    # annotations dealt with by the handler should be removed from the dict.
    PARSE_ENUM_MEMBER_ANNOTATIONS = auto()

    # Parse exception annotations.  The extendable specification object is an
    # exception.  The handler argument is a dict of annotations.  Any
    # annotations dealt with by the handler should be removed from the dict.
    PARSE_EXCEPTION_ANNOTATIONS = auto()

    # Parse function annotations.  The extendable specification object is a
    # function.  The handler argument is a dict of annotations.  Any
    # annotations dealt with by the handler should be removed from the dict.
    PARSE_FUNCTION_ANNOTATIONS = auto()

    # Parse mapped type annotations.  The extendable specification object is a
    # mapped type.  The handler argument is a dict of annotations.  Any
    # annotations dealt with by the handler should be removed from the dict.
    PARSE_MAPPED_TYPE_ANNOTATIONS = auto()

    # Parse namespace annotations.  The extendable specification object is a
    # class.  The handler argument is a dict of annotations.  Any annotations
    # dealt with by the handler should be removed from the dict.
    PARSE_NAMESPACE_ANNOTATIONS = auto()

    # Parse typedef annotations.  The extendable specification object is a
    # typedef.  The handler argument is a dict of annotations.  Any annotations
    # dealt with by the handler should be removed from the dict.
    PARSE_TYPEDEF_ANNOTATIONS = auto()

    # Parse union annotations.  The extendable specification object is a
    # class.  The handler argument is a dict of annotations.  Any annotations
    # dealt with by the handler should be removed from the dict.
    PARSE_UNION_ANNOTATIONS = auto()

    # Parse variable annotations.  The extendable specification object is a
    # variable.  The handler argument is a dict of annotations.  Any
    # annotations dealt with by the handler should be removed from the dict.
    PARSE_VARIABLE_ANNOTATIONS = auto()
