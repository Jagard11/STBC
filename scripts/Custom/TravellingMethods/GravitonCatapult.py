# prototype custom travelling method plugin script, by USS Frontier

#######################################
#######################################
###     GENERAL ATTRIBUTES
#######################################
#######################################
########
# name of this travelling method 
########
sName = "Graviton Catapult"

########
# if this travelling method is ship based. Warp for example is ship based, that means that any ship equipped with it can
# engage it anytime she wants. 
# Some travelling methods, like wormholes, are not ship based, that means ships need to enter the wormhole to travel.
########
bIsShipBased = 0


########################################
########################################
###     TRAVELER ATTRIBUTES
########################################
########################################
########
# if this travelling method can be used to tow ships.
########
bCanTowShips = 0

########
# path and file name to engine degradation sound alert
########
sDegradationSoundFile = "scripts\\Custom\\GalaxyCharts\\Sounds\\DegradationAlert.wav"

########
# if this travelling method should show starstreaks while travelling
# (starstreaks options setup in Galaxy Charts UMM Configuration menu)
########
bUseStarstreaks = 0

########
# if a ship can drop out of travel, while travelling.
########
bCanDropOut = 0

########
# if a ship can change it's destination while travelling.
########
bCanChangeCourse = 0

########
# if a ship can change it's speed while travelling.
########
bCanChangeSpeed = 0

########
# Phrase to show when ship is engaging this travelling method, the destination name is automatically added to the end
# so, like in warp, for example, it'll be "Warping to Kronos..."
########
sGoingTo = "Travelling to"

########
# Phrase to show when the ship drops out of travel (while travelling)
########
sDropOut = "Dropped out of travel..."

########
# if this travelling method can trigger RDFs when a ship exits travel.
########
bCanTriggerRDF = 1

########
# The following 2 floats define the range of values that can be set as the travelling speed of a ship using this travelling method.
# For warp, for example, it's from 1 to 9.99
# It's an arbitrary scale/range. The actual conversion to a exact speed unit (km/h) is done in the method ConvertSpeedAmount located below.
########
fMinimumSpeed = 1.0
fMaximumSpeed = 10.0

########
# A float, representing the radius (in kilometers) from a launch coordinate which a ship can be able to activate this non-ship-based travelling method
########
fLaunchRadius = 0.3

########
# This attribute specifies the travelling restrictions for this travelling method. Systems can be set to be restricted to this and/or other travelling
# methods in its system plugin (region plugin part)
# The value of this attribute must be a integer, one of the ones contained in the following enum (fyi, 'RS' is abbreviation of 'restricted system'):
# 0 = No restriction
# 1 = can only be used between RSs  (when in a RS to travel to another RS)
# 2 = travel from anywhere to a RS, but can only return to the system where ship came from
# 3 = travel from anywhere to a RS, and can return to any system
########
iRestrictionFlag = 0


###########################################
###########################################
####       TRAVELER METHODS
###########################################
###########################################
import App
import string
import MissionLib
import math
import Custom.GalaxyCharts.GalaxyLIB

########
# Method to check if the ship is equipped with this travelling method.
# Must return 1 if it has it, 0 if it does not.
# NOTE: this function is not used as a method of the Travel class as are the other functions here.
#       this is actually used just like a helper for the Travel Manager.
########
def IsShipEquipped(pShip):
	return 0


########
# Method to check if the ship can travel.
# Must return 1 if it can, otherwise return a string(reason why the ship couldn't travel)
########
def CanTravel(self):
	pShip = self.GetShip()
	vLC = self.GetLaunchCoordinates()
	if vLC == None:
		return "No launch coordinates are set..."
	pCatapult = GetCatapultShipForLC(vLC, self.Ship.GetContainingSet())
	if pCatapult == None:
		return "Couldn't find the catapult ship to go with current launch coordinates..."


	###
	###  CHECK IF CATAPULT CAN BE USED (not damaged/disabled, etc)
	### 
	pTractors = pCatapult.GetTractorBeamSystem()
	if pTractors != None:
		if pTractors.GetCondition() <= 0.0:
			return "Graviton Beam system of selected catapult is destroyed..."
		if pTractors.IsDisabled() == 1:
			return "Graviton Beam system of selected catapult is disabled..."
		if pTractors.IsOn() == 0:
			return "Graviton Beam system of selected catapult is offline..."
	else:
		return "Couldn't acquire Graviton Beam system of selected catapult..."

	### 
	###  CHECK IF SHIP FITS THE CATAPULT OPENING
	###
	pBeam1 = MissionLib.GetSubsystemByName(pCatapult, "Graviton Beam 1")
	if pBeam1 == None:
		return "Couldn't acquire catapult's "+pCatapult.GetName()+" Graviton Beam 1..."
	
	vDiff = App.TGPoint3()
	vDiff.Set(pBeam1.GetWorldLocation())
	vDiff.Subtract(pCatapult.GetWorldLocation())
	fGoodRadius = vDiff.Length()
	# before doing the major calculations for width and heigth tests, check if the ship is long enough to pass the catapult while at the launch coord.
	# because if she is that long, she won't be able to use this.
	if Custom.GalaxyCharts.GalaxyLIB.DistanceCheck(pShip, pCatapult) <= pShip.GetRadius():
		return "Ship is to long to use the graviton catapult..."
	lCoordPairs = []
	# first we add the 4 extremities of the circles following the axis
	lCoordPairs.append(  (0, fGoodRadius)  )
	lCoordPairs.append(  (0, -fGoodRadius)  )
	lCoordPairs.append(  (fGoodRadius, 0)  )
	lCoordPairs.append(  (-fGoodRadius, 0)  )
	# then we calculate the coordinate of each segment point, using one of the following degrees list: (BTW, exclude 0º and 90º degrees)
	# A)  [15.0, 30.0, 45.0, 60.0, 75.0]
	# B)  [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0]  -> more precision, more calculations
	for fDegrees in [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0]:
		fRadians = Custom.GalaxyCharts.GalaxyLIB.ConvertDegreesToRadians(fDegrees)
		fOpCat = math.sin(fRadians) * fGoodRadius     # Opposite catetum -> Y axis offset
		fAdjCat = math.cos(fRadians) * fGoodRadius    # Adjacent catetum -> X axis offset

		# Now we get each pair with these values, since around the circle they are all simetric.
		# this way we save much more time and system resources than making all the calculations for them as well.
		lCoordPairs.append(  (fAdjCat, fOpCat)  )
		lCoordPairs.append(  (-fAdjCat, -fOpCat)  )
		lCoordPairs.append(  (-fAdjCat, fOpCat)  )
		lCoordPairs.append(  (fAdjCat, -fOpCat)  )
	# finally we get the real 3D coords based on the coord pairs acquired above. Then we check passes the allowed radius.
	for tCoordPair in lCoordPairs:
		vPos = App.TGPoint3()
		vPos.Set(pShip.GetWorldLocation())
		vAddX = pShip.GetWorldRightTG()
		vAddX.Unitize()
		vAddX.Scale( tCoordPair[0] )
		vAddY = pShip.GetWorldUpTG()
		vAddY.Unitize()
		vAddY.Scale( tCoordPair[1] )
		vPos.Add( vAddX )
		vPos.Add( vAddY )		

		vPosStart = App.TGPoint3()
		vPosStart.Set( vPos )
		vStartOffset = pShip.GetWorldForwardTG()
		vStartOffset.Scale(10.0)
		vPosStart.Add( vStartOffset )

		vPosEnd = App.TGPoint3()
		vPosEnd.Set( vPos )
		vEndOffset = pShip.GetWorldBackwardTG()
		vEndOffset.Scale(10.0)
		vPosEnd.Add( vEndOffset )

		if pShip.LineCollides(vPosStart, vPosEnd):
			return "Ship is to wide or tall to use the graviton catapult..."

	return 1

########
# Method to check if the ship can continue travelling (she's travelling, yeah)
# must return 1 if she can, 0 if she can't travel anymore (thus will forcibly drop out).
########
def CanContinueTravelling(self):
	return 1

########
# Method to get the direction to turn the ship towards for her to travel. 
# return can be:
# None -> ship will travel blindly. That is, without turning to face a particular direction (possibly dodging potential obstacles)
# TGPoint3  -> the direction vector to turn towards.
# [TGPoint3, TGPoint3]  -> a list of direction vectors ( [forward, up] )  to turn and align towards.
########
def GetEngageDirection(self):
	vLC = self.GetLaunchCoordinates()
	pCatapult = GetCatapultShipForLC(vLC, self.Ship.GetContainingSet())
	if pCatapult == None:
		return None
	
	# raw, ugly check to see if our ship is facing the correct orientation...
	lShipDirs = [self.Ship.GetWorldForwardTG(), self.Ship.GetWorldUpTG()]
	lCatapultDirs = [pCatapult.GetWorldForwardTG(), pCatapult.GetWorldUpTG()]
	fPrecision = 0.03   # believe me, we need this.
	for i in range(2):
		v = lShipDirs[i]
		vC = lCatapultDirs[i]
		if abs(v.x - vC.x) < fPrecision:
			if abs(v.y - vC.y) < fPrecision: 
				if abs(v.z - vC.z) < fPrecision:
					#print "finally ok to travel with catapult"
					return None

	#print "nope, cant travel yet... ", v.x - vC.x , v.y - vC.y , v.z - vC.z

	return lCatapultDirs

########
# Method to do travelling method specific stuff before the ship engages travel. At this point, ship is already due to engage travel, that is,
# passed the checks to see if she can travel and is starting the travelling procedures.
# return value is not important.
########
def PreEngageStuff(self):
	return

########
# Method to do travelling method specific stuff before the ship exits travel. This happens right before the ship changes set to enter the its destination.
# return value is not important.
########
def PreExitStuff(self):
	return

########
# Method to setup the GFX effect sequences, and return them in the order:
# 1º entering travel sequence
# 2º during travel sequence
# 3º exiting travel sequence
########
def SetupSequence(self):
	# you can use this function as an example on how to create your own '.SetupSequence(self)' method for your
	# custom travelling method.
	
	# note that the only REQUIRED part is what the function return and the single parameter 'pTravel', so go to the end of the function
	# for more info

	################################################################################
	# from here below it is just the custom code to create the custom sequences
	# NOT-REQUIRED  STUFF
	# modify accordingly for your sequences
	################################################################################

	
	### 
	###  ENGAGING SEQ:
	###
	###  use: ship.TurnTowardOrientation(catapult.GetWorldForwardTG(), catapult.GetWorldUpTG())
	###	to make the ship face the right direction, use the value it returns as the time to wait until next action
	###
	###  turn on self-catapult top and bottom tractors (maybe model effect), keep them rotating, and right after start the forcefield
	###
	###  disable collision for ship
	###
	###  turn each of the 8 tractors one by one at the ship, and at each fire increase the effect of the "bubble" around the ship (from no bubble until
	###  very strong and noticeable bubble)
	###            OR
	###  turn all tractors at once on the ship, and create the bubble effect in it.
	###
	###  after some time, MAYBE flash the ship (like nacelle flash), boost the ship forward, wait some small time, play warp flash (or similar flash)
	###  and that ends it...
	###
	###  
	###  DURING SEQ:
	###  	 ** maybe make a one-time only action in this sequence, to happen when the ship just entered DURING phase, and use it to delete and finalize
	###       the models/things used in the engaging sequence
	###  
	###  EXITING SEQ:
	###    dunno yet... maybe leave it like warp.
	###

	pWS = self.TravelerSequence	
	
	sCustomActionsScript = "Custom.GalaxyCharts.WarpSequence_Override"
	
	pShip = pWS.GetShip()
	pPlayer = App.Game_GetCurrentPlayer()
	vLC = self.GetLaunchCoordinates()
	pCatapult = GetCatapultShipForLC(vLC, self.Ship.GetContainingSet())

	if pShip == None:
		return [None, None, None]
	if pCatapult == None:
		self.Logger.LogError("Couldn't get catapult ship for current launch coordinates... (setup sequence)")
		return [None, None, None]
	pSet = pShip.GetContainingSet()

	pWarpSet = pWS.Travel.GetTravelSetToUse()

	pEngageSeq = App.TGSequence_Create()

	#pDuringSeq = App.TGSequence_Create()

	pExitSeq = App.TGSequence_Create()

	##################  entering seq ##################	


	
	################################
	# WARNING: CLEARING CATAPULT SHIP AI
	# and for now, we are not restoring it later.
	pCatapult.ClearAI()
	# this is needed so that I can control here by code her tractor beams to fire at the ship
	################################

	# first make the ship face the right direction
	fEntryDelayTime = 0

	if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
		# if it's the player start the cinematic mode
		fEntryDelayTime = fEntryDelayTime + 2.0

		# Force a noninteractive cinematic view in space..
		pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
		pEngageSeq.AddAction(pCinematicStart, None)

		pCutsceneBegin = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pSet.GetName())
		pEngageSeq.AddAction(pCutsceneBegin, pCinematicStart)

		pSetupCam = App.TGScriptAction_Create(__name__, "SetupCamera", pSet, pCatapult, pShip)
		pEngageSeq.AddAction(pSetupCam, pCutsceneBegin)

		fTimeToMove = fEntryDelayTime + 18.1
		fCount = 1.0
		while fCount < fTimeToMove:
			#little workaround, macgyver style, to stop the moving of the camera when it reaches a certain point, 
			#but continue updating its orientation
			if fCount >= (fTimeToMove - 6.0):
				pMoveCamAction = App.TGScriptAction_Create(__name__, "MoveCamera", pSet, pCatapult, pShip, 0.0)
			else:
				pMoveCamAction = App.TGScriptAction_Create(__name__, "MoveCamera", pSet, pCatapult, pShip, 0.035)
			pEngageSeq.AddAction(pMoveCamAction, pSetupCam, fCount)
			fCount = fCount + 0.01
			if fCount >= fTimeToMove:
				break

		pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
		pEngageSeq.AddAction(pDisallowInput, pSetupCam)

	pTurnShip = App.TGScriptAction_Create(__name__, "PositionShip", pShip, vLC)
	pEngageSeq.AddAction(pTurnShip, None)

	print "Entry Delay for ship", pShip.GetName(), "is", fEntryDelayTime

	# then toggle the top/bottom tractor beam effects (the ones that fire in each other in the catapult)
	pTETE = App.TGScriptAction_Create(__name__, "ToggleEdgeTractorEffects", pCatapult, 1)
	pEngageSeq.AddAction(pTETE, pTurnShip, fEntryDelayTime + 1)

	# then toggle the forcefield that appears in the middle of the catapult
	pTF = App.TGScriptAction_Create(__name__, "ToggleForcefield", pCatapult, 1)
	pEngageSeq.AddAction(pTF, pTETE, 1.5)

	# disable collisions for ship
	pTSC = App.TGScriptAction_Create(__name__, "ToggleShipCollisions", pShip, 0)
	pEngageSeq.AddAction(pTSC, pTF)

	# then add the 8-stage graviton beam firing and bubble effect in a row
	pLastTBEAction = pTSC
	for i in range(8):
		pTGB = App.TGScriptAction_Create(__name__, "ToggleGravitonBeams", pCatapult, pShip, i+1)
		pEngageSeq.AddAction(pTGB, pLastTBEAction, 1.0)
		pTBE = App.TGScriptAction_Create(__name__, "ToggleBubbleEffect", pShip, i+1)
		pEngageSeq.AddAction(pTBE, pTGB)
		pLastTBEAction = pTBE

	# MAYBE FLASH THE SHIP SOMEHOW HERE
	# ALSO MAYBE MAKE SOME "KABUM" SOUND HERE

	# boost the ship at high speed
	pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 1, 100.0)
	pEngageSeq.AddAction(pBoostAction, pLastTBEAction, 2.0)	
	
	# Create a warp flash. Better if the flash is right where the catapult is located (meaning when the ship passes by the forcefield, warp flashes)
	pFlashAction1 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
	pEngageSeq.AddAction(pFlashAction1, pBoostAction, 0.6)

	# Hide the ship.
	pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 1)
	pEngageSeq.AddAction(pHideShip, pFlashAction1)

	# shutdown graviton beams.
	pCloseGB = App.TGScriptAction_Create(__name__, "ToggleGravitonBeams", pCatapult, pShip, 0)
	pEngageSeq.AddAction(pCloseGB, pHideShip)
	
	# shutdown bubble effect
	pCloseBE = App.TGScriptAction_Create(__name__, "ToggleBubbleEffect", pShip, 0)
	pEngageSeq.AddAction(pCloseBE, pCloseGB)

	# get it back into normal speed
	pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 0, 1.0)
	pEngageSeq.AddAction(pUnBoostAction, pCloseBE)

	# now we start to shutdown the edge tractor effects
	pCloseETE = App.TGScriptAction_Create(__name__, "ToggleEdgeTractorEffects", pCatapult, 0)
	pEngageSeq.AddAction(pCloseETE, pUnBoostAction, 3.0)

	# then shutdown the forcefield effect
	pCloseF = App.TGScriptAction_Create(__name__, "ToggleForcefield", pCatapult, 0)
	pEngageSeq.AddAction(pCloseF, pCloseETE)

	# wait some time to re-enable ship collisions and finish the engaging sequence.
	pEnableSC = App.TGScriptAction_Create(__name__, "ToggleShipCollisions", pShip, 1)
	pEngageSeq.AddAction(pEnableSC, pCloseF, 2.0)

	# and finally finish our cutscene cam. Traveler system takes care of finishing the cinematic mode and restoring control.
	pCutsceneEnd = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pSet.GetName())
	pEngageSeq.AddAction(pCutsceneEnd, pEnableSC)

	############### exiting begins ########

	# Get the destination set name from the module name, if applicable.
	pcDest = None
	pcDestModule = pWS.GetDestination()
	if (pcDestModule != None):
		pcDest = pcDestModule[string.rfind(pcDestModule, ".") + 1:]
		if (pcDest == None):
			pcDest = pcDestModule

	try:
		import Custom.NanoFXv2.NanoFX_Lib
		sRace = Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pShip)
		pWS.Logger.LogString("Got species of ship from NanoFXv2")
	except:
		sRace = ""

	# Add the actions for exiting warp only if the destination set exists.
	if(pWS.GetDestinationSet() != None):
		if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
			# Force a noninteractive cinematic view in space..
			pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
			pExitSeq.AddAction(pCinematicStart, None)

			pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
			pExitSeq.AddAction(pDisallowInput, pCinematicStart)

			# Add actions to move the camera in the destination set to watch the placement,
			# so we can watch the ship come in.
			# Initial position is reverse chasing the placement the ship arrives at.
			pCameraAction4 = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pcDest, pPlayer.GetName())
			pExitSeq.AddAction(pCameraAction4, pDisallowInput)
	
		# Hide the ship.
		pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 1)
		pExitSeq.AddAction(pHideShip, None)

		# Create the warp flash.
		pFlashAction2 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
		pExitSeq.AddAction(pFlashAction2, pHideShip, 0.7)

		# Un-Hide the ship
		pUnHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 0)
		pExitSeq.AddAction(pUnHideShip, pFlashAction2, 0.2)

		# Give it a little boost
		pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 1, 100.0)
		pExitSeq.AddAction(pBoostAction, pUnHideShip, 0.1)

		# Play the vushhhhh of exiting warp
		pWarpSoundAction2 = App.TGScriptAction_Create(sCustomActionsScript, "PlayWarpSound", pWS, "Exit Warp", sRace)
		pExitSeq.AddAction(pWarpSoundAction2, pBoostAction)
	
		# Make the ship return to normal speed.
		pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 0, 1.0)
		pExitSeq.AddAction(pUnBoostAction, pWarpSoundAction2, 2.0)

		# And finally finish the exit sequence
		# actually, just put up a empty action, the Traveler system automatically puts his exit sequence action at the
		# end of the sequence, and his exit action is necessary. However I want it to trigger at the right time, and doing
		# this, i'll achieve that.
		pExitSeqEND = App.TGScriptAction_Create(sCustomActionsScript, "NoAction")
		pExitSeq.AddAction(pExitSeqEND, pUnBoostAction, 1.5)

	###########################################################################################
	# end of the not-required stuff that sets up my sequences
	###########################################################################################

	# Now the following part, the return statement is VERY important.
	# it must return a list of 3 values, from beggining to end, they must be:
	# 1º: the engaging travel sequence  (plays once, when the ship enters the travel)
	# 2º: the during travel sequence    (plays repeatedly, while the ship is travelling)
	# 3º: the exiting travel sequence   (plays once, when the ship exits travel)

	# Note that each one of them can be None, if you don't want to have that sequence in your travel method.

	return [pEngageSeq, None, pExitSeq]


########
# Method to return "starting travel" events, much like those START_WARP events.
# must return a list with the events, possibly none (empty list)
########
def GetStartTravelEvents(self):
	return [ ]

########
# Method to return "exiting travel" events, much like those EXITED_SET or EXITED_WARP events.
# must return a list with the events, possibly none (empty list)
########
def GetExitedTravelEvents(self):
	return [ ]

########
# Method to return the travel set to use.
# must return a App.SetClass instance, it can't be None.
# NOTE: for the moment, this is probably the best way to make if ships can, or can not, be chased while warping.
########
def GetTravelSetToUse(self):
	try:
		import Custom.GalaxyCharts.Traveler
		pSet = None
		if self.IsPlayer == 1:
			pSet = Custom.GalaxyCharts.Traveler.Travel.pTravelSet
		elif self.IsPlayer == 0 and self.IsAIinPlayerRoute == 1:
			pSet = Custom.GalaxyCharts.Traveler.Travel.pTravelSet
		elif self.IsPlayer == 0 and self.IsAIinPlayerRoute == 0:
			pSet = Custom.GalaxyCharts.Traveler.Travel.pAITravelSet
		return pSet
	except:
		self._LogError("GetTravelSetToUse")

########
# Method to convert the speed this ship is travelling at to Cs ("c" is the physical constant that is equal to the speed of light, in km/h. So,
# in other words, this method should convert the "speed" of the ship, which is relative to this travelling method, to how many times is the ship
# travelling faster than the speed of light.
# must return a float  (like 1.0)
########
def ConvertSpeedAmount(fSpeed):
	speed = fSpeed * 160.0 * 7920.3222700376664
	return speed

########
# Method to return the normal max speed of this travelling method that this travel instance (ship) can achieve.
# For "normal", I mean, on normal circunstances, like for example, engines at 100% power.
# must return a float  (like 1.0)
########
def GetMaxSpeed(self):
	return 10.0

########
# Method to return the normal cruise speed of this travelling method that this travel instance (ship) can achieve.
# For "normal", I mean, on normal circunstances, like for example, engines at 100% power.
# must return a float  (like 1.0)
########
def GetCruiseSpeed(self):
	return 5.0

########
# Method to return the actual max speed of this travelling method that this travel instance (ship) can achieve.
# By "actual", I mean, in the current circunstances, like for example: in warp, engine power affects max speed. So the actual max speed
# that the ship can achieve will be different than the normal max speed if engine power is not at 100%.
# must return a float  (like 1.0)
########
def GetActualMaxSpeed(self):
	return 8.0

########
# Method to return the actual cruise speed of this travelling method that this travel instance (ship) can achieve.
# By "actual", I mean, in the current circunstances, like for example: in warp, engine power affects cruise speed. So the actual cruise speed
# that the ship can achieve will be different than the normal cruise speed if engine power is not at 100%.
# must return a float  (like 1.0)
########
def GetActualCruiseSpeed(self):
	return 5.0

########
# Method to return the list of systems that can be damaged by degradation of the travel (which happens when a ship travels faster than her 
# actual cruise speed).  In warp, for example, the systems that are damaged by degradation is the warp engines.
# must return a list  (like [])
########
def GetDegradationSystems(self):
	pHull = self.Ship.GetHull()
	return [ pHull ]

########
# Method to return the list of coordinates (points in space) in this set which the ship can activate this travelling method from.
# must return a list  (like [])
########
def GetLaunchCoordinatesList(pSet):
	lList = []
	for pShip in pSet.GetClassObjectList(App.CT_SHIP):
		if pShip.GetScript():
			sShipClass = string.split(pShip.GetScript(), '.')[-1]
			if sShipClass == "JLSGravitonCatapult":
				pPos = pShip.GetWorldLocation()
				pPlus = pShip.GetWorldBackwardTG()
				pPlus.Scale(10.0)
				pPos.Add(pPlus)
				lList.append(pPos)
	return lList


#########################################################
# NON-REQUIRED / HELPER  methods
#########################################################
def GetCatapultShipForLC(vLC, pSet):
	for pShip in pSet.GetClassObjectList(App.CT_SHIP):
		if pShip.GetScript():
			sShipClass = string.split(pShip.GetScript(), '.')[-1]
			if sShipClass == "JLSGravitonCatapult":
				pPos = pShip.GetWorldLocation()
				pPlus = pShip.GetWorldBackwardTG()
				pPlus.Scale(10.0)
				pPos.Add(pPlus)
				if pPos.x == vLC.x and pPos.y == vLC.y and pPos.z == vLC.z:
					return pShip
	return None

dBeamsShips = {}
def ToggleEdgeTractorEffects(pAction, pCatapult, bToggle):
	global dBeamsShips
	iCatapultID = pCatapult.GetObjID()
	if bToggle == 1 and not dBeamsShips.has_key(iCatapultID):
		import loadspacehelper
		pSet = pCatapult.GetContainingSet()
		pTopBeam = loadspacehelper.CreateShip("JLSCatapultBeams", pSet, "GCTopBeam_"+str(iCatapultID), "")
		pTopBeam.SetTranslateXYZ(0, 0, 0 )
		pTopBeam.SetInvincible(1)
		pTopBeam.SetHurtable(0)
		pTopBeam.SetTargetable(0)
		pTopBeam.SetCollisionsOn(0)
		pTopBeam.UpdateNodeOnly()
		pCatapult.AttachObject(pTopBeam)
		pTopBeam.UpdateNodeOnly()
		pBottomBeam = None#loadspacehelper.CreateShip("JLSCatapultBeams", pSet, "GCBottomBeam_"+str(iCatapultID), "")
		#pBottomBeam.SetTranslateXYZ(0, 0, 0 )
		#pBottomBeam.SetInvincible(1)
		#pBottomBeam.SetHurtable(0)
		#pBottomBeam.SetTargetable(0)
		#pBottomBeam.SetCollisionsOn(0)
		#pBottomBeam.UpdateNodeOnly()
		#pCatapult.AttachObject(pBottomBeam)
		#pBottomBeam.UpdateNodeOnly()
		pCatapult.UpdateNodeOnly()
		dBeamsShips[iCatapultID] = [pTopBeam, pBottomBeam]
	elif bToggle == 0 and dBeamsShips.has_key(iCatapultID):
		pTopBeam = dBeamsShips[iCatapultID][0]
		#pBottomBeam = dBeamsShips[iCatapultID][1]
		pCatapult.DetachObject(pTopBeam)
		#pCatapult.DetachObject(pBottomBeam)
		pSet = pCatapult.GetContainingSet()
		pSet.RemoveObjectFromSet(pTopBeam.GetName())
		#pSet.RemoveObjectFromSet(pBottomBeam.GetName())
		pTopBeam.SetDeleteMe(1)
		#pBottomBeam.SetDeleteMe(1)
		del dBeamsShips[iCatapultID]
	return 0

dForcefieldShips = {}
def ToggleForcefield(pAction, pCatapult, bToggle):
	global dForcefieldShips
	iCatapultID = pCatapult.GetObjID()
	if bToggle == 1 and not dForcefieldShips.has_key(iCatapultID):
		import loadspacehelper
		pSet = pCatapult.GetContainingSet()
		pForcefield = loadspacehelper.CreateShip("JLSCatapultPlane", pSet, "GCPlane_"+str(iCatapultID), "")
		pForcefield.SetTranslateXYZ(0, 0, 0 )
		pForcefield.SetInvincible(1)
		pForcefield.SetHurtable(0)
		pForcefield.SetTargetable(0)
		pForcefield.SetCollisionsOn(0)
		pForcefield.UpdateNodeOnly()
		pCatapult.AttachObject(pForcefield)
		pForcefield.UpdateNodeOnly()
		pCatapult.UpdateNodeOnly()
		dForcefieldShips[iCatapultID] = pForcefield
	elif bToggle == 0 and dForcefieldShips.has_key(iCatapultID):
		pForcefield = dForcefieldShips[iCatapultID]
		pCatapult.DetachObject(pForcefield)
		pSet = pCatapult.GetContainingSet()
		pSet.RemoveObjectFromSet(pForcefield.GetName())
		pForcefield.SetDeleteMe(1)
		del dForcefieldShips[iCatapultID]
	return 0

def ToggleShipCollisions(pAction, pShipObj, bToggle):
	pShip = App.ShipClass_Cast(pShipObj)
	if pShip != None:
		pShip.SetCollisionsOn(bToggle)
	return 0

def ToggleGravitonBeams(pAction, pCatapult, pTarget, iPhase):
	pCatapult = App.ShipClass_Cast(pCatapult)
	pTarget = App.ShipClass_Cast(pTarget)
	if pTarget == None or pCatapult == None:
		return 0
	fDisabledPercentage = 0.4
	pGravitonSys = pCatapult.GetTractorBeamSystem()
	pBeam1 = App.TractorBeamProjector_Cast(MissionLib.GetSubsystemByName(pCatapult, 'Graviton Beam 1'))
	pBeam2 = App.TractorBeamProjector_Cast(MissionLib.GetSubsystemByName(pCatapult, 'Graviton Beam 2'))
	pBeam3 = App.TractorBeamProjector_Cast(MissionLib.GetSubsystemByName(pCatapult, 'Graviton Beam 3'))
	pBeam4 = App.TractorBeamProjector_Cast(MissionLib.GetSubsystemByName(pCatapult, 'Graviton Beam 4'))
	pBeam5 = App.TractorBeamProjector_Cast(MissionLib.GetSubsystemByName(pCatapult, 'Graviton Beam 5'))
	pBeam6 = App.TractorBeamProjector_Cast(MissionLib.GetSubsystemByName(pCatapult, 'Graviton Beam 6'))
	pBeam7 = App.TractorBeamProjector_Cast(MissionLib.GetSubsystemByName(pCatapult, 'Graviton Beam 7'))
	pBeam8 = App.TractorBeamProjector_Cast(MissionLib.GetSubsystemByName(pCatapult, 'Graviton Beam 8'))
	if iPhase == 0:
		pGravitonSys.StopFiring()
		pBeam1.GetProperty().SetDisabledPercentage(fDisabledPercentage)
		pBeam2.GetProperty().SetDisabledPercentage(fDisabledPercentage)
		pBeam3.GetProperty().SetDisabledPercentage(fDisabledPercentage)
		pBeam4.GetProperty().SetDisabledPercentage(fDisabledPercentage)
		pBeam5.GetProperty().SetDisabledPercentage(fDisabledPercentage)
		pBeam6.GetProperty().SetDisabledPercentage(fDisabledPercentage)
		pBeam7.GetProperty().SetDisabledPercentage(fDisabledPercentage)
		pBeam8.GetProperty().SetDisabledPercentage(fDisabledPercentage)
	if iPhase == 1:
		pGravitonSys.StartFiring(pTarget)
		pGravitonSys.SetForceUpdate(1)
		pBeam1.GetProperty().SetDisabledPercentage(fDisabledPercentage)
		pBeam2.GetProperty().SetDisabledPercentage(2.0)
		pBeam3.GetProperty().SetDisabledPercentage(2.0)
		pBeam4.GetProperty().SetDisabledPercentage(2.0)
		pBeam5.GetProperty().SetDisabledPercentage(2.0)
		pBeam6.GetProperty().SetDisabledPercentage(2.0)
		pBeam7.GetProperty().SetDisabledPercentage(2.0)
		pBeam8.GetProperty().SetDisabledPercentage(2.0)		
	if iPhase == 2:
		pBeam5.GetProperty().SetDisabledPercentage(fDisabledPercentage)
	if iPhase == 3:
		pBeam4.GetProperty().SetDisabledPercentage(fDisabledPercentage)
	if iPhase == 4:
		pBeam8.GetProperty().SetDisabledPercentage(fDisabledPercentage)
	if iPhase == 5:
		pBeam2.GetProperty().SetDisabledPercentage(fDisabledPercentage)
	if iPhase == 6:
		pBeam6.GetProperty().SetDisabledPercentage(fDisabledPercentage)
	if iPhase == 7:
		pBeam3.GetProperty().SetDisabledPercentage(fDisabledPercentage)
	if iPhase == 8:
		pBeam7.GetProperty().SetDisabledPercentage(fDisabledPercentage)
	return 0

dBubbleShips = {}
def ToggleBubbleEffect(pAction, pShip, iPhase):
	global dBubbleShips
	iShipID = pShip.GetObjID()
	if iPhase >= 1:
		if not dBubbleShips.has_key(iShipID):
			import loadspacehelper
			pSet = pShip.GetContainingSet()
			pBubble = loadspacehelper.CreateShip("JLSCatapultBubble", pSet, "GCBubble_"+str(iShipID), "")
			pBubble.SetTranslateXYZ(0, 0, 0 )
			pBubble.SetInvincible(1)
			pBubble.SetHurtable(0)
			pBubble.SetTargetable(0)
			pBubble.SetCollisionsOn(0)
			pBubble.UpdateNodeOnly()
			pShip.AttachObject(pBubble)
			pBubble.UpdateNodeOnly()
			pShip.UpdateNodeOnly()
			pBubble.SetScale(1)
			pBubble.UpdateNodeOnly()
			fBubbleRadius = pBubble.GetRadius()
			dBubbleShips[iShipID] = pBubble, fBubbleRadius
		else:
			pBubble = dBubbleShips[iShipID][0]
			fBubbleRadius = dBubbleShips[iShipID][1]
		#update bubble scale
		fScale = iPhase * ( (pShip.GetRadius()/fBubbleRadius) / 8.0 )
		pBubble.SetTranslateXYZ(0, 0, 0 )
		pBubble.SetScale(fScale)
		pBubble.UpdateNodeOnly()
		pShip.UpdateNodeOnly()
	elif iPhase == 0 and dBubbleShips.has_key(iShipID):
		pBubble = dBubbleShips[iShipID][0]
		pShip.DetachObject(pBubble)
		pSet = pShip.GetContainingSet()
		pSet.RemoveObjectFromSet(pBubble.GetName())
		pBubble.SetDeleteMe(1)
		del dBubbleShips[iShipID]
	return 0

def SetupCamera(pAction, pSet, pCatapult, pShip):
	# we are using the camera "CutsceneCam" I think lol
	#  v1.Subtract(v2)  ->  vector from v2 pointing to v1

	sSet = pSet.GetName()
	pCatapult = App.ShipClass_Cast(pCatapult)
	pShip = App.ShipClass_Cast(pShip)

	#vPos = pCatapult.GetWorldLocation() #App.TGPoint3()
	#for vPlus in [pCatapult.GetWorldRightTG(), pCatapult.GetWorldForwardTG(), pCatapult.GetWorldUpTG()]:
	#	vPlus.Scale(30.0)
	#	vPos.Add(vPlus)

	pCamera = pSet.GetActiveCamera()

	#pMode = pCamera.GetCurrentCameraMode()
	#pMode.SetAttrFloat("AwayDistance", -25.0)
	#pMode.SetAttrFloat("ForwardOffset", 35.0)
	#pMode.SetAttrFloat("SideOffset", -28.0)
	#pMode.SetAttrFloat("RangeAngle1", 60.0)
	#pMode.SetAttrFloat("RangeAngle2", 100.0)
	#pMode.SetAttrFloat("RangeAngle3", -80.0)
	#pMode.SetAttrFloat("RangeAngle4", 80.0)
	#pMode.Update()
	#pMode.SetAttrFloat("AwayDistance", 25000.0)
	#pMode.Update()

	# we are using the camera "CutsceneCam" I think lol
	fDistance = 70 + App.g_kSystemWrapper.GetRandomNumber(50)

	# first we get the location for the camera (vLoc)
	#  -> a point in a random distance (fDistance) from the catapult.  (sphere projection)
	vLoc = pCatapult.GetWorldLocation()
	vPlus = App.TGPoint3_GetRandomUnitVector()
	vPlus.Unitize()
	vPlus.Scale(fDistance)
	vLoc.Add(vPlus)

	# now we get the camera's orientation forward vector (vFwd)
	#  -> the camera should be pointing at halfway the distance of the catapult to the ship.
	vFwd = pCatapult.GetWorldLocation()
	vAdd = pShip.GetWorldLocation()
	vAdd.Subtract( vFwd )
	fScale = vAdd.Length() / 2
	vAdd.Unitize()
	vAdd.Scale(fScale)
	vFwd.Add(vAdd)
	vFwd.Subtract(vLoc)   
	vFwd.Unitize()
	# from the forward vector, we get the right and up orientation vectors for the camera
	vRight = vFwd.Cross( App.TGPoint3_GetModelUp() )
	vUp = vRight.UnitCross( vFwd )

	# finally we position and align the camera to the vectors.
	pCamera.SetTranslate(vLoc)
	pCamera.AlignToVectors(vFwd, vUp)

	pCamera.UpdateNodeOnly()
	return 0

#yea, really ugly, I know... 
#But until I learn how to use this freakking BC camera to make a proper cutscene, this is one the best workarounds I found...
def MoveCamera(pAction, pSet, pCatapult, pShip, fDist):
	#  v1.Subtract(v2)  ->  vector from v2 pointing to v1
	pShip = App.ShipClass_Cast(pShip)

	#little workaround so that when the ship vanishes, the camera doesn't continue moving towards it.
	if pShip.IsHidden() == 1:
		return 0

	pCamera = pSet.GetActiveCamera()

	# do the regular move towards the catapult
	vPos = pCamera.GetWorldLocation()
	vMove = pCatapult.GetWorldLocation()
	vMove.Subtract(vPos)
	vMove.Unitize()
	vMove.Scale(fDist)
	vPos.Add(vMove)

	#now do our interactive camera movement, based on mouse movement, hoorah beat that lol
	fX = App.g_kInputManager.GetMouseDeltaX()
	fY = App.g_kInputManager.GetMouseDeltaY()
	vMoveRight = pCamera.GetWorldRightTG()
	vMoveRight.Scale( (fX/2) * fDist )
	vMoveUp = pCamera.GetWorldUpTG()
	vMoveUp.Scale( (fY/2) * fDist )
	vPos.Add(vMoveRight)
	vPos.Add(vMoveUp)

	# update orientation
	vFwd = pCatapult.GetWorldLocation()
	vAdd = pShip.GetWorldLocation()
	vAdd.Subtract( vFwd )
	fScale = vAdd.Length() / 2
	vAdd.Unitize()
	vAdd.Scale(fScale)
	vFwd.Add(vAdd)
	vFwd.Subtract(vPos)   
	vFwd.Unitize()	

	vRight = vFwd.Cross( App.TGPoint3_GetModelUp() )
	vUp = vRight.UnitCross( vFwd )
	pCamera.SetTranslate(vPos)
	pCamera.AlignToVectors(vFwd, vUp)

	pCamera.UpdateNodeOnly()
	return 0

def PositionShip(pAction, pShip, vPos):
	pShip.SetTranslate(vPos)
	pShip.UpdateNodeOnly()
	return 0