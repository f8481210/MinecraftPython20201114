#檔名
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlocks(x+10,y+1,z+10,x-10,y-1,z-10,0)