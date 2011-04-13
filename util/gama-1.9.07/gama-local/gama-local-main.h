/*
    GNU Gama C++ library
    Copyright (C) 1999, 2002, 2003  Ales Cepek <cepek@gnu.org>

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
 *  $Id: gama-local-main.h,v 1.10 2008/04/13 10:02:31 cepek Exp $
 */

#ifndef GAMA_MAIN__gama_main__gm_mn__g_m__g______________________________h___
#define GAMA_MAIN__gama_main__gm_mn__g_m__g______________________________h___

#include <gnu_gama/outstream.h>

#include <cstring>
#include <gnu_gama/version.h>
#include <gnu_gama/intfloat.h>
#include <gnu_gama/xml/localnetwork.h>

#include <gamalib/language.h>
#include <gamalib/local/gamadata.h>
#include <gamalib/xml/gkfparser.h>
#include <gamalib/local/network_svd.h>
#include <gamalib/local/network_gso.h>
#include <gamalib/local/network_chol.h>
#include <gamalib/local/network_env.h>
#include <gamalib/local/acord.h>
#include <gamalib/local/lpoint.h>

#include <gamalib/local/results/text/approximate_coordinates.h>
#include <gamalib/local/results/text/network_description.h>
#include <gamalib/local/results/text/general_parameters.h>
#include <gamalib/local/results/text/fixed_points.h>
#include <gamalib/local/results/text/adjusted_observations.h>
#include <gamalib/local/results/text/adjusted_unknowns.h>
#include <gamalib/local/results/text/outlying_abs_terms.h>
#include <gamalib/local/results/text/reduced_observations.h>
#include <gamalib/local/results/text/reduced_observations_to_ellipsoid.h>
#include <gamalib/local/results/text/residuals_observations.h>
#include <gamalib/local/results/text/error_ellipses.h>
#include <gamalib/local/results/text/test_linearization.h>


//---------------------------------------------------------------------------

int help()
{
  using namespace std;
  using namespace GaMaLib;
  
  cerr << "\n" 
       << "Adjustment of local geodetic network (modified TK)"
       << "        version: "<< GNU_gama::GNU_gama_version
       << " / " << GNU_gama::GNU_gama_compiler << "\n"
       << "************************************\n"
       << "http://www.gnu.org/software/gama/\n\n"
       << "Usage: " << /*argv[0]*/"gama-local" 
       << "  input.xml "
       << " [options]\n\n";
  cerr << "Options:\n"
       << "\n";
  cerr << "--algorithm  svd | gso | cholesky | envelope\n" 
       << "--language   en | ca | cz | du | fi | fr | hu | ru | ua \n"
       << "--encoding   utf-8 | iso-8859-2 | iso-8859-2-flat | cp-1250 "
       << "| cp-1251\n"
       << "--angles     400 | 360\n"  
       << "--latitude   <latitude> in degrees\n"
       << "--ellipsoid  <ellipsoid name>\n"
       << "--text       adjustment_results.txt\n"
       << "--xml        adjustment_results.xml\n"
    /* << "--obs        observation_equations.txt (obsolete format)\n" */
       << "--cov-band   covariance matrix of adjusted parameters in XML output\n"
       << "             n  = -1  for full covariance matrix (implicit value)\n"
       << "             n >=  0  covariances are computed only for bandwidth n\n"
       << "--version\n"
       << "--help\n";
  cerr << endl;
  return 1;
}


int GaMa_Main(int argc, char **argv)
{
  using namespace std;
  using namespace GaMaLib;
  
  string description;
  const char* c;
  const char* argv_1 = 0;
  // const char* argv_2 = 0;    *** version 1.9.01 ***
  const char* argv_algo = 0;
  const char* argv_lang = 0;
  const char* argv_enc  = 0;
  const char* argv_angles = 0;
  const char* argv_ellipsoid = 0;
  const char* argv_latitude = 0;
  const char* argv_txtout = 0;
  const char* argv_xmlout = 0;
  const char* argv_obsout = 0;
  const char* argv_covband = 0;
  const char* argv_cpoint_x = 0;
  const char* argv_cpoint_y = 0;
  const char* argv_cpoint_z = 0;

  bool correction_to_ellipsoid = false;
  LocalPoint cpoint = LocalPoint::XYZ(0.0, 0.0, 0.0);

  GNU_gama::Ellipsoid el;
  double latitude = M_PI/4.0;
  
  for (int i=1; i<argc; i++)
    {
      c = argv[i];
      if (*c != '-')    // **** one or two parameters (file names) ****
        { 
          if (!argv_1) {
              argv_1 = c;
              continue;
            }
          // if (!argv_2) {     *** only one parameter and options ***
          //     argv_2 = c;    *** since version 1.9.01           ***
          //     continue;
          // }
	  std::cerr << "err 1";
          return help();
        }

      // ****  options  ****

      if(*c && *c == '-') c++;
      if(*c && *c == '-') c++;
      string name = string(c);
      c = argv[++i];

      std::cerr << "option: --" << name << "  value: " << c << endl;

      if      (name == "help"      ) return help();
      else if (name == "version"   ) return GNU_gama::version("gama-local", "Ales Cepek");
      else if ( i   ==  argc       ) { std::cerr << "err 0"; return help();}
      else if (name == "algorithm" ) argv_algo = c; 
      else if (name == "language"  ) argv_lang = c;
      else if (name == "encoding"  ) argv_enc  = c;
      else if (name == "angles"    ) argv_angles = c;
      else if (name == "ellipsoid" ) argv_ellipsoid = c;
      else if (name == "latitude"  ) argv_latitude = c;
      else if (name == "text"      ) argv_txtout = c;
      else if (name == "xml"       ) argv_xmlout = c;
      else if (name == "obs"       ) argv_obsout = c;
      else if (name == "cov-band"  ) argv_covband = c;
      else if (name == "cpoint-x"  ) argv_cpoint_x = c;
      else if (name == "cpoint-y"  ) argv_cpoint_y = c;
      else if (name == "cpoint-z"  ) argv_cpoint_z = c;
      else{
	  std::cerr << "unknown option: --" << name << endl;
          return help();
      }
    }
  
  if (!argv_1) {
	  std::cerr << "Error: No imput XML file";
	return help();
  }
  if (!argv_lang)
    set_gama_language(en);
  else
    {
      if      (!strcmp("en", argv_lang)) set_gama_language(en);
      else if (!strcmp("ca", argv_lang)) set_gama_language(ca);
      else if (!strcmp("cs", argv_lang)) set_gama_language(cz);
      else if (!strcmp("cz", argv_lang)) set_gama_language(cz);
      else if (!strcmp("du", argv_lang)) set_gama_language(du);
      else if (!strcmp("fi", argv_lang)) set_gama_language(fi);
      else if (!strcmp("fr", argv_lang)) set_gama_language(fr);
      else if (!strcmp("hu", argv_lang)) set_gama_language(hu);
      else if (!strcmp("ru", argv_lang)) set_gama_language(ru);
      else if (!strcmp("ua", argv_lang)) set_gama_language(ua);
      else {
	      std::cerr << "Unknown language: " << argv_lang << endl;
              return help();
      }
    }

  LocalNetwork* IS;
  ostream* output = 0;

  ofstream fcout;
  if (argv_txtout) 
    if (!strcmp(argv_txtout, "-"))
      {
        output = &std::cout;
      } 
    else
      {
        fcout.open(argv_txtout);  
        output = &fcout;
      }

  GNU_gama::OutStream cout(output);
  
  if (argv_enc)
    {
      using namespace GNU_gama;

      if (!strcmp("utf-8", argv_enc)) 
        cout.set_encoding(OutStream::utf_8);
      else if (!strcmp("iso-8859-2", argv_enc)) 
        cout.set_encoding(OutStream::iso_8859_2);
      else if (!strcmp("iso-8859-2-flat", argv_enc)) 
        cout.set_encoding(OutStream::iso_8859_2_flat);
      else if (!strcmp("cp-1250", argv_enc)) 
        cout.set_encoding(OutStream::cp_1250);
      else if (!strcmp("cp-1251", argv_enc)) 
        cout.set_encoding(OutStream::cp_1251);
      else
	std::cerr << "Unknown encoding: " << argv_enc << endl;
        return help();
    }

  
  try {
    
    try {
      
      if (!argv_algo) 
        {
          IS = new LocalNetwork_svd;        // implicit algorithm
        }
      else {
        if (     !strcmp("svd",      argv_algo)) IS = new LocalNetwork_svd;
        else if (!strcmp("gso",      argv_algo)) IS = new LocalNetwork_gso;
        else if (!strcmp("cholesky", argv_algo)) IS = new LocalNetwork_chol;
        else if (!strcmp("envelope", argv_algo)) IS = new LocalNetwork_env;
        else {
		std::cerr << "Unknown algorithm: " << argv_algo << endl;
		return help();
	}
      }

      if (argv_angles)
        {
          if (!strcmp("400", argv_angles))
            IS->set_gons();
          else if (!strcmp("360", argv_angles))
            IS->set_degrees();
          else{
	    std::cerr << "Unknown angle: " << argv_angles << endl;
            return help();
	  }
        }

      if (argv_covband)
        {
          std::istringstream istr(argv_covband);
          int band = -1;
          if (!(istr >> band) || band < -1) { std::cerr<<"Error: cov-band"; return help();}
          char c;
          if (istr >> c) return help();

          IS->set_xml_covband(band);
        }

    }
    catch (...) {
      throw 
        GaMaLib::Exception(T_GaMa_exception_1);
    }
    

    if (argv_latitude)
    {
        if ( !GNU_gama::IsFloat(string(argv_latitude)) ){
		std::cerr << "Error: latitude";
            return help();
	}

        //latitude = atof(argv_latitude) * M_PI / (IS->gons() ? 200 : 180);
        latitude = atof(argv_latitude) * M_PI / 180;

	correction_to_ellipsoid = true;
    }

    GNU_gama::set(&el, GNU_gama::ellipsoid_wgs84);

    if (argv_ellipsoid)
    {
        using namespace GNU_gama;
        
        gama_ellipsoid gama_el = ellipsoid(argv_ellipsoid);
        if  ( (gama_el == ellipsoid_unknown) || GNU_gama::set(&el,  gama_el) ){
		std::cerr << "Error: ellipsoid";
            return help();
	}
	    
	correction_to_ellipsoid = true;
    }

    if (argv_cpoint_x && argv_cpoint_y)
    {
        if ( !GNU_gama::IsFloat(string(argv_cpoint_x)) ){
		std::cerr << "Error: cpoint-x";
            return help();
	}

        if ( !GNU_gama::IsFloat(string(argv_cpoint_y)) ){
		std::cerr << "Error: cpoint-y";
            return help();
	}

        cpoint.set_xy(atof(argv_cpoint_x), atof(argv_cpoint_y));
    }

    if (argv_cpoint_z)
    {
        if ( !GNU_gama::IsFloat(string(argv_cpoint_z)) ){
		std::cerr << "Error: cpoint-z";
            return help();
	}

        cpoint.set_z(atof(argv_cpoint_z));
    }


    
    ifstream soubor(argv_1);
    
    {
      GKFparser gkf(IS->PD, IS->OD);
      try 
        {
          char c;
          int  n, konec = 0;
          string radek;
          do 
            {
              radek = "";
              n     = 0;
              while (soubor.get(c))
                {
                  radek += c;
                  n++;
                  if (c == '\n') break;
                }
              if (!soubor) konec = 1;
              
              gkf.xml_parse(radek.c_str(), n, konec);
            }
          while (!konec);
          
          IS->apriori_m_0(gkf.m0_apr );
          IS->conf_pr    (gkf.konf_pr);
          IS->tol_abs    (gkf.tol_abs);

          IS->update_constrained_coordinates(gkf.update_constr);
 
          if (gkf.typ_m0_apriorni)
            IS->set_m_0_apriori();
          else
            IS->set_m_0_aposteriori();
          
          description = gkf.description;
          IS->epoch = gkf.epoch;
        }
      catch (...) 
        {
          throw;         // should be added later ???
        }
    }
    
  }
  catch (const GaMaLib::ParserException& v) {
    cerr << "\n" << T_GaMa_exception_2a << "\n\n"
         << T_GaMa_exception_2b << v.line << " : " << v.text << endl;
    return 3;      
  }
  catch (const GaMaLib::Exception& v) {
    cerr << "\n" <<T_GaMa_exception_2a << "\n"
         << "\n***** " << v.text << "\n\n";
    return 2;
  }
  catch (...) 
    {
      cerr << "\n" << T_GaMa_exception_2a << "\n\n";
      throw;
      // return 3;
    }
  
  
  try {
    
    {
      cout << T_GaMa_Adjustment_of_geodetic_network << " (modified TK)        "
           << T_GaMa_version << GNU_gama::GNU_gama_version 
           << "-" << IS->algorithm()
           << " / " << GNU_gama::GNU_gama_compiler << "\n"
           << underline(T_GaMa_Adjustment_of_geodetic_network, '*') << "\n"
           << "http://www.gnu.org/software/gama/\n\n\n";
    }

    if (IS->PD.empty())
      throw GaMaLib::Exception(T_GaMa_No_points_available);
    
    if (IS->OD.clusters.empty())
      throw GaMaLib::Exception(T_GaMa_No_observations_available);
    
    try
      {
        if (!GaMaConsistent(IS->PD))
          {
            cout << T_GaMa_inconsistent_coordinates_and_angles << "\n\n\n";
          }
	// approximate coordinates
        Acord acord(IS->PD, IS->OD); //point data, observation data
	/*
	 * lib/gamalib/local/network.h
	 * lib/gamalib/local/gamadata.h
	 * lib/gnu_gama/obsdata.h
	 * lib/gamalib/local/acord.h
	 * lib/gamalib/local/median/g2d_coordinates.h
	 */

        acord.execute();
	//ReducedObservationsText(IS,&(acord.RO), cout);

	// correction to ellipsoid
        if (correction_to_ellipsoid)
        {
            ReduceToEllipsoid reduce_to_el(IS->PD, IS->OD, el, latitude, cpoint);
            LocalPoint lp = reduce_to_el.execute();
	    cout << "\nCentral point: x=" << lp.x() << " y=" << lp.y() << " z=" << lp.z() << "\n\n";
	    std::cerr<< "Central point: x=" << lp.x() << " y=" << lp.y() << " z=" << lp.z() << endl;

            ReducedObservationsToEllipsoidText(IS, reduce_to_el.getMap(), cout);
	    //LocalPoint lp = reduce_to_el.EllipsoidFunction.getCentralPoint();
        }

        ApproximateCoordinates(&acord, cout);

      }
    catch(GaMaLib::Exception e)
      {
        cerr << e.text << endl;
        return 1;
      }
    catch(...)
      {
        cerr << "Gama / Acord: approximate coordinates failed\n\n";
        return 1;
      }
    
    // cerr << IS->PD << IS->OD << "\n\n";
    
    if (IS->sum_points() == 0 || IS->sum_unknowns() == 0)
      {
        throw GaMaLib::Exception(T_GaMa_No_network_points_defined);
      }
    else
      {
        if (IS->huge_abs_terms())
          {
            OutlyingAbsoluteTerms(IS, cout);
            IS->remove_huge_abs_terms();
            cout << T_GaMa_Observatios_with_outlying_absolute_terms_removed
                 << "\n\n\n";
          }

        if (!IS->connected_network())
          cout  << T_GaMa_network_not_connected << "\n\n\n";

        NetworkDescription(description, cout);
        if (GeneralParameters(IS, cout))
          {
            int iterace = 0;
            do 
              {
                if(++iterace > 1)
                  {
                    cout << "\n         ******  " 
                         << iterace << T_GaMa_adjustment_iteration 
                         << "  ******\n\n"
                         << T_GaMa_Approximate_coordinates_replaced << "\n"
                         << underline(T_GaMa_Approximate_coordinates_replaced,
                                      '*') << "\n\n\n";
                    
                    IS->refine_approx();
                    GeneralParameters(IS, cout);
                  }
                FixedPoints     (IS, cout);
                AdjustedUnknowns(IS, cout);
              } 
            while (TestLinearization(IS, cout) && iterace < 3);
            
            ErrorEllipses        (IS, cout);
            AdjustedObservations (IS, cout);
            ResidualsObservations(IS, cout);
        
          }
        
        if (argv_obsout)
          {
            ofstream opr(argv_obsout);
            IS->project_equations(opr);
          }
        
        // implicit output
        if (!argv_txtout && !argv_xmlout) argv_xmlout = "-";

        if (argv_xmlout)
          {
            IS->set_gons();

            GNU_gama::LocalNetworkXML xml(IS);
            xml.description = description;

            if (!strcmp(argv_xmlout, "-"))
              {
                xml.write(std::cout);
              }
            else
              {
                ofstream file(argv_xmlout);
                xml.write(file);
            }
          }
        
      }
    
    delete IS; 
    return 0;   
    
  }
  catch (const GaMaLib::Exception& V) 
    {
      cout << "\n" << T_GaMa_solution_ended_with_error << "\n\n"
           << "****** " << V.text << "\n\n";
    }
  catch(const GNU_gama::Exception::adjustment& choldec)
    {
      cout << "\n" << T_GaMa_solution_ended_with_error << "\n\n"
           << "****** " << choldec.str << "\n\n";
    }
  catch(...)
    {
      cout << "\n" << T_GaMa_internal_program_error << "\n\n";
    }
  
  return 1;
}

//---------------------------------------------------------------------------

#endif







