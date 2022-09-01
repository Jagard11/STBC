######################################################################
#     PlanetShipAddon.py    v1
#                                 by USS Frontier
####
# little script to handle planet ships.  This will create a atmosphere ship and a glow to go along with the planet ship, giving more realism.
# you can set some configurable values of the glow and the atmosphere by calling the functions:
#	SetPlanetShipGlowSize(pPlanetShip, fSize)
#	SetPlanetShipGlowColor(pPlanetShip, fRed, fGreen, fBlue, fAlpha)
#	SetPlanetShipAtmosphereScript(pPlanetShip, sAtmosphereShipScript)
#	SetPlanetShipAtmosphereScaleBonus(pPlanetShip, fScaleBonus)
#	SetPlanetShipAtmosphereAngularVelocity(pPlanetShip, fX, fY, fZ)
#######
# also, you can add new planet ship classes and new atmosphere ship classes by adding their ship script name to the according list, as follows:
#	lPlanetShipClasses.append( sPlanetShipScript )  
#	lAtmosphereShipClasses.append( sAtmosphereShipScript )
###########################################################################
import App
import Foundation
import string
import loadspacehelper

###
#List of ship scripts that are planet ships
lPlanetShipClasses = ['EarthCordanilus', 'OcampaPlanet', 'AveryIII', 'BorgPrime', 'DemonPlanet', 'IcePlanet', 'KrenimHomeworld', 'MalonPlanet', 'WaterPlanet', 'Sikaris', 'Talax', 'VaadwaurHomeworld', 'Rinax', 'Tarok', 'Deltoria', 'VhnoriHomeworld', 'TranswarpHubSun', 'Veloce']


###
#List of ship scripts that are planet atmospheres
lAtmosphereShipClasses = ['AtmosphereC', 'AtmosphereO', 'AtmosphereAv', 'AtmosphereBorg', 'AtmosphereE', 'AtmosphereMP', 'AtmosphereD', 'AtmosphereV', 'AtmosphereGas', 'AtmosphereUn']

###
# Main Trigger - OBJECT_CREATED
# Checks if a planet ship was created, and if it finds one, it creates the "add-ons" for it, like the glow and App.Planet class for atmospheric effect.
# BEWARE: Glow's lifetime...
dPlanetAddons = {}
class PlanetShipTrigger(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)
	def __call__(self, pObject, pEvent):
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip:
			sShipClass = GetShipType(pShip)
			if sShipClass in lPlanetShipClasses:
				self.CreatePlanetShipAddons(pShip)
		if pObject and pEvent:
			pObject.CallNextHandler(pEvent)
	def CreatePlanetShipAddons(self, pPlanet):
		global dPlanetAddons
		pSet = pPlanet.GetContainingSet()
		
		####################################
		# variable config values 

		fGlowRadiusModifier = GetPlanetShipGlowSize(pPlanet)            #Config: Glow radius modifier
		pColor = GetPlanetShipGlowColor(pPlanet)                        #Config: glow color
		sAtmosScript = GetPlanetShipAtmosphereScript(pPlanet)           #Config: atmosphere script name
		fAtmosScaleBonus = GetPlanetShipAtmosphereScaleBonus(pPlanet)   #Config: bonus value to add to the atmosphere ship scale.
		vAngVelocity = GetPlanetShipAtmosphereAngularVelocity(pPlanet)  #Config: atmosphere angular velocity.
		#fAtmosEffectRadiusModifier = 3.0                               #Config: atmosphere effect radius modifier - UNUSED for now

		####################################		

		# create the atmosphere - a ship obj
		sAtmosName = pPlanet.GetName() + " Atmosphere"
		pAtmosphere = loadspacehelper.CreateShip(sAtmosScript, pSet, sAtmosName, "")
		pAtmosphere.SetTranslateXYZ(0.0, 0.0, 0.0)
		pAtmosphere.SetInvincible(1)
		pAtmosphere.SetHurtable(0)
		pAtmosphere.SetTargetable(0)
		pAtmosphere.SetCollisionsOn(0)
		pAtmosphere.SetAngularVelocity(vAngVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
		pAtmosphere.UpdateNodeOnly()
		pPlanet.AttachObject(pAtmosphere)
		pAtmosphere.SetScale(1)
		pAtmosphere.UpdateNodeOnly()
		fAtmosScale = (pPlanet.GetRadius()/pAtmosphere.GetRadius()) + fAtmosScaleBonus
		#print "AtmosScale:", fAtmosScale, "(", pPlanet.GetRadius(),"/",pAtmosphere.GetRadius(),"+",fAtmosScaleBonus, ")"
		pAtmosphere.SetScale(fAtmosScale)

		# create the glow - a torpedo obj
		kPoint = App.TGPoint3()
		kPoint.SetXYZ(0.0, 0.0, 0.0)
		fGlowRadius = pPlanet.GetRadius() * fGlowRadiusModifier
		#print "GlowRadius:", fGlowRadius
		pNullColor = App.TGColorA()
		pNullColor.SetRGBA(0.0, 0.0, 0.0, 0.0)
		pGlow = CreateGlowEmmiter(pPlanet, kPoint, pSet, 0, 0, 0, pNullColor, 60000.0, fGlowRadiusModifier, None, pColor)
		pPlanet.AttachObject(pGlow)

		# create a planet obj... but why? lol
		#pPlanetObj = App.Planet_Create(pPlanet.GetRadius()/2, "data/models/environment/earth.nif")
		##pPlanet.EnableCollisionsWith(pPlanetObj, 0)
		#pSet.AddObjectToSet(pPlanetObj, pPlanet.GetName() + " ClassObj")
		#vLoc = pPlanet.GetWorldLocation()
		#pPlanetObj.SetTranslateXYZ(vLoc.x, vLoc.y, vLoc.z)
		#pPlanetObj.SetAtmosphereRadius(pPlanetObj.GetAtmosphereRadius() + (pPlanet.GetRadius()*fAtmosEffectRadiusModifier) )
		#pPlanetObj.UpdateNodeOnly()
		#pPlanetObj.SetHidden(1)
		##pPlanet.AttachObject(pPlanetObj)

		dPlanetAddons[pPlanet.GetName()] = {"Glow": pGlow, "Atmosphere": pAtmosphere, }# "ClassObj": pPlanetObj}

PlanetShipTrigger = PlanetShipTrigger('Planet Ship Trigger', App.ET_OBJECT_CREATED)

#############################################################################################
### Helper Functions to setup a planet ship's  glow and atmosphere values.
#############################################################################################
dPlanetShipInfo = {}
def SetPlanetShipGlowSize(pPlanet, fSize):
	sShipClass = GetShipType(pPlanet)
	if not sShipClass in lPlanetShipClasses:
		return
	if not dPlanetShipInfo.has_key(pPlanet.GetName()):
		dPlanetShipInfo[pPlanet.GetName()] = {}
	dPlanetShipInfo[pPlanet.GetName()]["GlowSize"] = fSize

def SetPlanetShipGlowColor(pPlanet, fRed, fGreen, fBlue, fAlpha):
	sShipClass = GetShipType(pPlanet)
	if not sShipClass in lPlanetShipClasses:
		return
	if not dPlanetShipInfo.has_key(pPlanet.GetName()):
		dPlanetShipInfo[pPlanet.GetName()] = {}
	pColor = App.TGColorA()
	pColor.SetRGBA(fRed, fGreen, fBlue, fAlpha)
	dPlanetShipInfo[pPlanet.GetName()]["GlowColor"] = pColor

def SetPlanetShipAtmosphereScript(pPlanet, sAtmosphereShipScript):
	sShipClass = GetShipType(pPlanet)
	if not sShipClass in lPlanetShipClasses:
		return
	if not sAtmosphereShipScript in lAtmosphereShipClasses:
		return
	if not dPlanetShipInfo.has_key(pPlanet.GetName()):
		dPlanetShipInfo[pPlanet.GetName()] = {}
	dPlanetShipInfo[pPlanet.GetName()]["AtmosphereScript"] = sAtmosphereShipScript

def SetPlanetShipAtmosphereScaleBonus(pPlanet, fScaleBonus):
	sShipClass = GetShipType(pPlanet)
	if not sShipClass in lPlanetShipClasses:
		return
	if not dPlanetShipInfo.has_key(pPlanet.GetName()):
		dPlanetShipInfo[pPlanet.GetName()] = {}
	dPlanetShipInfo[pPlanet.GetName()]["AtmosScaleBonus"] = fScaleBonus

def SetPlanetShipAtmosphereAngularVelocity(pPlanet, fX, fY, fZ):
	sShipClass = GetShipType(pPlanet)
	if not sShipClass in lPlanetShipClasses:
		return
	if not dPlanetShipInfo.has_key(pPlanet.GetName()):
		dPlanetShipInfo[pPlanet.GetName()] = {}
	vAngVelocity = App.TGPoint3()
	vAngVelocity.SetXYZ(fX, fY, fZ)
	dPlanetShipInfo[pPlanet.GetName()]["AtmosAngVelocity"] = vAngVelocity

#############################################################################################
### Helper Functions to get a planet ship's  glow and atmosphere values.
#############################################################################################
def GetPlanetShipGlowSize(pPlanet):
	if not dPlanetShipInfo.has_key(pPlanet.GetName()):
		return 56
	return dPlanetShipInfo[pPlanet.GetName()]["GlowSize"]

def GetPlanetShipGlowColor(pPlanet):
	if not dPlanetShipInfo.has_key(pPlanet.GetName()):
		pColor = App.TGColorA()
		pColor.SetRGBA(0.9, 0.9, 0.9, 0.22)
		return pColor
	return dPlanetShipInfo[pPlanet.GetName()]["GlowColor"]

def GetPlanetShipAtmosphereScript(pPlanet):
	if not dPlanetShipInfo.has_key(pPlanet.GetName()):
		return "AtmosphereC"
	return dPlanetShipInfo[pPlanet.GetName()]["AtmosphereScript"]

def GetPlanetShipAtmosphereScaleBonus(pPlanet):
	if not dPlanetShipInfo.has_key(pPlanet.GetName()):
		return 0.001
	return dPlanetShipInfo[pPlanet.GetName()]["AtmosScaleBonus"]

def GetPlanetShipAtmosphereAngularVelocity(pPlanet):
	if not dPlanetShipInfo.has_key(pPlanet.GetName()):
		vAngVelocity = App.TGPoint3()
		vAngVelocity.SetXYZ(0, 0, -0.03)
		return vAngVelocity
	return dPlanetShipInfo[pPlanet.GetName()]["AtmosAngVelocity"]

########################################################################################

###
# OBJECT_DESTROYED trigger to properly handle the destruction of a planet ship, cleaning things up.
class PlanetShipDestroyedTrigger(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)
	def __call__(self, pObject, pEvent):
		global dPlanetAddons
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip:
			sShipClass = GetShipType(pShip)
			if sShipClass in lPlanetShipClasses:
				if dPlanetAddons.has_key(pShip.GetName()):
					#pPlanetObj = dPlanetAddons[pShip.GetName()]["ClassObj"]
					#pSet = pPlanetObj.GetContainingSet()
					#pSet.RemoveObjectFromSet(pPlanetObj.GetName())
					del dPlanetAddons[pShip.GetName()]
		if pObject and pEvent:
			pObject.CallNextHandler(pEvent)

PlanetShipDestroyedTrigger('Planet Ship Destroyed Trigger', App.ET_OBJECT_DESTROYED)


###################################################################
# Helper Functions
#########################################################
def GetShipType(pShip):
	if pShip.GetScript():
		return string.split(pShip.GetScript(), '.')[-1]
	return None

def CreateGlowEmmiter(pParent,kPoint,pSet,fGlowRate,fMinGlowSize,fMaxGlowSize,pGlowColor=None,fLifetime=60.0,fCoreSize=4.0,pFlareColor=None,pCoreColor=None,fCoreRotatingSpeed=0,iNumberOfFlares=0,fFlareSize=0.0,fFlareLifetime=0.01):
	global GlowRate, GlowMinSize, GlowMaxSize, GlowColor, CoreSize, FlareColor, CoreColor, CoreRotatingSpeed, NumberOfFlares, FlareSize, FlareLifetime
	GlowRate = fGlowRate
	MinGlowSize = fMinGlowSize
	MaxGlowSize = fMaxGlowSize
	CoreSize = fCoreSize
	if pGlowColor:
		GlowColor = pGlowColor
	if pFlareColor:
		FlareColor = pFlareColor
	if pCoreColor:
		CoreColor = pCoreColor
	CoreRotatingSpeed = fCoreRotatingSpeed
	NumberOfFlares = iNumberOfFlares
	FlareSize = fFlareSize
	FlareLifetime = fFlareLifetime
	Vec = App.TGPoint3()
	Vec.SetXYZ(kPoint.x, kPoint.y, kPoint.z)
	pTorp = App.Torpedo_Create(__name__, Vec)
	pTorp.SetTarget(App.NULL_ID)
	pTorp.SetParent(pParent.GetObjID())
	pTorp.SetCollisionFlags(App.ObjectClass.CFB_NO_COLLISIONS)
	TorpName = str(pParent.GetName())+" Glow Emmiter"
	pSet.AddObjectToSet(pTorp, TorpName)
	pTorp.SetLifetime(fLifetime)
	pTorp.UpdateNodeOnly()
	return pTorp

###############################################################################
### Glow Emmiter Variables ###############
# these are changed before creating a glow emmiter, don't change them here.
CoreSize = 4.0
GlowRate = 6.0                 #
GlowMinSize = 100.0            #  Just some default values, incase they aren't set before this emmiter is created.  
GlowMaxSize = 300.0            #
GlowColor = App.TGColorA()
GlowColor.SetRGBA(254.0 / 255.0, 0.0 / 255.0, 86.0 / 255.0, 0.3700000)
CoreColor = App.TGColorA()
CoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
FlareColor = App.TGColorA()
FlareColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 0.800000)
CoreRotatingSpeed = 0
NumberOfFlares = 0
FlareSize = 0.0
FlareLifetime = 0.01

def Create(pTorp):
	global GlowRate, GlowMinSize, GlowMaxSize, GlowColor, CoreSize, FlareColor, CoreColor, CoreRotatingSpeed, NumberOfFlares, FlareSize, FlareLifetime
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					CoreColor,
					CoreSize,
					CoreRotatingSpeed,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					GlowColor,
					GlowRate,	
					GlowMinSize,	 
					GlowMaxSize,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					FlareColor,										
					NumberOfFlares,		
					FlareSize,		
					FlareLifetime)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.001)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)
	return(0)
def GetLaunchSpeed():
	return(0.0)
def GetLaunchSound():
	return("")
def GetPowerCost():
	return(0.0)
def GetName():
	return("Glow Emmiter")
def GetDamage():
	return 0.0
def GetGuidanceLifetime():
	return 0.0
def GetMaxAngularAccel():
	return 0.0
#################################################################################################