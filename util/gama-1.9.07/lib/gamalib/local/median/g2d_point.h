/*  
    Geodesy and Mapping C++ Library (GNU GaMa / GaMaLib)
    Copyright (C) 1999  Jiri Vesely <vesely@gama.fsv.cvut.cz>
                  2001  Ales Cepek  <cepek@fsv.cvut.cz>

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
 *  $Id: g2d_point.h,v 1.2 2007/06/26 15:04:07 cepek Exp $
 */

/*************************************************************
 * approximate coordinates of a single point                 *
 *************************************************************/

#ifndef GaMaLib_g2d_point_h__GaMaLib_Median_Pribl_b_H
#define GaMaLib_g2d_point_h__GaMaLib_Median_Pribl_b_H

#include <gamalib/local/gamadata.h>
#include <gamalib/local/pobs/bearing.h>
#include <gamalib/local/median/g2d_exception.h>
#include <gamalib/local/median/g2d_helper.h>


namespace GaMaLib {

  class ApproxPoint
    {

    private:
      Helper_list solved_points;
      PointData SB;
      PointID   CB;
      ObservationList SM;
      ObservationList SM_U;         // for inner angles
      ObservationList SM_S;  	    // for outer bearings
      LocalPoint v_point;           // final point - output
      LocalPoint v_point2;          //             - ambiguous solutions (two)
      PointData* SB_puv;            // repeating calc. with another Point ID 
      ObservationList* SM_puv;
      Solution_state_tag state_;    // Solution_state_tag -> see g2d_helper.h
      void ClearLists();  	    // empty helper lists

      Angle* makeAngle(const ObservationList::iterator i, 
                       const ObservationList::iterator j)
        {
          Direction* s1 = dynamic_cast<Direction*>(*i);
          Direction* s2 = dynamic_cast<Direction*>(*j);
          if(!(s1 && s2))
            throw g2d_exc("ApproxPoint::makeAngle : missing direction");
          Double angle = s2->value() - s1->value();
          return new Angle(s1->from(),s1->to(),s2->to(),
                           (angle < 0 ? angle+2*M_PI : angle));
        }
      Direction* makeBearing(const Angle* u, const PointID& cb)
        {
          PointID point = (u->to() == cb ? u->fs() : u->to());
          Double sm = bearing(SB[u->from()],SB[point]);
          sm += (u->to() == cb ? -u->value() : u->value());
          sm += (sm < 0 ? 2*M_PI : 0);
          sm -= (sm >= 2*M_PI ? 2*M_PI : 0);
          return new Direction(u->from(),cb,sm);
        }
      Direction* makeBearing(const Direction* s, const PointID& cb)
        {
          Double sm = s->value() + s->orientation();
          sm -= (sm >= 2*M_PI ? 2*M_PI : 0);
          return new Direction(s->from(),cb,sm);
        }
      bool KnownTarget(ObservationList::const_iterator i)
        {
          // true: target coordinates are known
          const Angle* u = dynamic_cast<const Angle*>(*i);
          return KnownTarget1(i) && (u ? KnownTarget2(u) : true);
        }
      bool KnownTarget1(ObservationList::const_iterator i)
        {
          return SB[(*i)->to()].test_xy();
        }
      bool KnownTarget2(const Angle* u)
        {
          // true: target coordinates of agle's right site are known
          return SB[u->fs()].test_xy();
        }
      bool knownStandpoint(ObservationList::const_iterator i)
        {
          // true: standpoint coordinates and orientation shift are known
          // 1999.07.06 - AC
          // Direction* s = dynamic_cast<Direction*>(*i);
          // return SB[(*i)->from()].test_xy() &&
          //       (s ? SB[s->from()].poc_orpos() > s->osnova() : true);
          bool test_xyz = SB[(*i)->from()].test_xy();
          if (test_xyz)
            {
              if (const Direction *s = dynamic_cast<const Direction*>(*i))
                {
                  if (!s->test_orientation()) return false;
                }
            }
          return test_xyz;
        }
      void ArrangeObservations(ObservationList&);
      void reset(PointData*, ObservationList*, const PointID&);


    public:
      ApproxPoint(PointData* sb, ObservationList* sm, const PointID& cb)
        : SB_puv(sb), SM_puv(sm), state_(missing_init)
        {
          reset(sb,sm,cb);
        }
      ApproxPoint(PointData* sb, ObservationList* sm) 
        : SB_puv(sb), SM_puv(sm), state_(missing_init) 
        {
        }
      ~ApproxPoint()
        {
          ClearLists();
        } 
      void calculation(PointData* sb, ObservationList* sm, const PointID& cb)
        {
          SB_puv = sb;
          SM_puv = sm;
          reset(sb,sm,cb);
          calculation();
        }
      void calculation(const PointID& cb)
        {
          reset(SB_puv, SM_puv, cb);
          calculation();
        }
      void calculation();
      Solution_state_tag state() const 
        { 
          return state_; 
        }
      LocalPoint Solution()
        {
          if(state_ == calculation_not_done)
            throw g2d_exc("ApproxPoint: computation not done");
          if(state_ == no_solution)
            throw g2d_exc("ApproxPoint: no solution");
          return v_point;
        }
      LocalPoint solution_2()
        {
          if(state_ == calculation_not_done)
            throw g2d_exc("ApproxPoint: computation not done");
          if(state_ == no_solution)
            throw g2d_exc("ApproxPoint: no solution");
          if(state_ == unique_solution)
            throw g2d_exc("ApproxPoint: only unique solution");
          return v_point2;
        }
    };


} // namespace GaMaLib


#endif






