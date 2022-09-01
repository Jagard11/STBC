import App
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.500000, 0.380392, 0.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.500000, 0.870588, 0.602745, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.5, 0.03) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.0015)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(35.0)

def GetLaunchSound():
	return("RailGunA")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Rail Gun")

def GetDamage():
	return 125.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.05

def GetLifetime():
	return 10.0
