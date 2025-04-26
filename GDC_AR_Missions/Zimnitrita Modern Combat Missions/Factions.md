# Paramétrer les factions et unités RHS dans le framework Combats Ops (type Everon)

## USMC (joueurs) vs MSV (IA)

### Faction MSV utilisée : VKPO_Summer

* X_Groups_X : {8DE0C0830FE0C33D}Prefabs/Groups/OPFOR/Group_USSR_Base.et -> {217AB4493CAB5362}Prefabs/Groups/OPFOR/RHS_AFRF/MSV/VKPO_Summer/Group_RHS_RF_MSV_VKPO_S_Base.et
* X_Kill / X_Officer_X / X_offGuards_X : {DCB41B3746FDD1BE}Prefabs/Characters/Factions/OPFOR/USSR_Army/Character_USSR_Rifleman.et -> {5C75226D45102461}Prefabs/Characters/Factions/OPFOR/RHS_AFRF/MSV/VKPO_Summer/RandomSoldiers/Character_RHS_RF_MSV_VKPO_S_Rifleman_Random.et
* X_Kill / X_Officer_X / X_offGuards_X : {5436629450D8387A}Prefabs/Characters/Factions/OPFOR/USSR_Army/Character_USSR_SL.et -> {06127C628A0588EB}Prefabs/Characters/Factions/OPFOR/RHS_AFRF/MSV/VKPO_Summer/RandomSoldiers/Character_RHS_RF_MSV_VKPO_S_SL_Random.et
* X_Kill / X_Officer_X / SlotKill : {5117311FB822FD1F}Prefabs/Characters/Factions/OPFOR/USSR_Army/Character_USSR_Officer.et -> {13F471430D84970C}Prefabs/Characters/Factions/OPFOR/RHS_AFRF/MSV/VKPO_Summer/Character_RHS_RF_MSV_VKPO_S_Officer.et
* X_Outposts / X_Outpos_X / Guard : Character_USSR_Rifleman.et -> Character_RHS_RF_MSV_VKPO_S_Rifleman_Random.et
* X_Patrols / X_Patrol_X : {CB58D90EA14430AD}Prefabs/Groups/OPFOR/Group_USSR_SentryTeam.et -> {85591815191600FC}Prefabs/Groups/OPFOR/RHS_AFRF/MSV/VKPO_Summer/Group_RHS_RF_MSV_VKPO_S_SentryTeam.et
* X_QRF / x_QRFpool / X_QRFGroup : {E552DABF3636C2AD}Prefabs/Groups/OPFOR/Group_USSR_RifleSquad.et -> {256AEA338E84EC28}Prefabs/Groups/OPFOR/RHS_AFRF/MSV/VKPO_Summer/Group_RHS_RF_MSV_VKPO_S_RifleSquad.et
* X_RanGuards : Character_USSR_Rifleman.et -> Character_RHS_RF_MSV_VKPO_S_Rifleman_Random.et
* X_StaticUnits / X_Group_X : Character_USSR_Rifleman.et -> Character_RHS_RF_MSV_VKPO_S_Rifleman_Random.et
* {96C784C502AC37DA}Prefabs/Characters/Factions/OPFOR/USSR_Army/Character_USSR_MG.et -> {FBB329ECA28B85A7}Prefabs/Characters/Factions/OPFOR/RHS_AFRF/MSV/VKPO_Summer/Character_RHS_RF_MSV_VKPO_S_AR.et

Reste à gérer les médics et les grenadiers

# Modifications des noms de faction

Sur les QRFGroups - Faction Key : USSR -> RHS_AFRF
Sur les QRFGroups - Faction Key USSR -> RHS_AFRF
X__Logic \ TriggerQRF - SCR_ScenarioFrameworkSlotTrigger - Faction Key : USSR -> RHS_AFRF
X__Logic \ TriggerQRF - SCR_ScenarioFrameworkSlotTrigger - Activated By This Faction : USSR -> RHS_AFRF
X_SpawnPoints \ Slot - Faction Key : US -> RHS_USAF
X_SpawnPoints \ Slot - Object To Spawn : SpawnPoint_US_CP.et -> SpawnPoint_USMC_CP.et
X_ClearArea \ LayerX \ SlotClearArea_X - Faction Key : US -> RHS_USAF
X_ClearArea \ LayerX \ SlotClearArea_X - Activated By This Faction : US -> RHS_USAF

Sur toutes les taches X_ClearArea, X_Destroy, X_Documents, X_Kill - Faction Key : <vide> -> RHS_USAF
