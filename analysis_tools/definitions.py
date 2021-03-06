#!/usr/bin/env python

# Copyright (c) 2016 GoSecure Inc.

OPCODES = {
    0 : "NOP",
    1 : "ADD",
    2 : "SUB",
    3 : "MUL",
    4 : "DIV",
    5 : "MOD",
    6 : "SL",
    7 : "SR",
    8 : "CONCAT",
    9 : "BW_OR",
    10 : "BW_AND",
    11 : "BW_XOR",
    12 : "BW_NOT",
    13 : "BOOL_NOT",
    14 : "BOOL_XOR",
    15 : "IS_IDENTICAL",
    16 : "IS_NOT_IDENTICAL",
    17 : "IS_EQUAL",
    18 : "IS_NOT_EQUAL",
    19 : "IS_SMALLER",
    20 : "IS_SMALLER_OR_EQUAL",
    21 : "CAST",
    22 : "QM_ASSIGN",
    23 : "ASSIGN_ADD",
    24 : "ASSIGN_SUB",
    25 : "ASSIGN_MUL",
    26 : "ASSIGN_DIV",
    27 : "ASSIGN_MOD",
    28 : "ASSIGN_SL",
    29 : "ASSIGN_SR",
    30 : "ASSIGN_CONCAT",
    31 : "ASSIGN_BW_OR",
    32 : "ASSIGN_BW_AND",
    33 : "ASSIGN_BW_XOR",
    34 : "PRE_INC",
    35 : "PRE_DEC",
    36 : "POST_INC",
    37 : "POST_DEC",
    38 : "ASSIGN",
    39 : "ASSIGN_REF",
    40 : "ECHO",
    41 : "PRINT",
    42 : "JMP",
    43 : "JMPZ",
    44 : "JMPNZ",
    45 : "JMPZNZ",
    46 : "JMPZ_EX",
    47 : "JMPNZ_EX",
    48 : "CASE",
    49 : "SWITCH_FREE",
    50 : "BRK",
    51 : "CONT",
    52 : "BOOL",
    53 : "INIT_STRING",
    54 : "ADD_CHAR",
    55 : "ADD_STRING",
    56 : "ADD_VAR",
    57 : "BEGIN_SILENCE",
    58 : "END_SILENCE",
    59 : "INIT_FCALL_BY_NAME",
    60 : "DO_FCALL",
    61 : "DO_FCALL_BY_NAME",
    62 : "RETURN",
    63 : "RECV",
    64 : "RECV_INIT",
    65 : "SEND_VAL",
    66 : "SEND_VAR",
    67 : "SEND_REF",
    68 : "NEW",
    69 : "INIT_NS_FCALL_BY_NAME",
    70 : "FREE",
    71 : "INIT_ARRAY",
    72 : "ADD_ARRAY_ELEMENT",
    73 : "INCLUDE_OR_EVAL",
    74 : "UNSET_VAR",
    75 : "UNSET_DIM",
    76 : "UNSET_OBJ",
    77 : "FE_RESET",
    78 : "FE_FETCH",
    79 : "EXIT",
    80 : "FETCH_R",
    81 : "FETCH_DIM_R",
    82 : "FETCH_OBJ_R",
    83 : "FETCH_W",
    84 : "FETCH_DIM_W",
    85 : "FETCH_OBJ_W",
    86 : "FETCH_RW",
    87 : "FETCH_DIM_RW",
    88 : "FETCH_OBJ_RW",
    89 : "FETCH_IS",
    90 : "FETCH_DIM_IS",
    91 : "FETCH_OBJ_IS",
    92 : "FETCH_FUNC_ARG",
    93 : "FETCH_DIM_FUNC_ARG",
    94 : "FETCH_OBJ_FUNC_ARG",
    95 : "FETCH_UNSET",
    96 : "FETCH_DIM_UNSET",
    97 : "FETCH_OBJ_UNSET",
    98 : "FETCH_DIM_TMP_VAR",
    99 : "FETCH_CONSTANT",
    100 : "GOTO",
    101 : "EXT_STMT",
    102 : "EXT_FCALL_BEGIN",
    103 : "EXT_FCALL_END",
    104 : "EXT_NOP",
    105 : "TICKS",
    106 : "SEND_VAR_NO_REF",
    107 : "CATCH",
    108 : "THROW",
    109 : "FETCH_CLASS",
    110 : "CLONE",
    111 : "RETURN_BY_REF",
    112 : "INIT_METHOD_CALL",
    113 : "INIT_STATIC_METHOD_CALL",
    114 : "ISSET_ISEMPTY_VAR",
    115 : "ISSET_ISEMPTY_DIM_OBJ",
    116 : "SEND_VAL_EX",
    117 : "SEND_VAR",
    118 : "INIT_USER_CALL",
    119 : "SEND_ARRAY",
    120 : "SEND_USER",
    121 : "STRLEN",
    122 : "DEFINED",
    123 : "TYPE_CHECK",
    124 : "VERIFY_RETURN_TYPE",
    125 : "FE_RESET_RW",
    126 : "FE_FETCH_RW",
    127 : "FE_FREE",
    128 : "INIT_DYNAMIC_CALL",
    129 : "DO_ICALL",
    130 : "DO_UCALL",
    131 : "DO_FCALL_BY_NAME",
    132 : "PRE_INC_OBJ",
    133 : "PRE_DEC_OBJ",
    134 : "POST_INC_OBJ",
    135 : "POST_DEC_OBJ",
    136 : "ASSIGN_OBJ",
    137 : "OP_DATA",
    138 : "INSTANCEOF",
    139 : "DECLARE_CLASS",
    140 : "DECLARE_INHERITED_CLASS",
    141 : "DECLARE_FUNCTION",
    142 : "RAISE_ABSTRACT_ERROR",
    143 : "DECLARE_CONST",
    144 : "ADD_INTERFACE",
    145 : "DECLARE_INHERITED_CLASS_DELAYED",
    146 : "VERIFY_ABSTRACT_CLASS",
    147 : "ASSIGN_DIM",
    148 : "ISSET_ISEMPTY_PROP_OBJ",
    149 : "HANDLE_EXCEPTION",
    150 : "USER_OPCODE",
    152 : "ZEND_JMP_SET",
    153 : "ZEND_DECLARE_LAMBDA_FUNCTION",
    154 : "ZEND_ADD_TRAIT",
    155 : "ZEND_BIND_TRAITS",
    156 : "ZEND_SEPARATE",
    157 : "ZEND_FETCH_CLASS_NAME",
    158 : "ZEND_CALL_TRAMPOLINE",
    159 : "ZEND_DISCARD_EXCEPTION",
    160 : "ZEND_YIELD",
    161 : "ZEND_GENERATOR_RETURN",
    162 : "ZEND_FAST_CALL",
    163 : "ZEND_FAST_RET",
    164 : "ZEND_RECV_VARIADIC",
    165 : "ZEND_SEND_UNPACK",
    166 : "ZEND_POW",
    167 : "ZEND_ASSIGN_POW",
    168 : "ZEND_BIND_GLOBAL",
    169 : "ZEND_COALESCE",
    170 : "ZEND_SPACESHIP",
    171 : "ZEND_DECLARE_ANON_CLASS",
    172 : "ZEND_DECLARE_ANON_INHERITED_CLASS",
}

# regular data types
IS_UNDEF                    = 0
IS_NULL                     = 1
IS_FALSE                    = 2
IS_TRUE                     = 3
IS_LONG                     = 4
IS_DOUBLE                   = 5
IS_STRING                   = 6
IS_ARRAY                    = 7
IS_OBJECT                   = 8
IS_RESOURCE                 = 9
IS_REFERENCE                = 10

# constant expressions
IS_CONSTANT                 = 11
IS_CONSTANT_AST             = 12

# fake types
_IS_BOOL                    = 13
IS_CALLABLE                 = 14
IS_VOID                     = 18

# internal types
IS_INDIRECT                 = 15
IS_PTR                      = 17
_IS_ERROR                   = 19

# Op Types
IS_CONST    =   1 << 0
IS_TMP_VAR  =   1 << 1
IS_VAR      =   1 << 2
IS_UNUSED   =   1 << 3
IS_CV       =   1 << 4
