/*  
    GNU Gama -- adjustment of geodetic networks
    Copyright (C) 2005  Ales Cepek <cepek@gnu.org> 
                        Boris Pihtin <cyb@bendery.md>

    This file is part of the GNU Gama C++ library.
    
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
 *  $Id: encoding_cp1251.cpp,v 1.2 2007/06/26 15:04:11 cepek Exp $
 */

#include <string.h>
#include <gnu_gama/xml/encoding.h>

#ifdef __cplusplus
namespace GNU_gama {
#endif


int cp1251_unicode(int* tab)
{
   int cp1251_unicode[]={

     // values in the table are copied from the GNU 'recode' library,
     // file cp1251.h:
     //
     //    ftp://ftp.gnu.org/pub/gnu/recode/recode-3.6.tar.gz
     // 
     
     /* 0x80 */
     0x0402, 0x0403, 0x201a, 0x0453, 0x201e, 0x2026, 0x2020, 0x2021,
     0x20ac, 0x2030, 0x0409, 0x2039, 0x040a, 0x040c, 0x040b, 0x040f,
     /* 0x90 */
     0x0452, 0x2018, 0x2019, 0x201c, 0x201d, 0x2022, 0x2013, 0x2014,
     0xfffd, 0x2122, 0x0459, 0x203a, 0x045a, 0x045c, 0x045b, 0x045f,
     /* 0xa0 */
     0x00a0, 0x040e, 0x045e, 0x0408, 0x00a4, 0x0490, 0x00a6, 0x00a7,
     0x0401, 0x00a9, 0x0404, 0x00ab, 0x00ac, 0x00ad, 0x00ae, 0x0407,
     /* 0xb0 */
     0x00b0, 0x00b1, 0x0406, 0x0456, 0x0491, 0x00b5, 0x00b6, 0x00b7,
     0x0451, 0x2116, 0x0454, 0x00bb, 0x0458, 0x0405, 0x0455, 0x0457,
     /* 0xc0 */
     0x0410, 0x0411, 0x0412, 0x0413, 0x0414, 0x0415, 0x0416, 0x0417,
     0x0418, 0x0419, 0x041a, 0x041b, 0x041c, 0x041d, 0x041e, 0x041f,
     /* 0xd0 */
     0x0420, 0x0421, 0x0422, 0x0423, 0x0424, 0x0425, 0x0426, 0x0427,
     0x0428, 0x0429, 0x042a, 0x042b, 0x042c, 0x042d, 0x042e, 0x042f,
     /* 0xe0 */
     0x0430, 0x0431, 0x0432, 0x0433, 0x0434, 0x0435, 0x0436, 0x0437,
     0x0438, 0x0439, 0x043a, 0x043b, 0x043c, 0x043d, 0x043e, 0x043f,
     /* 0xf0 */
     0x0440, 0x0441, 0x0442, 0x0443, 0x0444, 0x0445, 0x0446, 0x0447,
     0x0448, 0x0449, 0x044a, 0x044b, 0x044c, 0x044d, 0x044e, 0x044f,
   };                       
         
   unsigned int i,j;              
   for (i=0;i<0x00000080;i++)tab[i]=(int)i;
   for (j=0;i<256;i++) tab[i]=cp1251_unicode[j++];                    
   return 1;
}


char* utf8_cp1251(char *buf)
{
  static int tab[256];
  static bool init_tab = true;
  if (init_tab)  
    {       
      cp1251_unicode((int*)tab);
      init_tab = false;  
    }       
  unsigned int u;
  char *p,*q;
  p=q=buf;
  while (*p){
          p+=Utf8Decode((int&)u,(unsigned char*)p);
          if (u>0x80){
             int i;
             for (i=0x80;i<256;i++)
                 if (tab[i]==(int)u){*q=i;break;}
             if (i==256)*q=u;
          }else *q=u;
          q++;
  }
  *q=0;
  return buf; 
}


#ifdef __cplusplus
}   //  namespace GNU_gama
#endif









