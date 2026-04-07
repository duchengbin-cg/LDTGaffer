import Gaffer
import GafferScene
import GafferUI
import os
import pathlib

print ("LDTGAFFER:startup:gui:nodes")

def __LDTShaderBallScene() :

	return Gaffer.Reference( "LDTShaderBallScene" )

def __LDTShaderBallScenePostCreator( node, menu ) :

	# Windows-safe reference loading:
	# - Do not hardcode slashes or assume a Linux root.
	# - Prefer the plugin root from env var `LDTGaffer` (fallback to `LDTGAFFER`).
	# - Build an absolute path and pass a POSIX-style string to `node.load()`.
	pluginRoot = os.environ.get( "LDTGaffer" ) or os.environ.get( "LDTGAFFER" )
	relative = pathlib.Path( "resources" ) / "boxes" / "LDTShaderBallScene.grf"

	absolutePath = None
	if pluginRoot:
		absolutePath = (pathlib.Path( pluginRoot ) / relative).resolve()
	else:
		# Fallback: try GAFFER_REFERENCE_PATHS (platform specific separator)
		referencePaths = os.environ.get( "GAFFER_REFERENCE_PATHS", "" )
		for p in [x for x in referencePaths.split( os.pathsep ) if x]:
			candidate = (pathlib.Path( p ) / "LDTShaderBallScene.grf").resolve()
			if candidate.exists():
				absolutePath = candidate
				break

	if absolutePath is None:
		raise RuntimeError(
			"Cannot locate LDTShaderBallScene.grf. "
			"Please set env var `LDTGaffer` (preferred) or `GAFFER_REFERENCE_PATHS`."
		)

	node.load( absolutePath.as_posix() )

def __Phong ():
	shader_node = GafferScene.OpenGLShader( "Phong" )
	shader_node.loadShader( "Phong" )
	return shader_node

nodeMenu = GafferUI.NodeMenu.acquire( application )

nodeMenu.append(
	path = "/LDT/primitives/LDTShaderBallScene",
	nodeCreator = __LDTShaderBallScene,
	postCreator = __LDTShaderBallScenePostCreator,
	searchText = "LDTShaderBallScene"
)

nodeMenu.append(
	path = "/LDT/OpenGL/Phong",
	nodeCreator = __Phong,
	searchText = "Phong"
)
