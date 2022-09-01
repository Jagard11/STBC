#######################################
#######################################
###     GENERAL ATTRIBUTES
#######################################
#######################################
########
# name of this travelling method 
########
sName = "Quantum Singularity"

########
# if this travelling method is ship based. Warp for example is ship based, that means that any ship equipped with it can
# engage it anytime she wants. 
# Some travelling methods, like wormholes, are not ship based, that means ships need to enter the wormhole to travel.
########
bIsShipBased = 1


########################################
########################################
###     TRAVELER ATTRIBUTES
########################################
########################################
########
# if this travelling method can be used to tow ships.
########
bCanTowShips = 1

########
# path and file name to engine degradation sound alert
########
sDegradationSoundFile = "scripts\\Custom\\GalaxyCharts\\Sounds\\DegradationAlert.wav"

########
# if this travelling method should show starstreaks while travelling
# (starstreaks options setup in Galaxy Charts UMM Configuration menu)
########
bUseStarstreaks = 1

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
sGoingTo = "Going to"

########
# Phrase to show when the ship drops out of travel (while travelling)
########
sDropOut = "unused - ship cant drop out from quantum singularity"

########
# if this travelling method can trigger RDFs when a ship exits travel.
########
bCanTriggerRDF = 1

########
# if this travelling method always engages blindly (if yes, it means that the Traveler system won't bother turning the ship to face a good (no obstacles)
# direction.  If no, the Traveler system will try to turn the ship to a good direction in-case she isn't in one.)
########
bAlwaysBlind = 1

########
# The following 2 floats define the range of values that can be set as the travelling speed of a ship using this travelling method.
# For warp, for example, it's from 1 to 9.99
# It's an arbitrary scale/range. The actual conversion to a exact speed unit (km/h) is done in the method ConvertSpeedAmount located below.
########
fMinimumSpeed = 1.0
fMaximumSpeed = 1.0

########
# A float, representing the radius (in kilometers) from a launch coordinate which a ship can be able to activate this non-ship-based travelling method
########
fLaunchRadius = 0.0

########
# This attribute specifies the travelling restrictions for this travelling method. Systems can be set to be restricted to this and/or other travelling
# methods in its system plugin (region plugin part)
# The value of this attribute must be a integer, one of the ones contained in the following enum (fyi, 'RS' is abbreviation of 'restricted system'):
# 0 = No restriction
# 1 = can only be used between RSs  (when in a RS to travel to another RS)
# 2 = travel from anywhere to a RS, but can only return to the system where ship came from
# 3 = travel from anywhere to a RS, and can return to any system
########
iRestrictionFlag = 2

###########################################
###########################################
####       TRAVELER METHODS
###########################################
###########################################
import App
import string
import MissionLib
import math

########
# Method to check if the ship is equipped with this travelling method.
# Must return 1 if it has it, 0 if it does not.
# NOTE: this function is not used as a method of the Travel class as are the other functions here.
#       this is actually used just like a helper for the Travel Manager.
########
def IsShipEquipped(pShip):
	pImpEngines = pShip.GetImpulseEngineSubsystem()
	pSensors = pShip.GetSensorSubsystem()
	if pImpEngines != None and pSensors != None:
		pPower = pShip.GetPowerSubsystem()
		if pPower.GetMainBatteryLimit() >= 80000.0:
			return 1
	return 0


########
# Method to check if the ship can travel.
# Must return 1 if it can, otherwise return a string(reason why the ship couldn't travel)
########
def CanTravel(self):
	pShip = self.GetShip()
	pPlayer = App.Game_GetCurrentPlayer()
	bIsPlayer = 0
	if pPlayer and pShip.GetObjID() == pPlayer.GetObjID():
		bIsPlayer = 1
	pHelm = App.CharacterClass_GetObject(App.g_kSetManager.GetSet("bridge"), "Helm")
	pImpulseEngines = pShip.GetImpulseEngineSubsystem()
	if not pImpulseEngines:
		return "No Impulse Engines."

	if (pImpulseEngines.GetPowerPercentageWanted() == 0.0):
		# Ship is trying to warp with their engines off.
		if bIsPlayer == 1:
			pXO = App.CharacterClass_GetObject(App.g_kSetManager.GetSet("bridge"), "XO")
			if pXO:
				MissionLib.QueueActionToPlay(App.CharacterAction_Create(pXO, App.CharacterAction.AT_SAY_LINE, "EngineeringNeedPowerToEngines", None, 1))
		return "Impulse Engines offline."

	pSensors = pShip.GetSensorSubsystem()
	if pSensors.GetSensorRange() <= 2000.0:
		return "Insufficient Sensor Array."

	pPower = pShip.GetPowerSubsystem()
	if pPower.GetMainBatteryPower() < 80000.0:
		return "Insufficent Battery Power."
	return 1

########
# Method to check if the ship can continue travelling (she's travelling, yeah)
# must return 1 if she can, 0 if she can't travel anymore (thus will forcibly drop out).
########
def CanContinueTravelling(self):
	#since we can't drop out from quantum singularity, and any quantum-sing. travel should be pretty fast, almost instantaneous, no need for this.
	return 1

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
	
	# note that the only REQUIRED part is what the function returns and the single and only parameter 'self', so go to the end of the function
	# for more info

	################################################################################
	# from here below it is just the custom code to create the custom sequences
	# NOT-REQUIRED  STUFF
	# modify accordingly for your sequences
	#########
	# NOTE:  ALL tractor related actions that are used here for the engaging and for the exiting
	#        warp sequences ARE REQUIRED if you want to be able to succesfully (and beautifully)
	#	   tractor ships thru your travel. (in this example, thru warp)
	################################################################################

	pWS = self.TravelerSequence	
	
	sCustomActionsScript = "Custom.GalaxyCharts.WarpSequence_Override"
	
	pShip = pWS.GetShip()
	pPlayer = App.Game_GetCurrentPlayer()
	pSet = pShip.GetContainingSet()

	if pShip == None:
		return [None, None, None]

	pWarpSet = pWS.Travel.GetTravelSetToUse()

	pEngageWarpSeq = App.TGSequence_Create()

	#pDuringWarpSeq = App.TGSequence_Create()

	pExitWarpSeq = App.TGSequence_Create()

	###########################entering sequence####################
	if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
		# Force a noninteractive cinematic view in space..
		pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
		pEngageWarpSeq.AddAction(pCinematicStart, None)

		pCutsceneBegin = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pSet.GetName())
		pEngageWarpSeq.AddAction(pCutsceneBegin, pCinematicStart)

		pSetupCam = App.TGScriptAction_Create(__name__, "SetupCamera", pSet, pShip)
		pEngageWarpSeq.AddAction(pSetupCam, pCutsceneBegin)

		fTimeToMove = 14.0
		fCount = 0.2
		while fCount < fTimeToMove:
			pMoveCamAction = App.TGScriptAction_Create(__name__, "MoveCamera", pSet, pShip, 0.12)
			pEngageWarpSeq.AddAction(pMoveCamAction, pSetupCam, fCount)
			fCount = fCount + 0.01
			if fCount >= fTimeToMove:
				break

		pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
		pEngageWarpSeq.AddAction(pDisallowInput, pSetupCam)

	pHardStopAction = App.TGScriptAction_Create(__name__, "HardStopShip", pShip.GetObjID() )
	pEngageWarpSeq.AddAction(pHardStopAction, None)

	pFireBeam = App.TGScriptAction_Create(__name__, "FireQSBeam", pShip.GetObjID())
	pEngageWarpSeq.AddAction(pFireBeam, pHardStopAction, 0.7)

	pCreateSingularity = App.TGScriptAction_Create(__name__, "CreateQuantumSingularity", pShip.GetObjID(), 11.0)
	pEngageWarpSeq.AddAction(pCreateSingularity, pFireBeam, 1.0)

	pStopBeam = App.TGScriptAction_Create(__name__, "StopQSBeam", pShip.GetObjID())
	pEngageWarpSeq.AddAction(pStopBeam, pCreateSingularity, 3.0)

	pDeductPower = App.TGScriptAction_Create(__name__, "DeductPowerFromBatteries", pShip.GetObjID(), 80000.0)
	pEngageWarpSeq.AddAction(pDeductPower, pStopBeam)

	pBoostShip = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 1, 30.0)
	pEngageWarpSeq.AddAction(pBoostShip, pDeductPower, 0.5)

	fTimeToFlash = 14.0
	if pWS.Travel.bTractorStat == 1:
		fCount = 0.0
		while fCount < fTimeToFlash:
			pMaintainTowingAction = App.TGScriptAction_Create(sCustomActionsScript, "MaintainTowingAction", pWS)
			pEngageWarpSeq.AddAction(pMaintainTowingAction, None, fCount)
			fCount = fCount + 0.01
			if fCount >= fTimeToFlash:
				break

	# Create the warp flash.
	pFlashAction1 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
	pEngageWarpSeq.AddAction(pFlashAction1, pBoostShip, 5.0)

	# Hide the ship.
	pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 1)
	pEngageWarpSeq.AddAction(pHideShip, pFlashAction1)

	pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 0, 1.0)
	pEngageWarpSeq.AddAction(pUnBoostAction, pHideShip)
	
	pCheckTowing = App.TGScriptAction_Create(sCustomActionsScript, "EngageSeqTractorCheck", pWS)
	pEngageWarpSeq.AddAction(pCheckTowing, pHideShip)	

	pCutsceneEnd = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pSet.GetName())
	pEngageWarpSeq.AddAction(pCutsceneEnd, pCheckTowing, 3.9)

	pEnWarpSeqEND = App.TGScriptAction_Create(sCustomActionsScript, "NoAction")
	pEngageWarpSeq.AddAction(pEnWarpSeqEND, pUnBoostAction, 4.0)

	############### exiting begins ########

	# Add the actions for exiting warp only if the destination set exists.
	if(pWS.GetDestinationSet() != None):
		if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
			# Force a noninteractive cinematic view in space..
			pCinematicStart = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
			pExitWarpSeq.AddAction(pCinematicStart, None)

			pCutsceneBegin = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", self.DestSet.GetName())
			pExitWarpSeq.AddAction(pCutsceneBegin, pCinematicStart)

			pSetupCam = App.TGScriptAction_Create(__name__, "SetupCamera", self.DestSet, pShip, 1)
			pExitWarpSeq.AddAction(pSetupCam, pCutsceneBegin)

			fTimeToMove = 6.0
			fCount = 0.2
			while fCount < fTimeToMove:
				pMoveCamAction = App.TGScriptAction_Create(__name__, "MoveCamera", self.DestSet, pShip, 0.12, 1)
				pExitWarpSeq.AddAction(pMoveCamAction, pSetupCam, fCount)
				fCount = fCount + 0.01
				if fCount >= fTimeToMove:
					break

			pDisallowInput = App.TGScriptAction_Create("MissionLib", "RemoveControl")
			pExitWarpSeq.AddAction(pDisallowInput, pSetupCam)
	
		# Hide the ship.
		pHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 1)
		pExitWarpSeq.AddAction(pHideShip, None)

		# Check for towee
		if pWS.Travel.bTractorStat == 1:
			pHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pWS.Travel.Towee.GetObjID(), 1)
			pExitWarpSeq.AddAction(pHideTowee, pHideShip)

		pCreateSingularity = App.TGScriptAction_Create(__name__, "CreateExitQuantumSingularity", pShip.GetObjID(), 5.0 )		
		pExitWarpSeq.AddAction(pCreateSingularity, pHideShip, 0.7)

		# Create the warp flash.
		pFlashAction2 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
		pExitWarpSeq.AddAction(pFlashAction2, pCreateSingularity, 1.5)

		# Un-Hide the ship
		pUnHideShip = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pShip.GetObjID(), 0)
		pExitWarpSeq.AddAction(pUnHideShip, pFlashAction2, 0.2)

		# Un-hide the Towee, plus if it exists, also set up the maintain chain
		## REMEMBER: any changes in the time of this sequence will also require a re-check of this part, to make sure
		##           we're making the right amount of MaintainTowing actions.
		if pWS.Travel.bTractorStat == 1:
			pUnHideTowee = App.TGScriptAction_Create(sCustomActionsScript, "HideShip", pWS.Travel.Towee.GetObjID(), 0)
			pExitWarpSeq.AddAction(pUnHideTowee, pUnHideShip)

			fCount = 0.0
			while fCount < 3.6:
				pMaintainTowingAction = App.TGScriptAction_Create(sCustomActionsScript, "MaintainTowingAction", pWS)
				pExitWarpSeq.AddAction(pMaintainTowingAction, pUnHideTowee, fCount)
				fCount = fCount + 0.01
				if fCount >= 3.6:
					break

		# Give it a little boost
		pBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 1, 70.0)
		pExitWarpSeq.AddAction(pBoostAction, pUnHideShip, 0.1)

		# Make the ship return to normal speed.
		pUnBoostAction = App.TGScriptAction_Create(sCustomActionsScript, "BoostShipSpeed", pShip.GetObjID(), 0, 1.0)
		pExitWarpSeq.AddAction(pUnBoostAction, pBoostAction, 2.0)

		pCutsceneEnd = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", self.DestSet.GetName())
		pExitWarpSeq.AddAction(pCutsceneEnd, pUnBoostAction, 1.5)

		# And finally finish the exit sequence
		# actually, just put up a empty action, the Traveler system automatically puts his exit sequence action at the
		# end of the sequence, and his exit action is necessary. However I want it to trigger at the right time, and doing
		# this, i'll achieve that.
		pExitWarpSeqEND = App.TGScriptAction_Create(sCustomActionsScript, "NoAction")
		pExitWarpSeq.AddAction(pExitWarpSeqEND, pCutsceneEnd)

	###########################################################################################
	# end of the not-required stuff that sets up my sequences
	###########################################################################################

	# Now the following part, the return statement is VERY important.
	# it must return a list of 3 values, from beggining to end, they must be:
	# 1º: the engaging travel sequence  (plays once, when the ship enters the travel)
	# 2º: the during travel sequence    (plays repeatedly, while the ship is travelling)
	# 3º: the exiting travel sequence   (plays once, when the ship exits travel)

	# Note that each one of them can be None, if you don't want to have that sequence in your travel method.

	return [pEngageWarpSeq, None, pExitWarpSeq]


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
	speed = 2600.0 * 70920.3  #1600 times faster than max warp
	return speed

########
# Method to return the normal max speed of this travelling method that this travel instance (ship) can achieve.
# For "normal", I mean, on normal circunstances, like for example, engines at 100% power.
# must return a float  (like 1.0)
########
def GetMaxSpeed(self):
	return 1.0

########
# Method to return the normal cruise speed of this travelling method that this travel instance (ship) can achieve.
# For "normal", I mean, on normal circunstances, like for example, engines at 100% power.
# must return a float  (like 1.0)
########
def GetCruiseSpeed(self):
	return 1.0

########
# Method to return the actual max speed of this travelling method that this travel instance (ship) can achieve.
# By "actual", I mean, in the current circunstances, like for example: in warp, engine power affects max speed. So the actual max speed
# that the ship can achieve will be different than the normal max speed if engine power is not at 100%.
# must return a float  (like 1.0)
########
def GetActualMaxSpeed(self):
	return 1.0

########
# Method to return the actual cruise speed of this travelling method that this travel instance (ship) can achieve.
# By "actual", I mean, in the current circunstances, like for example: in warp, engine power affects cruise speed. So the actual cruise speed
# that the ship can achieve will be different than the normal cruise speed if engine power is not at 100%.
# must return a float  (like 1.0)
########
def GetActualCruiseSpeed(self):
	return 1.0

########
# Method to return the list of systems that can be damaged by degradation of the travel (which happens when a ship travels faster than her 
# actual cruise speed).  In warp, for example, the systems that are damaged by degradation is the warp engines.
# must return a list  (like [])
########
def GetDegradationSystems(self):
	return [ ]

########
# Method to return the list of coordinates (points in space) in this set which the ship can activate this travelling method from.
# must return a list  (like [])
########
def GetLaunchCoordinatesList(pSet):
	return []


#########################################################
# NON-REQUIRED / HELPER  methods
#########################################################
def HardStopShip(pAction, iShipID):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), iShipID)
	if pShip != None:
		vZero = App.TGPoint3()
		vZero.SetXYZ(0.0, 0.0, 0.0)
		pShip.SetSpeed(0, pShip.GetWorldForwardTG(), App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
		pShip.SetVelocity(vZero)
		pShip.SetAngularVelocity(vZero, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
		pShip.SetAcceleration(vZero)
		pShip.SetAngularAcceleration(vZero)	
	return 0

dDummys = {}
def FireQSBeam(pAction, iShipID):
	global dDummys
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), iShipID)
	if pShip != None:
		import loadspacehelper
		pSet = pShip.GetContainingSet()
		pQSBeam = loadspacehelper.CreateShip("QSDummy", pSet, "QSBeam_"+pShip.GetName(), "")
		pQSBeam.SetTranslateXYZ(0, pShip.GetRadius()*0.9, 0 )
		pQSBeam.SetInvincible(1)
		pQSBeam.SetHurtable(0)
		pQSBeam.SetTargetable(0)
		pQSBeam.SetCollisionsOn(0)
		pQSBeam.UpdateNodeOnly()
		pShip.AttachObject(pQSBeam)
		pQSBeam.UpdateNodeOnly()

		pQSDummy = loadspacehelper.CreateShip("QSDummy", pSet, "QSDummy_"+pShip.GetName(), "")
		vLoc = pShip.GetWorldLocation()
		vAdd = pShip.GetWorldForwardTG()
		vAdd.Scale(87)
		vLoc.Add(vAdd)
		pQSDummy.SetTranslate(vLoc)
		pQSDummy.SetInvincible(1)
		pQSDummy.SetHurtable(1)
		pQSDummy.SetTargetable(0)
		pQSDummy.SetCollisionsOn(0)
		pQSDummy.UpdateNodeOnly()

		pShip.UpdateNodeOnly()

		pQSBeam.GetPhaserSystem().StartFiring(pQSDummy)
		dDummys[iShipID] = [pQSBeam, pQSDummy]
	return 0

def StopQSBeam(pAction, iShipID):
	global dDummys
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), iShipID)
	if pShip != None and iShipID in dDummys.keys():
		pQSBeam = dDummys[iShipID][0]
		pQSDummy = dDummys[iShipID][1]
		pQSBeam.GetPhaserSystem().StopFiring()
		pShip.DetachObject(pQSBeam)
		pSet = pShip.GetContainingSet()
		pSet.RemoveObjectFromSet(pQSBeam.GetName())
		pSet.RemoveObjectFromSet(pQSDummy.GetName())
		pQSBeam.SetDeleteMe(1)
		pQSDummy.SetDeleteMe(1)
		del dDummys[iShipID]
	return 0

def CreateQuantumSingularity(pAction, iShipID, fLifetime):
	#the lifetime of the torp used to create the singularity effect should be enough so that the torpedo vanishes a few moments after the flash
	# this also helps us since we wont need an "delete singularity" action =)
	# create torp a little ahead of the ship, where the beam was firing at
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), iShipID)
	if pShip != None:
		pSet = pShip.GetContainingSet()
		vPos = pShip.GetWorldLocation()
		vAdd = pShip.GetWorldForwardTG()
		vAdd.Scale(87)
		vPos.Add(vAdd)

		pTorp = App.Torpedo_Create(__name__, vPos)
		pTorp.SetTarget(App.NULL_ID)
		pTorp.SetParent(iShipID)
		pTorp.SetCollisionFlags(App.ObjectClass.CFB_NO_COLLISIONS)
		TorpName = "QSEffect_"+pShip.GetName()
		pSet.AddObjectToSet(pTorp, TorpName)
		pTorp.SetLifetime(fLifetime)
		pTorp.UpdateNodeOnly()
	return 0

def CreateExitQuantumSingularity(pAction, iShipID, fLifetime):
	#the lifetime of the torp used to create the singularity effect should be enough so that the torpedo vanishes a few moments after the flash
	# this also helps us since we wont need an "delete singularity" action =)
	#create torp in the same spot as the ship
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), iShipID)
	if pShip != None:
		pSet = pShip.GetContainingSet()

		vPos = pShip.GetWorldLocation()

		pTorp = App.Torpedo_Create(__name__, vPos)
		pTorp.SetTarget(App.NULL_ID)
		pTorp.SetParent(iShipID)
		pTorp.SetCollisionFlags(App.ObjectClass.CFB_NO_COLLISIONS)
		TorpName = "QSEffect_"+pShip.GetName()
		pSet.AddObjectToSet(pTorp, TorpName)
		pTorp.SetLifetime(fLifetime)
		pTorp.UpdateNodeOnly()
	return 0

def DeductPowerFromBatteries(pAction, iShipID, fAmount):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), iShipID)
	if pShip != None:
		pPower = pShip.GetPowerSubsystem()
		if pPower != None:
			pPower.StealPower(fAmount)
	return 0

def SetupCamera(pAction, pSet, pShip, bForExit = 0):
	# we are using the camera "CutsceneCam" I think lol
	sSet = pSet.GetName()
	pShip = App.ShipClass_Cast(pShip)

	pCamera = pSet.GetActiveCamera()

	fDistance = 120 + App.g_kSystemWrapper.GetRandomNumber(100)

	vLoc = pShip.GetWorldLocation()
	if bForExit == 0:
		vAdd = pShip.GetWorldForwardTG()
		vAdd.Scale( 87 /2.0)
		vLoc.Add(vAdd)
		vFwd = App.TGPoint3()
		vFwd.Set(vLoc)
		vPlus = App.TGPoint3_GetRandomUnitVector()
		vPlus.Unitize()
		vPlus.Scale(fDistance)
		vLoc.Add(vPlus)
	else:
		vPlus = App.TGPoint3_GetRandomUnitVector()
		vPlus.Unitize()
		vPlus.Scale(fDistance)
		vLoc.Add(vPlus)
		vFwd = pShip.GetWorldLocation()

	vFwd.Subtract(vLoc)
	vFwd.Unitize()
	vRight = vFwd.Cross( App.TGPoint3_GetModelUp() )
	vUp = vRight.UnitCross( vFwd )
	pCamera.SetTranslate(vLoc)
	pCamera.AlignToVectors(vFwd, vUp)

	pCamera.UpdateNodeOnly()
	return 0

#yea, really ugly, I know... 
#But until I learn how to use this freakking BC camera to make a proper cutscene, this is one the best workarounds I found...
def MoveCamera(pAction, pSet, pShip, fDist, bForExit = 0):
	pShip = App.ShipClass_Cast(pShip)

	#little workaround so that when the ship vanishes, the camera doesn't continue moving towards it.
	if pShip.IsHidden() == 1:
		return 0

	pQSDummy = App.ShipClass_Cast(App.ObjectClass_GetObject( None, "QSDummy_"+pShip.GetName() ))
	pQS = App.ObjectClass_GetObject( None, "QSEffect_"+pShip.GetName() )

	pCamera = pSet.GetActiveCamera()

	fDistance = 120 + App.g_kSystemWrapper.GetRandomNumber(100)

	vPos = pCamera.GetWorldLocation()
	
	vMove = pShip.GetWorldLocation()
	vMove.Subtract(vPos)
	vMove.Unitize()
	vMove.Scale(fDist)

	vPos.Add(vMove)

	vFwd = pShip.GetWorldLocation()

	vAdd = pShip.GetWorldForwardTG()
	if bForExit == 1:
		vAdd.Scale(-1)

	fAddScale = 1.0
	if pQSDummy == None and pQS == None:
		fAddScale = 87/2.0
	elif pQSDummy != None:
		vQSDLoc = pQSDummy.GetWorldLocation()
		vQSDLoc.Subtract(vFwd)
		fAddScale = vQSDLoc.Length() / 2
	elif pQS != None:
		vQSLoc = pQS.GetWorldLocation()
		vQSLoc.Subtract(vFwd)
		fAddScale = vQSLoc.Length() / 2

	vAdd.Scale(fAddScale)

	vFwd.Add(vAdd)
	vFwd.Subtract(vPos)
	vFwd.Unitize()
	vRight = vFwd.Cross( App.TGPoint3_GetModelUp() )
	vUp = vRight.UnitCross( vFwd )
	pCamera.SetTranslate(vPos)
	pCamera.AlignToVectors(vFwd, vUp)

	pCamera.UpdateNodeOnly()
	return 0

def GetEngageDirection(self):
	# Get all the objects along the line that we'll
	# be warping through.
	debug(__name__ + ", GetEngageDirection")
	fRayLength = 4000.0
	vOrigin = self.Ship.GetWorldLocation()
	vEnd = self.Ship.GetWorldForwardTG()
	vEnd.Scale(fRayLength)
	vEnd.Add(vOrigin)
	
	lsObstacles = self.GetWarpObstacles(vOrigin, vEnd)
	# If we have no obstacles in the way, we're good.
	if len(lsObstacles) == 0:
		vZero = App.TGPoint3()
		vZero.SetXYZ(0, 0, 0)
		self.Ship.SetTargetAngularVelocityDirect(vZero)
		return None

	vBetterDirection = None
	# We've got obstacles in the way.
	if not vBetterDirection:
		# Cast a few rays
		# and try to find a good direction to go.  If we don't
		# find a good direction, that's bad...
		for iRayCount in range(50):
			vRay = App.TGPoint3_GetRandomUnitVector()

			# Bias it toward our Forward direction.
			vRay.Scale(1.5)
			vRay.Add(self.Ship.GetWorldForwardTG())
			vRay.Unitize()

			vEnd = App.TGPoint3()
			vEnd.Set(vRay)
			vEnd.Scale(fRayLength)

			vEnd.Add(vOrigin)
			lsObstacles = self.GetWarpObstacles(vOrigin, vEnd)
			if not lsObstacles:
				# Found a good direction.
				vBetterDirection = vRay
				break

	if vBetterDirection:
		# Return the better direction to turn to, the Travel will take care of the rest.
		return vBetterDirection
	return None


##########################################################################################################################
# to create the QS effect
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(199.0 / 233.0, 147.0 / 255.0, 45.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(233.0 / 255.0, 147.0 / 255.0, 45.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 0.800000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/JLSQSCore.tga",
					kCoreColor,
					4.5,      #core size
					3.0,	    #core rotating speed
					"data/Textures/Tactical/JLSQSGlow.tga", 
					kGlowColor,
					0.5,	   #glow rate
					16.0,	   #min glow size
					30.0,	   #max glow size
					"data/Textures/Tactical/JLSQSBlank.tga",
					kFlareColor,			#flare color							
					10,		     #number of flares
					5.0,		      #flare size
					0.1)          #flare lifetime
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