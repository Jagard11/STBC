# by USS Sovereign

# Imports
import App
import Foundation
import MissionLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import JumpspaceConfiguration

# GFX Folder
GFX = 'scripts/Custom/Jumpspace/GFX/'

# Load the GFX animation
def StartGFX():
                pPlayer = MissionLib.GetPlayer()
                pModule = __import__(pPlayer.GetScript())

                # Is there a customization for this ship available?
                if hasattr(pModule, "JumpspaceCustomizations"):
                    pCustomization = pModule.JumpspaceCustomizations()
                    
                    # Customization exists, but does the flash entry exist?
                    if pCustomization.has_key('FlashAnimation'):
                        # Yes it does exist!
                        pFlash = "scripts/Custom/Jumpspace/GFX/" + pCustomization['FlashAnimation']
                        
                        LoadGFX(4, 4, pFlash)

                    else:
                        # There doesn't seem to be an entry of a custom flash for this ship so check for user defined ones
                        reload(JumpspaceConfiguration)
                        
                        if JumpspaceConfiguration.FlashGFX == 'Default':
                            LoadGFX(4, 4, GFX + "JumpspaceFlash.tga")
                            
                        else:
                            pFlash = "scripts/Custom/Jumpspace/GFX/" + JumpspaceConfiguration.FlashGFX

                            LoadGFX(4, 4, pFlash)

                # No customizations available for this ship, now checking for user defined stuff
                else:
                        reload(JumpspaceConfiguration)
                        
                        if JumpspaceConfiguration.FlashGFX == 'Default':
                            LoadGFX(4, 4, GFX + "JumpspaceFlash.tga")
                            
                        else:
                            pFlash = "scripts/Custom/Jumpspace/GFX/" + JumpspaceConfiguration.FlashGFX

                            LoadGFX(4, 4, pFlash)
def EndFlashGFX():
                #print 'the Jumpspace exit GFX should be loading now...'   
                LoadGFX(4, 4, GFX + "JumpspaceFlashExit.tga")
                #print 'the SigmaJumpspaceFlashExit.tga should be seen now...'   
def SigmaFlashGFX():
                #print 'the Sigma Transdimensional Drive GFX should be loading now...'   
                LoadGFX(4, 4, GFX + "SigmaJumpspaceFlash.tga")
                #print 'the SigmaJumpspaceFlash.tga should be seen now...'   

# Create flash effect on a ship
def CreateGFX(pShip):
		pAttachTo = pShip.GetNode()
                fSize = pShip.GetRadius() * 5
		pSequence = App.TGSequence_Create()	
		pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())

                sFile = GetTexture()
                fLifeTime = 1
                fRed = 255.0
                fGreen = 255.0
                fBlue = 255.0
                fBrightness = 0.8
                fSpeed = 1
       
		pEffect = App.AnimTSParticleController_Create()
		pEffect.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
		pEffect.AddColorKey(1.0, fRed / 255, fGreen / 255, fBlue / 255)
		pEffect.AddAlphaKey(0.0, 1.0)
		pEffect.AddAlphaKey(1.0, 1.0)
		pEffect.AddSizeKey(0.0, fSize)
		pEffect.AddSizeKey(1.0, fSize)
		
                pEffect.SetEmitLife(fSpeed)
                pEffect.SetEmitFrequency(1)
                pEffect.SetEffectLifeTime(fSpeed + fLifeTime)
                pEffect.SetInheritsVelocity(0)
                pEffect.SetDetachEmitObject(0)
                pEffect.CreateTarget(sFile)
                pEffect.SetTargetAlphaBlendModes(0, 7)
                pEffect.SetEmitFromObject(pEmitFrom)
                pEffect.AttachEffect(pAttachTo)                
                fEffect = App.EffectAction_Create(pEffect)
                pSequence.AddAction(fEffect)
                pSequence.Play ()
                
                return
                
def B5CreateGFX(pShip):
		pAttachTo = pShip.GetNode()
                fSize = pShip.GetRadius() * 5
		pSequence = App.TGSequence_Create()	
		pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())

                sFile = B5GetTexture()
                fLifeTime = 1
                fRed = 200.0
                fGreen = 255.0
                fBlue = 255.0
                fBrightness = 0.8
                fSpeed = 1
       
		pEffect = App.AnimTSParticleController_Create()
		pEffect.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
		pEffect.AddColorKey(1.0, fRed / 255, fGreen / 255, fBlue / 255)
		pEffect.AddAlphaKey(0.0, 1.0)
		pEffect.AddAlphaKey(1.0, 1.0)
		pEffect.AddSizeKey(0.0, fSize)
		pEffect.AddSizeKey(1.0, fSize)
		
                pEffect.SetEmitLife(fSpeed)
                pEffect.SetEmitFrequency(1)
                pEffect.SetEffectLifeTime(fSpeed + fLifeTime)
                pEffect.SetInheritsVelocity(0)
                pEffect.SetDetachEmitObject(0)
                pEffect.CreateTarget(sFile)
                pEffect.SetTargetAlphaBlendModes(0, 7)
                pEffect.SetEmitFromObject(pEmitFrom)
                pEffect.AttachEffect(pAttachTo)                
                fEffect = App.EffectAction_Create(pEffect)
                pSequence.AddAction(fEffect)
                pSequence.Play ()
                
                return

def B5SigmaCreateGFX(pShip):
		pAttachTo = pShip.GetNode()
                fSize = pShip.GetRadius() * 5
		pSequence = App.TGSequence_Create()	
		pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())

                sFile = B5SigmaGetTexture()
                fLifeTime = 1
                fRed = 200.0
                fGreen = 255.0
                fBlue = 255.0
                fBrightness = 1.0
                fSpeed = 1
       
		pEffect = App.AnimTSParticleController_Create()
		pEffect.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
		pEffect.AddColorKey(1.0, fRed / 255, fGreen / 255, fBlue / 255)
		pEffect.AddAlphaKey(0.0, 1.0)
		pEffect.AddAlphaKey(1.0, 1.0)
		pEffect.AddSizeKey(0.0, fSize)
		pEffect.AddSizeKey(1.0, fSize)
		
                pEffect.SetEmitLife(fSpeed)
                pEffect.SetEmitFrequency(1)
                pEffect.SetEffectLifeTime(fSpeed + fLifeTime)
                pEffect.SetInheritsVelocity(0)
                pEffect.SetDetachEmitObject(0)
                pEffect.CreateTarget(sFile)
                pEffect.SetTargetAlphaBlendModes(0, 7)
                pEffect.SetEmitFromObject(pEmitFrom)
                pEffect.AttachEffect(pAttachTo)                
                fEffect = App.EffectAction_Create(pEffect)
                pSequence.AddAction(fEffect)
                pSequence.Play ()
                
                return

# Returns texture filename
def GetTexture():
                pPlayer = MissionLib.GetPlayer()
                pModule = __import__(pPlayer.GetScript())

                # Is there a customization for this ship available?
                if hasattr(pModule, "JumpspaceCustomizations"):
                    pCustomization = pModule.JumpspaceCustomizations()
                    
                    # Customization exists, but does the flash entry exist?
                    if pCustomization.has_key('FlashAnimation'):
                        # Yes it does exist!
                        strFile = GFX + pCustomization['FlashAnimation']
                        
                    else:
                         # There doesn't seem to be an entry of a custom flash for this ship
                        reload(JumpspaceConfiguration)
                        
                        if JumpspaceConfiguration.FlashGFX == 'Default':
                            strFile = GFX + "JumpspaceFlash.tga"
                            
                        else:
                            strFile = GFX + JumpspaceConfiguration.FlashGFX

                # No customizations available for this ship
                else:
                        reload(JumpspaceConfiguration)
                        
                        if JumpspaceConfiguration.FlashGFX == 'Default':
                            strFile = GFX + "JumpspaceFlash.tga"
                            
                        else:
                            strFile = GFX + JumpspaceConfiguration.FlashGFX
                
                return strFile
def B5GetTexture():
                strFile = GFX + "JumpspaceFlashExit.tga"
                return strFile
def B5SigmaGetTexture():
                strFile = GFX + "SigmaJumpspaceFlash.tga"
                return strFile


# Loads textures
def LoadGFX(iNumXFrames, iNumYFrames, sFile):
                fX = 0.0
                fY = 0.0

                pContainer = App.g_kTextureAnimManager.AddContainer(sFile)   
                pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)
                for index in range(iNumXFrames * iNumYFrames):
                        pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
                        fX = fX + (1.0 / iNumXFrames)

                        if (fX == 1.0):
                            fX = 0.0
                            fY = fY + (1.0 / iNumYFrames)
