#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.
#
AC_PREREQ(2.59)
AC_INIT([gama], [1.9.07], [bug-gama@gnu.org])
AC_CONFIG_SRCDIR([lib/gnu_gama/version.cpp])
AC_CONFIG_HEADER([config.h])
AC_CONFIG_AUX_DIR([scripts/config.aux])

AM_INIT_AUTOMAKE

# Checks for programs.
AC_PROG_AWK
AC_PROG_CXX
AC_PROG_CC
AC_PROG_CPP
AC_PROG_LN_S
AC_PROG_MAKE_SET
AC_PROG_RANLIB

# Checks for libraries.
AC_CHECK_LIB([expat], [main])

# Checks for header files.
AC_HEADER_STDC
AC_CHECK_HEADER(expat.h, , [AC_MSG_ERROR(
                [Couldn't find expat.h...try installing libexpat-dev] )])

# Checks for typedefs, structures, and compiler characteristics.
AC_HEADER_STAT
AC_HEADER_STDBOOL
AC_C_CONST
AC_C_INLINE
AC_TYPE_OFF_T
AC_TYPE_SIZE_T

# Checks for library functions.
AC_FUNC_ERROR_AT_LINE
AC_FUNC_MALLOC
AC_FUNC_MEMCMP
AC_FUNC_MMAP
AC_FUNC_REALLOC
AC_FUNC_SETVBUF_REVERSED
AC_CHECK_FUNCS([memmove memset munmap pow sqrt])

AC_OUTPUT([Makefile 
           lib/Makefile
           gama-g3/Makefile
           gama-local/Makefile
           scripts/Makefile          
           doc/Makefile
           xml/Makefile
          ])

