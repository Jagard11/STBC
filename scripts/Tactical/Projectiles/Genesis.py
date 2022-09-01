import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (255.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((149.0 / 255.0), (192.0 / 255.0), (76.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((149.0 / 295.0), (1920.0 / 25.0), (76.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/PoleronCore.tga', kCoreColor, 0.6, 1.0, 'data/Textures/Tactical/PoleronCore.tga', kGlowColor, 1.0, 0.8, 3.3, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 44, 1.7, 0.1)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.9)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.POSITRON)
    return 0


def GetLaunchSpeed():
    return 33.8


def GetLaunchSound():
    return 'Quantum Torpedo'


def GetPowerCost():
    return 10.0


def GetName():
    return 'Genesis Device'


def GetDamage():
    return 9000.0


def GetGuidanceLifetime():
    return 1.0


def GetMaxAngularAccel():
    return 3.0

