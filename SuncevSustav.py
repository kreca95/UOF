import math
from vpython import *

# Gravitacijska konstanta
G = 6.67 * math.pow(10,-11)

# Masa marsa
MR = 0.642 * math.pow(10,24)
# Masa zemlje
MZ = 5.973 * math.pow(10,24)
# Masa venere
MV = 4.87 * math.pow(10,24)
# Masa merkura
MM = 0.33 * math.pow(10,24)
# Masa sunca
MS = 1.989 * math.pow(10,30)

#Radius Sunce - Mars
RSR = 227900000000
# Radius Sunce - Zemlja
RSZ = 149600000000
# Radius Sunce - Venera
RSV = 108200000000
#Radius Sunce - Merkur
RSM = 57900000000

#Gravitacijska sila Sunce -Mars
FRS = G*(MS*MR)/math.pow(RSR,2)
# Gravitacijska sila Sunce - Zemlja
FZS = G*(MS*MZ)/math.pow(RSZ,2)
# Gravitacijska sila Sunce - Venera
FVS = G*(MS*MV)/math.pow(RSV,2)
# Gravitacijska sila Sunce - Merkur
FMS = G*(MS*MM)/math.pow(RSM,2)

# velocity Marsa naspram Sunca(rad/s)
wR = math.sqrt(FRS/(MR * RSR))
# Velocity Zemlje (m/s)
vR = wR*RSR
print(vR)
print(wR)
# velocity Zemlje naspram Sunca(rad/s)
wZ = math.sqrt(FZS/(MZ * RSZ))
# Velocity Zemlje (m/s)
vZ = wZ*RSZ

# velocity Venere naspram Sunca(rad/s)
wV = math.sqrt(FVS/(MV * RSV))
# Velocity Venere (m/s)
vV = wV*RSV

# velocity Merkura naspram Sunca(rad/s)
wM = math.sqrt(FMS/(MM * RSM))
# Velocity Merkura (m/s)
vM = wM*RSM



# Initial angular position
theta0 = 0

def positionMars(t):
    theta = theta0 + wR * t
    return theta

def positionZemlje(t):
    theta = theta0 + wZ * t
    return theta

def positionMerkur(t):
    theta = theta0 + wM * t
    return theta

def positionVenera(t):
    theta = theta0 + wV * t
    return theta

# Parametri sustava
v = vector(0.5,0,0)
R = sphere(pos=vector(8,0,0),color=color.red,radius=.4,make_trail=True)
Z = sphere(pos=vector(7,0,0),texture = textures.earth,radius=.5,make_trail=True)
V = sphere(pos=vector(6,0,0),color=color.magenta,radius=.5,make_trail=True)
M = sphere(pos=vector(4,0,0),color=color.orange,radius=.2,make_trail=True)
S = sphere(pos=vector(0,0,0),color=color.yellow,radius=2.5)

#Velocity za kretnju u Z smjeru
S.velocity = vector(0,0,1)
Z.velocity = vector(0,0,1)
M.velocity = vector(0,0,1)
V.velocity = vector(0,0,1)
R.velocity = vector(0,0,1)

t = 0
thetaTerra1 = 0
dt = 5500
deltat = 0.005
dthetaR = positionMars(t+dt)- positionMars(t)
dthetaZ = positionZemlje(t+dt)- positionZemlje(t)
dthetaM = positionMerkur(t+dt)- positionMerkur(t)
dthetaV = positionVenera(t+dt)- positionVenera(t)

scene.camera.follow(S)
while True:
    rate(200)
    
    #rotacija oko Sunca
    thetaMars = positionMars(t+dt)- positionMars(t)
    thetaZemlje = positionZemlje(t+dt)- positionZemlje(t)
    thetaMerkur = positionMerkur(t+dt)- positionMerkur(t)
    thetaVenera = positionVenera(t+dt)- positionVenera(t)
    
    R.pos = rotate(R.pos,angle=thetaMars,axis=vec(0,0,1))
    Z.pos = rotate(Z.pos,angle=thetaZemlje,axis=vec(0,0,1))
    M.pos = rotate(M.pos,angle=thetaMerkur,axis=vec(0,0,1))
    V.pos = rotate(V.pos,angle=thetaVenera,axis=vec(0,0,1))
    
    #kretnja kroz svemir u Z smjeru
    S.pos =  S.pos + S.velocity * deltat
    Z.pos =  Z.pos + Z.velocity * deltat
    M.pos =  M.pos + M.velocity * deltat
    V.pos =  V.pos + V.velocity * deltat
    R.pos =  R.pos + R.velocity * deltat
    
    t += dt
    
    
    
    
    
    
    
    
    
    
    
