import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (255.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (255.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((255.0 / 255.0), (96.0 / 255.0), (0.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/TorpedoCore.tga', kCoreColor, 0.5, 1.0, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 4.0, 0.2, 0.7, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 32, 0.2, 0.7)
    pTorp.SetDamage(700000)
    pTorp.SetDamageRadiusFactor(0.19)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUMTORPEDO)
    return 0


def GetLaunchSpeed():
    return 30


def GetLaunchSound():
    return 'Plasma1'


def GetPowerCost():
    return 20.0


def GetName():
    return 'T.Plasma'


def GetDamage():
    return 1000.0


def GetGuidanceLifetime():
    return 40.0


def GetMaxAngularAccel():
    return 0.15

