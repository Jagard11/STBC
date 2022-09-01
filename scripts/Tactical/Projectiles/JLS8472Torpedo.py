import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (0.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((255.0 / 255.0), (153.0 / 255.0), (0.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((255.0 / 255.0), (255.0 / 128.0), (0.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/JLS8472Core.tga', kCoreColor, 0.4, 3.0, 'data/Textures/Tactical/JLS8472Glow.tga', kGlowColor, 0.5, 0.1, 1.2, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 40, 0.8, 0.04)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.19)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    return 0


def GetLaunchSpeed():
    return 65.0


def GetLaunchSound():
    return 'JLS8472Torp'


def GetPowerCost():
    return 25.0


def GetName():
    return 'Energy Discharge'


def GetDamage():
    return 5250.0


def GetGuidanceLifetime():
    return 0.2


def GetMaxAngularAccel():
    return 0.2
