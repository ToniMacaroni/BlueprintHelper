import bpy

bl_info = {
    "name": "Blueprint Helper",
    "category": "3D View",
    "author": "Toni Macaroni",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "description": "Helper for exporting Sons of the Forest blueprints."
}

item_enum_vals = [
		('ITEM_3DPRINTEDARROW', "3dPrintedArrow", "3dPrintedArrow", 618),
		('ITEM_3DPRINTEDFLASK', "3dPrintedFlask", "3dPrintedFlask", 426),
		('ITEM_3DPRINTEDGPSLOCATORCASE', "3dPrintedGpsLocatorCase", "3dPrintedGpsLocatorCase", 657),
		('ITEM_3DPRINTEDGRAPPLINGHOOK', "3dPrintedGrapplingHook", "3dPrintedGrapplingHook", 560),
		('ITEM_3DPRINTEDSLED', "3dPrintedSled", "3dPrintedSled", 428),
		('ITEM_3DPRINTERRESIN', "3dPrinterResin", "3dPrinterResin", 390),
		('ITEM_9MMAMMO', "9mmAmmo", "9mmAmmo", 362),
		('ITEM_ACTIONCAMERA', "ActionCamera", "ActionCamera", 637),
		('ITEM_AIRCANISTER', "AirCanister", "AirCanister", 469),
		('ITEM_ALBUMCOVER', "AlbumCover", "AlbumCover", 467),
		('ITEM_ALIVERABBIT', "AliveRabbit", "AliveRabbit", 728),
		('ITEM_ALOEVERA', "AloeVera", "AloeVera", 451),
		('ITEM_ALOEVERASEED', "AloeVeraSeed", "AloeVeraSeed", 596),
		('ITEM_ARROWLEAFBALSAMROOT', "ArrowleafBalsamroot", "ArrowleafBalsamroot", 454),
		('ITEM_ARROWLEAFSEED', "ArrowleafSeed", "ArrowleafSeed", 597),
		('ITEM_ARTIFACT', "Artifact", "Artifact", 707),
		('ITEM_ARTIFACTPIECEA', "ArtifactPieceA", "ArtifactPieceA", 662),
		('ITEM_ARTIFACTPIECEB', "ArtifactPieceB", "ArtifactPieceB", 667),
		('ITEM_ARTIFACTPIECEC', "ArtifactPieceC", "ArtifactPieceC", 668),
		('ITEM_ARTIFACTPIECED', "ArtifactPieceD", "ArtifactPieceD", 669),
		('ITEM_ARTIFACTPIECEE', "ArtifactPieceE", "ArtifactPieceE", 689),
		('ITEM_ARTIFACTPIECEF', "ArtifactPieceF", "ArtifactPieceF", 708),
		('ITEM_ARTIFACTPIECEG', "ArtifactPieceG", "ArtifactPieceG", 712),
		('ITEM_BACKPACK', "Backpack", "Backpack", 402),
		('ITEM_BATTERIES', "Batteries", "Batteries", 527),
		('ITEM_BIBLEPAPERD', "BiblePaperD", "BiblePaperD", 716),
		('ITEM_BIBLEPAPERSCRAPA', "BiblePaperScrapA", "BiblePaperScrapA", 721),
		('ITEM_BINOCULARS', "Binoculars", "Binoculars", 341),
		('ITEM_BLACKBERRIES', "Blackberries", "Blackberries", 595),
		('ITEM_BLACKBERRYSEED', "BlackberrySeed", "BlackberrySeed", 598),
		('ITEM_BLUEBERRIES', "Blueberries", "Blueberries", 445),
		('ITEM_BLUEBERRYSEED', "BlueberrySeed", "BlueberrySeed", 599),
		('ITEM_BLUEPRINTATTRACTSHRINE', "BlueprintAttractShrine", "BlueprintAttractShrine", 711),
		('ITEM_BLUEPRINTBASICLOGSLED', "BlueprintBasicLogSled", "BlueprintBasicLogSled", 638),
		('ITEM_BLUEPRINTBIRDHOUSE', "BlueprintBirdHouse", "BlueprintBirdHouse", 581),
		('ITEM_BLUEPRINTBONECHAIR', "BlueprintBoneChair", "BlueprintBoneChair", 579),
		('ITEM_BLUEPRINTBONECHANDELIER', "BlueprintBoneChandelier", "BlueprintBoneChandelier", 588),
		('ITEM_BLUEPRINTBOOK', "BlueprintBook", "BlueprintBook", 552),
		('ITEM_BLUEPRINTCLOCK', "BlueprintClock", "BlueprintClock", 681),
		('ITEM_BLUEPRINTDOUBLEBED', "BlueprintDoubleBed", "BlueprintDoubleBed", 683),
		('ITEM_BLUEPRINTDRYINGRACK', "BlueprintDryingRack", "BlueprintDryingRack", 530),
		('ITEM_BLUEPRINTFISHTRAP', "BlueprintFishTrap", "BlueprintFishTrap", 582),
		('ITEM_BLUEPRINTGOLDARMORPLATER', "BlueprintGoldArmorPlater", "BlueprintGoldArmorPlater", 714),
		('ITEM_BLUEPRINTGORECHAIR', "BlueprintGoreChair", "BlueprintGoreChair", 670),
		('ITEM_BLUEPRINTGORECOUCH', "BlueprintGoreCouch", "BlueprintGoreCouch", 671),
		('ITEM_BLUEPRINTGRINDTRAP', "BlueprintGrindTrap", "BlueprintGrindTrap", 679),
		('ITEM_BLUEPRINTHANGGLIDERLAUNCHER', "BlueprintHangGliderLauncher", "BlueprintHangGliderLauncher", 726),
		('ITEM_BLUEPRINTHANGINGSKULLLIGHT', "BlueprintHangingSkullLight", "BlueprintHangingSkullLight", 625),
		('ITEM_BLUEPRINTHEADTROPHYMOUNT', "BlueprintHeadTrophyMount", "BlueprintHeadTrophyMount", 645),
		('ITEM_BLUEPRINTITEMPLATING', "BlueprintItemPlating", "BlueprintItemPlating", 665),
		('ITEM_BLUEPRINTLEGLAMP', "BlueprintLegLamp", "BlueprintLegLamp", 701),
		('ITEM_BLUEPRINTMACETRAP', "BlueprintMaceTrap", "BlueprintMaceTrap", 656),
		('ITEM_BLUEPRINTMANNEQUIN', "BlueprintMannequin", "BlueprintMannequin", 584),
		('ITEM_BLUEPRINTPLANTERFLOOR', "BlueprintPlanterFloor", "BlueprintPlanterFloor", 587),
		('ITEM_BLUEPRINTPLANTERWALL', "BlueprintPlanterWall", "BlueprintPlanterWall", 586),
		('ITEM_BLUEPRINTPLATERCOUNTER', "BlueprintPlaterCounter", "BlueprintPlaterCounter", 713),
		('ITEM_BLUEPRINTPOWEREDCROSS', "BlueprintPoweredCross", "BlueprintPoweredCross", 666),
		('ITEM_BLUEPRINTRADIO', "BlueprintRadio", "BlueprintRadio", 659),
		('ITEM_BLUEPRINTRADIOTRAP', "BlueprintRadioTrap", "BlueprintRadioTrap", 658),
		('ITEM_BLUEPRINTRAINCATCHER', "BlueprintRainCatcher", "BlueprintRainCatcher", 629),
		('ITEM_BLUEPRINTREPELSHRINE', "BlueprintRepelShrine", "BlueprintRepelShrine", 710),
		('ITEM_BLUEPRINTROCKPATH', "BlueprintRockPath", "BlueprintRockPath", 622),
		('ITEM_BLUEPRINTSCARECROW', "BlueprintScarecrow", "BlueprintScarecrow", 585),
		('ITEM_BLUEPRINTSHELF', "BlueprintShelf", "BlueprintShelf", 621),
		('ITEM_BLUEPRINTSMALLLOGCABIN', "BlueprintSmallLogCabin", "BlueprintSmallLogCabin", 591),
		('ITEM_BLUEPRINTSMALLRABBITHUTCH', "BlueprintSmallRabbitHutch", "BlueprintSmallRabbitHutch", 730),
		('ITEM_BLUEPRINTSPEARTHROWERTRAP', "BlueprintSpearThrowerTrap", "BlueprintSpearThrowerTrap", 688),
		('ITEM_BLUEPRINTSPINTRAP', "BlueprintSpinTrap", "BlueprintSpinTrap", 682),
		('ITEM_BLUEPRINTSPOTLIGHT', "BlueprintSpotlight", "BlueprintSpotlight", 680),
		('ITEM_BLUEPRINTSPRINGTRAP', "BlueprintSpringTrap", "BlueprintSpringTrap", 632),
		('ITEM_BLUEPRINTSTICKBED', "BlueprintStickBed", "BlueprintStickBed", 532),
		('ITEM_BLUEPRINTSTICKCHAIR', "BlueprintStickChair", "BlueprintStickChair", 531),
		('ITEM_BLUEPRINTSTICKLADDER', "BlueprintStickLadder", "BlueprintStickLadder", 580),
		('ITEM_BLUEPRINTSTONEFIREPLACE', "BlueprintStoneFireplace", "BlueprintStoneFireplace", 641),
		('ITEM_BLUEPRINTSTORAGEBONES', "BlueprintStorageBones", "BlueprintStorageBones", 608),
		('ITEM_BLUEPRINTSTORAGEFIREWOOD', "BlueprintStorageFirewood", "BlueprintStorageFirewood", 702),
		('ITEM_BLUEPRINTSTORAGELOGS', "BlueprintStorageLogs", "BlueprintStorageLogs", 609),
		('ITEM_BLUEPRINTSTORAGEROCKS', "BlueprintStorageRocks", "BlueprintStorageRocks", 607),
		('ITEM_BLUEPRINTSTORAGESPEARS', "BlueprintStorageSpears", "BlueprintStorageSpears", 700),
		('ITEM_BLUEPRINTSTORAGESTICKS', "BlueprintStorageSticks", "BlueprintStorageSticks", 610),
		('ITEM_BLUEPRINTSTORAGESTONES', "BlueprintStorageStones", "BlueprintStorageStones", 649),
		('ITEM_BLUEPRINTTABLE', "BlueprintTable", "BlueprintTable", 620),
		('ITEM_BLUEPRINTTABLEROUND', "BlueprintTableRound", "BlueprintTableRound", 673),
		('ITEM_BLUEPRINTTELEPORTER', "BlueprintTeleporter", "BlueprintTeleporter", 709),
		('ITEM_BLUEPRINTTRAPBONEMAKER', "BlueprintTrapBoneMaker", "BlueprintTrapBoneMaker", 549),
		('ITEM_BLUEPRINTTRAPFLYSWATTER', "BlueprintTrapFlySwatter", "BlueprintTrapFlySwatter", 550),
		('ITEM_BLUEPRINTTRAPSMALLANIMALCATCHER', "BlueprintTrapSmallAnimalCatcher", "BlueprintTrapSmallAnimalCatcher", 551),
		('ITEM_BLUEPRINTUBERTRAP', "BlueprintUberTrap", "BlueprintUberTrap", 672),
		('ITEM_BLUEPRINTWALLSHELF', "BlueprintWallShelf", "BlueprintWallShelf", 623),
		('ITEM_BLUEPRINTWALLTORCH', "BlueprintWallTorch", "BlueprintWallTorch", 624),
		('ITEM_BLUEPRINTWEAPONRACK', "BlueprintWeaponRack", "BlueprintWeaponRack", 533),
		('ITEM_BLUEPRINTWEAPONRACKWALL', "BlueprintWeaponRackWall", "BlueprintWeaponRackWall", 704),
		('ITEM_BONE', "Bone", "Bone", 405),
		('ITEM_BONEARMOUR', "BoneArmour", "BoneArmour", 494),
		('ITEM_BUCKSHOTAMMO', "BuckshotAmmo", "BuckshotAmmo", 364),
		('ITEM_BUNKERMAPA', "BunkerMapA", "BunkerMapA", 693),
		('ITEM_BUNKERPAMPHLET', "BunkerPamphlet", "BunkerPamphlet", 509),
		('ITEM_C4BRICK', "C4Brick", "C4Brick", 420),
		('ITEM_CANNEDFOOD', "CannedFood", "CannedFood", 434),
		('ITEM_CANOPENER', "CanOpener", "CanOpener", 432),
		('ITEM_CATFOOD', "CatFood", "CatFood", 464),
		('ITEM_CEREALBOX', "CerealBox", "CerealBox", 425),
		('ITEM_CHICORY', "Chicory", "Chicory", 465),
		('ITEM_CHICORYSEED', "ChicorySeed", "ChicorySeed", 605),
		('ITEM_CIRCUITBOARD', "CircuitBoard", "CircuitBoard", 416),
		('ITEM_CIRCUSPAMPHLET', "CircusPamphlet", "CircusPamphlet", 705),
		('ITEM_CLOTH', "Cloth", "Cloth", 415),
		('ITEM_COINS', "Coins", "Coins", 502),
		('ITEM_COMBATKNIFE', "CombatKnife", "CombatKnife", 380),
		('ITEM_COMPACTPISTOL', "CompactPistol", "CompactPistol", 355),
		('ITEM_COMPACTPISTOLRAIL', "CompactPistolRail", "CompactPistolRail", 376),
		('ITEM_COOKINGPOT', "CookingPot", "CookingPot", 517),
		('ITEM_CRAFTEDARROW', "CraftedArrow", "CraftedArrow", 507),
		('ITEM_CRAFTEDBOW', "CraftedBow", "CraftedBow", 443),
		('ITEM_CRAFTEDCLUB', "CraftedClub", "CraftedClub", 477),
		('ITEM_CRAFTEDSPEAR', "CraftedSpear", "CraftedSpear", 474),
		('ITEM_CREEPYARMOUR', "CreepyArmour", "CreepyArmour", 593),
		('ITEM_CREEPYSKIN', "CreepySkin", "CreepySkin", 592),
		('ITEM_CROSS', "Cross", "Cross", 468),
		('ITEM_CROSSBOW', "Crossbow", "Crossbow", 365),
		('ITEM_CROSSBOWAMMOBOLT', "CrossbowAmmoBolt", "CrossbowAmmoBolt", 368),
		('ITEM_CULTPAMPHLET', "CultPamphlet", "CultPamphlet", 633),
		('ITEM_CULTSIGNF', "CultSignF", "CultSignF", 686),
		('ITEM_CULTSIGNG', "CultSignG", "CultSignG", 695),
		('ITEM_CULTSIGNH', "CultSignH", "CultSignH", 696),
		('ITEM_CULTSIGNI', "CultSignI", "CultSignI", 697),
		('ITEM_CULTSIGNJ', "CultSignJ", "CultSignJ", 698),
		('ITEM_CULTSIGNK', "CultSignK", "CultSignK", 699),
		('ITEM_DEERHEAD', "DeerHead", "DeerHead", 651),
		('ITEM_DEERHIDE', "DeerHide", "DeerHide", 472),
		('ITEM_DEERHIDEARMOUR', "DeerHideArmour", "DeerHideArmour", 519),
		('ITEM_DEVILSCLUB', "DevilsClub", "DevilsClub", 449),
		('ITEM_DEVILSCLUBSEED', "DevilsClubSeed", "DevilsClubSeed", 600),
		('ITEM_DUCKHEAD', "DuckHead", "DuckHead", 642),
		('ITEM_DUCTTAPE', "DuctTape", "DuctTape", 419),
		('ITEM_EAGLEHEAD', "EagleHead", "EagleHead", 643),
		('ITEM_EMAILPRINTOUTASTROLOGYA', "EmailPrintoutAstrologyA", "EmailPrintoutAstrologyA", 539),
		('ITEM_EMAILPRINTOUTASTROLOGYB', "EmailPrintoutAstrologyB", "EmailPrintoutAstrologyB", 540),
		('ITEM_EMAILPRINTOUTASTROLOGYC', "EmailPrintoutAstrologyC", "EmailPrintoutAstrologyC", 541),
		('ITEM_EMAILPRINTOUTBALLETA', "EmailPrintoutBalletA", "EmailPrintoutBalletA", 545),
		('ITEM_EMAILPRINTOUTCAVELIGHTING', "EmailPrintoutCaveLighting", "EmailPrintoutCaveLighting", 521),
		('ITEM_EMAILPRINTOUTGOLFA', "EmailPrintoutGolfA", "EmailPrintoutGolfA", 534),
		('ITEM_EMAILPRINTOUTGOLFB', "EmailPrintoutGolfB", "EmailPrintoutGolfB", 535),
		('ITEM_EMAILPRINTOUTGOLFC', "EmailPrintoutGolfC", "EmailPrintoutGolfC", 536),
		('ITEM_EMAILPRINTOUTGOLFD', "EmailPrintoutGolfD", "EmailPrintoutGolfD", 537),
		('ITEM_EMAILPRINTOUTGOVERNMENTA', "EmailPrintoutGovernmentA", "EmailPrintoutGovernmentA", 614),
		('ITEM_EMAILPRINTOUTGOVERNMENTB', "EmailPrintoutGovernmentB", "EmailPrintoutGovernmentB", 615),
		('ITEM_EMAILPRINTOUTGOVERNMENTC', "EmailPrintoutGovernmentC", "EmailPrintoutGovernmentC", 616),
		('ITEM_EMAILPRINTOUTMRPUFFYFINANCIAL', "EmailPrintoutMrPuffyFinancial", "EmailPrintoutMrPuffyFinancial", 528),
		('ITEM_EMAILPRINTOUTMRPUFFYWILL', "EmailPrintoutMrPuffyWill", "EmailPrintoutMrPuffyWill", 526),
		('ITEM_EMAILPRINTOUTPAINTINGA', "EmailPrintoutPaintingA", "EmailPrintoutPaintingA", 538),
		('ITEM_EMAILPRINTOUTPOLITICIANA', "EmailPrintoutPoliticianA", "EmailPrintoutPoliticianA", 542),
		('ITEM_EMAILPRINTOUTPOLITICIANB', "EmailPrintoutPoliticianB", "EmailPrintoutPoliticianB", 543),
		('ITEM_EMAILPRINTOUTPOLITICIANC', "EmailPrintoutPoliticianC", "EmailPrintoutPoliticianC", 544),
		('ITEM_EMAILPRINTOUTSQUEAKYSHOESA', "EmailPrintoutSqueakyShoesA", "EmailPrintoutSqueakyShoesA", 546),
		('ITEM_EMAILPRINTOUTSQUEAKYSHOESB', "EmailPrintoutSqueakyShoesB", "EmailPrintoutSqueakyShoesB", 547),
		('ITEM_EMAILPRINTOUTSQUEAKYSHOESC', "EmailPrintoutSqueakyShoesC", "EmailPrintoutSqueakyShoesC", 548),
		('ITEM_EMERGENCYPACK', "EmergencyPack", "EmergencyPack", 483),
		('ITEM_ENERGYBAR', "EnergyBar", "EnergyBar", 441),
		('ITEM_ENERGYDRINK', "EnergyDrink", "EnergyDrink", 439),
		('ITEM_ENERGYMIX', "EnergyMix", "EnergyMix", 461),
		('ITEM_ENERGYMIXPLUS', "EnergyMixPlus", "EnergyMixPlus", 462),
		('ITEM_FEATHER', "Feather", "Feather", 479),
		('ITEM_FIREAXE', "FireAxe", "FireAxe", 431),
		('ITEM_FIREWEED', "Fireweed", "Fireweed", 453),
		('ITEM_FIREWEEDSEED', "FireweedSeed", "FireweedSeed", 601),
		('ITEM_FISH', "Fish", "Fish", 436),
		('ITEM_FISHINGEMAILA', "FishingEmailA", "FishingEmailA", 677),
		('ITEM_FISHINGEMAILB', "FishingEmailB", "FishingEmailB", 678),
		('ITEM_FISHINGEMAILC', "FishingEmailC", "FishingEmailC", 692),
		('ITEM_FLARE', "Flare", "Flare", 440),
		('ITEM_FLASHLIGHT', "Flashlight", "Flashlight", 471),
		('ITEM_FLASHLIGHTMOD', "FlashlightMod", "FlashlightMod", 378),
		('ITEM_FLYAMANITAMUSHROOM', "FlyAmanitaMushroom", "FlyAmanitaMushroom", 400),
		('ITEM_FOODCUBEBRAIN', "FoodCubeBrain", "FoodCubeBrain", 569),
		('ITEM_FOODCUBESTEAK', "FoodCubeSteak", "FoodCubeSteak", 570),
		('ITEM_FOODCUBESTEAKANDBACON', "FoodCubeSteakAndBacon", "FoodCubeSteakAndBacon", 571),
		('ITEM_GOLDENARMOUR', "GoldenArmour", "GoldenArmour", 572),
		('ITEM_GOLDMASK', "GoldMask", "GoldMask", 435),
		('ITEM_GOLFBALL', "GolfBall", "GolfBall", 524),
		('ITEM_GOLFCARTBATTERY', "GolfCartBattery", "GolfCartBattery", 661),
		('ITEM_GOLFPUTTER', "GolfPutter", "GolfPutter", 525),
		('ITEM_GPSLOCATOR', "GPSLocator", "GPSLocator", 529),
		('ITEM_GPSTRACKER', "GPSTracker", "GPSTracker", 412),
		('ITEM_GRABBAG', "GrabBag", "GrabBag", 351),
		('ITEM_GRENADE', "Grenade", "Grenade", 381),
		('ITEM_GRENADEAMMO', "GrenadeAmmo", "GrenadeAmmo", 382),
		('ITEM_GUARANABERRIES', "GuaranaBerries", "GuaranaBerries", 594),
		('ITEM_GUARANASEED', "GuaranaSeed", "GuaranaSeed", 602),
		('ITEM_GUITAR', "Guitar", "Guitar", 340),
		('ITEM_HALFLOG', "HalfLog", "HalfLog", 408),
		('ITEM_HALFLOGPLANK', "HalfLogPlank", "HalfLogPlank", 577),
		('ITEM_HANGGLIDER', "HangGlider", "HangGlider", 626),
		('ITEM_HEALTHMIX', "HealthMix", "HealthMix", 455),
		('ITEM_HEALTHMIXPLUS', "HealthMixPlus", "HealthMixPlus", 456),
		('ITEM_HOLOVILLENOTICEA', "HolovilleNoticeA", "HolovilleNoticeA", 562),
		('ITEM_HOLOVILLENOTICEB', "HolovilleNoticeB", "HolovilleNoticeB", 563),
		('ITEM_HOLOVILLENOTICEC', "HolovilleNoticeC", "HolovilleNoticeC", 564),
		('ITEM_HOLOVILLENOTICED', "HolovilleNoticeD", "HolovilleNoticeD", 565),
		('ITEM_HOODIE', "Hoodie", "Hoodie", 490),
		('ITEM_HORSETAIL', "Horsetail", "Horsetail", 450),
		('ITEM_HORSETAILSEED', "HorsetailSeed", "HorsetailSeed", 603),
		('ITEM_HYDNUMREPANDUMMUSHROOM', "HydnumRepandumMushroom", "HydnumRepandumMushroom", 399),
		('ITEM_JIANYUEMAILPRINTOUTA', "JianyuEmailPrintoutA", "JianyuEmailPrintoutA", 694),
		('ITEM_KATANA', "Katana", "Katana", 367),
		('ITEM_KEYCARDGUEST', "KeyCardGuest", "KeyCardGuest", 567),
		('ITEM_KEYCARDMAINTENANCE', "KeyCardMaintenance", "KeyCardMaintenance", 566),
		('ITEM_KEYCARDVIP', "KeyCardVIP", "KeyCardVIP", 568),
		('ITEM_KINGOYSTERMUSHROOM', "KingOysterMushroom", "KingOysterMushroom", 398),
		('ITEM_KNIGHTV', "KnightV", "KnightV", 630),
		('ITEM_LASERSIGHTMOD', "LaserSightMod", "LaserSightMod", 375),
		('ITEM_LEAF', "Leaf", "Leaf", 484),
		('ITEM_LEAFARMOUR', "LeafArmour", "LeafArmour", 473),
		('ITEM_LEATHERJACKET', "LeatherJacket", "LeatherJacket", 493),
		('ITEM_LIGHTBULB', "LightBulb", "LightBulb", 635),
		('ITEM_LOG_LEGACY', "Log_Legacy", "Log_Legacy", 78),
		('ITEM_LOGPLANK', "LogPlank", "LogPlank", 395),
		('ITEM_LOOTPOUCH', "LootPouch", "LootPouch", 508),
		('ITEM_MACHETE2', "Machete2", "Machete2", 359),
		('ITEM_MEAT', "Meat", "Meat", 433),
		('ITEM_MODERNAXE', "ModernAxe", "ModernAxe", 356),
		('ITEM_MOLOTOV', "Molotov", "Molotov", 388),
		('ITEM_MOLOTOVAMMO', "MolotovAmmo", "MolotovAmmo", 389),
		('ITEM_MONEY', "Money", "Money", 496),
		('ITEM_MOOSEHEAD', "MooseHead", "MooseHead", 652),
		('ITEM_MREPACK', "MrePack", "MrePack", 438),
		('ITEM_MRPUFFTONTABLECARD', "MrPufftonTableCard", "MrPufftonTableCard", 627),
		('ITEM_MRSPUFFTONTABLECARD', "MrsPufftonTableCard", "MrsPufftonTableCard", 628),
		('ITEM_NEWSPAPERCUTOUT', "NewspaperCutout", "NewspaperCutout", 612),
		('ITEM_NEWSPAPERCUTOUTOUTBID', "NewspaperCutoutOutbid", "NewspaperCutoutOutbid", 613),
		('ITEM_NEWSPAPERDCUTOUT', "NewspaperDCutout", "NewspaperDCutout", 706),
		('ITEM_NIGHTVISIONGOGGLES', "NightVisionGoggles", "NightVisionGoggles", 354),
		('ITEM_NOVELA', "NovelA", "NovelA", 423),
		('ITEM_NOVELB', "NovelB", "NovelB", 424),
		('ITEM_NOVELC', "NovelC", "NovelC", 574),
		('ITEM_NOVELD', "NovelD", "NovelD", 575),
		('ITEM_NOVELF', "NovelF", "NovelF", 631),
		('ITEM_NUMBERSPRINTOUT', "NumbersPrintout", "NumbersPrintout", 611),
		('ITEM_OLDJACKET', "OldJacket", "OldJacket", 491),
		('ITEM_OLDNOTEA', "OldNoteA", "OldNoteA", 674),
		('ITEM_OLDNOTEB', "OldNoteB", "OldNoteB", 675),
		('ITEM_OLDNOTEC', "OldNoteC", "OldNoteC", 676),
		('ITEM_OLDNOTED', "OldNoteD", "OldNoteD", 685),
		('ITEM_OLDNOTEE', "OldNoteE", "OldNoteE", 684),
		('ITEM_OLDNOTEF', "OldNoteF", "OldNoteF", 691),
		('ITEM_OLDNOTEG', "OldNoteG", "OldNoteG", 717),
		('ITEM_OYSTER', "Oyster", "Oyster", 466),
		('ITEM_PAPERTARGET', "PaperTarget", "PaperTarget", 518),
		('ITEM_PERSONALNOTEA', "PersonalNoteA", "PersonalNoteA", 653),
		('ITEM_PERSONALNOTEB', "PersonalNoteB", "PersonalNoteB", 654),
		('ITEM_PERSONALNOTEC', "PersonalNoteC", "PersonalNoteC", 655),
		('ITEM_PERSONALNOTEE', "PersonalNoteE", "PersonalNoteE", 718),
		('ITEM_PERSONALNOTEF', "PersonalNoteF", "PersonalNoteF", 719),
		('ITEM_PERSONALNOTEG', "PersonalNoteG", "PersonalNoteG", 720),
		('ITEM_PICKAXE', "Pickaxe", "Pickaxe", 663),
		('ITEM_PILLS', "Pills", "Pills", 437),
		('ITEM_PISTOLAMMOBOX', "PistolAmmoBox", "PistolAmmoBox", 370),
		('ITEM_PISTOLSUPPRESSOR', "PistolSuppressor", "PistolSuppressor", 374),
		('ITEM_PLASMALIGHTER', "PlasmaLighter", "PlasmaLighter", 413),
		('ITEM_PRIESTOUTFIT', "PriestOutfit", "PriestOutfit", 703),
		('ITEM_PUFFTONEMAILA', "PufftonEmailA", "PufftonEmailA", 687),
		('ITEM_PUFFTONEMAILB', "PufftonEmailB", "PufftonEmailB", 722),
		('ITEM_PUFFTONEMAILC', "PufftonEmailC", "PufftonEmailC", 723),
		('ITEM_PUFFYJACKET', "PuffyJacket", "PuffyJacket", 500),
		('ITEM_QUARTERLOG', "QuarterLog", "QuarterLog", 406),
		('ITEM_QUARTERLOGPLANK', "QuarterLogPlank", "QuarterLogPlank", 576),
		('ITEM_RABBITHEAD', "RabbitHead", "RabbitHead", 646),
		('ITEM_RACCOONHEAD', "RaccoonHead", "RaccoonHead", 715),
		('ITEM_RADIO', "Radio", "Radio", 590),
		('ITEM_RAMENNOODLES', "RamenNoodles", "RamenNoodles", 421),
		('ITEM_REBREATHER', "Rebreather", "Rebreather", 444),
		('ITEM_REDMASK', "RedMask", "RedMask", 391),
		('ITEM_REPAIRTOOL', "RepairTool", "RepairTool", 422),
		('ITEM_REVOLVER', "Revolver", "Revolver", 386),
		('ITEM_RIFLE', "Rifle", "Rifle", 361),
		('ITEM_RIFLEAMMO', "RifleAmmo", "RifleAmmo", 387),
		('ITEM_RIFLERAILMOD', "RifleRailMod", "RifleRailMod", 383),
		('ITEM_ROCK', "Rock", "Rock", 393),
		('ITEM_ROPE', "Rope", "Rope", 403),
		('ITEM_ROPEGUN', "RopeGun", "RopeGun", 522),
		('ITEM_SALMONBERRIES', "Salmonberries", "Salmonberries", 447),
		('ITEM_SALMONBERRYSEED', "SalmonberrySeed", "SalmonberrySeed", 604),
		('ITEM_SEAGULLHEAD', "SeagullHead", "SeagullHead", 648),
		('ITEM_SEVEREDARM', "SeveredArm", "SeveredArm", 480),
		('ITEM_SEVEREDHEAD', "SeveredHead", "SeveredHead", 482),
		('ITEM_SEVEREDLEG', "SeveredLeg", "SeveredLeg", 481),
		('ITEM_SHIITAKEMUSHROOM', "ShiitakeMushroom", "ShiitakeMushroom", 397),
		('ITEM_SHOTGUNAMMOBOXBUCKSHOT', "ShotgunAmmoBoxBuckshot", "ShotgunAmmoBoxBuckshot", 371),
		('ITEM_SHOTGUNAMMOBOXSLUG', "ShotgunAmmoBoxSlug", "ShotgunAmmoBoxSlug", 372),
		('ITEM_SHOTGUNPUMPACTION', "ShotgunPumpAction", "ShotgunPumpAction", 358),
		('ITEM_SHOTGUNRAIL', "ShotgunRail", "ShotgunRail", 346),
		('ITEM_SHOVEL', "Shovel", "Shovel", 485),
		('ITEM_SILKPYJAMAS', "SilkPyjamas", "SilkPyjamas", 487),
		('ITEM_SKULL', "Skull", "Skull", 430),
		('ITEM_SKUNKHEAD', "SkunkHead", "SkunkHead", 729),
		('ITEM_SLINGSHOT', "Slingshot", "Slingshot", 459),
		('ITEM_SLUGAMMO', "SlugAmmo", "SlugAmmo", 363),
		('ITEM_SMALLROCK', "SmallRock", "SmallRock", 476),
		('ITEM_SMALLTURTLEHEAD', "SmallTurtleHead", "SmallTurtleHead", 644),
		('ITEM_SNOWBERRIES', "Snowberries", "Snowberries", 448),
		('ITEM_SNOWBERRYSEED', "SnowberrySeed", "SnowberrySeed", 725),
		('ITEM_SOLAFITEARMOUR', "SolafiteArmour", "SolafiteArmour", 727),
		('ITEM_SOLAFITEORE', "SolafiteOre", "SolafiteOre", 664),
		('ITEM_SOLARPANEL', "SolarPanel", "SolarPanel", 634),
		('ITEM_SPACESUIT', "SpaceSuit", "SpaceSuit", 639),
		('ITEM_SQUIRRELHEAD', "SquirrelHead", "SquirrelHead", 647),
		('ITEM_STICK', "Stick", "Stick", 392),
		('ITEM_STOCKPRICEPRINTOUT', "StockPricePrintout", "StockPricePrintout", 617),
		('ITEM_STONE', "Stone", "Stone", 640),
		('ITEM_STORYPAGES', "StoryPages", "StoryPages", 690),
		('ITEM_STRUCTURE ELEMENT', "Structure Element", "Structure Element", 520),
		('ITEM_STUNGUN', "StunGun", "StunGun", 353),
		('ITEM_STUNGUNAMMO', "StunGunAmmo", "StunGunAmmo", 369),
		('ITEM_STUNGUNAMMOBOX', "StunGunAmmoBox", "StunGunAmmoBox", 457),
		('ITEM_TACTICALAXE', "TacticalAxe", "TacticalAxe", 379),
		('ITEM_TACTICALBOOTS', "TacticalBoots", "TacticalBoots", 501),
		('ITEM_TACTICALBOW', "TacticalBow", "TacticalBow", 360),
		('ITEM_TACTICALBOWAMMO', "TacticalBowAmmo", "TacticalBowAmmo", 373),
		('ITEM_TACTICALCHAINSAW', "TacticalChainsaw", "TacticalChainsaw", 394),
		('ITEM_TACTICALJACKET', "TacticalJacket", "TacticalJacket", 495),
		('ITEM_TACTICALPANTS', "TacticalPants", "TacticalPants", 489),
		('ITEM_TARP', "Tarp", "Tarp", 504),
		('ITEM_TASERSTICK', "TaserStick", "TaserStick", 396),
		('ITEM_TECHARMOUR', "TechArmour", "TechArmour", 554),
		('ITEM_TECHMESH', "TechMesh", "TechMesh", 553),
		('ITEM_THREEQUARTERLOG', "ThreeQuarterLog", "ThreeQuarterLog", 409),
		('ITEM_THREEQUARTERLOGPLANK', "ThreeQuarterLogPlank", "ThreeQuarterLogPlank", 578),
		('ITEM_TIMEBOMB', "TimeBomb", "TimeBomb", 417),
		('ITEM_TORCH', "Torch", "Torch", 503),
		('ITEM_TURTLEEGG', "TurtleEgg", "TurtleEgg", 401),
		('ITEM_TURTLEHEAD', "TurtleHead", "TurtleHead", 650),
		('ITEM_TURTLESHELL', "TurtleShell", "TurtleShell", 506),
		('ITEM_TUTORIALBOOK', "TutorialBook", "TutorialBook", 589),
		('ITEM_TUXEDO', "Tuxedo", "Tuxedo", 492),
		('ITEM_TWINBERRIES', "Twinberries", "Twinberries", 446),
		('ITEM_TWINBERRYSEED', "TwinberrySeed", "TwinberrySeed", 724),
		('ITEM_VIRGINIACAMOSUIT', "VirginiaCamoSuit", "VirginiaCamoSuit", 558),
		('ITEM_VIRGINIADRESS', "VirginiaDress", "VirginiaDress", 556),
		('ITEM_VIRGINIALEATHERSUIT', "VirginiaLeatherSuit", "VirginiaLeatherSuit", 557),
		('ITEM_VIRGINIASWIMSUIT', "VirginiaSwimSuit", "VirginiaSwimSuit", 619),
		('ITEM_VIRGINIATRACKSUIT', "VirginiaTrackSuit", "VirginiaTrackSuit", 555),
		('ITEM_VODKABOTTLE', "VodkaBottle", "VodkaBottle", 414),
		('ITEM_WALKIETALKIE', "WalkieTalkie", "WalkieTalkie", 486),
		('ITEM_WETSUIT', "Wetsuit", "Wetsuit", 499),
		('ITEM_WIRE', "Wire", "Wire", 418),
		('ITEM_WRISTWATCH', "Wristwatch", "Wristwatch", 410),
		('ITEM_YARRO', "Yarro", "Yarro", 452),
		('ITEM_YARROSEED', "YarroSeed", "YarroSeed", 606),
		('ITEM_ZIPLINEROPE', "ZiplineRope", "ZiplineRope", 523)
	]

item_id_enum = bpy.props.EnumProperty(items=item_enum_vals)

class SearchMyEnum(bpy.types.Operator):
    bl_idname = "object.item_id_enum_search"
    bl_label = ""
    bl_property = "item_id_enum_val"

    item_id_enum_val: item_id_enum

    def execute(self, context):
        context.scene.item_id_enum = self.item_id_enum_val
        context.region.tag_redraw()
        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        wm.invoke_search_popup(self)
        return {'RUNNING_MODAL'}

class SetItemID(bpy.types.Operator):
    bl_idname = "object.set_item_id"
    bl_label = "Set Item ID"
    
    # Define an integer property for the input box
    def execute(self, context):
        items = context.scene.bl_rna.properties["item_id_enum"].enum_items
        item_id = items[context.scene.item_id_enum].value
        for obj in bpy.context.selected_objects:
            obj.data["ItemId"] = item_id

        return {'FINISHED'}
    

class SetupCollision(bpy.types.Operator):
    bl_idname = "object.setup_collision"
    bl_label = "Setup Collision"
    
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            if obj.type != 'MESH':
                continue
            
            if not obj.name.startswith("collision"):
                obj.name = "collision." + obj.name
            obj.display_type = 'BOUNDS'

        return {'FINISHED'}
    

class ItemIDPanel(bpy.types.Panel):
    bl_label = "Blueprint Helper"
    bl_idname = "OBJECT_PT_blueprint_helper"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Blueprint Helper"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        active_object = context.view_layer.objects.active

        if active_object == None:
            layout.label(text = "Nothing selected")
            return
        
        if active_object.type != 'MESH':
            layout.label(text = "Select a mesh")
            return
        
        layout.label(text = "Active Object")
        layout.prop(active_object.data, "ItemId")
        layout.separator()
        
        layout.label(text = "Apply to objects")
        layout.prop(context.scene, "item_id_enum", text="Item")
        # current_item_name = layout.enum_item_name(context.scene, "item_id_enum", context.scene.item_id_enum)
        layout.operator(SearchMyEnum.bl_idname, text="Search")
        #layout.prop(context.scene, "item_id")
        layout.operator(SetItemID.bl_idname, text="Apply")
        layout.separator()

        layout.label(text = "Utility")
        layout.operator("object.setup_collision")
        layout.separator()

        layout.label(text = "Export")
        layout.operator("export_scene.gltf", text="Export")


def register():
    bpy.types.Mesh.ItemId = bpy.props.IntProperty(name="Item ID", default=0)
    bpy.types.Scene.item_id_enum = item_id_enum
    bpy.types.Scene.item_id = bpy.props.IntProperty(name="Item ID", default=0)
    bpy.utils.register_class(SetItemID)
    bpy.utils.register_class(ItemIDPanel)
    bpy.utils.register_class(SearchMyEnum)
    bpy.utils.register_class(SetupCollision)

def unregister():
    bpy.utils.unregister_class(SetItemID)
    bpy.utils.unregister_class(ItemIDPanel)
    bpy.utils.unregister_class(SearchMyEnum)
    bpy.utils.unregister_class(SetupCollision)
    del bpy.types.Scene.item_id
    del bpy.types.Scene.item_id_enum

if __name__ == "__main__":
    register()