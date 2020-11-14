from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlock(x,y+1,z,46)
mc.setBlock(x,y+2,z,46)
mc.setBlock(x,y+3,z,46)
mc.setBlock(x,y+4,z,46)
mc.setBlock(x,y+5,z,46)
mc.setBlock(x,y+6,z,46)
mc.setBlock(x,y+7,z,46)