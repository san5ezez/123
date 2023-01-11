from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 0
y = 100
z = 0
import time
while 999999999999999999999999999999999999:
    wait = input("Как дела??")
    if wait == "Норм":
        mc.postToChat("О, у меня тоже!")
        mc.postToChat("Ладно я пошол пока!")
        mc.setBlocks(x, y, z, 100, 200, 100, 57)
    if wait == "Плохо":
        wwait = input("Блин жаль): Ладно го мем расскожу?  :")
        if wwait == "Го" or "" or "ГО":
            mc.postToChat("На фото котёночек приблизил свой мокрый нос к снимающей его камере. Подпись поверх:«i'm a top»«i'm a bottom»ok well i'm a creep i'm a weirdo(«я актив»«я пассив»окей ну я слизняк я чудак")
        if wwait == "Нееее" or "Не" or "No" or "Нет!":
            mc.postToChat("Ладно пока!")
mc.postToChat("Спасибо что пользуетесь нашей услугой!")