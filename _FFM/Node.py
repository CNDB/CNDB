# -*- coding: iso-8859-15 -*-
# Copyright (C) 2012 Mag. Christian Tanzer All rights reserved
# Glasauergasse 32, A--1130 Wien, Austria. tanzer@swing.co.at
# #*** <License> ************************************************************#
# This module is part of the package FFM.
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
#    FFM.Node
#
# Purpose
#    Model a node of FFM
#
# Revision Dates
#     6-Mar-2012 (CT) Creation
#    19-Jul-2012 (RS) Add `position`
#    20-Jul-2012 (RS) `Node` no longer inherits from `PAP.Subject`
#    18-Sep-2012 (RS) Add `owner` and `manager`
#    ��revision-date�����
#--

from   __future__  import absolute_import, division, print_function, unicode_literals

from   _MOM.import_MOM        import *
from   _MOM._Attr.Position    import A_Position
from   _FFM                   import FFM
from   _GTW._OMP._PAP         import PAP, Person, Subject

import _FFM.Entity

_Ancestor_Essence = FFM.Object

class Node (_Ancestor_Essence) :
    """Model a node of FFM"""

    class _Attributes (_Ancestor_Essence._Attributes) :

        _Ancestor = _Ancestor_Essence._Attributes

        class name (A_String) :
            """Name of the node"""

            kind               = Attr.Primary
            max_length         = 64
            ignore_case        = True
            completer          = Attr.Completer_Spec  (2, Attr.Selector.primary)

        # end class name

        class manager (A_Id_Entity) :
            """Manager of the node"""

            kind               = Attr.Required
            P_Type             = PAP.Person

        # end class manager

        class owner (A_Id_Entity) :
            """Owner of the node, defaults to manager"""

            kind               = Attr.Optional
            Kind_Mixins        = (Attr.Computed_Mixin, )
            P_Type             = PAP.Subject

            def computed (self, obj) :
                if obj :
                    return obj.manager
            # end def computed

        # end class owner

        class position (A_Position) :
            """GPS position and optional height of the node"""

            kind               = Attr.Optional

        # end class position

        class map_p (A_Boolean) :
            """Show in map."""

            kind               = Attr.Optional
            default            = True

        # end class map_p

    # end class _Attributes

# end class Node

if __name__ != "__main__" :
    FFM._Export ("*")
### __END__ FFM.Node
