from bcdebug import debug
import App

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug("Loading " + __name__ + " module...")

# A little preprocessing AI that resets its
# contained AI when its SetTarget external
# function is called.
class ResetOnTargetChange:
	def CodeAISet(self):
		# Register our SetTarget external function.
		debug(__name__ + ", CodeAISet")
		self.pCodeAI.RegisterExternalFunction("SetTarget",
			{ "Name" : "SetTarget" } )

	def SetTarget(self, sTarget):
		# Time to reset our contained AI.
		debug(__name__ + ", SetTarget")
		pContained = self.pCodeAI.GetContainedAI()
		pContained.Reset()

	def GetNextUpdateTime(self):
		# Never really needs to call Update.
		debug(__name__ + ", GetNextUpdateTime")
		return 3600.0

	def Update(self, dEndTime):
		debug(__name__ + ", Update")
		return App.PreprocessingAI.PS_NORMAL

# A little preprocessing AI that trims down the
# target list to the list of targets that the player
# isn't tractoring.
class PruneTargetList:
	def __init__(self, pAllTargetsGroup):
		debug(__name__ + ", __init__")
		self.pTargets = pAllTargetsGroup
		self.lsBackupTargetList = pAllTargetsGroup.GetNameTuple()

		# Add event handlers...
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		# Listen for when tractor beams start to hit things, or stop hitting things.
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_TRACTOR_BEAM_STARTED_HITTING, self.pEventHandler, "TractorStartedHitting")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_TRACTOR_BEAM_STOPPED_HITTING, self.pEventHandler, "TractorStoppedHitting")

	def TractorStartedHitting(self, pEvent):
		# Check who's firing this tractor beam.
		debug(__name__ + ", TractorStartedHitting")
		try:
			pShip = App.TractorBeamProjector_Cast( pEvent.GetSource() ).GetParentShip()

			if pShip.GetObjID() != App.Game_GetCurrentPlayer().GetObjID():
				# The player isn't the one generating this event.
				return
		except AttributeError: return

		# If we got this far, the player's ship is the one that just started
		# hitting another with its tractor beam.  Get the name of the object
		# being tractored.
		sTarget = App.ObjectClass_Cast(pEvent.GetDestination()).GetName()

		# Remove this thing from the list of targets.
		if (sTarget in self.lsBackupTargetList)  and  (sTarget in self.pTargets.GetNameTuple()):
			self.pTargets.RemoveName(sTarget)

#			debug("Removed %s from target list %s." % (sTarget, self.pTargets.GetNameTuple()))

	def TractorStoppedHitting(self, pEvent):
		# Check who was firing this tractor beam.
		debug(__name__ + ", TractorStoppedHitting")
		try:
			pShip = App.TractorBeamProjector_Cast( pEvent.GetSource() ).GetParentShip()

			if pShip.GetObjID() != App.Game_GetCurrentPlayer().GetObjID():
				# The player isn't the one generating this event.
				return
		except AttributeError: return

		# If we got this far, the player's ship is the one that just stopped
		# hitting something with its tractor beam.  Get the name of the object
		# that was being tractored
		sTarget = App.ObjectClass_Cast(pEvent.GetDestination()).GetName()

		# Add this thing back into the list of targets, if it should be there.
		if (sTarget in self.lsBackupTargetList)  and  (sTarget not in self.pTargets.GetNameTuple()):
			self.pTargets.AddName(sTarget)

#			debug("Added %s to target list %s." % (sTarget, self.pTargets.GetNameTuple()))

	def GetNextUpdateTime(self):
		# Never really needs to call Update.
		debug(__name__ + ", GetNextUpdateTime")
		return 3600.0

	def Update(self, dEndTime):
		debug(__name__ + ", Update")
		return App.PreprocessingAI.PS_NORMAL

def CreateAI(pShip, *lTargets):
	debug(__name__ + ", CreateAI")
	pAllTargetsGroup = App.ObjectGroup_ForceToGroup(lTargets)
	sInitialTarget = pAllTargetsGroup.GetNameTuple()[0]




	#########################################
	# Creating PlainAI Stay at (476, 26)
	pStay = App.PlainAI_Create(pShip, "Stay")
	pStay.SetScriptModule("Stay")
	pStay.SetInterruptable(1)
	# Done creating PlainAI Stay
	#########################################
	#########################################
	# Creating PreprocessingAI TractorDocking at (472, 87)
	## Setup:
	import AI.Preprocessors
	pTractorScript = AI.Preprocessors.FireScript(sInitialTarget)
	pTractorScript.AddTractorBeam(pShip, App.TractorBeamSystem.TBS_DOCK_STAGE_1)
	## The PreprocessingAI:
	pTractorDocking = App.PreprocessingAI_Create(pShip, "TractorDocking")
	pTractorDocking.SetInterruptable(1)
	pTractorDocking.SetPreprocessingMethod(pTractorScript, "Update")
	pTractorDocking.SetContainedAI(pStay)
	# Done creating PreprocessingAI TractorDocking
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (305, 163)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (452, 160)
	pPriorityList.AddAI(pTractorDocking, 1)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (150, 186)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (250, 192)
	pSequence.AddAI(pPriorityList)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating PreprocessingAI ResetWhenTargetChanges at (47, 177)
	## Setup:
	pResetScript = ResetOnTargetChange()
	## The PreprocessingAI:
	pResetWhenTargetChanges = App.PreprocessingAI_Create(pShip, "ResetWhenTargetChanges")
	pResetWhenTargetChanges.SetInterruptable(1)
	pResetWhenTargetChanges.SetPreprocessingMethod(pResetScript, "Update")
	pResetWhenTargetChanges.SetContainedAI(pSequence)
	# Done creating PreprocessingAI ResetWhenTargetChanges
	#########################################
	#########################################
	# Creating PreprocessingAI SelectTarget at (45, 227)
	## Setup:
	import AI.Preprocessors
	pSelectionPreprocess = AI.Preprocessors.SelectTarget(pAllTargetsGroup)
	## The PreprocessingAI:
	pSelectTarget = App.PreprocessingAI_Create(pShip, "SelectTarget")
	pSelectTarget.SetInterruptable(1)
	pSelectTarget.SetPreprocessingMethod(pSelectionPreprocess, "Update")
	pSelectTarget.SetContainedAI(pResetWhenTargetChanges)
	# Done creating PreprocessingAI SelectTarget
	#########################################
	#########################################
	# Creating PreprocessingAI PruneTargets at (44, 284)
	## Setup:
	pPrune = PruneTargetList( pAllTargetsGroup )
	## The PreprocessingAI:
	pPruneTargets = App.PreprocessingAI_Create(pShip, "PruneTargets")
	pPruneTargets.SetInterruptable(1)
	pPruneTargets.SetPreprocessingMethod(pPrune, "Update")
	pPruneTargets.SetContainedAI(pSelectTarget)
	# Done creating PreprocessingAI PruneTargets
	#########################################
	return pPruneTargets
