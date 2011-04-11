/*  
    Geodesy and Mapping C++ Library (GNU GaMa / GaMaLib)
    Copyright (C) 1999  Ales Cepek <cepek@fsv.cvut.cz>

    This file is part of the GNU GaMa / GaMaLib C++ Library.
    
    This library is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License, or
    (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
*/

/*
 *  $Id: capi_exception.h,v 1.2 2007/06/26 15:04:05 cepek Exp $
 */

#ifndef GNU__GaMa__C_API_Cgama_exception_handling_functions_header_file____
#define GNU__GaMa__C_API_Cgama_exception_handling_functions_header_file____

#ifdef __cplusplus
extern "C" {
#endif

  void        Cgama_init(int);

  const char* Cgama_exception();
  void        Cgama_exception_clean();
  int         Cgama_exception_unknown();
  int         Cgama_exception_GKF_parser_line();

#ifdef __cplusplus
}
#endif

#endif



