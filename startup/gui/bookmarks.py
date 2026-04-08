import os

import GafferUI

print ("LDTGAFFER:startup:gui:bookmarks")

bookmarks = GafferUI.Bookmarks.acquire( application )

# Windows-safe plugin root:
# - Prefer `LDTGaffer`
# - Fallback to legacy `LDTGAFFER`
_ldtRoot = os.environ.get( "LDTGaffer" ) or os.environ.get( "LDTGAFFER" ) or os.path.expandvars( "$LDTGAFFER" )
bookmarks.add( "LDTGAFFER", _ldtRoot )
bookmarks.add( "LDTGAFFER_EXTENSIONS", os.path.expandvars( "$GAFFER_EXTENSION_PATHS" ) )
bookmarks.add( "LDTGAFFER_REFERENCE", os.path.expandvars( "$GAFFER_REFERENCE_PATHS" ) )
bookmarks.add( "GAFFER_EXAMPLES", os.path.expandvars( "$GAFFER_EXAMPLES" ) )

bookmarks.setDefault( _ldtRoot )
