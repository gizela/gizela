/*  
    Geodesy and Mapping C++ Library (GNU GaMa / GaMaLib)
    Copyright (C) 2001  Ales Cepek <cepek@fsv.cvut.cz>

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
 *  $Id: linearization.h,v 1.2 2007/06/26 15:04:05 cepek Exp $
 */

#ifndef GaMaLib__LocalLinearization______GaMaLib___Local___Linearization_____
#define GaMaLib__LocalLinearization______GaMaLib___Local___Linearization_____

#include <gamalib/linearization.h>
#include <gamalib/local/gamadata.h>

namespace GaMaLib {

  class LocalLinearization : public Linearization 
    {

    public:
      
      LocalLinearization(PointData& pd, double m) : PD(pd), maxn(0), m0(m) {}
      
      int  unknowns() const { return maxn; }
      void linearization(const Observation* o) const
        {
          rhs = size = 0;
          
          if     (const Direction  *dir = dynamic_cast<const Direction *>(o))
            direction(dir);
          else if(const Distance   *dis = dynamic_cast<const Distance  *>(o))
            distance(dis);
          else if(const Angle      *ang = dynamic_cast<const Angle     *>(o))
            angle(ang);
          else if(const H_Diff     *h_d = dynamic_cast<const H_Diff    *>(o))
            h_diff(h_d);
          else if(const S_Distance *s_d = dynamic_cast<const S_Distance*>(o))
            s_distance(s_d);
          else if(const Z_Angle    *z_a = dynamic_cast<const Z_Angle   *>(o))
            z_angle(z_a);
          else if(const X          *x__ = dynamic_cast<const X         *>(o))
            x(x__);
          else if(const Y          *y__ = dynamic_cast<const Y         *>(o))
            y(y__);
          else if(const Z          *z__ = dynamic_cast<const Z         *>(o))
            z(z__);
          else if(const Xdiff      *xdf = dynamic_cast<const Xdiff     *>(o))
            xdiff(xdf);
          else if(const Ydiff      *ydf = dynamic_cast<const Ydiff     *>(o))
            ydiff(ydf);
          else if(const Zdiff      *zdf = dynamic_cast<const Zdiff     *>(o))
            zdiff(zdf);
        }

    private:

      mutable PointData&   PD;
      mutable int          maxn;
      double               m0;
      
      void direction  (const Direction  *obs) const;
      void distance   (const Distance   *obs) const;
      void angle      (const Angle      *obs) const;
      void h_diff     (const H_Diff     *obs) const;
      void s_distance (const S_Distance *obs) const;
      void z_angle    (const Z_Angle    *obs) const;
      void x          (const X          *obs) const;
      void y          (const Y          *obs) const;
      void z          (const Z          *obs) const;
      void xdiff      (const Xdiff      *obs) const;
      void ydiff      (const Ydiff      *obs) const;
      void zdiff      (const Zdiff      *obs) const;
    };
  
}

#endif



/*
 *{
 *  obs->linearization(PD, maxn, m0);
 *  rhs  = obs->rhs();
 *  size = obs->ncoef();
 *  for (size_t i=1; i<=size; i++)
 *    {
 *      coeff[i-1] = obs->coef(i+1); // WARNING: coefficients are shifted by 1!
 *      index[i-1] = obs->indx(i);
 *    }
 *}
 */

