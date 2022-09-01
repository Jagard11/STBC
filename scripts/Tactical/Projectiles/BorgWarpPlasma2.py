########################################################################
#	Filename:	BorgWarpPlasma2.py			       #
#								       #
#	Description:	Creates a Borg Warp Plasma torpedo	       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (255.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((149.0 / 255.0), (192.0 / 255.0), (76.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((149.0 / 255.0), (192.0 / 255.0), (76.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/TorpedoCore.tga', kCoreColor, 0.3, 1.0, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 4.0, 0.9, 1.7, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 24, 0.9, 0.04)
    pTorp.SetDamage(1500.0)
    pTorp.SetDamageRadiusFactor(0.4)
    pTorp.SetGuidanceLifetime(60.0)
    pTorp.SetMaxAngularAccel(0.2)
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.POSITRON)
    return 0

def GetLaunchSpeed():
    return 65.0

def GetLaunchSound():
    return("Warp Plasma Torpedo")

def GetPowerCost():
    return 10.0

def GetName():
    return("Warp Plasma")