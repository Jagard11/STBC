from bcdebug import debug
###########################################################################
# Bridge Commander Scripters: The New Generation Basic Function Library
# BCSTNGLib.py -- Version 1.2 -- Last update by USS Sovereign -- 04/03/2006
# by USS Sovereign and Wowbagger
#
# No infringement is intended against LibEngineering or ATP_GUIUtils.  We
# just want to have all the functions we regularly use in one tidy place.
# And there are a lot of them, aren't there?
#
# Update notes: Revised some functions and removed prints and added some
# new functions, mostly updated the library from DS9FX library!
###########################################################################

import App
import MainMenu.mainmenu
import Custom.Autoload.LoadEngineeringExtension
import Foundation
import MissionLib
from Custom.QBautostart.Libs.LibEngineering import GetEngineeringNextEventType

# Grabs a button instance.
def GetButton(sButtonName, sMenuName, sSubMenuName = None):
        debug(__name__ + ", GetButton")
        pMenu   = GetBridgeMenu(sMenuName)
        pButton = pMenu.GetButton(sButtonName)
        if not pButton:
                pSubMenu = pMenu.GetSubmenu(sSubMenuName)
                if not pSubMenu:                        
                        return None
                else:
                        pButton = pSubMenu.GetButton(sButtonName)
                        
        return pButton


# Mirror function for GetButton()
def GetAnyButton(sButtonName, sMenuName, sSubMenuName = None):
        debug(__name__ + ", GetAnyButton")
        GetButton(sButtonName, sMenuName, sSubMenuName)


# Grabs a submenu instance.
def GetSubmenu(sSubMenuName, sMenuName):
        debug(__name__ + ", GetSubmenu")
        pBridgeMenu = GetBridgeMenu(sMenuName)
        pMenu = pBridgeMenu.GetSubmenu(sSubMenuName)
        if not pMenu: 
                return
        return pMenu


# Mirror function fo GetSubmenu()
def GetAnySubmenu(sSubMenuName, sMenuName):
        debug(__name__ + ", GetAnySubmenu")
        GetSubmenu(sSubMenuName, sMenuName)


# Mostly from Defiant's LibEngineering; why mess with a good function?
def CreateButton(sButtonName, sMenuName, Function, sToButton = None, EventInt = 0):        
        debug(__name__ + ", CreateButton")
        pMenu = GetBridgeMenu(sMenuName)

        if sToButton:
                pToButton = pMenu.GetSubmenu(sToButton)
        
        ET_EVENT = App.Mission_GetNextEventType()

        pMenu.AddPythonFuncHandlerForInstance(ET_EVENT, Function)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_EVENT)
        pEvent.SetDestination(pMenu)
        pEvent.SetInt(EventInt)
        pButton = App.STButton_CreateW(App.TGString(sButtonName), pEvent)
    
        if not pToButton:
                pMenu.PrependChild(pButton)
        else:
                pToButton.PrependChild(pButton)

        return pButton


# Deletes a button. 
def DeleteButton(sMenuName, sButtonName, sSubMenuName = None):
        debug(__name__ + ", DeleteButton")
        pButton = GetButton(sMenuName, sButtonName, sSubMenuName)

	pMenu   = GetBridgeMenu(sMenuName)
        if not pMenu:
                return

        #if sSubMenuName != None:
        #        pSubMenu = pMenu.GetSubmenu(sSubMenuName)
        #        if not pSubMenu:
        #                return
        #        pButton = pSubMenu.GetButton(sButtonName)
        #else:
        #	pButton = pMenu.GetButton(sButtonName)

        if pButton:
                pMenu.DeleteChild(pButton)

        return


# Moves buttons from one menu to another.
def MoveButton(sMenuName, sButtonName, sDestinationBridgeMenuName, sDestinationSubMenuName = None):
                # Grab the starting menu.
                debug(__name__ + ", MoveButton")
                pMenu = GetBridgeMenu(sMenuName)
                if not pMenu:
                        return

                # Grab the starting button.    
                pButton = pMenu.GetButton(sButtonName)
                if not pButton:
                        pButton = pMenu.GetSubmenu(sButtonName)
                        if not pButton: 
                                return

                # Copy the button instance before deleting it.
                pButtonCopy = pButton
                pMenu.RemoveChild(pButton)

                # Get the destination menu.
                pDestinationMenu = GetBridgeMenu(sDestinationBridgeMenuName)

                # Add the button to the menu/submenu.
                if sDestinationSubMenuName:
                        pDestinationSubMenu = pDestinationMenu.GetSubmenu(sDestinationSubMenuName)
                        if not pDestinationSubMenu:
                                return
                        pDestinationSubMenu.PrependChild(pButtonCopy)
                else:
                        pDestinationMenu.PrependChild(pButtonCopy)


# Makes and places text entry button.  Based off of/stolen from a function in NanoFX_ConfigMenu.py. 
def CreateTextEntry(pPane, sButtonName, sDefaultButton = "", iButtonWidth = 0.215625, iButtonHeight = 0.02193, pButtonEvent = None):
                # Start with our button, which names the entry box.
                debug(__name__ + ", CreateTextEntry")
                pButton = App.STRoundedButton_CreateW(App.TGString(sButtonName), pButtonEvent, iButtonWidth, iButtonHeight)
                pButton.SetDisabledColor(App.g_kMainMenuBorderMainColor)
                pButton.SetDisabled (0)
                pButton.SetColorBasedOnFlags()
                pButton.SetVisible()

                fButtonWidth = pButton.GetWidth()
                fButtonHeight = pButton.GetHeight()

                # Create a pane for the box.
                pTextPane = App.TGPane_Create(fButtonWidth, 1.0)
                LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

                # Create the text tag
                pText = App.TGParagraph_CreateW(App.TGString(sDefaultButton))
                fTextWidth = pText.GetWidth()
                pTextPane.AddChild(pText, fTextWidth, 0)
                        
                ## Create the name entry button
                pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
                pcLCARS = pGraphicsMode.GetLcarsString()

                # Create the default string.
                GoFlightSmallFont()
                pTextEntry = App.TGParagraph_CreateW(App.TGString(sDefaultButton))
                pTextEntry.Resize(fButtonWidth - fTextWidth, pTextEntry.GetHeight(), 0)
                pTextEntry.SetReadOnly(0)
                GoSmallFont()

                pTextPane.AddChild(pTextEntry, fButtonWidth + 0.005, (LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT - pTextEntry.GetHeight()) / 2.0)

                pBackground = App.TGIcon_Create(pcLCARS, 200, App.g_kTextEntryColor)
                pBackground.Resize(fButtonWidth - fTextWidth, LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT, 0)
                pTextPane.AddChild(pBackground, fTextWidth, 0)

                # Now resize the pane to be the height of text entry
                pTextPane.Resize(fButtonWidth, LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT + 0.008, 0)

                pPane.AddChild(pButton)

                pText = App.TGParagraph_Cast(pTextPane.GetNthChild(1))
            	pPane.AddChild(pText, pButton.GetLeft() + fButtonWidth + 0.003, pButton.GetTop() - pButton.GetHeight(), 0)
                pText.SetVisible()

                return pButton, pTextPane, pText


# Mostly from SetVolumeButton made by Totally Games -- USS Sovereign, this code is used to create a warp slidebar in new change warp speed
def CreateSliderbar (pName, eType, fValue, RangeMin = 0.0, RangeMax = 1.0, Width = 0.2, Height = 0.0364):
	debug(__name__ + ", CreateSliderbar")
	pTopWindow = App.TopWindow_GetTopWindow()
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	pBar = App.STNumericBar_Create ()

        # set our range 
	pBar.SetRange(RangeMin, RangeMax)
	pBar.SetKeyInterval(0.1)
	pBar.SetMarkerValue(1.0)
	pBar.SetValue(fValue)
	pBar.SetUseMarker(0)
	pBar.SetUseAlternateColor(0)
	pBar.SetUseButtons(0)

	kNormalColor = App.g_kSTMenu3NormalBase
	kEmptyColor = App.g_kSTMenu3Disabled

	pBar.SetNormalColor(kNormalColor)
	pBar.SetEmptyColor(kEmptyColor)
	pText = pBar.GetText()
	pText.SetStringW(pName)

	pBar.Resize (Width, Height, 0)

	pEvent = App.TGFloatEvent_Create ()
	pEvent.SetDestination(pOptionsWindow)
	pEvent.SetFloat (fValue)
	pEvent.SetEventType(eType)

	pBar.SetUpdateEvent(pEvent)

	return pBar        

# Makes a submenu for a given bridge menu.	
def CreateMenu(sNewMenuName, sBridgeMenuName, bAppend = 0):
	debug(__name__ + ", CreateMenu")
	pMenu = GetBridgeMenu(sBridgeMenuName)
       	pNewMenu = App.STMenu_Create(sNewMenuName)
        if bAppend == 1:
        	pMenu.AddChild(pNewMenu)
        else:
        	pMenu.PrependChild(pNewMenu)

        return pNewMenu


# Specially just for engineering fix ;)  Adds buttons BELOW the main part of
# Brex's menu (or, in theory, anyone else's).
def CreateEngineerMenu(NewMenuName, BridgeMenuName):
	debug(__name__ + ", CreateEngineerMenu")
	pMenu = GetBridgeMenu(BridgeMenuName)
       	pDropDownMenu = App.STMenu_Create(NewMenuName)
	pMenu.AddChild(pDropDownMenu)

        # this is where the magic happens and it fixes the issues, in the future I might be able to fix it even further but
        # I don't see a way to do it ATM
	pLowest = FindLowestChild(pMenu)
	pDropDownMenu.SetPosition(pLowest.GetLeft(), pLowest.GetBottom(), 0)

	pMenu.AddChild(None)

        return pDropDownMenu


# From ATP Library.  Needed for our fix; a bit modified but nothing major.
# Just a bit improved to be honest ;) --Sovereign
def FindLowestChild(Pane):
        debug(__name__ + ", FindLowestChild")
        Index = Pane.GetTrueNumChildren() - 1
        iBottom = 0
        LowestChild = None
        Current = None
        while Index >= 0:
            Current = Pane.GetTrueNthChild(Index)
            CurrentBottom = Current.GetBottom()
            if(CurrentBottom > iBottom):
                iBottom = CurrentBottom
                LowestChild = Current
            Index = Index - 1
        return LowestChild


# From ATP_GUIUtils -- From The Notes Of USS SOVEREIGN: Very useful.  ;)
def GetBridgeMenu(menuName):
	debug(__name__ + ", GetBridgeMenu")
	pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	if(pDatabase is None):
		return
	App.g_kLocalizationManager.Unload(pDatabase)
	return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))


# Mirror function for BCSTNGLib.
def GetNextEventType():
        debug(__name__ + ", GetNextEventType")
        return App.Mission_GetNextEventType()


# A simpler version of the timer creator from MissionLib.  Added to help certain poor slobs in BCS: TNG who may or may not wear four pips.
# A more customizable version is available in the MissionLib.
# **NOTE: This function not compatible with MissionLib.DeleteAllMissionTimers()/DeleteAllEpisodeTimers().**
def CreateTimer(sFunctionHandler, fCountdownTime):
	# Setup the handler function.
	debug(__name__ + ", CreateTimer")
	pGame = App.Game_GetCurrentGame()
	if (pGame == None):
		return None
	pEpisode = pGame.GetCurrentEpisode()
	if (pEpisode == None):
		return None
	pMission = pEpisode.GetCurrentMission()
	if (pMission == None):
		return None

	pMission.AddPythonFuncHandlerForInstance(GetEngineeringNextEventType(), sFunctionHandler)

	# Create the event and the event timer.
	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(GetEngineeringNextEventType())
	pEvent.SetDestination(pMission)
	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + fCountdownTime)
	pTimer.SetDelay(0)
	pTimer.SetDuration(0)
	pTimer.SetEvent(pEvent)

        # Add the timer to the game.
	App.g_kTimerManager.AddTimer(pTimer)
	
	return pTimer


# A companion to CreateTimer().
def DeleteTimer(pTimer):
        debug(__name__ + ", DeleteTimer")
        try:
            App.g_kTimerManager.DeleteTimer(pTimer.GetObjID())
            App.g_kRealtimeTimerManager.DeleteTimer(pTimer.GetObjID())
        except AttributeError:
            #print "Timer already deleted.  Proceed."
            pass


# From QBautostart. Again, why mess with a good function?
def AddKeyBind(KeyName, Function, EventInt = 0, Group = "General", eType = App.KeyboardBinding.GET_INT_EVENT):
	debug(__name__ + ", AddKeyBind")
	if not hasattr(Foundation, "g_kKeyBucket"):
		return
        mode = Custom.Autoload.LoadEngineeringExtension.mode
        pMission = MissionLib.GetMission()
        ET_KEY_EVENT = GetNextEventType()
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_KEY_EVENT, pMission, Function)
        Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig(KeyName, KeyName, ET_KEY_EVENT, eType, EventInt, Group, dict = {"modes": [mode]}))


def GoFlightSmallFont():
            debug(__name__ + ", GoFlightSmallFont")
            App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])
            return

def GoSmallFont():
            debug(__name__ + ", GoSmallFont")
            App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont, MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])
            return

def GoLargeFont():
            debug(__name__ + ", GoLargeFont")
            App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcLargeFont, MainMenu.mainmenu.g_kLargeFontSize[MainMenu.mainmenu.g_iRes])
            return


# A great way to do... well, a lot of things.  Very usefyl
def CheckActiveMutator(MutatorName):
        debug(__name__ + ", CheckActiveMutator")
        Foundation.LoadConfig()
	for i in Foundation.mutatorList._arrayList:
		fdtnMode = Foundation.mutatorList._keyList[i]
		if fdtnMode.IsEnabled() and (fdtnMode.name == MutatorName):
			return 1
	return 0


# Set Friendly AI - I noticed a flaw in qbautos version it said friendly ai but
# was actually enemy ai -- Sovvy
def CreateEnemyAI(pShip):
        debug(__name__ + ", CreateEnemyAI")
        pEnemies        = MissionLib.GetEnemyGroup()
        if not pEnemies.GetNameTuple():
            pEnemies.AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI Attack at (194, 57)
	import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, pEnemies, Difficulty = 1, FollowTargetThroughWarp=1, UseCloaking=1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 12, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (41, 304)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pWait)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles


# also fixed up
def CreateFriendlyAI(pShip):
        debug(__name__ + ", CreateFriendlyAI")
        pFriendlies     = MissionLib.GetFriendlyGroup()
	#########################################
	# Creating CompoundAI Attack at (108, 133)
	import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, pFriendlies, Difficulty = 1, FollowTargetThroughWarp = 1, UseCloaking = 1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating PlainAI Turn at (237, 47)
	pTurn = App.PlainAI_Create(pShip, "Turn")
	pTurn.SetScriptModule("ManeuverLoop")
	pTurn.SetInterruptable(1)
	pScript = pTurn.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelLeft())
	# Done creating PlainAI Turn
	#########################################
	#########################################
	# Creating PlainAI Turn_2 at (353, 55)
	pTurn_2 = App.PlainAI_Create(pShip, "Turn_2")
	pTurn_2.SetScriptModule("ManeuverLoop")
	pTurn_2.SetInterruptable(1)
	pScript = pTurn_2.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelRight())
	# Done creating PlainAI Turn_2
	#########################################
	#########################################
	# Creating PlainAI Turn_3 at (429, 103)
	pTurn_3 = App.PlainAI_Create(pShip, "Turn_3")
	pTurn_3.SetScriptModule("ManeuverLoop")
	pTurn_3.SetInterruptable(1)
	pScript = pTurn_3.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelUp())
	# Done creating PlainAI Turn_3
	#########################################
	#########################################
	# Creating PlainAI Turn_4 at (448, 147)
	pTurn_4 = App.PlainAI_Create(pShip, "Turn_4")
	pTurn_4.SetScriptModule("ManeuverLoop")
	pTurn_4.SetInterruptable(1)
	pScript = pTurn_4.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelDown())
	# Done creating PlainAI Turn_4
	#########################################
	#########################################
	# Creating RandomAI FlyPointlessly at (198, 181)
	pFlyPointlessly = App.RandomAI_Create(pShip, "FlyPointlessly")
	pFlyPointlessly.SetInterruptable(1)
	# SeqBlock is at (309, 185)
	pFlyPointlessly.AddAI(pTurn)
	pFlyPointlessly.AddAI(pTurn_2)
	pFlyPointlessly.AddAI(pTurn_3)
	pFlyPointlessly.AddAI(pTurn_4)
	# Done creating RandomAI FlyPointlessly
	#########################################
	#########################################
	# Creating SequenceAI RepeatForever at (195, 224)
	pRepeatForever = App.SequenceAI_Create(pShip, "RepeatForever")
	pRepeatForever.SetInterruptable(1)
	pRepeatForever.SetLoopCount(-1)
	pRepeatForever.SetResetIfInterrupted(1)
	pRepeatForever.SetDoubleCheckAllDone(1)
	pRepeatForever.SetSkipDormant(0)
	# SeqBlock is at (295, 228)
	pRepeatForever.AddAI(pFlyPointlessly)
	# Done creating SequenceAI RepeatForever
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (30, 228)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (149, 235)
	pPriorityList.AddAI(pAttack, 1)
	pPriorityList.AddAI(pRepeatForever, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (29, 285)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (29, 332)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 12, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAvoidObstacles)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait

# also fixed up
def CreateStarbaseEnemyAI(pShip):
        debug(__name__ + ", CreateStarbaseEnemyAI")
        pEnemies        = MissionLib.GetEnemyGroup()
        if not pEnemies.GetNameTuple():
            pEnemies.AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI StarbaseAttack at (194, 57)
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, pEnemies)
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pStarbaseAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait

# also fixed up
def CreateStarbaseFriendlyAI(pShip):
        debug(__name__ + ", CreateStarbaseFriendlyAI")
        pFriendlies     = MissionLib.GetFriendlyGroup()
	#########################################
	# Creating CompoundAI StarbaseAttack at (194, 57)
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, pFriendlies)
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pStarbaseAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait

