# Plays a specific intro video

# Imports
import App
import MissionLib

# Vars
SeqID = App.NULL_ID
pMoviePaneID = App.NULL_ID
bMusicState = 0

# Play the movie
def PlayMovieSeq(s):
        global SeqID, pMoviePaneID

        sMov = "data/Movies/" + s
        
        pMoviePane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pMoviePane)
        pMoviePane.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__ + ".HandleKeyboard")
        pSequence = App.TGSequence_Create()        
        pAction = App.TGScriptAction_Create(__name__, "EnterMovie")
        pSequence.AppendAction(pAction)
        pMovie = App.TGMovieAction_Create(s, 1, 1)
        pMovie.SetSkippable(1)
        pSequence.AppendAction(pMovie)
        pAction = App.TGScriptAction_Create(__name__, "ExitMovie")
        pSequence.AppendAction(pAction)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)

        SeqID = pSequence.GetObjID()
        pMoviePaneID = pMoviePane.GetObjID()

        pSequence.Play()

def EnterMovie(pAction):
        global bMusicState
        
        pTopWindow = App.TopWindow_GetTopWindow()
        if (pTopWindow == None):
                return None

        pTopWindow.SetNotVisible()

        pTopWindow.DisableOptionsMenu(1)
        pTopWindow.AllowMouseInput(0)

        App.g_kUtopiaModule.Pause(1)

        bMusicState = App.g_kMusicManager.IsEnabled()
        
        App.g_kMusicManager.SetEnabled(0)

        App.InterfaceModule_DoTheRightThing()

        return 0

def ExitMovie(pAction):
        global bMusicState 
        
        App.g_kMovieManager.SwitchOutOfMovieMode()

        pTopWindow = App.TopWindow_GetTopWindow()
        if (pTopWindow == None):
                return None

        pTopWindow.SetVisible()

        pTopWindow.DisableOptionsMenu(0)
        pTopWindow.AllowMouseInput(1)

        App.g_kUtopiaModule.Pause(0)

        App.g_kMusicManager.SetEnabled(bMusicState)

        try:
                pTop = App.TopWindow_GetTopWindow()
                pTop.ForceBridgeVisible()
                pTop.ForceTacticalVisible()

        except:
                pass

        return 0

def HandleKeyboard(pPane, pEvent):
        global SeqID

        KeyType = pEvent.GetKeyState()
        CharCode = pEvent.GetUnicode()

        if KeyType == App.TGKeyboardEvent.KS_KEYUP:
                if (CharCode == App.WC_ESCAPE):
                        pSequence = App.TGSequence_Cast(App.TGObject_GetTGObjectPtr(SeqID))
                        try:
                                pSequence.Skip()
                        except:
                                pass

                        SeqID = App.NULL_ID

                        BackToNormal(None)

                        pEvent.SetHandled()

        if (pEvent.EventHandled() == 0):
                if pPane and pEvent:
                        pPane.CallNextHandler(pEvent)

def BackToNormal(pAction):
        global SeqID
        SeqID = App.NULL_ID

        App.g_kMovieManager.SwitchOutOfMovieMode()

        App.g_kUtopiaModule.Pause(0)

        App.g_kMusicManager.SetEnabled(1)

        pTopWindow = App.TopWindow_GetTopWindow()
        if (pTopWindow == None):
                return

        pTopWindow.SetVisible()

        pTopWindow.DisableOptionsMenu(0)
        pTopWindow.AllowMouseInput(1)

        try:
                pTop = App.TopWindow_GetTopWindow()
                pTop.ForceBridgeVisible()
                pTop.ForceTacticalVisible()

        except:
                pass

        pSequence = App.TGSequence_Create()        
        pAct = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAct, 0.1)
        pSequence.Play()

        return 0


def KillPane(pAction):
        global pMoviePaneID

        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pMoviePaneID))
        App.g_kRootWindow.DeleteChild(pPane)

        App.InterfaceModule_DoTheRightThing()

        pMoviePaneID = App.NULL_ID

        return 0
