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
 *  $Id: orientation.cpp,v 1.3 2007/08/02 12:05:33 cepek Exp $
 */

#include <gamalib/local/orientation.h>
#include <gamalib/cluster.h>
#include <gamalib/local/gamadata.h>
#include <algorithm>
#include <sstream>
#include <iomanip>

using namespace GaMaLib;

typedef GNU_gama::Cluster<Observation>  Cluster;


void Orientation::add_all()
{
  ObservationList::const_iterator iterator = OL.begin();
  Double l1;
  int    dir_count;

  while (iterator != OL.end()) 
    if (const Direction* direction = dynamic_cast<const Direction*>(*iterator))
      {
        Cluster* cluster = const_cast<Cluster*>(direction->ptr_cluster());
        StandPoint* standpoint = static_cast<StandPoint*>(cluster);
        if (standpoint->test_orientation())
          {
            const Cluster* ca = direction->ptr_cluster();
            const Cluster* cb = ca;
            while (iterator != OL.end())
              {
                cb = (*iterator)->ptr_cluster();
                if (ca == cb)
                  ++iterator;
                else
                  break;
              }
          }
        else
          {
            orientation(iterator, l1, dir_count);
            if (dir_count > 0) standpoint->set_orientation(l1);
          }
      }
    else
      ++iterator;
}


void Orientation::orientation(ObservationList::const_iterator& mer,
                              Double& z, int& dir_count)
{
   const Cluster* current = (*mer)->ptr_cluster();
   PointData::const_iterator pa = PL.find( (*mer)->from() );
   if (pa == PL.end() || !(*pa).second.test_xy())
   {
      while (mer != OL.end() && (*mer)->ptr_cluster() == current)  ++mer;

      z = 0;
      dir_count = 0;
      return;
   }

   std::vector<Double> sz;

   while ( mer != OL.end() && (*mer)->ptr_cluster() == current )
   {
      if (const Direction* direction = dynamic_cast<const Direction*>(*mer))
        {
          PointData::const_iterator pb = PL.find(direction->to());
          if (pb != PL.end() && (*pb).second.test_xy())
            {
              // gama 1.9.04
              double zn;
              try
                {
                  zn = bearing((*pa).second, (*pb).second);
                }
              catch (GaMaLib::Exception e)
                {
                  std::stringstream s;
                  s.precision(5);
                  s << e.text << "\n\n";

                  s.precision(5);
                  s.setf(std::ios_base::fixed, std::ios_base::floatfield);

                  s << std::setw(13) << pa->first;
                  s << "  x = " << std::setw(13) << pa->second.x();
                  s << "  y = " << std::setw(13) << pa->second.y();
                  s << "\n";

                  s << std::setw(13) << pb->first;
                  s << "  x = " << std::setw(13) << pb->second.x();
                  s << "  y = " << std::setw(13) << pb->second.y();
                  s << "\n";

                  throw GaMaLib::Exception(s.str());
                }
              catch (...)
                {
                  throw;
                }
              double sn = direction->value();
              double df = zn - sn;
              // if (df < 0) df += 2*M_PI;  ......  gamalib-1.1.13
              while (df > M_PI)
                df -= 2*M_PI;
              while (df < -M_PI)
                df += 2*M_PI;
              sz.push_back(df);
            }
        }
      ++mer;
   }

   Double l1 = 0;
   Float  d  = 0;          // mean deviation
   int    n  = sz.size();

   if (n)
   {
      std::sort(sz.begin(), sz.end());
      Double l1a = sz[(n-1)/2];
      Double l1b = sz[n/2];
      if (abs(l1b - l1a) > M_PI/2 && n < 3)
         l1 = l1a;
      else
         l1 = (sz[n/2] + sz[(n-1)/2]) / 2;
         
      for (int i=0; i<n; i++)
         d += abs(sz[i] - l1);
      d /= n;
      if (l1 < 0) l1 += 2*M_PI;
   }

   z = l1;
   dir_count = n;
   return;
}


