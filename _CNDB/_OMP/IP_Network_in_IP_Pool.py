# -*- coding: utf-8 -*-
# Copyright (C) 2014 Dr. Ralf Schlatterbeck All rights reserved
# Reichergasse 131, A--3411 Weidling, Austria. rsc@runtux.com
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
#    CNDB.OMP.IP_Network_in_IP_Pool
#
# Purpose
#    Model IP networks in an IP pool
#
# Revision Dates
#     3-Jul-2014 (RS) Creation
#    16-Sep-2014 (CT) Add `left.rev_ref_attr_name`
#    ««revision-date»»···
#--

from   __future__  import absolute_import, division, print_function, unicode_literals

from   _MOM.import_MOM        import *
from   _CNDB                  import CNDB
import _CNDB._OMP

import _CNDB._OMP.IP_Network
import _CNDB._OMP.IP_Pool

_Ancestor_Essence = CNDB.OMP.Link2

class IP_Network_in_IP_Pool (_Ancestor_Essence) :
    """IP networks in an IP pool."""

    is_partial  = True

    class _Attributes (_Ancestor_Essence._Attributes) :

        _Ancestor = _Ancestor_Essence._Attributes

        ### Primary attributes

        class left (_Ancestor.left) :
            """IP network."""

            role_type          = CNDB.OMP.IP_Network
            rev_ref_attr_name  = "ip_network"
            max_links          = 1

        # end class left

        class right (_Ancestor.right) :
            """IP pool."""

            role_type          = CNDB.OMP.IP_Pool

        # end class right

    # end class _Attributes

# end class IP_Network_in_IP_Pool

if __name__ != "__main__" :
    CNDB.OMP._Export ("*")
### __END__ CNDB.OMP.IP_Network_in_IP_Pool
