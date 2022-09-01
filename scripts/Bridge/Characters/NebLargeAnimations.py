from bcdebug import debug
# LargeAnimations.py
# This file includes all animations shared by large characters

import App
import Bridge.Characters.CommonAnimations



	# Place at T
def PlaceAtT(pCharacter):
	debug(__name__ + ", PlaceAtT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_stand_t_l.nif", "db_stand_t_l")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "db_stand_t_l")
	pSequence.AddAction(pAction)
	return pSequence

	# Seat at T
def SeatedT(pCharacter):
	debug(__name__ + ", SeatedT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_seated_t_l.nif", "db_seated_t_l")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "db_seated_t_l", 0, 0, 1)
	pSequence.AddAction(pAction)
	return pSequence

	# Turn T towards captain large
def TurnAtTTowardsCaptain(pCharacter):
	debug(__name__ + ", TurnAtTTowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_face_capt_t.nif", "db_face_capt_t")
	kAM.LoadAnimation ("data/animations/db_chair_T_face_capt.nif", "db_chair_T_face_capt")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_face_capt_t", 0, 0, 1), pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "db_chair_T_face_capt", 0, 0), pOpenEyes)
	return pSequence

	# Turn back T from looking at captain
def TurnBackAtTFromCaptain(pCharacter):
	debug(__name__ + ", TurnBackAtTFromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_face_capt_t_reverse.nif", "db_face_capt_t_reverse")
	kAM.LoadAnimation ("data/animations/db_chair_T_face_capt_reverse.nif", "db_chair_T_face_capt_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_face_capt_t_reverse", 0, 0, 1), pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "db_chair_T_face_capt_reverse", 0, 0), pOpenEyes)
	return pSequence

	# From L1 to T
def MoveFromL1ToT(pCharacter):
	debug(__name__ + ", MoveFromL1ToT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_L1toT_l.nif", "db_L1toT_l")
	kAM.LoadAnimation ("data/animations/DB_sit_T_l.nif", "db_sit_T_l")
	kAM.LoadAnimation ("data/animations/db_chair_T_in.nif", "db_chair_T_in")
	kAM.LoadAnimation ("data/animations/db_door_l1.nif", "doorl1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_WalkFromLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_L1toT_l", 0, 0, 1)
	pSequence.AddAction(pAnimAction_WalkFromLift, pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "doorl1", 0, 0), pOpenEyes, 0.125)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_sit_T_l", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pAnimAction_WalkFromLift, 0.0)
	fTime = kAM.GetAnimationLength("db_sit_T_l")
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "db_chair_T_in", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_WalkFromLift, 0.0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBTactical"))
	pEvent = App.TGIntEvent_Create ()
	pEvent.SetEventType (App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

	# From T to L1
def MoveFromTToL1(pCharacter):
	debug(__name__ + ", MoveFromTToL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_stand_t_l.nif", "db_stand_t_l")
	kAM.LoadAnimation ("data/animations/DB_chair_T_out.nif", "DB_chair_T_out")
	kAM.LoadAnimation ("data/animations/db_TtoL1_l.nif", "db_TtoL1_l")
	kAM.LoadAnimation ("data/animations/db_door_l1.nif", "doorl1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_stand_t_l", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Stand, pOpenEyes)
	fTime = kAM.GetAnimationLength("db_stand_t_l")
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "DB_chair_T_out", 0, 0), pOpenEyes)
	pAnimAction_WalkToLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "db_TtoL1_l", 0, 0)
	pSequence.AddAction(pAnimAction_WalkToLift, pAnimAction_Stand, 0.0)
	fTime = fTime + kAM.GetAnimationLength("db_TtoL1_l")
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "doorl1", 0, 0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "DBL1L"))
	pEvent = App.TGIntEvent_Create ()		# Add event to hide character after it gets into the turbolift
	pEvent.SetEventType (App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_HIDDEN)
	pAnimAction.AddCompletedEvent(pEvent)
	pSequence.AddAction(pAnimAction, pOpenEyes, fTime - 1.7)	
	return pSequence

	# lean left animation
def THit(pCharacter):
	#print("Hit T")
	debug(__name__ + ", THit")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_hit_t.NIF", "db_hit_t")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	# Lean
	pLeanAction = App.TGAnimAction_Create(pAnimNode, "db_hit_t", 0, 0)
	pSequence.AddAction(pLeanAction)

#	if (App.g_kSystemWrapper.GetRandomNumber(5) == 3):
#		if (pCharacter.GetGender() == 0):
#			pSequence.AddAction(App.TGSoundAction_Create("MaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))
#		else:
#			pSequence.AddAction(App.TGSoundAction_Create("FemaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))

	return pSequence

	# lean hard left animation
def THitHard(pCharacter):
	debug(__name__ + ", THitHard")
	return THit (pCharacter)

####################################################
# E-Bridge Animations
####################################################

	# Place at T
def EBPlaceAtT(pCharacter):
#	print("Place T")
	debug(__name__ + ", EBPlaceAtT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_t_l.nif", "EB_stand_t_l")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "EB_stand_t_l")
	pSequence.AddAction(pAction)
	return pSequence

	# Place at L1
def EBPlaceAtL1(pCharacter):
	debug(__name__ + ", EBPlaceAtL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/eb_L1toT_l.nif", "eb_L1toT_l")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "eb_L1toTt_l")
	pSequence.AddAction(pAction)
	return pSequence

	# Seat at T
def EBSeatedT(pCharacter):
#	print("Seated T")
	debug(__name__ + ", EBSeatedT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_seated_t_l.nif", "EB_seated_t_l")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "EB_seated_t_l", 0, 0, 1)
	pSequence.AddAction(pAction)
	return pSequence

	# Turn T towards captain large
def EBTurnAtTTowardsCaptain(pCharacter):
#	print("Turn T")
	debug(__name__ + ", EBTurnAtTTowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_face_capt_t.nif", "EB_face_capt_t")
	kAM.LoadAnimation ("data/animations/EB_chair_T_face_capt.nif", "EB_chair_T_face_capt")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_face_capt_t", 0, 0, 1), pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "EB_chair_T_face_capt", 0, 0), pOpenEyes)
	return pSequence

	# Turn back T from looking at captain
def EBTurnBackAtTFromCaptain(pCharacter):
#	print("Turn Back T")
	debug(__name__ + ", EBTurnBackAtTFromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_face_capt_reverse.nif", "EB_face_capt_t_reverse")
	kAM.LoadAnimation ("data/animations/EB_chair_T_face_capt_reverse.nif", "EB_chair_T_face_capt_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_face_capt_t_reverse", 0, 0, 1), pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "EB_chair_T_face_capt_reverse", 0, 0), pOpenEyes)
	return pSequence

	# From T to L1
def EBMoveFromTToL1(pCharacter):
#	print("Move to T")
	debug(__name__ + ", EBMoveFromTToL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_t_l.nif", "EB_stand_t_l")
	kAM.LoadAnimation ("data/animations/EB_chair_T_out.nif", "EB_chair_T_out")
	kAM.LoadAnimation ("data/animations/EB_TtoL1_l.nif", "EB_TtoL1_l")
	kAM.LoadAnimation ("data/animations/EB_door_l1.nif", "EB_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_t_l", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Stand)
	fTime = kAM.GetAnimationLength("EB_stand_t_l")
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "EB_chair_T_out", 0, 0))
	pAnimAction_WalkToLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_TtoL1_l", 0, 0)
	pSequence.AddAction(pAnimAction_WalkToLift, pAnimAction_Stand)
	fTime = fTime + kAM.GetAnimationLength("EB_TtoL1_l")
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_Door_L1", 0, 0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBL1L"))
	pEvent = App.TGIntEvent_Create ()		# Add event to hide character after it gets into the turbolift
	pEvent.SetEventType (App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_HIDDEN)
	pAnimAction.AddCompletedEvent(pEvent)
	pSequence.AddAction(pAnimAction, App.TGAction_CreateNull(), fTime - 1.7)	
	return pSequence

	# lean left animation
def EBTHit(pCharacter):
	debug(__name__ + ", EBTHit")
	return None
	#print("Hit T - animation doesn't exist")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_hit_t.NIF", "EB_hit_t")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	# Lean
	pLeanAction = App.TGAnimAction_Create(pAnimNode, "EB_hit_t", 0, 0)
	pSequence.AddAction(pLeanAction)

	# open eyes and close mouth
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)

	# Return to default.
	pAction = App.CharacterAction_Create (pCharacter, App.CharacterAction.AT_DEFAULT);
	pSequence.AddAction (pAction, pLeanAction)

#	if (App.g_kSystemWrapper.GetRandomNumber(5) == 3):
#		if (pCharacter.GetGender() == 0):
#			pSequence.AddAction(App.TGSoundAction_Create("MaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))
#		else:
#			pSequence.AddAction(App.TGSoundAction_Create("FemaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))

	return pSequence

	# lean hard left animation
def EBTHitHard(pCharacter):
	debug(__name__ + ", EBTHitHard")
	return THit (pCharacter)

# Looking at the other stations
def DBTTalkC(pCharacter):
	debug(__name__ + ", DBTTalkC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_T_Talk_to_C_L.NIF", "DB_T_Talk_to_C_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_T_Talk_to_C_L", 0, 0, 1)
	return pAnimAction1

def DBTTalkE(pCharacter):
	debug(__name__ + ", DBTTalkE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_T_Talk_to_E_L.NIF", "DB_T_Talk_to_E_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_T_Talk_to_E_L", 0, 0, 1)
	return pAnimAction1

def DBTTalkH(pCharacter):
	debug(__name__ + ", DBTTalkH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_T_Talk_to_H_L.NIF", "DB_T_Talk_to_H_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_T_Talk_to_H_L", 0, 0, 1)
	return pAnimAction1

def DBTTalkS(pCharacter):
	debug(__name__ + ", DBTTalkS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_T_Talk_to_S_L.NIF", "DB_T_Talk_to_S_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_T_Talk_to_S_L", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBTTalkX(pCharacter):
	debug(__name__ + ", DBTTalkX")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_T_Talk_X_L.NIF", "DB_T_Talk_X_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_T_Talk_X_L", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBTTalkFinC(pCharacter):
	debug(__name__ + ", DBTTalkFinC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_T_Talk_fin_C_L.NIF", "DB_T_Talk_fin_C_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_T_Talk_fin_C_L", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBTTalkFinE(pCharacter):
	debug(__name__ + ", DBTTalkFinE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_T_Talk_fin_E_L.NIF", "DB_T_Talk_fin_E_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_T_Talk_fin_E_L", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBTTalkFinH(pCharacter):
	debug(__name__ + ", DBTTalkFinH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_T_Talk_fin_H_L.NIF", "DB_T_Talk_fin_H_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_T_Talk_fin_H_L", 0, 0, 1)
	return pAnimAction1

def DBTTalkFinS(pCharacter):
	debug(__name__ + ", DBTTalkFinS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_T_Talk_fin_S_L.NIF", "DB_T_Talk_fin_S_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_T_Talk_fin_S_L", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def DBTTalkFinX(pCharacter):
	debug(__name__ + ", DBTTalkFinX")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/DB_T_Talk_X_L_reverse.NIF", "DB_T_Talk_X_L_reverse")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "DB_T_Talk_X_L_reverse", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

# E-Bridge looks
def EBTTalkC(pCharacter):
	debug(__name__ + ", EBTTalkC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_T_Talk_to_G2_L.NIF", "EB_T_Talk_to_G2_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_T_Talk_to_G2_L", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBTTalkE(pCharacter):
	debug(__name__ + ", EBTTalkE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_T_Talk_to_G3_L.NIF", "EB_T_Talk_to_G3_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_T_Talk_to_G3_L", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBTTalkH(pCharacter):
	debug(__name__ + ", EBTTalkH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_T_Talk_to_H_L.NIF", "EB_T_Talk_to_H_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_T_Talk_to_H_L", 0, 0, 1)
	return pAnimAction1

def EBTTalkS(pCharacter):
	debug(__name__ + ", EBTTalkS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_T_Talk_to_G2_L.NIF", "EB_T_Talk_to_G2_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_T_Talk_to_G2_L", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBTTalkFinC(pCharacter):
	debug(__name__ + ", EBTTalkFinC")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_T_Talk_fin_G2_L.NIF", "EB_T_Talk_fin_G2_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_T_Talk_fin_G2_L", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBTTalkFinE(pCharacter):
	debug(__name__ + ", EBTTalkFinE")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_T_Talk_fin_G3_L.NIF", "EB_T_Talk_fin_G3_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_T_Talk_fin_G3_L", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1

def EBTTalkFinH(pCharacter):
	debug(__name__ + ", EBTTalkFinH")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_T_Talk_fin_H_L.NIF", "EB_T_Talk_fin_H_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_T_Talk_fin_H_L", 0, 0, 1)
	return pAnimAction1

def EBTTalkFinS(pCharacter):
	debug(__name__ + ", EBTTalkFinS")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_T_Talk_fin_G2_L.NIF", "EB_T_Talk_fin_G2_L")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pAnimAction1 = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_T_Talk_fin_G2_L", 0, 0, 1)
	pAnimAction1.SetDuration(0.5)
	return pAnimAction1


####################################################
# Nebula-Bridge Animations
####################################################

	# Place at T
def NebPlaceAtT(pCharacter):
#	print("Place T")
	debug(__name__ + ", NebPlaceAtT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_stand_t_l.nif", "Neb_stand_t_l")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "Neb_stand_t_l")
	pSequence.AddAction(pAction)
	return pSequence

	# Place at L1
def NebPlaceAtL1(pCharacter):
	debug(__name__ + ", NebPlaceAtL1")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_L1toT_l.nif", "Neb_L1toT_l")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimPosition_Create(pAnimNode, "Neb_L1toTt_l")
	pSequence.AddAction(pAction)
	return pSequence

	# Seat at T
def NebSeatedT(pCharacter):
#	print("Seated T")
	debug(__name__ + ", NebSeatedT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_seated_t_l.nif", "Neb_seated_t_l")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "Neb_seated_t_l", 0, 0, 1)
	pSequence.AddAction(pAction)
	return pSequence

	# Turn T towards captain large
def NebTurnAtTTowardsCaptain(pCharacter):
#	print("Turn T")
	debug(__name__ + ", NebTurnAtTTowardsCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_face_capt_t.nif", "Neb_face_capt_t")
	kAM.LoadAnimation ("data/animations/Neb_chair_T_face_capt.nif", "Neb_chair_T_face_capt")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_face_capt_t", 0, 0, 1), pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "Neb_chair_T_face_capt", 0, 0), pOpenEyes)
	return pSequence

	# Turn back T from looking at captain
def NebTurnBackAtTFromCaptain(pCharacter):
#	print("Turn Back T")
	debug(__name__ + ", NebTurnBackAtTFromCaptain")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/Neb_face_capt_reverse.nif", "Neb_face_capt_t_reverse")
	kAM.LoadAnimation ("data/animations/Neb_chair_T_face_capt_reverse.nif", "Neb_chair_T_face_capt_reverse")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pCharacter.GetAnimNode(), "Neb_face_capt_t_reverse", 0, 0, 1), pOpenEyes)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "Neb_chair_T_face_capt_reverse", 0, 0), pOpenEyes)
	return pSequence

	# From L1 to T
def EBMoveFromL1ToT(pCharacter):
#	print("Move to L1 T")
	debug(__name__ + ", EBMoveFromL1ToT")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_L1toT_l.nif", "EB_L1toT_l")
	kAM.LoadAnimation ("data/animations/EB_sit_T_l.nif", "EB_sit_T_l")
	kAM.LoadAnimation ("data/animations/EB_chair_T_in.nif", "EB_chair_T_in")
	kAM.LoadAnimation ("data/animations/EB_door_l1.nif", "EB_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimAction_WalkFromLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_L1toT_l", 0, 0, 1)
	pSequence.AddAction(pAnimAction_WalkFromLift)
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "EB_Door_L1", 0, 0), App.TGAction_CreateNull(), 0.125)
	pAnimAction_Sit = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_sit_T_l", 0, 0)
	pSequence.AddAction(pAnimAction_Sit, pAnimAction_WalkFromLift, 0.0)
	fTime = kAM.GetAnimationLength("EB_sit_T_l")
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_chair_T_in", 0, 0)
	pSequence.AddAction(pAnimAction, pAnimAction_WalkFromLift)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBTactical"))
	pEvent = App.TGIntEvent_Create ()
	pEvent.SetEventType (App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_SEATED)
	pSequence.AddCompletedEvent(pEvent)
	return pSequence

	# From T to L1
#def EBMoveFromTToL1(pCharacter):
#	print("Move to T")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/EB_stand_t_l.nif", "EB_stand_t_l")
	kAM.LoadAnimation ("data/animations/EB_chair_T_out.nif", "EB_chair_T_out")
	kAM.LoadAnimation ("data/animations/EB_TtoL1_l.nif", "EB_TtoL1_l")
	kAM.LoadAnimation ("data/animations/EB_door_l1.nif", "EB_Door_L1")
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridge = pSet.GetObject("bridge")
	pBridgeNode = pBridge.GetAnimNode()
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimAction_Stand = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_stand_t_l", 0, 0, 1)
	pSequence.AddAction(pAnimAction_Stand)
	fTime = kAM.GetAnimationLength("EB_stand_t_l")
	pSequence.AddAction(App.TGAnimAction_Create(pBridgeNode, "EB_chair_T_out", 0, 0))
	pAnimAction_WalkToLift = App.TGAnimAction_Create(pCharacter.GetAnimNode(), "EB_TtoL1_l", 0, 0)
	pSequence.AddAction(pAnimAction_WalkToLift, pAnimAction_Stand)
	fTime = fTime + kAM.GetAnimationLength("EB_TtoL1_l")
	pAnimAction = App.TGAnimAction_Create(pBridgeNode, "EB_Door_L1", 0, 0)
	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_SET_LOCATION_NAME, "EBL1L"))
	pEvent = App.TGIntEvent_Create ()		# Add event to hide character after it gets into the turbolift
	pEvent.SetEventType (App.ET_CHARACTER_ANIMATION_DONE)
	pEvent.SetDestination (pCharacter)
	pEvent.SetInt (App.CharacterClass.CS_HIDDEN)
	pAnimAction.AddCompletedEvent(pEvent)
	pSequence.AddAction(pAnimAction, App.TGAction_CreateNull(), fTime - 1.7)	
	return pSequence

	# lean left animation
def NebTHit(pCharacter):
	debug(__name__ + ", NebTHit")
	return None
	#print("Hit T - animation doesn't exist")
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/db_hit_t.NIF", "Neb_hit_t")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()

	# Lean
	pLeanAction = App.TGAnimAction_Create(pAnimNode, "Neb_hit_t", 0, 0)
	pSequence.AddAction(pLeanAction)

	# open eyes and close mouth
	pOpenEyes = Bridge.Characters.CommonAnimations.EyesOpenMouthClosed(pCharacter)
	pSequence.AddAction(pOpenEyes)

	# Return to default.
	pAction = App.CharacterAction_Create (pCharacter, App.CharacterAction.AT_DEFAULT);
	pSequence.AddAction (pAction, pLeanAction)

#	if (App.g_kSystemWrapper.GetRandomNumber(5) == 3):
#		if (pCharacter.GetGender() == 0):#
#			pSequence.AddAction(App.TGSoundAction_Create("MaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))
#		else:
#			pSequence.AddAction(App.TGSoundAction_Create("FemaleEek"+ str(App.g_kSystemWrapper.GetRandomNumber(7)+1)))

	return pSequence

	# lean hard left animation
def NebTHitHard(pCharacter):
	debug(__name__ + ", NebTHitHard")
	return NebTHit (pCharacter)


#############################################################################################################


###############################################################################
#	TLookAroundConsoleDown, TConsoleInteraction
#	
#	Tactical-specific definitions for these functions
#	
#	Args:	pCharacter		- the character to call on
#	
#	Return:	pSequence	- the created sequence
###############################################################################
def TLookAroundConsoleDown(pCharacter):
	debug(__name__ + ", TLookAroundConsoleDown")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	if not (pCharacter):
		return None

	# Look forward, fore right, and right
	iNumLooks = App.g_kSystemWrapper.GetRandomNumber(4)+2
	pSequence = App.TGSequence_Create()
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumLooks):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(4)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleLookDown(pCharacter)
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleLookDownForeLeft(pCharacter)
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleLookDownForeRight(pCharacter)
		elif (iRandAction == 3):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleLookDownRight(pCharacter)

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence


def DBTConsoleInteraction(pCharacter):
	debug(__name__ + ", DBTConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	if not (pCharacter):
		return None

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
	pSequence = App.TGSequence_Create()
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumPresses):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(10)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_T", "A")
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_T", "B")
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_T", "C")
		elif (iRandAction == 3):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_T", "D")
		elif (iRandAction == 4):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_T", "E")
		elif (iRandAction == 5):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "DB_T", "F")
		elif (iRandAction == 6):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "DB_T", "A")
		elif (iRandAction == 7):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "DB_T", "B")
		elif (iRandAction == 8):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "DB_T", "C")
		elif (iRandAction == 9):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "DB_T", "D")

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence

def NebTConsoleInteraction(pCharacter):
	debug(__name__ + ", NebTConsoleInteraction")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	if not (pCharacter):
		return None

	iNumPresses = App.g_kSystemWrapper.GetRandomNumber(6)+3
	pSequence = App.TGSequence_Create()
	pLastAction = App.TGAction_CreateNull()

	for i in range (iNumPresses):
		iRandAction = App.g_kSystemWrapper.GetRandomNumber(10)

		if (iRandAction == 0):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_T", "A")
		elif (iRandAction == 1):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_T", "B")
		elif (iRandAction == 2):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_T", "C")
		elif (iRandAction == 3):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_T", "D")
		elif (iRandAction == 4):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_T", "E")
		elif (iRandAction == 5):
			pNextAction = Bridge.Characters.CommonAnimations.PushingButtons(pCharacter, "EB_T", "F")
		elif (iRandAction == 6):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "EB_T", "A")
		elif (iRandAction == 7):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "EB_T", "B")
		elif (iRandAction == 8):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "EB_T", "C")
		elif (iRandAction == 9):
			pNextAction = Bridge.Characters.CommonAnimations.ConsoleSlide(pCharacter, "EB_T", "D")

		pSequence.AddAction(pNextAction, pLastAction)
		pLastAction = pNextAction

	pSequence.AppendAction(App.CharacterAction_Create(pCharacter, App.CharacterAction.AT_BREATHE))

	return pSequence


