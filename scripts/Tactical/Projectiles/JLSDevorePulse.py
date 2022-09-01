###############################################################################
#	Filename:	JLSKrenimPulse.py
#	
#	Modified:	8/18/02 -	
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.600000, 0.600000, 0.800000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.800000, 0.700000, 1.000000, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.80, 0.20) 	

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLifetime():
        return 60

def GetLaunchSpeed():
	return(65)

def GetLaunchSound():
	return("JLSDevoreP")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Polaron Torpedo")

def GetDamage():
	return 1300

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 1000

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 1300

def GetGuidanceLifetime():
	return 1.0

def GetMaxAngularAccel():
	return 1.5