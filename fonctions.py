### Fonction de création des données
def setData(user,coop,murs,potions,portes,eaus,enemies,changement):
    mursData = []
    for mur in murs:
        mursData.append({
            "pos": mur.pos,
            "genre": mur.genre,
        })

    potionsData = []
    for potion in potions:
        potionsData.append({
            "pos": potion.pos,
            "type": potion.type,
        })

    portesData = []
    for porte in portes:
        portesData.append({
            "pos": porte.pos,
        })

    eausData = []
    for eau in eaus:
        eausData.append({
            "pos": eau.pos
        })

    enemyData = []
    for enemy in enemies:
        enemyData.append({
            "pos": enemy.pos,
            "vie": enemy.vie,
            "defense": enemy.defense,
            "level": enemy.level,
            "type": enemy.type
        })

    userData = {
    "id": user.id,
    "pos": user.pos,
    "vie": user.vie,
    "attaque": user.attaque,
    "defense": user.defense,
    "level": user.level,
    "xp": user.xp
    }

    coopData = {
    "id": coop.id,
    "pos": coop.pos,
    "vie": coop.vie,
    "attaque": coop.attaque,
    "defense": coop.defense,
    "level": coop.level,
    "xp": coop.xp
    }

    data = {
    "murs": mursData,
    "potions": potionsData,
    "portes": portesData,
    "eaus": eausData,
    "enemies":enemyData,
    "user":userData,
    "coop": coopData,
    "changement": changement
    }

    return data
