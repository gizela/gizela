/*  
    Geodesy and Mapping C++ Library (GNU GaMa / GaMaLib)
    Copyright (C) 2000  Ales Cepek <cepek@fsv.cvut.cz>

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
 *  $Id: write.cpp,v 1.2 2007/06/26 15:04:07 cepek Exp $
 */

#include <iostream>
#include <iomanip>
#include <typeinfo>
#include <gamalib/local/gamadata.h>
#include <gamalib/local/pobs/format.h>
#include <gamalib/observation.h>

namespace GaMaLib {

typedef GNU_gama::List<GNU_gama::Cluster<Observation>*> ClusterList;


std::ostream& operator << (std::ostream& str, PointData& sez)
{
  using namespace std;
  int prec_p = str.precision();
  std::ios_base::fmtflags flag_p = str.flags();
  str.setf(ios_base::fixed);
  
  int maxkl = 0;
  for (PointData::iterator i=sez.begin(); i!=sez.end(); ++i)
    {
      int k = (*i).first.length();
      // maxkl = max( maxkl, k);   
      if (k > maxkl) maxkl = k;
    }
    
  {   // for ...
    for (PointData::iterator i=sez.begin(); i!=sez.end(); ++i)
      {
        const PointID& cb  = (*i).first;
        LocalPoint&    bod = (*i).second;
        
        
        str << "<point id=";
        for (int j=cb.length(); j<maxkl; j++)
          str << ' ';
        str << "\"" << cb << "\"";
        
        if (bod.test_xy())
          {
            str.precision(Format::coord_p());
            str << " x=";
            str << "\"" << bod.x() << "\"";
            str << " y=";
            str.precision(Format::coord_p());
            str << "\"" << bod.y() << "\"";
          }
        if (bod.test_z())
          {
            str << " z=";
            str.precision(Format::coord_p());
            str << "\"" << bod.z() << "\"";
          }
        
        string fix, adj, axy, az;

        if (bod.fixed_xy()      )  fix += "xy";
        if (bod.fixed_z ()      )  fix += "z" ; 
        if (bod.free_xy()       )  axy  = "xy";
        if (bod.constrained_xy())  axy  = "XY";
        if (bod.free_z()        )  az   = "z" ;
        if (bod.constrained_z() )  az   = "Z" ;
        adj = axy + az;
        
        if (fix != "")  str << " fix=\"" << fix << "\"";
        if (adj != "")  str << " adj=\"" << adj << "\"";

        str << " />\n";
      }
  }   // for ...
  
  str.precision(prec_p);
  str.flags(flag_p);
  
  return str;
}
 


std::ostream& operator << (std::ostream& str, ObservationData& od)
{
  using namespace std;
  int prec_p = str.precision();
  std::ios_base::fmtflags flag_p = str.flags();
  str.setf(ios_base::fixed);
  
  for (ClusterList::iterator c=od.clusters.begin(); c!=od.clusters.end(); ++c)
    {
      bool common_standpoint = true;
      string start_tag, end_tag;

      if (const StandPoint *sp = dynamic_cast<StandPoint*>(*c))
        {
          start_tag = "\n<obs";
          if (sp->observation_list.empty()) continue;
          PointID first_id = sp->station;
          ObservationList::const_iterator i=sp->observation_list.begin();
          while (++i != sp->observation_list.end())
            if (first_id != (*i)->from())
              {
                common_standpoint = false;
                break;
              }
          if (common_standpoint)
            start_tag += " from=\"" + first_id + "\">\n";
          else
            start_tag += ">\n";

          end_tag   = "</obs>\n"; 
        }
      else if (typeid(**c) == typeid(Coordinates))
        {
          start_tag = "\n<coordinates>\n";
          end_tag   = "</coordinates>\n";
        }
      else if (typeid(**c) == typeid(HeightDifferences))
        {
          start_tag = "\n<height-differences>\n";
          end_tag   = "</height-differences>\n";
        }

      str << start_tag;
                   
      const ObservationList& ol = (*c)->observation_list;
      for (ObservationList::const_iterator i=ol.begin(); i!=ol.end(); ++i)
        {
          str << "   ";
          (*i)->write(str, !common_standpoint);
          str << "\n";
        }

      if ((*c)->covariance_matrix.bandWidth())
        {
          const CovMat& C = (*c)->covariance_matrix;
          Index  dim   = C.dim();
          Index  band  = C.bandWidth();
          str << "\n<cov-mat dim=\"" << dim 
              << "\" band=\"" << band << "\">\n";
          for (Index i=1; i<=dim; i++)
            {
              for (Index j=i; j<=i+band && j <=dim; j++)
                str << C(i,j) << " ";
              str << "\n";
            }
          str << "</cov-mat>\n";
        }
      
      str << end_tag;
    }
  
  str.precision(prec_p);
  str.flags(flag_p);
  
  return str;
}
 
}







