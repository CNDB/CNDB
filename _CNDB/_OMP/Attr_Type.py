# -*- coding: utf-8 -*-
# Copyright (C) 2012-2014 Mag. Christian Tanzer All rights reserved
# Glasauergasse 32, A--1130 Wien, Austria. tanzer@swing.co.at
# #*** <License> ************************************************************#
# This module is part of the package CNDB.OMP.
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This module is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this module. If not, see <http://www.gnu.org/licenses/>.
# #*** </License> ***********************************************************#
#
#++
# Name
#    CNDB.OMP.Attr_Type
#
# Purpose
#    Define attribute types for package CNDB
#
# Revision Dates
#    14-Mar-2012 (CT) Creation
#    20-Aug-2012 (RS) Add `A_TX_Power`
#    27-Aug-2012 (RS) Add import of `math.log`
#    22-Sep-2012 (RS) Remove `A_Wireless_Protocol`
#    20-Nov-2012 (CT) Fix `A_TX_Power._from_string`, add `_default_unit`
#    05-Dec-2012 (RS) Add `A_Polarization`
#    17-Dec-2012 (CT) Add `A_Wireless_Mode`
#    17-Dec-2012 (RS) Fix unit dBW, use decadic logarithm for dB
#     5-Jun-2013 (CT) Use `is_attr_type`, not home-grown code
#     7-Aug-2013 (CT) Add `A_Polarization.C_Type`
#    20-Jun-2014 (RS) Add `A_Netmask_Interval` and derivatives
#    23-Jun-2014 (RS) Derive `A_Netmask_Interval` from `A_Int_Interval`
#                     `A_Int_Interval_C` doesn't currently work
#    24-Jun-2014 (RS) Undo latest change now that `A_Int_Interval_C` works
#     3-Jul-2014 (RS) Add `_A_IP_Netmask_`, `_A_IP_Quota_` and derivatives,
#                     model _A_IP_Netmask_Interval_ after same scheme
#    ««revision-date»»···
#--

from   __future__  import absolute_import, division, print_function, unicode_literals

from   math                     import log

from   _MOM.import_MOM          import *
from   _MOM.import_MOM          import _A_Unit_, _A_Float_, _A_Named_Value_
from   _CNDB                    import CNDB
import _CNDB._OMP
from   _TFL.I18N                import _
from _MOM._Attr.Number_Interval import A_Int_Interval_C

import _CNDB._OMP.Wireless_Mode

class A_Polarization (_A_Named_Value_) :
    """Antenna polarisation"""

    ( horizontal
    , vertical
    , left_circular
    , right_circular
    )            = range (4)

    example      = "vertical"
    typ          = "Antenna Polarization"
    P_Type       = int
    C_Type       = A_Int
    Table        = \
        { "horizontal"     : horizontal
        , "vertical"       : vertical
        , "left circular"  : left_circular
        , "right circular" : right_circular
        }

# end class A_Polarization

class A_TX_Power (_A_Unit_, _A_Float_) :
    """Transmit Power specified in multiples of W or dBW, dBm,
       converted to dBm.
    """

    typ             = _ ("TX Power")
    needs_raw_value = True
    _default_unit   = "dBm"
    _unit_dict      = dict \
        ( mW        = 1
        ,  W        = 1.E3
        , kW        = 1.E6
        , MW        = 1.E9
        , dBm       = 1
        , dBmW      = 1 # alias for dBm, see http://en.wikipedia.org/wiki/DBm
        , dBW       = 1
        )

    def _from_string (self, s, obj, glob, locl) :
        v    = self.__super._from_string (s, obj, glob, locl)
        pat  = self._unit_pattern
        unit = ""
        if pat.search (s) :
            unit = pat.unit
        if unit.startswith ('dB') :
            if unit == 'dBW' :
                v += 30
        else :
            v = log (v) / log (10) * 10.
        return v
    # end def _from_string

# end class A_TX_Power

class A_Wireless_Mode (MOM.Attr._A_Named_Object_) :
    """Wireless mode to use for %(ui_type_name)s"""

    example     = u"Ad_Hoc"
    typ         = "wl-mode"
    Table       = CNDB.OMP.Wireless_Mode.Table

# end class A_Wireless_Mode

class _A_IP_Netmask_ (A_Int) :
    """IP Network mask."""

    min_value   = 0

# end class _A_IP_Netmask_

class A_IP4_Netmask (_A_IP_Netmask_) :

    max_value   = 32

# end class A_IP4_Netmask

class A_IP6_Netmask (_A_IP_Netmask_) :

    max_value   = 32

# end class A_IP6_Netmask

class _A_IP_Quota_ (_A_IP_Netmask_) :
    """Quota for reservation from an IP_Network."""

    desc         = \
        """Quota is specified as a netmask. Reserved networks
           are summed up and it is checked if the sum reaches
           the size of a network with the given netmask. If
           this netmask is reached no new reservations are
           permitted.
        """

# end class _A_IP_Quota_

class A_IP4_Quota (_A_IP_Quota_, A_IP4_Netmask) : pass
class A_IP6_Quota (_A_IP_Quota_, A_IP6_Netmask) : pass

class _A_IP_Netmask_Interval_ (A_Int_Interval_C) :
    """Interval of network masks (upper limit defaults to lower limit)"""

    _Overrides = dict \
        ( start  = dict
            ( min_value = 0
            )
        , finish = dict
            ( min_value = 0
            )
        )

# end class _A_IP_Netmask_Interval_

class A_IP4_Netmask_Interval (_A_IP_Netmask_Interval_) :

    _Overrides = dict \
        ( start  = dict
            ( max_value = 32
            )
        , finish = dict
            ( max_value = 32
            )
        )

# end class A_IP4_Netmask_Interval

class A_IP6_Netmask_Interval (_A_IP_Netmask_Interval_) :

    _Overrides = dict \
        ( start  = dict
            ( max_value = 128
            )
        , finish = dict
            ( max_value = 128
            )
        )

# end class A_IP6_Netmask_Interval

__all__ = tuple (k for (k, v) in globals ().iteritems () if is_attr_type (v))

if __name__ != "__main__" :
    CNDB.OMP._Export ("*")
### __END__ CNDB.OMP.Attr_Type
