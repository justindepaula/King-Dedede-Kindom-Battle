from gamelib import*
#Master Games
#Justin De Paula
#King Dedede Kingdom Battle

#Objects and Lists
game=Game(800,600,"King DeDeDe Kingdom Battle")
aura=Animation("aura.png",4,game,764/4,191)
ddd=Image("ddd.png",game)
hdd=Image("hdd.png",game)
bd=Image("bd.png",game)
hbd=Image("hbd.png",game)
bkb=Image("bbg.jpg",game)
bkt=Image("tutorial.jpg",game)
bk1=Image("forest.jpg",game)
bk2=Image("iceberg.jpg",game)
bk3=Image("Volcarona.jpg",game)
bk4=Image("boss.jpg",game)
bk4s=Image("boss.jpg",game)
bks=Image("erm.png",game)
Crown=Image("crown.png",game)
crown2=Image("crown.png",game)
dddoodle=Image("dddoodle.png",game)
fist=Image("fist.png",game)
buff=Image("buff_d.png",game)
sunset=Image("sunset.jpg",game)
star=Image("star.png",game)
stard=Image("star.png",game)
yeowch=Animation("dddoom.png",4,game,200,200)
win=Animation("win.png",2,game,200,200)
border_t = Animation("Border.jpg",1,game,196,1)
border_b = Animation("Border.jpg",1,game,196,1)
cp=Image("pdd.png",game)
cphp=Image("cphp.png",game)
alien=Image("alien.png",game)
ahp=Image("ahp.png",game)
satan=Image("satan.png",game)
dhp=Image("satan_head.png",game)
hmims=Image("hmims.png",game)
tmags=Image("tmims.png",game)
tmags2=Image("tmg.png",game)
magos=Image("mims.png",game)
mags2=Image("mg.png",game)
mhp=Image("mhp.png",game)
glitch=Animation("glitch.png",72,game,3072/6,4056/12)
portal=Image("portal.png",game)
exalien=Image("exalien.gif",game)
exahp=Image("exahp.png",game)
excp=Image("expdd.png",game)
excphp=Image("excphp.png",game)
exsatan=Image("exsatan.png",game)
exdhp=Image("exsatan_head.png",game)
exmags=Image("exmg.png",game)
magss=Image("ms.png",game)
ca_alien=Image("ca_alien.gif",game)
ca_cp=Image("ca_pdd.png",game)
ca_satan=Image("ca_satan.png",game)
f=Font((0,0,0),24,(0,0,0),"impact")
f1=Font((255,255,255),24,(0,0,255),"impact")
f2=Font((255,255,255),18,(0,0,0),"georgia")
fD2=Font((75,100,255),18,(0,0,0),"georgia")
f3=Font((255,255,255),38,(0,0,0),"georgia")
fD3=Font((250,0,175),38,(0,0,0),"georgia")
fx=Font((255,0,0),60,(255,0,0),"georgia")
cd=Image("construction_dee.png",game)
cd2=Image("construction_dee2.png",game)
osg=Image("mgf.png",game)
bhp=Image("bhp.png",game)
mgportal=Image("mg_portal.png",game)
explosion=Animation("ex2.png",7,game,922/7,126)
kill=Sound("kill.wav",1)
iwannadddie=Image("dddoodle.png",game)
lasers = []
lasers2 = []
eggs = []
gudeggs = []
dms = []
dmsu = []
pp = []
hardpp = []
pp2 = []
thisisit = []
m78Rt3u0q1 = []
redux = []
explosions = []
crown = 0

#Resize Station
bkb.resizeTo(800,600)
bkt.resizeTo(800,600)
bk1.resizeTo(800,600)
bk2.resizeTo(800,600)
bk3.resizeTo(800,600)
bk4.resizeTo(800,600)
bks.resizeTo(800,600)
bd.resizeBy(-5)
Crown.resizeBy(50)
star.resizeBy(-75)
alien.resizeBy(-65)
ahp.resizeBy(-70)
buff.resizeBy(-75)
ddd.resizeBy(-55)
dddoodle.resizeBy(-85)
cphp.resizeBy(-75)
fist.resizeBy(-65)
sunset.resizeTo(800,600)
yeowch.resizeBy(-20)
win.resizeBy(-20)
cp.resizeBy(-10)
cd.resizeBy(-20)
cd2.resizeBy(-20)
satan.resizeBy(-25)
magos.resizeBy(-60)
tmags.resizeBy(-60)
aura.resizeBy(20)
crown2.resizeBy(-70)
exmags.resizeBy(20)
ca_alien.resizeBy(-65)
exalien.resizeBy(-65)
exahp.resizeBy(-70)
excp.resizeBy(-10)
excphp.resizeBy(-85)
ca_satan.resizeBy(-25)
exsatan.resizeBy(-25)
portal.resizeBy(-90)
osg.resizeBy(-65)
glitch.resizeBy(-80)
mgportal.resizeBy(-40)
bhp.resizeBy(-20)
explosion.resizeBy(50)
hbd.resizeBy(-20)
iwannadddie.resizeBy(70)

#Moving Station
bd.moveTo(100,300)
star.moveTo(100,236)
star.setSpeed(15,270)
border_t.moveTo(0,-20)
border_b.moveTo(0,620)
dddoodle.moveTo(50,560)
ahp.moveTo(650,550)
ddd.x = 60
yeowch.y = 250
cphp.moveTo(660,560)
cd.moveTo(600,400)
dhp.moveTo(660,560)
magos.y = 200
tmags.y = 200
mhp.moveTo(650,560)
bk4s.y = 500
aura.y = 190
mags2.y = 200
stard.y = 450
exmags.y = 150
exahp.moveTo(650,550)
excphp.moveTo(660,550)
exdhp.moveTo(660,560)
osg.setSpeed(10,90)
osg.x = 1000
osg.y = 200
bhp.x = 50
bhp.y = 560
glitch.x = 650
glitch.y = 560
mgportal.y = 100

#List Making
for index in range(100):
    lasers.append(Image("bullet.png",game))
    dmsu.append(Image("fire.png",game))
    pp.append(Image("mgf.png",game))
    pp2.append(Image("firfball.png",game))
for index in range(125):
    eggs.append(Image("boi.png",game))
    lasers2.append(Image("bullet.png",game))
    hardpp.append(Image("firfball.png",game))
for index in range(75):
    dms.append(Image("fire.png",game))
for index in range(150):
    gudeggs.append(Image("boi.png",game))
for index in range(200):
    m78Rt3u0q1.append(Image("msf.png",game))
    redux.append(Image("msfr.png",game))
    explosions.append(Animation("explosion.png",8,game,922/8,70))
for index in range(100):
    x = randint(1000,7500)
    y = randint(50,550)
    lasers[index].setSpeed(5,90)
    lasers[index].resizeBy(-80)
    lasers[index].moveTo(x,y)
for index in range(125):
    x = randint(1000,7000)
    y = randint(50,550)
    lasers2[index].setSpeed(6,90)
    lasers2[index].resizeBy(-80)
    lasers2[index].moveTo(x,y)
for index in range(125):
    x = randint(1000,7000)
    y = randint(50,550)
    eggs[index].setSpeed(4,90)
    eggs[index].resizeBy(-80)
    eggs[index].moveTo(x,y)
for index in range(150):
    x = randint(1000,7000)
    y = randint(50,550)
    gudeggs[index].setSpeed(3,90)
    gudeggs[index].resizeBy(-80)
    gudeggs[index].moveTo(x,y)
for index in range(75):
    x = randint(1000,8000)
    y = randint(50,550)
    dms[index].setSpeed(6,90)
    dms[index].resizeBy(-60)
    dms[index].moveTo(x,y)
for index in range(100):
    x = randint(1000,7000)
    y = randint(50,550)
    dmsu[index].setSpeed(8,90)
    dmsu[index].resizeBy(-50)
    dmsu[index].moveTo(x,y)
for index in range(100):
    x = randint(1000,8000)
    y = randint(50,550)
    pp[index].setSpeed(4,90)
    pp[index].resizeBy(-85)
    pp[index].moveTo(x,y)
for index in range(100):
    x = randint(1000,7500)
    y = randint(50,550)
    pp2[index].setSpeed(7,90)
    pp2[index].resizeBy(-75)
    pp2[index].moveTo(x,y)
for index in range(125):
    x = randint(1000,7000)
    y = randint(50,550)
    hardpp[index].setSpeed(8,90)
    hardpp[index].resizeBy(-70)
    hardpp[index].moveTo(x,y)
for index in range(200):
    x = randint(1000,7000)
    y = randint(50,550)
    m78Rt3u0q1[index].setSpeed(10,90)
    m78Rt3u0q1[index].resizeBy(-85)
    m78Rt3u0q1[index].moveTo(x,y)
for index in range(200):
    x = randint(250,550)
    y = randint(1500,5000)
    redux[index].setSpeed(10,0)
    redux[index].resizeBy(-85)
    redux[index].moveTo(x,y)
while not game.over:# Start screen
    game.processInput()
    bkb.draw()
    iwannadddie.draw()
    game.drawText("King Dedede Kingdom Battle",175,450,fD3)
    game.drawText("Press SPACE to Continue",300,550,fD2)
    if keys.Pressed[K_SPACE]:
        game.over=True
    if keys.Pressed[K_c] and keys.Pressed[K_r] and keys.Pressed[K_o] and keys.Pressed[K_w]:
        crown = 1
        game.over = True
    game.update(30)
game.over=False
while not game.over and crown == 1:# Start screen?
    game.processInput()
    bkb.draw()
    iwannadddie.draw()
    game.drawText("King Dedede Kingdom Battle",175,450,fD3)
    if keys.Pressed[K_n] and keys.Pressed[K_e] and keys.Pressed[K_d]:
        crown = 2
        game.over = True
    game.update(30)
game.over=False
iwannadddie.visible = False
while not game.over and crown == 2:# Vhat?
    game.processInput()
    bkb.draw()
    exmags.draw()
    game.drawText("How did you-",300,250,f3)
    game.drawText("Oh it doesn't matter",240,300,f3)
    game.drawText("You'll fail either way",240,350,f3)
    game.drawText("Best of luck to you",245,400,f3)
    game.drawText("Press RIGHT to Continue",300,550,f2)
    if keys.Pressed[K_RIGHT]:
        game.over=True
    game.update(30)
game.over = False
while not game.over and crown == 0:# tutorial 1/3
    game.processInput()
    bkt.draw()
    bd.draw()
    game.drawText("Great King!",300,25,f3)
    game.drawText("Magolor has found the Master Crown",150,125,f3)
    game.drawText("and now wishes to take over the",200,225,f3)
    game.drawText("universe starting with your kingdom!",183,325,f3)
    game.drawText("Press RIGHT to continue",300,525,f2)
    if keys.Pressed[K_RIGHT]:
        game.over=True
    game.update(30)
game.over=False
while not game.over and crown == 0:# tutorial 2/3
    game.processInput()
    bkt.draw()
    bd.draw()
    stard.draw()
    stard.rotateBy(4,"right")
    game.drawText("Press the UP and DOWN arrow keys to move",25,75,f3)
    game.drawText("Press SPACE to shoot stars",175,125,f3)
    game.drawText("Remember that if you miss your shot,",125,175,f3)
    game.drawText("You will have to wait a while",200,225,f3)
    game.drawText("before you can fire again",200,275,f3)
    game.drawText("Press SPACE to Continue",300,550,f2)
    if keys.Pressed[K_SPACE]:
        game.over=True
    game.update(30)
game.over = False
stard.visible = False
while not game.over and crown == 0:# tutorial 3/3
    game.processInput()
    bkt.draw()
    bd.draw()
    stard.draw()
    stard.rotateBy(4,"right")
    game.drawText("Magolor has assembled his army",125,50,f3)
    game.drawText("There are many strong enemies",200,225,f3)
    game.drawText("that await you",325,275,f3)
    game.drawText("Good Luck Great King !",225,475,f3)
    game.drawText("Press RIGHT to continue",300,525,f2)
    if keys.Pressed[K_RIGHT]:
        game.over=True
    game.update(30)
game.over = False
while not game.over and crown == 2:# SS1
    game.processInput()
    bk1.draw()
    ca_alien.draw()
    game.drawText("Dsl Ziv Blf? Svok Nv!",310,450,f2)
    game.drawText("Press SPACE to Continue",300,550,f2)
    if keys.Pressed[K_SPACE]:
        game.over=True
    game.update(30)
game.over = False
ca_alien.visible = False
exalien.setSpeed(6,0)
exalien.x = 700
exalien.health = 200
ddd.health = 150
game.setMusic("ddd_song.wav")
game.playMusic()
while not game.over and crown == 2:# L 1
    game.processInput()
    bk1.draw()
    star.move()
    ddd.draw()
    exahp.draw()
    exalien.move(True)
    dddoodle.draw()
    border_t.draw()
    border_b.draw()
    game.drawText("HP:" + str(ddd.health),dddoodle.x + 50,dddoodle.y,f)
    game.drawText("HP:" + str(exalien.health),exahp.x + 50,exahp.y,f)
    if keys.Pressed[K_DOWN]:
        ddd.y += 10
    if keys.Pressed[K_UP]:
        ddd.y -= 10
    if ddd.collidedWith(border_t):
        ddd.y = 50
    if ddd.collidedWith(border_b):
        ddd.y = 550
    for index in range(125):
        lasers2[index].move()
        if lasers2[index].collidedWith(ddd,"rectangle"):
            ddd.health -= 10
            lasers2[index].visible = False
        if lasers2[index].isOffScreen("left"):
            lasers2[index].x = 8000
    if keys.Pressed[K_SPACE] and star.visible == False:
        star.visible = True
        star.x = ddd.x
        star.y = ddd.y
        star.move()
    if star.collidedWith(exalien):
        exalien.health -= 10
        star.visible = False
    if star.x >= 1500:
        star.visible = False
    if exalien.health <= 0:
        game.over = True
    if keys.Pressed[K_0]:
        ddd.health = 0
    if ddd.health <= 0:
        game.over = True
    game.update(30)
game.over = False
ddd.visible = False
star.visible = False
exalien.visible = False
dddoodle.visible = False
exahp.visible = False
bk1.visible = False
while not game.over and ddd.health <= 0 and crown == 2:# Game over 1/2
    game.processInput()
    game.over=True
    game.update(30)
game.over = False
game.stopMusic()
game.setMusic("oof.wav")
game.playMusic()
while not game.over and ddd.health <= 0 and crown == 2:# Game over 2/2
    game.processInput()
    sunset.draw()
    yeowch.draw()
    game.drawText("Good Night Sweet King",320,150,f2)
    if game.over == True:
        game.quit()
    game.update(10)
game.stopMusic()
bk1.visible = True
while not game.over and crown == 0:# Level 1 Start screen
    game.processInput()
    bk1.draw()
    alien.draw()
    game.drawText("Think you can beat me?",310,450,f2)
    game.drawText("Press SPACE to Continue",300,550,f2)
    if keys.Pressed[K_SPACE]:
        game.over=True
    game.update(30)
game.over=False
ddd.visible = True
star.visible = True
dddoodle.visible = True
alien.setSpeed(4,0)
alien.x = 700
alien.health = 150
ddd.health = 150
game.setMusic("ddd_song.wav")
game.playMusic()
while not game.over and crown == 0:# Level 1
    game.processInput()
    bk1.draw()
    star.move()
    ddd.draw()
    ahp.draw()
    alien.move(True)
    dddoodle.draw()
    border_t.draw()
    border_b.draw()
    game.drawText("HP:" + str(ddd.health),dddoodle.x + 50,dddoodle.y,f)
    game.drawText("HP:" + str(alien.health),ahp.x + 50,ahp.y,f)
    if keys.Pressed[K_DOWN]:
        ddd.y += 10
    if keys.Pressed[K_UP]:
        ddd.y -= 10
    if ddd.collidedWith(border_t):
        ddd.y = 50
    if ddd.collidedWith(border_b):
        ddd.y = 550
    for index in range(100):
        lasers[index].move()
        if lasers[index].collidedWith(ddd,"rectangle"):
            ddd.health -= 10
            lasers[index].visible = False
    if keys.Pressed[K_SPACE] and star.visible == False:
        star.visible = True
        star.x = ddd.x
        star.y = ddd.y
        star.move()
    if star.collidedWith(alien):
        alien.health -= 10
        star.visible = False
    if star.x >= 1500:
        star.visible = False
    if alien.health <= 0:
        game.over = True
    if keys.Pressed[K_0]:
        ddd.health = 0
    if ddd.health <= 0:
        game.over = True
    game.update(30)    
game.over = False
ddd.visible = False
star.visible = False
alien.visible = False
dddoodle.visible = False
ahp.visible = False
game.stopMusic()

while not game.over and ddd.health >= 1 and exalien.health >= 1 and crown == 2:#O-You cheatin?
    game.processInput()
    bkb.draw()
    kill.play()
    magss.resizeBy(60)
    magss.draw()
    game.drawText("I saw you cheating",200,350,fx)
    if game.over == True:
        game.quit()
    game.update(30)

while not game.over and ddd.health >= 1 and alien.health >= 1 and crown == 0:#O-You cheatin?
    game.processInput()
    bkb.draw()
    kill.play()
    magss.resizeBy(60)
    magss.draw()
    game.drawText("I saw you cheating",200,350,fx)
    if game.over == True:
        game.quit()
    game.update(30)

while not game.over and ddd.health <= 0:# Game over 1/2
    game.processInput()
    game.over=True
    game.update(30)
game.over = False
game.stopMusic()
game.setMusic("oof.wav")
game.playMusic()
while not game.over and ddd.health <= 0:# Game over 2/2
    game.processInput()
    sunset.draw()
    yeowch.draw()
    game.drawText("Good Night Sweet King",320,150,f2)
    if game.over == True:
        game.quit()
    game.update(10)
game.stopMusic()
while not game.over and ddd.health >= 0:# Level 1 Victory
    game.processInput()
    bk1.draw()
    win.draw()
    game.drawText("You Win!",325,100,f3)
    game.drawText("Press RIGHT to continue",295,450,f2)
    if keys.Pressed[K_RIGHT]:
        game.over = True
    game.update(10)
bk1.visible = False
win.visible = False
game.over  = False
while not game.over and crown == 2:# SS2
    game.processInput()
    bk2.draw()
    ca_cp.draw()
    game.drawText("Gsviv Rh Ml Slkv Uli Fh!",295,450,f2)
    game.drawText("Press SPACE to continue",300,550,f2)
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.update(30)
ca_cp.isible = False
game.over = False
ddd.visible = True
dddoodle.visible = True
star.visible = True
excp.moveTo(710,300)
excp.setSpeed(5,0)
excp.health = 300
ddd.health = 200
game.setMusic("ddd_song.wav")
game.playMusic()
while not game.over and crown == 2:# L2
    game.processInput()
    bk2.draw()
    ddd.draw()
    star.move()
    excp.move(True)
    dddoodle.draw()
    excphp.draw()
    if ddd.collidedWith(border_t):
        ddd.y = 50
    if ddd.collidedWith(border_b):
        ddd.y = 550
    if keys.Pressed[K_DOWN]:
        ddd.y += 10
    if keys.Pressed[K_UP]:
        ddd.y -= 10
    game.drawText("HP:" + str(ddd.health),dddoodle.x + 50,dddoodle.y,f)
    game.drawText("HP:" + str(excp.health),excphp.x + 50,excphp.y,f)
    if keys.Pressed[K_SPACE] and star.visible == False:
        star.visible = True
        star.x = ddd.x
        star.y = ddd.y
        star.move()
    if star.collidedWith(excp):
        excp.health -= 10
        star.visible = False
    if star.x >= 1500:
        star.visible = False
    if excp.health <= 0:
        game.over = True
    if ddd.health <= 0:
        game.over = True
    for index in range(125):
        gudeggs[index].move()
        if gudeggs[index].collidedWith(ddd,"rectangle"):
            ddd.health -= 10
            gudeggs[index].visible = False
        if gudeggs[index].isOffScreen("left"):
            gudeggs[index].x = 7500
    game.update(30)
game.over = False
excp.visible = False
excphp.visible = False
while not game.over and ddd.health <= 0:# Game over 1/2
    game.processInput()
    game.over=True
    game.update(30)
game.over = False
game.stopMusic()
game.setMusic("oof.wav")
game.playMusic()
while not game.over and ddd.health <= 0:# Game over 2/2
    game.processInput()
    sunset.draw()
    yeowch.draw()
    game.drawText("Good Night Sweet King",320,150,f2)
    if game.over == True:
        game.quit()
    game.update(10)
while not game.over and crown == 0:# Level 2 Start Screen
    game.processInput()
    bk2.draw()
    cp.draw()
    game.drawText("It is I",375,400,f2)
    game.drawText("The Great King Dedede",310,425,f2)
    game.drawText("Press SPACE to continue",300,550,f2)
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.update(30)
game.over = False
ddd.visible = True
dddoodle.visible = True
star.visible = True
cp.moveTo(710,300)
cp.setSpeed(5,0)
cp.health = 200
ddd.health = 200
game.setMusic("ddd_song.wav")
game.playMusic()
while not game.over and crown == 0:# Level 2
    game.processInput()
    bk2.draw()
    ddd.draw()
    star.move()
    cp.move(True)
    dddoodle.draw()
    cphp.draw()
    if ddd.collidedWith(border_t):
        ddd.y = 50
    if ddd.collidedWith(border_b):
        ddd.y = 550
    if keys.Pressed[K_DOWN]:
        ddd.y += 10
    if keys.Pressed[K_UP]:
        ddd.y -= 10
    game.drawText("HP:" + str(ddd.health),dddoodle.x + 50,dddoodle.y,f)
    game.drawText("HP:" + str(cp.health),cphp.x + 50,cphp.y,f)
    if keys.Pressed[K_SPACE] and star.visible == False:
        star.visible = True
        star.x = ddd.x
        star.y = ddd.y
        star.move()
    if star.collidedWith(cp):
        cp.health -= 10
        star.visible = False
    if star.x >= 1500:
        star.visible = False
    if cp.health <= 0:
        game.over = True
    if keys.Pressed[K_0]:
        ddd.health = 0
    if ddd.health <= 0:
        game.over = True
    for index in range(125):
        eggs[index].move()
        if eggs[index].collidedWith(ddd,"rectangle"):
            ddd.health -= 10
            eggs[index].visible = False
        if eggs[index].isOffScreen("left"):
            eggs[index].x = 8000
    game.update(30)
game.over = False
game.stopMusic()
'''
while not game.over and ddd.health >= 1 and excp.health >= 1 and crown == 2:#O-You're cheatin?
    game.processInput()
    bkb.draw()
    kill.play()
    magss.resizeBy(60)
    magss.draw()
    game.drawText("I saw you cheating",200,350,fx)
    if game.over == True:
        game.quit()
    game.update(30)
while not game.over and ddd.health >= 1 and cp.health >= 1 and crown == 0:#O-You're cheatin?
    game.processInput()
    bkb.draw()
    kill.play()
    magss.resizeBy(60)
    magss.draw()
    game.drawText("I saw you cheating",200,350,fx)
    if game.over == True:
        game.quit()
    game.update(30)
'''
while not game.over and ddd.health <= 0:# Game over 1/2
    game.processInput()
    game.over=True
    game.update(30)
game.over = False
game.stopMusic()
game.setMusic("oof.wav")
game.playMusic()
while not game.over and ddd.health <= 0:# Game over 2/2
    game.processInput()
    sunset.draw()
    yeowch.draw()
    game.drawText("Good Night Sweet King",320,150,f2)
    if game.over == True:
        game.quit()
    game.update(10)
ddd.visible = False
star.visible = False
cp.visible = False
dddoodle.visible = False
cphp.visible = False
win.visible = True
game.stopMusic()
while not game.over and ddd.health >= 0:# Level 2 Victory
    game.processInput()
    bk2.draw()
    win.draw()
    game.drawText("You Win!",325,100,f3)
    game.drawText("Press RIGHT to continue",295,450,f2)
    if keys.Pressed[K_RIGHT]:
        game.over = True
    game.update(10)
bk2.visible = False
win.visible = False
game.over = False
while not game.over and crown == 2:# SS3
    game.processInput()
    bk3.draw()
    ca_satan.draw()
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.drawText("Dv Droo Mlg Yv Hzevw",310,425,f2)
    game.drawText("Dv Droo Mlg Yv Hkzivw",310,475,f2)
    game.drawText("Press SPACE to continue",300,550,f2)
    game.update(30)
game.over  = False
ca_satan.visible = False
exsatan.setSpeed(8,0)
exsatan.x = 720
ddd.visible = True
dddoodle.visible = True
ddd.health = 250
exsatan.health = 250
game.setMusic("ddd_song.wav")
game.playMusic()
while not game.over and crown == 2:# L3
    game.processInput()
    bk3.draw()
    ddd.draw()
    exsatan.move(True)
    star.move()
    dddoodle.draw()
    exdhp.draw()
    if ddd.collidedWith(border_t):
        ddd.y = 50
    if ddd.collidedWith(border_b):
        ddd.y = 550
    if keys.Pressed[K_DOWN]:
        ddd.y += 10
    if keys.Pressed[K_UP]:
        ddd.y -= 10
    game.drawText("HP:" + str(ddd.health),dddoodle.x + 50,dddoodle.y,f1)
    game.drawText("HP:" + str(exsatan.health),exdhp.x + 50,exdhp.y,f1)
    if keys.Pressed[K_SPACE] and star.visible == False:
        star.visible = True
        star.x = ddd.x
        star.y = ddd.y
        star.move()
    if star.collidedWith(exsatan):
        exsatan.health -= 10
        star.visible = False
    if star.x >= 1500:
        star.visible = False
    if exsatan.health <= 0:
        game.over = True
    if ddd.health <= 0:
        game.over = True
    for index in range(75):
        dmsu[index].move()
        if dmsu[index].collidedWith(ddd,"rectangle"):
            ddd.health -= 10
            dmsu[index].visible = False
        if dmsu[index].isOffScreen("left"):
            dmsu[index].x = 8000
    game.update(30)
while not game.over and ddd.health <= 0:# Game over 1/2
    game.processInput()
    game.over=True
    game.update(30)
game.over = False
game.stopMusic()
game.setMusic("oof.wav")
game.playMusic()
while not game.over and ddd.health <= 0:# Game over 2/2
    game.processInput()
    sunset.draw()
    yeowch.draw()
    game.drawText("Good Night Sweet King",320,150,f2)
    if game.over == True:
        game.quit()
    game.update(10)
game.over = False
ddd.visible = False
star.visible = False
dddoodle.visible = False
bkt.visible = True
win.visible = True
game.stopMusic()
while not game.over and crown == 0:# Level 3 Start Screen
    game.processInput()
    bk3.draw()
    satan.draw()
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.drawText("How did I get here ?",325,450,f2)
    game.drawText("Press SPACE to continue",300,550,f2)
    game.update(30)
game.over  = False
satan.setSpeed(7,0)
satan.x = 720
ddd.visible = True
dddoodle.visible = True
ddd.health = 250
satan.health = 200
game.setMusic("ddd_song.wav")
game.playMusic()
while not game.over and crown == 0:# Level 3
    game.processInput()
    bk3.draw()
    ddd.draw()
    satan.move(True)
    star.move()
    dddoodle.draw()
    dhp.draw()
    if ddd.collidedWith(border_t):
        ddd.y = 50
    if ddd.collidedWith(border_b):
        ddd.y = 550
    if keys.Pressed[K_DOWN]:
        ddd.y += 10
    if keys.Pressed[K_UP]:
        ddd.y -= 10
    game.drawText("HP:" + str(ddd.health),dddoodle.x + 50,dddoodle.y,f1)
    game.drawText("HP:" + str(satan.health),dhp.x + 50,dhp.y,f1)
    if keys.Pressed[K_SPACE] and star.visible == False:
        star.visible = True
        star.x = ddd.x
        star.y = ddd.y
        star.move()
    if star.collidedWith(satan):
        satan.health -= 10
        star.visible = False
    if star.x >= 1500:
        star.visible = False
    if satan.health <= 0:
        game.over = True
    if keys.Pressed[K_0]:
        ddd.health = 0
    if ddd.health <= 0:
        game.over = True
    for index in range(75):
        dms[index].move()
        if dms[index].collidedWith(ddd,"rectangle"):
            ddd.health -= 10
            dms[index].visible = False
        if dms[index].isOffScreen("left"):
            dms[index].x = 8000
    game.update(30)
game.over = False
game.stopMusic()

while not game.over and ddd.health >= 1 and exsatan.health >= 1 and crown == 2:#O-You're cheatin?
    game.processInput()
    bkb.draw()
    kill.play()
    magss.resizeBy(60)
    magss.draw()
    game.drawText("I saw you cheating",200,350,fx)
    if game.over == True:
        game.quit()
    game.update(30)
while not game.over and ddd.health >= 1 and satan.health >= 1 and crown == 0:#O-You're cheatin?
    game.processInput()
    bkb.draw()
    kill.play()
    magss.resizeBy(60)
    magss.draw()
    game.drawText("I saw you cheating",200,350,fx)
    if game.over == True:
        game.quit()
    game.update(30)
while not game.over and ddd.health <= 0:# Game over 1/2
    game.processInput()
    game.over=True
    game.update(30)
game.over = False
game.stopMusic()
game.setMusic("oof.wav")
game.playMusic()
while not game.over and ddd.health <= 0:# Game over 2/2
    game.processInput()
    sunset.draw()
    yeowch.draw()
    game.drawText("Good Night Sweet King",320,150,f2)
    if game.over == True:
        game.quit()
    game.update(10)
game.over = False
ddd.visible = False
star.visible = False
satan.visible = False
dddoodle.visible = False
dhp.visible = False
win.visible = True
game.stopMusic()
while not game.over and ddd.health >= 0:# Level 3 Victory
    game.processInput()
    bk3.draw()
    win.draw()
    game.drawText("You Win!",325,100,f3)
    game.drawText("Press RIGHT to continue",295,450,f2)
    if keys.Pressed[K_RIGHT]:
        game.over = True
    game.update(10)
bk3.visible = False
win.visible = False
game.over = False
exmags.x = 700
exmags.health = 200
exmags.setSpeed(9,0)
ddd.health = 300
ddd.visible = True
dddoodle.visible = True
while not game.over and crown == 2:# L4
    game.processInput()
    bk4.draw()
    ddd.draw()
    star.move()
    dddoodle.draw()
    exmags.move(True)
    mhp.draw()
    if ddd.collidedWith(border_t):
        ddd.y = 50
    if ddd.collidedWith(border_b):
        ddd.y = 550
    if keys.Pressed[K_DOWN]:
        ddd.y += 10
    if keys.Pressed[K_UP]:
        ddd.y -= 10
    game.drawText("HP:" + str(ddd.health),dddoodle.x + 50,dddoodle.y,f1)
    game.drawText("HP:" + str(exmags.health),mhp.x + 50,mhp.y,f1)
    if keys.Pressed[K_SPACE] and star.visible == False:
        star.visible = True
        star.x = ddd.x
        star.y = ddd.y
        star.move()
    if star.collidedWith(exmags):
        exmags.health -= 10
        star.visible = False
    if star.x >= 1500:
        star.visible = False
    if exmags.health <= 0:
        game.over = True
    if ddd.health <= 0:
        game.over = True
    for index in range(125):
        hardpp[index].move()
        if hardpp[index].collidedWith(ddd,"rectangle"):
            ddd.health -= 10
            hardpp[index].visible = False
        if hardpp[index].isOffScreen("left"):
            hardpp[index].x = 8000
    game.update(30)
game.over = False
game.stopMusic()
while not game.over and ddd.health >= 1 and exmags.health >= 1 and crown == 2:#O-You're cheatin?
    game.processInput()
    bkb.draw()
    kill.play()
    magss.resizeBy(60)
    magss.draw()
    game.drawText("I saw you cheating",200,350,fx)
    if game.over == True:
        game.quit()
    game.update(30)
while not game.over and ddd.health <= 0 and crown == 2:# Game over 1/2
    game.processInput()
    game.over=True
    game.update(30)
game.over = False
game.stopMusic()
game.setMusic("oof.wav")
game.playMusic()
while not game.over and ddd.health <= 0 and crown == 2:# Game over 2/2
    game.processInput()
    sunset.draw()
    yeowch.draw()
    game.drawText("Good Night Sweet King",320,150,f2)
    if game.over == True:
        game.quit()
    game.update(10)
game.stopMusic()
ddd.visible = False
star.visible = False
exmags.speed = 0
exmags.moveTo(400,200)
while not game.over and crown == 2:# HooH
    game.processInput()
    bk4.draw()
    exmags.draw()
    game.drawText("NOOOO !",315,300,f3)
    game.drawText("I won't be defeated !",235,400,f3)
    game.drawText("Press RIGHT to continue",295,500,f2)
    if keys.Pressed[K_RIGHT]:
        game.over = True
    game.update(30)
game.over = False
exmags.y = 300
while not game.over and crown == 2:# Oh boi
    game.processInput()
    bk4.draw()
    exmags.draw()
    portal.draw()
    if portal.collidedWith(bk4):
        portal.resizeBy(5)
    if portal.width >= 5000 and portal.height >= 5000:
        game.over = True
    game.update(30)
game.over = False
exmags.visible = False
portal.visible = False
magss.y = 200
while not game.over and crown == 2:# Cookie Country
    game.processInput()
    bkb.draw()
    magss.draw()
    game.drawText("MUAHAHAHAHA",250,350,f3)
    game.drawText("Press C to continue",317,550,f2)
    if keys.Pressed[K_c]:
        game.over = True
    game.update(30)
game.over = False
while not game.over and crown == 2:# Raisin Ruins
    game.processInput()
    bkb.draw()
    magss.draw()
    game.drawText("I have unleashed my true power!",150,350,f3)
    game.drawText("Press R to continue",317,550,f2)
    if keys.Pressed[K_r]:
        game.over = True
    game.update(30)
game.over = False
while not game.over and crown == 2:# Onion Ocean
    game.processInput()
    bkb.draw()
    magss.draw()
    game.drawText("That Magolor was a worthy puppet",125,350,f3)
    game.drawText("But now I no longer have a need for his body!",30,450,f3)
    game.drawText("Press O to continue",317,550,f2)
    if keys.Pressed[K_o]:
        game.over = True
    game.update(30)
game.over = False
while not game.over and crown == 2:# White Wafers
    game.processInput()
    bkb.draw()
    magss.draw()
    game.drawText("You can not stop me!",250,350,f3)
    game.drawText("I am unstoppable!",250,425,f3)
    game.drawText("Press W to continue",317,550,f2)
    if keys.Pressed[K_w]:
        game.over = True
    game.update(30)
game.over = False
magss.setSpeed(0.00001,90)
magos.y = 225
magos.x = 1000
magos.setSpeed(7,90)
while not game.over and crown == 2:# Nutty Noon
    game.processInput()
    bkb.draw()
    magss.move()
    osg.move()
    if osg.collidedWith(magss):
        magss.speed = 7
        game.drawText("GAAAH!",325,350,f3)
    if osg.x <= -200:
        osg.visible = False
    if osg.visible == False:
        magos.move()
    if magos.x <= 400:
        magos.speed = 0
        game.drawText("Finally, A friendly face!",225,350,f3)
        game.drawText("Press N to continue",317,550,f2)
    if keys.Pressed[K_n] and magos.x <= 400:
        game.over = True
    game.update(30)
game.over = False
while not game.over and crown == 2:# Egg Engines
    game.processInput()
    bkb.draw()
    magos.draw()
    game.drawText("I'll transform you",250,350,f3)
    game.drawText("so you can beat the master crown",140,425,f3)
    game.drawText("Press E to continue",317,550,f2)
    if keys.Pressed[K_e]:
        game.over = True
    game.update(30)
game.over = False
while not game.over and crown == 2:# Dangerous Dinner
    game.processInput()
    bkb.draw()
    magos.draw()
    mgportal.draw()
    game.drawText("Now go save the world!",235,450,f3)
    game.drawText("Press D to continue",317,550,f2)
    if keys.Pressed[K_d]:
        game.over = True
    game.update(30)
game.over = False
while not game.over and crown == 2:# Iob ho
    game.processInput()
    bkb.draw()
    magos.draw()
    mgportal.draw()
    if mgportal.collidedWith(bk4):
        mgportal.resizeBy(5)
    if mgportal.width >= 4500 and mgportal.height >= 4500:
        game.over = True
    game.update(30)
game.over = False
mgportal.visible = False
magos.visible = False
magss.x = 400
magss.resizeBy(-10)
game.stopMusic()
game.setMusic("goodsong.wav")
game.playMusic()
while not game.over and crown == 2:# SSA
    game.processInput()
    bks.draw()
    magss.draw()
    game.drawText("It will be 'game over' soon enough",150,350,f3)
    game.drawText("Press SPACE to continue",300,550,f2)
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.update(30)
game.over = False
magss.visible = True
magss.setSpeed(10,0)
magss.x = 720
magss.resizeBy(-30)
buff.health = 450
buff.x = 80
magss.health = 1000
fist.setSpeed(15,270)
while not game.over and crown == 2:# 7h3 1 7Ru3 f1N41 13v31
    game.processInput()
    ey = randint(50,550)
    bks.draw()
    buff.draw()
    fist.move()
    bhp.draw()
    magss.move(True)
    glitch.draw()
    if buff.collidedWith(border_t):
        buff.y = 50
    if buff.collidedWith(border_b):
        buff.y = 550
    if keys.Pressed[K_DOWN]:
        buff.y += 10
    if keys.Pressed[K_UP]:
        buff.y -= 10
    game.drawText("HP:" + str(buff.health),bhp.x + 50,bhp.y,f1)
    game.drawText("HP:" + str(magss.health),glitch.x + 65,glitch.y,f1)
    if keys.Pressed[K_SPACE] and fist.visible == False:
        fist.visible = True
        fist.x = buff.x
        fist.y = buff.y
        fist.move()
    if fist.collidedWith(magss):
        magss.health -= 10
        fist.visible = False
    if fist.x >= 1200:
        fist.visible = False
    if magss.health <= 0:
        game.over = True
    if buff.health <= 0:
        game.over = True
    for index in range(200):
        m78Rt3u0q1[index].move()
        if m78Rt3u0q1[index].collidedWith(buff,"rectangle"):
            buff.health -= 10
            m78Rt3u0q1[index].x = 6000
            m78Rt3u0q1[index].y = ey
        if m78Rt3u0q1[index].collidedWith(fist,"rectangle"):
            m78Rt3u0q1[index].setSpeed(15,270)
            if m78Rt3u0q1[index].collidedWith(magss,"rectangle"):
                magss.health -= 5
                m78Rt3u0q1[index].x = 6000
                m78Rt3u0q1[index].y = ey
                m78Rt3u0q1[index].setSpeed(10,90)
        if m78Rt3u0q1[index].isOffScreen("left"):
            m78Rt3u0q1[index].x = 6000
            m78Rt3u0q1[index].y = ey
        if m78Rt3u0q1[index].x >= 7000:
            m78Rt3u0q1[index].x = 6000
            m78Rt3u0q1[index].y = ey
            m78Rt3u0q1[index].setSpeed(10,90)
        if game.over == True:
            m78Rt3u0q1[index].visible = False
    game.update(30)
game.over = False
game.stopMusic()
explosion.x = buff.x
explosion.y = buff.y
game.stopMusic()
while not game.over and buff.health >= 0 and magss.health >= 0 and crown == 2:#   
    game.processInput()
    bkb.draw()
    magss.draw()
    explosion.draw(False)
    if game.over == True:
        game.quit()
    game.update(20)
while not game.over and buff.health <= 0 and crown == 2:# Game over 1/2
    game.processInput()
    game.over=True
    game.update(30)
game.over = False
game.stopMusic()
game.setMusic("oof.wav")
game.playMusic()
while not game.over and buff.health <= 0 and crown == 2:# Game over 2/2
    game.processInput()
    sunset.draw()
    yeowch.draw()
    game.drawText("Good Night Sweet King",320,150,f2)
    if game.over == True:
        game.quit()
    game.update(10)
game.stopMusic()
ddd.visible = False
bhp.visible = False
glitch.visible = False
magss.x = 400
magss.y = 350
magss.resizeBy(25)
while not game.over and crown == 2: # SSNAAAAAAAAAAAAAAAAAAAKEEEEE!
    game.processInput()
    bks.draw()
    magss.draw()
    game.drawText("N-No I!",340,450,f3)
    game.drawText("Press SPACE to continue",300,550,f2)
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.update(30)
game.over = False
magss.setSpeed(1,1)
while not game.over and crown == 2: # OOOOOOOOOAAAH MY! OOOOOOOOOOOAAH MY GOD!
    game.processInput()
    bks.draw()
    magss.move()
    for index in range(200):
        redux[index].move()
        if redux[index].collidedWith(magss):
            xx = randint(300,500)
            xy = randint(200,280)
            explosions[index].moveTo(xx,xy)
            magss.angle += 10
            game.drawText("Press SPACE to continue",295,550,f2)
            if keys.Pressed[K_SPACE]:
                game.over = True
        if redux[index].isOffScreen("top"):
            redux[index].y = 3000
    game.update(30)
game.over = False
ddd.visible = True
star.visible = False
magss.visible = False
explosion.x = 400
explosion.y = 200
crown2.y = 200
while not game.over and crown == 2: # KABLOOOOOEYY!
    game.processInput()
    bks.draw()
    crown2.draw()
    explosion.draw(False)
    game.drawText("Press RIGHT to continue",295,550,f2)
    if keys.Pressed[K_RIGHT]:
        game.over = True
    game.update(5)
game.over = False
magos.visible = True
magos.setSpeed(10,0)
magos.y = 800
magos.x = 400
crown2.x = 325
crown2.y = 200
while not game.over and crown == 2: # hello there
    game.processInput()
    bks.draw()
    magos.move()
    crown2.draw()
    if magos.y <= 220:
        magos.speed = 0
    if magos.speed == 0:
        game.drawText("We should keep this in a safe place",150,350,f3)
        game.drawText("Press SPACE to continue",295,550,f2)
    if keys.Pressed[K_SPACE] and magos.speed == 0:
        game.over = True
    game.update(30)
game.over = False
crown2.visible = False
while not game.over and crown == 2: # You're welcome
    game.processInput()
    bks.draw()
    magos.draw()
    game.drawText("Anyway , King Dedede",225,300,f3)
    game.drawText("I wanted to thank you for saving me",125,375,f3)
    game.drawText("from the master crown's control",150,450,f3)
    game.drawText("Press RIGHT to continue",295,550,f2)
    if keys.Pressed[K_RIGHT]:
        game.over = True
    game.update(30)
game.over = False
while not game.over and crown == 2: # No prob bob
    game.processInput()
    bks.draw()
    magos.draw()
    game.drawText("I hope you can forgive me",200,300,f3)
    game.drawText("For as you can see",225,375,f3)
    game.drawText("I wasn't exactly myself",210,450,f3)
    game.drawText("Press SPACE to continue",295,550,f2)
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.update(30)
game.over = False
portal.visible = True
portal.width = 100
portal.height = 100
portal.y = 100
while not game.over and crown == 2: # It's Magolor
    game.processInput()
    bks.draw()
    magos.draw()
    portal.draw()
    game.drawText("Now, Let's go home",225,300,f3)
    game.drawText("Press RIGHT to continue",295,550,f2)
    if keys.Pressed[K_RIGHT]:
        game.over = True
    game.update(30)
game.over = False
while not game.over and crown == 2: # Yeah
    game.processInput()
    bks.draw()
    magos.draw()
    portal.draw()
    if portal.collidedWith(bks):
        portal.resizeBy(5)
    if portal.width >= 4500 and portal.height >= 4500:
        game.over = True
    game.update(30)
game.over = False
bkt.visible = True
hbd.x = 125
hbd.y = 450
hdd.x = 375
hdd.y = 490
hmims.x = 650
hmims.resizeBy(-20)
hmims.y = 490
cd.x = 500
cd.y = 200
cd2.x = 300
cd2.y = 200
while not game.over and crown == 2:# The end
    game.processInput()
    bkt.draw()
    hbd.draw()
    hdd.draw()
    hmims.draw()
    cd.draw()
    cd2.draw()
    game.drawText("Master Games",290,50,f3)
    game.drawText("Thank you for playing our game!",150,300,f3)
    game.update(30)
magos.moveTo(400,200)
magss.visible = True
while not game.over and crown == 0:# This is it!
    game.processInput()
    bk4.draw()
    magos.draw()
    game.drawText("So you're finally here ...",250,300,f3)
    game.drawText("I am Magolor",300,400,f3)
    game.drawText("Press SPACE to continue",275,550,f2)
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.update(30)
game.over = False
magos.setSpeed(4,0)
magos.x = 720
ddd.visible = True
dddoodle.visible = True
ddd.health = 300
magos.health = 100
game.setMusic("ddd_song.wav")
game.playMusic()
while not game.over and crown == 0:# Level 4
    game.processInput()
    bk4.draw()
    ddd.draw()
    magos.move(True)
    star.move()
    dddoodle.draw()
    mhp.draw()
    if ddd.collidedWith(border_t):
        ddd.y = 50
    if ddd.collidedWith(border_b):
        ddd.y = 550
    if keys.Pressed[K_DOWN]:
        ddd.y += 10
    if keys.Pressed[K_UP]:
        ddd.y -= 10
    game.drawText("HP:" + str(ddd.health),dddoodle.x + 50,dddoodle.y,f1)
    game.drawText("HP:" + str(magos.health),mhp.x + 50,mhp.y,f1)
    if keys.Pressed[K_SPACE] and star.visible == False:
        star.visible = True
        star.x = ddd.x
        star.y = ddd.y
        star.move()
    if star.collidedWith(magos):
        magos.health -= 10
        star.visible = False
    if star.x >= 1500:
        star.visible = False
    if magos.health <= 0:
        game.over = True
    if keys.Pressed[K_0]:
        ddd.health = 0
    if ddd.health <= 0:
        game.over = True
    for index in range(100):
        pp[index].move()
        if pp[index].collidedWith(ddd,"rectangle"):
            ddd.health -= 10
            pp[index].visible = False
    game.update(30)
game.over = False
game.stopMusic()
while not game.over and ddd.health >= 1 and magos.health >= 1 and crown == 0:#O-You're cheatin?
    game.processInput()
    bkb.draw()
    kill.play()
    magss.resizeBy(60)
    magss.draw()
    game.drawText("I saw you cheating",200,350,fx)
    if game.over == True:
        game.quit()
    game.update(30)
while not game.over and ddd.health <= 0:# Game over 1/2
    game.processInput()
    game.over=True
    game.update(30)
game.over = False
game.stopMusic()
game.setMusic("oof.wav")
game.playMusic()

while not game.over and ddd.health <= 0:# Game over 2/2
    game.processInput()
    sunset.draw()
    yeowch.draw()
    game.drawText("Good Night Sweet King",320,150,f2)
    if game.over == True:
        game.quit()
    game.update(10)
game.stopMusic()
game.over = False
game.stopMusic()
ddd.visible = False
star.visible = False
magos.visible = False
magos.speed = 0
dddoodle.visible = False
mhp.visible = False
magos.moveTo(400,200)
magos.visible = True
while not game.over and crown == 0:# You Won!
    game.processInput()
    bk4.draw()
    magos.draw()
    game.drawText("Alright ...",340,300,f3)
    game.drawText("You may have beaten me but ...",200,400,f3)
    game.drawText("Press RIGHT to continue",295,500,f2)
    if keys.Pressed[K_RIGHT]:
        game.over = True
    game.update(30)
game.over = False
magos.visible = False
crown2.visible = True
crown2.y = 155
crown2.x = 400
while not game.over and crown == 0:# Wait What
    game.processInput()
    bk4.draw()
    tmags.draw()
    aura.draw()
    crown2.draw()
    game.drawText("I will show you what true pain feels like !",80,350,f3)
    game.drawText("Press SPACE to continue",285,550,f2)
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.update(30)
game.over = False
aura.visible = False
tmags.visible = False
crown2.visible = False
while not game.over and crown == 0:# Oh It's on!
    game.processInput()
    bk4.draw()
    mags2.draw()
    game.drawText("This is the true power of the master crown !",50,350,f3)
    game.drawText("Press RIGHT to continue",295,500,f2)
    if keys.Pressed[K_RIGHT]:
        game.over = True
    game.update(30)
game.over = False
bk4.visible = False
ddd.visible = True
star.visible = True
dddoodle.visible = True
mhp.visible = True
mags2.x = 700
mags2.health = 300
mags2.setSpeed(8,0)
bk4.visible = True
mags2.visible = True
while not game.over and crown == 0:# True Level 4
    game.processInput()
    bk4.draw()
    ddd.draw()
    star.move()
    dddoodle.draw()
    mags2.move(True)
    mhp.draw()
    if ddd.collidedWith(border_t):
        ddd.y = 50
    if ddd.collidedWith(border_b):
        ddd.y = 550
    if keys.Pressed[K_DOWN]:
        ddd.y += 10
    if keys.Pressed[K_UP]:
        ddd.y -= 10
    game.drawText("HP:" + str(ddd.health),dddoodle.x + 50,dddoodle.y,f1)
    game.drawText("HP:" + str(mags2.health),mhp.x + 50,mhp.y,f1)
    if keys.Pressed[K_SPACE] and star.visible == False:
        star.visible = True
        star.x = ddd.x
        star.y = ddd.y
        star.move()
    if star.collidedWith(mags2):
        mags2.health -= 10
        star.visible = False
    if star.x >= 1500:
        star.visible = False
    if mags2.health <= 0:
        game.over = True
    if keys.Pressed[K_0]:
        ddd.health = 0
    if ddd.health <= 0:
        game.over = True
    for index in range(100):
        pp2[index].move()
        if pp2[index].collidedWith(ddd,"rectangle"):
            ddd.health -= 10
            pp2[index].visible = False
        if pp2[index].isOffScreen("left"):
            pp2[index].x = 8500
    game.update(30)
game.stopMusic()
game.over = False
while not game.over and ddd.health >= 1 and mags2.health >= 1 and crown == 0:#O-You're cheatin?
    game.processInput()
    bkb.draw()
    kill.play()
    magss.resizeBy(60)
    magss.draw()
    game.drawText("I saw you cheating",200,350,fx)
    if game.over == True:
        game.quit()
    game.update(30)
while not game.over and ddd.health <= 0 and crown == 0:# Game over 1/2
    game.processInput()
    game.over=True
    game.update(30)
game.over = False
game.stopMusic()
game.setMusic("oof.wav")
game.playMusic()
while not game.over and ddd.health <= 0 and crown == 0:# Game over 2/2
    game.processInput()
    sunset.draw()
    yeowch.draw()
    game.drawText("Good Night Sweet King",320,150,f2)
    if game.over == True:
        game.quit()
    game.update(10)
ddd.visible = False
star.visible = False
mags2.speed = 0
mags2.moveTo(400,200)
game.stopMusic()
while not game.over and crown == 0:#Take That!
    game.processInput()
    bk4.draw()
    mags2.draw()
    game.drawText("I-Impossible !",295,300,f3)
    game.drawText("How did you beat me ?",235,400,f3)
    game.drawText("Press SPACE to continue",295,500,f2)
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.update(30)
game.over = False
tmags2.setSpeed(7,0)
tmags2.moveTo(400,300)
crown2.moveTo(400,-100)
crown2.setSpeed(5,180)
while not game.over and crown == 0:#Long Live The King
    game.processInput()
    bk4.draw()
    tmags2.move()
    game.drawText("NOOOOOOOOOOOO",205,500,f3)
    if tmags2.y <= -200:
        game.over = True
    game.update(30)
game.over = False
tmags2.visible = False
bd.visible = True
bd.moveTo(400,440)
bd.resizeBy(-15)
while not game.over and crown == 0:# We win epic dub gamers
    game.processInput()
    bk4.draw()
    bd.draw()
    game.drawText("Great work great king!",200,25,f3)
    game.drawText("You defeated Magolor!",200,75,f3)
    game.drawText("Unfortunately, Magolor took the ",110,125,f3)
    game.drawText("Master crown with him",200,175,f3)
    game.drawText("He could be plotting his revenge!",100,275,f3)
    game.drawText("Press SPACE to continue",295,550,f2)
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.update(30)
game.over = False
mags2.moveTo(400,100)
while not game.over and crown == 0:# THE END?
    game.processInput()
    bkb.draw()
    mags2.draw()
    game.drawText("Impressive job Player",225,200,f3)
    game.drawText("Thanks for keeping me entertained",100,250,f3)
    game.drawText("It was humorous watching you squirm around",25,300,f3)
    game.drawText("You could never type 'Crowned'",150,350,f3)
    game.drawText("in the title screen",250,400,f3)
    game.drawText("BAD END",300,525,f3)
    game.update(30)
game.quit()
