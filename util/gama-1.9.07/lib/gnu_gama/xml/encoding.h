/*  
    Geodesy and Mapping C++ Library (GNU GaMa / GaMaLib)
    Copyright (C) 2000  Petr Doubrava <petr@gepro.cz>

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
 *  $Id: encoding.h,v 1.2 2007/06/26 15:04:11 cepek Exp $
 */

#include <gnu_gama/xml_expat.h>

#ifndef GaMaLib_GKF__XML__encoding__h_
#define GaMaLib_GKF__XML__encoding__h_


#ifdef __cplusplus
namespace GNU_gama {
#endif

int   cp1250_unicode(int* tab);
int   cp1251_unicode(int* tab);
int   iso_8859_2_unicode(int* tab);
int   ascii(int* tab);
char* utf8_cp1250(char *buf);
char* utf8_cp1251(char *buf);
char* utf8_iso_8859_2(char *buf);
char* utf8_ascii(char *buf);
int   Utf8Decode(int& u, unsigned char *buf);
int   UnknownEncodingHandler(void *userData, const char *name,
                           XML_Encoding *info);

#ifdef __cplusplus
}  // namespace GNU_gama                
#endif


#endif



