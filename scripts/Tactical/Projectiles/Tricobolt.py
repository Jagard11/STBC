import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((240.0 / 255.0), (240.0 / 255.0), (240.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((100.0 / 255.0), (40.0 / 255.0), (240.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((80.0 / 255.0), (200.0 / 255.0), (207.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/TorpedoCore.tga', kCoreColor, 0.2, 1.0, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 4.0, 0.2, 0.7, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 6, 0.7, 0.4)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.19)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHASEDPLASMA)
    return 0


def GetLaunchSpeed():
    return 20


def GetLaunchSound():
	return("Tricobolt")


def GetPowerCost():
    return 50.0


def GetName():
    return 'Tri-Cobolt'


def GetDamage():
    return 2750.0


def GetGuidanceLifetime():
    return 10.0


def GetMaxAngularAccel():
    return 0.15

