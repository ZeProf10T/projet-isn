from entities import User, Enemy
from object import Mur, Potion, Porte, Eau


def murporte(screen):
    murs = []
    for x in range(0,480,32):
        y = 0
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for x in range(0,480,32):
        y = 448
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for y in range(32,448,32):
        x = 0
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for y in range(32,448,32):
        x = 448
        if y != 224:
            mur = Mur(screen,x,y,"mur")
            murs.append(mur)

    enemies=[]
    potions=[]
    portes = [
    Porte(screen,448,224)
    ]
    eaus=[]

    return murs, enemies, potions, portes, eaus

def classic(screen):
    murs = []
    for x in range(0,480,32):
        y = 0
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for x in range(0,480,32):
        y = 448
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)


    for y in range(32,448,32):
        x = 0
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for y in range(32,448,32):
        x = 448
        if y != 224:
            mur = Mur(screen,x,y,"mur")
            murs.append(mur)

    enemies = [
    Enemy(screen,64,64,1,1),
    Enemy(screen,160,64,1,2),
    Enemy(screen,256,64,1,3),
    Enemy(screen,352,64,3,1),
    ]

    potions = [
    Potion(screen, 64,384,"heal"),
    Potion(screen,160,384,"xp"),
    Potion(screen,256,384,"atk"),
    ]

    portes = [
    Porte(screen,448,224)
    ]

    eaus = [
    ]

    return murs, enemies, potions, portes, eaus

def deux(screen):
    murs = []
    for x in range(0,480,32):
        y = 0
        mur = Mur(screen,x,y, "mur")
        murs.append(mur)

    for x in range(0,480,32):
        y = 448
        mur = Mur(screen,x,y, "mur")
        murs.append(mur)

    for y in range(32,448,32):
        x = 0
        mur = Mur(screen,x,y, "mur")
        murs.append(mur)

    for y in range(32,448,32):
        x = 448
        if y != 224:
            mur = Mur(screen,x,y, "mur")
            murs.append(mur)

    for y in range(32,448,32):
        x = 288
        if y != 224:
            mur = Mur(screen,x,y, "eau")
            murs.append(mur)
    for y in range(32,448,32):
        x = 320
        if y != 224:
            mur = Mur(screen,x,y, "eau")
            murs.append(mur)
    for y in range(32,448,32):
        x = 352
        if y != 224:
            mur = Mur(screen,x,y, "eau")
            murs.append(mur)

    murs.append(Mur(screen,64,64,"pierre"))
    murs.append(Mur(screen,128,384,"pierre"))
    murs.append(Mur(screen,224,96,"pierre"))
    murs.append(Mur(screen,384,384,"pierre"))

    murs.append(Mur(screen,288,224,"pont"))
    murs.append(Mur(screen,320,224,"pont"))
    murs.append(Mur(screen,352,224,"pont"))



    enemies = [
    ]

    potions = [
    ]

    portes = [
    Porte(screen,448,224)
    ]

    eaus = [
    ]

    return murs, enemies, potions, portes, eaus

def troix(screen):
    murs = []
    for x in range(0,480,32):
        y = 0
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for x in range(0,480,32):
        y = 416
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)


    for x in range(0,480,32):
        y = 32
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for x in range(0,480,32):
        y = 384
        mur = Mur(screen,x,y,"lave")
        murs.append(mur)


    for x in range(0,480,32):
        y = 64
        mur = Mur(screen,x,y,"lave")
        murs.append(mur)

    for x in range(0,480,32):
        y = 448
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)



    for y in range(32,448,32):
        x = 0
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for y in range(32,448,32):
        x = 448
        if y != 224:
            mur = Mur(screen,x,y,"mur")
            murs.append(mur)

    for y in range(96,384,32):
        x = 288
        mur = Mur(screen,x,y,"lave")
        murs.append(mur)
    for y in range(96,384,32):
        x = 320
        mur = Mur(screen,x,y,"lave")
        murs.append(mur)
    for y in range(96,384,32):
        x = 256
        mur = Mur(screen,x,y,"lave")
        murs.append(mur)


    enemies = []
    for y in range(96,384,32):
        x = 224
        nmy = Enemy(screen,x,y,1,4)
        enemies.append(nmy)

    potions = [
    Potion(screen,384,192,"heal"),
    Potion(screen,384,256,"heal")
    ]

    portes = [

    Porte(screen,448,224)
    ]
    eaus = []

    return murs, enemies, potions, portes, eaus

def quatre(screen):
    murs = [
    Mur(screen,224,416,"pierre")
    ]
    for x in range(0,480,32):
        y = 0
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for x in range(0,480,32):
        y = 448
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for x in range(0,480,32):
        y = 64
        if x != 224 and x != 352:
            mur = Mur(screen,x,y,"mur")
            murs.append(mur)

    for x in range(0,480,32):
        y = 416
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)
    for x in range(0,224,32):
        y = 32
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)
    for x in range(384,456,32):
            y = 32
            mur = Mur(screen,x,y,"mur")
            murs.append(mur)
    for x in range(0,480,32):
        y = 384
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)


    for y in range(32,448,32):
        x = 0
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for y in range(32,448,32):
        x = 448
        if y != 224:
            mur = Mur(screen,x,y,"mur")
            murs.append(mur)


    for y in range(96,384,32):
        x = 288
        mur = Mur(screen,x,y,"lave")
        murs.append(mur)
    for y in range(96,384,32):
        x = 320
        mur = Mur(screen,x,y,"lave")
        murs.append(mur)
    for y in range(96,384,32):
        x = 256
        mur = Mur(screen,x,y,"lave")
        murs.append(mur)

    for y in range(96,384,32):
        x =128
        if y != 256:
            mur = Mur(screen,x,y,"eau")
            murs.append(mur)
    for y in range(96,384,32):
        x = 160
        if y != 256:
            mur = Mur(screen,x,y,"eau")
            murs.append(mur)

    for x in range(128,192,32):
        y = 256
        mur = Mur(screen,x,y,"pont")
        murs.append(mur)

    murs.append(Mur(screen,224,352,"pierre"))
    murs.append(Mur(screen,224,320,"pierre"))
    murs.append(Mur(screen,416,96,"pierre"))
    enemies=[
    Enemy(screen,224,64,1,4),
    Enemy(screen,352,64,1,4),
    Enemy(screen,64,128,1,1),
    Enemy(screen,96,256,1,1),
    Enemy(screen,416,256,1,3),
    Enemy(screen,384,96,1,3)
    ]
    for x in range(224,384,32):
        y = 32
        nmy = Enemy(screen,x,y,1,4)
        enemies.append(nmy)
    potions=[
    Potion(screen,192,224,"atk")
    ]
    portes = [
    Porte(screen,448,224)
    ]
    eaus=[]

    return murs, enemies, potions, portes, eaus


def cinq(screen):
    murs = []
#ca marche pas psk y'a pas de mur sur les coyté jcrois
    for y in range(160,288,32):
        x = 0
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for y in range(160,288,32):
        x = 448
        if y != 224:
            mur = Mur(screen,x,y,"mur")
            murs.append(mur)
    for x in range(0,128,32):
        y = 128
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for x in range(32,456,32):
        y =160
        if x != 32 and x!= 64:
            mur = Mur(screen,x,y,"mur")
            murs.append(mur)
    for x in range(0,456,32):
        y =288
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    murs.append(Mur(screen,128,256,"pierre"))
    murs.append(Mur(screen,128,224,"pierre"))

    murs.append(Mur(screen,256,192,"pierre"))
    murs.append(Mur(screen,256,224,"pierre"))

    murs.append(Mur(screen,384,256,"pierre"))
    murs.append(Mur(screen,384,224,"pierre"))
    enemies=[
    Enemy(screen,128,192,2,1),
    Enemy(screen,256,256,2,1),
    Enemy(screen,384,192,2,3)
    ]
    potions=[
    Potion(screen,416,224,"heal"),
    Potion(screen,416,256,"heal")
    ]
    portes = [
    Porte(screen,448,224)
    ]
    eaus=[]

    return murs, enemies, potions, portes, eaus

def six(screen):
    murs = []
    for x in range(0,480,32):
        y = 0
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for x in range(0,480,32):
        y = 448
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for y in range(32,448,32):
        x = 0
        mur = Mur(screen,x,y,"mur")
        murs.append(mur)

    for y in range(32,448,32):
        x = 448
        if y != 224:
            mur = Mur(screen,x,y,"mur")
            murs.append(mur)

    enemies=[
    Enemy(screen,256,192,1,5),
    Enemy(screen,288,192,1,6),
    Enemy(screen,256,224,1,7),
    Enemy(screen,288,224,1,8),
    Enemy(screen,416,224,1,9),
    Enemy(screen,416,256,1,9),
    Enemy(screen,416,192,1,9)
    ]

    potions=[
    Potion(screen,256,192,"atkboss"),
    Potion(screen,288,192,"atkboss"),
    Potion(screen,256,224,"atkboss"),
    Potion(screen,288,224,"atkboss")
    ]
    portes = [
    Porte(screen,448,224)
    ]
    eaus=[]

    return murs, enemies, potions, portes, eaus
