Star Trek: Bridge Commander Patch README
----------------------------------------

Fixes:
+ Added capability for multiplayer hosts to ban players
+ Problem in E6M5 with shuttles sometimes not leaving the planet, which means the mission cannot be completed.
+ Zhukov registry texture being upside-down
+ Fixed "redshirts" getting stuck in an animation after falling down
+ Multiplayer names containing '[' causing problems when restarting the game.  If you believe that your copy of the game suffers from this problem, please delete the config file, that is found where you installed the game, before launching and repatching.
+ Better support for adding custom missions

PLEASE NOTE:  If you install the patch to the wrong directory or cancel the patch installation, then you will need to reinstall "Bridge Commander" before you can apply the patch correctly.  Also, if you need to reinstall the patch, please reinstall the game prior to reinstalling the patch.

Multiplayer Banning
-------------------

Multiplayer hosts can now ban players from their server. You can access this capability from the
multiplayer menu (hitting Esc during play) -- it works similarly to the Boot option already there.
Click on a player's name, then click Ban, and their IP address will no longer be allowed to connect
to your server.

Banned IPs are saved, so they will be remembered across multiplayer sessions. They will be placed in 
the file 'banlist.txt', in the Bridge Commander directory. You can edit this file by hand to add or
remove IP addresses if you wish. There should be one address per line in the text file.

When editing by hand, you can also ban ranges of IPs by replacing a part of the address with '255'.
For example, to ban everyone from 127.0.0.x (where x is any number), add this to 'banlist.txt':

	127.0.0.255

