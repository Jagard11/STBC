from bcdebug import debug
##########################################################################################################################
#        Race Plugin script   (created by the Race Plugin Creator Tool (v1.0.0.0)
###########
# this script sets up a race and info about her that some mods like Construct, Distress Signal (Distress call), and
# Galaxy Charts uses, to get a race's ship, escorts, and other things.
##########################################################################################################################

########
##  Name of this race
sName = "Klingon"

########
## List of strings containing the names of the enemy races  (put a "ALL" to make it enemy to everybody)
lEnemies = ["Borg", "Breen", "Cardassian", "Dominion", "8472", "Sona", "Romulan"]

########
## List of strings containing the names of the friendly races
lFriendlies = ["Federation"]

########
## a float representing the peace value  (in the range of 0 to 1, being 1 the most peacefull races )
fPeaceValue = 0.10

########
## the name of the ship selecting menu (you know, in QuickBattle), in which we can look for ships to add to this race
sLookInMenu = "Klingon Ships"

########
## list of the ship script name  of ships of this race, to be added manually (that is, besides looking in the above 
## mentioned menu)
lDefaultShips = ["BirdOfPrey", "Vorcha", "CloakFireBirdOfPrey", "FeklhrMK2", "KTinga", "KlingonShuttle", "Kvort", "MPneghvar", "Neghvar", "ftbneghvar", ]

########
## dictionary showing the escorts of a ship class  (for a example, check the Dominion race script)
## "ship class to be escorted": list of ship classes that escort it
dEscorts = {
}

########
## list of the ship script name of starbase ships of this race, to be added manually (that is, besides looking in the
## above mentioned menu)
lDefaultBases = ["KlingonImperialStarbase", ]

########
## the name of the ship selecting menu (you know, in QuickBattle), in which we can look for ships to add to this race
sInitialShipBuild = "KlingonShuttle"

########
## Dictionary of resources of this race
## "resource name": amount of resources
dResources = {
}

########
## A list of names of ships of this race
lShipNames = [
"IKS NI'yIN",
"IKS Non'urgh",
"IKS Qun'jIH",
"IKS Nagh'SIS",
"IKS Pol'Quj",
"IKS Jach'Saj",
"IKS JorwI'apoq",
"IKS Sup'tIch",
"IKS HoH'bIH",
"IKS 'Iw'pub",
"IKS YepHa'Hub",
"IKS Qut'a'Dol",
"IKS LeSpoH'qI'",
"IKS WIH'Hotlh",
"IKS JIH'wIv",
"IKS NgeH'che'",
"IKS Chaq ta'Soppu'bogh",
"IKS Ghew'e'lo'wamwl",
"IKS Qa'ang",
"IKS Sop ghaH",
"IKS Qi'tu'Daq",
"IKS QaStaHvis",
"IKS Ghah'ochDaq",
"IKS Pa'ylnejll",
"IKS Hur Daq",
"IKS LuDech",
"IKS Vav buSba",
"IKS Qechvam",
"IKS Qelqa'lu'neSQo'jaj",
"IKS DaHjaj'oh",
"IKS Ghel'Di'ylaj",
"IKS Bangjaj'e",
"IKS QorwaghDaq",
"IKS TuQpa",
"IKS BasDaS",
"IKS Jach Pagh",
"IKS SuH'ovelya",
"IKS MpuDl'rlntaH",
"IKS 'lHbogh",
"IKS Heghpu'ej",
"IKS Hurgh'ragh",
"IKS TajHu'",
"IKS Duy'Hub",
"IKS Begh'poQ",
"IKS Wuv'a'tem",
"IKS Deb'choS",
"IKS Ghoch'ragh",
"IKS Ghar'Qotlh",
"IKS Qugh'tung",
"IKS Tu'a'rop",
"IKS Nay'par",
"IKS GhoH'Sot",
"IKS Do'Ha'",
"IKS Jiyajbe'",
"IKS VIghajbe'",
"IKS Hijol'peng",
"IKS Mich'pagh",
"IKS Qup'SoH",
"IKS TlhIH'Hu",
"IKS Hob'DIS",
"IKS Chong'pogh",
"IKS TaD'moH",
"IKS Huj'a'SIp",
"IKS Dun'wo'",
"IKS Vut'bol",
"IKS Maw'HeSwI'",
"IKS QuHvaj'Qob",
"IKS Tar'be'",
"IKS Qul'bIQ",
"IKS Jib'lalDan",
"IKS Hegh'QeDp",
"IKS Hob'DIS",
"IKS Qap'ghargh",
"IKS Luq'argh",
"IKS iqaD'nem",
"IKS MajQa'be'",
"IKS Qut'Such",
"IKS NaS'puchpa'",
"IKS LoS'maH",
"IKS Sap'leng",
"IKS JuS'mung",
"IKS RaQpo'juS",
"IKS SID'ghom",
"IKS BIQ'a'ngo'",
"IKS BI'ngo'",
"IKS Dom'SIS",
"IKS Dakh'yi'DIL",
"IKS Qo'",
"IKS Ylje'",
"IKS Yaj'a'",
"IKS Bllugh",
"IKS Jol ylchu'",
"IKS Gho'be'",
"IKS Doh'",
"IKS TIQ'IwSev",
"IKS TIH'Hich",
"IKS HuS'ngeb",
"IKS BImoqu'",
"IKS BInep",
"IKS YijatlhQo'",
"IKS Quoc'Truong",
"IKS Boog'aloo",
"IKS Yach'off",
"IKS Mierda",
"IKS Pen'deHo",
"IKS Azzassin",
"IKS Culo",
"IKS Poon'tang",
"IKS Geez",
"IKS Puto",
"IKS Verga",
"IKS Perra",
"IKS Pedo",
"IKS Caraho",
"IKS MukFug",
"IKS Sug'dik",
"IKS Shagnutz",
"IKS Buk'fug",
"IKS Quak'ho",
"IKS Sheite",
"IKS Azzwiip",
"IKS Booti",
"IKS Qok'azz",
"IKS Batang",
"IKS Chin'gas",
"IKS Chinga'dera",
"IKS Mocho",
"IKS Yerk'ov",
"IKS Boo'gar",
"IKS Scheissa",
"IKS Futza",
"IKS Boo'gi",
"IKS Cra'pola",
"IKS Fuz'nuz",
"IKS Mooki",
"IKS Wisz",
"IKS Ratshiz",
"IKS Budtfug",
"IKS Hrastich",
"IKS Juk'bax",
"IKS Mierda",
"IKS puuq vI'legh",
"IKS DaSpu'",
"IKS Wa'maH cha",
"IKS Ghorgh 'ju",
"IKS Hegh'qang",
"IKS MaDo'choH",
"IKS Ji'SoptaH",
"IKS Pa'vo'yIjaH",
"IKS Visu'Qo",
"IKS Jigz",
"IKS Beet'ov",
"IKS jer'Kov",
"IKS Poon'tang",
"IKS Pul'ga",
"IKS punQazzh",
"IKS nInj'Ah",
"IKS DraKula",
"IKS Ma'maH cha",
"IKS Hoo'chi'maMa",
"IKS Dung'qang",
"IKS ArrmpiT",
"IKS ButHool",
"IKS Piz'on'yaH",
"IKS Eaat'Me",
"IKS Blo'jobba",
"IKS Haba'la'babba",
"IKS farTstnk",
"IKS Baad'smel",
"IKS YeeHa",
"IKS Woohaa",
"IKS Buutfug",
"IKS Azzpikr",
"IKS Eaatshid",
"IKS Horzazz",
"IKS GuufBal",
"IKS Bulshid",
"IKS ouThowz",
"IKS Que'erz",
"IKS Faggz",
"IKS Furtsniif",
"IKS puk oI'lagh",
"IKS Das Puuk'",
"IKS Wa'maH cha",
"IKS Ghorgh'wiz",
"IKS Hegh'funk",
"IKS MacIn'toj",
"IKS Wizon'yU",
"IKS Pa'vlo'v",
"IKS Vickzu'Qo",
"IKS Dok'craap",
"IKS Jer'kof",
"IKS Horz Poope",
"IKS Nipo",
"IKS Azz'fuk",
"IKS ET me",
"IKS Punk",
"IKS Nutz",
"IKS Balz'tuYu",
"IKS yU stnk",
"IKS Dumazz",
"IKS Puzee",
"IKS Wa'maH cha",
"IKS Onhunglo",
"IKS Puke'ya",
"IKS Barfnak",
"IKS Quisno",
"IKS Yuk",
"IKS Zitfac",
"IKS oo Gly",
"IKS Hurl'up",
"IKS Kraust",
"IKS Ch'ink",
"IKS Bat'crp",
"IKS fa'Art",
"IKS Hangh'frut",
"IKS MaDo'gz",
"IKS Dob'SotaH",
"IKS Pak'vu'yIjuH",
"IKS Vizu'Qok",
"IKS Snott",
"IKS FarQ",
"IKS Cheez'wiz",
"IKS Tarnexh",
"IKS Jihz",
"IKS Pizz",
"IKS Fagut",
"IKS Frute",
"IKS Slurpi",
"IKS Querfagg",
"IKS Smelit",
"IKS Bougar",
"IKS Nigwiz",
"IKS Qok'Yu",
"IKS Chin'gado",
"IKS pen'Deha",
"IKS fuk'Yu",
"IKS Buzznutzs",
"IKS Chingas",
"IKS Wazup",
"IKS Wa'zoo",
"IKS Ustinc",
"IKS Chichi",
"IKS Fartnutz",
"IKS Dofus",
"IKS Hoo'terz",
"IKS uP'chuk",
"IKS Likmi",
"IKS Com'paq",
"IKS pU zee",
"IKS Fug' me",
"IKS Regur'Ge",
"IKS Fug'slutz",
"IKS Tur'rd",
"IKS Up'yurz",
"IKS StikIt",
"IKS Scwanz",
"IKS Atu'fon'dulu",
"IKS muTha",
"IKS Slurpi",
"IKS Snotola",
"IKS Dawg'shid",
"IKS DihaRia",
"IKS Zinj",
"IKS Baklath",
"IKS Quezin'arT",
"IKS Foochi",
"IKS Jo'mamaz",
"IKS Whee'zer",
"IKS Goofla",
"IKS Wang'chng",
"IKS Schit",
"IKS SchniTzl",
"IKS Fongulu",
"IKS Whoopur",
"IKS FuxIt",
"IKS Fuuzbot",
"IKS Mo'jo",
"IKS Pooch",
"IKS WeeNur",
"IKS Blarnay",
"IKS FugZit",
"IKS Doork",
"IKS Whazoo",
"IKS aNuz",
"IKS VaGinle",
"IKS WaHaaka",
"IKS Luzer",
"IKS WhiimP",
"IKS DoH",
"IKS Yoma'maz",
"IKS Chi'nko",
"IKS Mad're",
"IKS Gadzookz",
"IKS Muud",
"IKS Baarfuup",
"IKS Woozniak",
"IKS Who'Ya",
"IKS YurbuTT",
"IKS LeDuk",
"IKS ItcHit",
"IKS Chu'onDiz",
"IKS Pulga",
"IKS EeTraTz",
"IKS MoDjuH",
"IKS MaHma'sux",
"IKS Dong'yag",
"IKS Sux",
"IKS Saz QuacH",
"IKS Lok Nez",
"IKS Wuzit",
"IKS Mojav",
"IKS ITH ica",
"IKS Goop Quon",
"IKS MongHrel",
"IKS Suqit",
"IKS Dumbazz",
"IKS BuulcrapH",
"IKS QuSmel",
"IKS HokeDoHki",
]

## We are all done now. The Races script will take care of setting up the RaceInfo objects.