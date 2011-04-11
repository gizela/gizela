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
 *  $Id: medianf.h,v 1.2 2007/06/26 15:04:04 cepek Exp $
 */

#ifndef GaMaLib_Median_Func_h
#define GaMaLib_Median_Func_h

#include <gamalib/matvec.h>

namespace GaMaLib {

template <typename Float, typename Exc>
Float median(GenVec<Float, Exc>& a)
{
   sort(a);
   return (a((a.dim()+1)/2) + a((a.dim()+2)/2))/2;
}

template <typename Float, typename Exc>
double MAD(GenVec<Float, Exc>& a)
{
   const Float c = median(a);

   Float d;
   for (int i=1; i<=a.dim(); i++)
      {
         d = a(i) - c;
         a(i) = (d>=0) ? d : -d;
      }

   return median(a)/0.6745;
}

}      // namespace GaMaLib
#endif
