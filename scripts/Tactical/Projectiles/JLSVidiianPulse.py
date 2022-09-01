###############################################################################
#	Filename:	JLSKrenimPulse.py
#	
#	Modified:	8/18/02 -	
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a Krenim disruptor blast which goes through shields.
#	
#	Args:	pTorp - the "torpedo", ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 0.800000, 0.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 1.000000, 0.500000, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.0, 0.30) 	

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
	return(45)

def GetLaunchSound():
	return("JLSVidiianP")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Polaron Torpedo")

def GetDamage():
	return 1200

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 900

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 1200

def GetGuidanceLifetime():
	return 0.9

def GetMaxAngularAccel():
	return 2.5