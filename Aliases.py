from Helper import color
from Helper import sudo

import random
import org.bukkit as bukkit

itemnamewhitelist = "1234567890abcdeflmnok"

# /fast
# /fixme

# Time Commands
@hook.command("day", description="Set your time to day.")
def onCommandDay(sender,args):
    sender.sendMessage("Your time was set to day.")
    sender.setPlayerTime(6000,0)
    return True

@hook.command("night", descriptoin="Set your time to night.")
def onCommandNight(sender,args):
    sender.sendMessage("Your time was set to night.")
    sender.setPlayerTime(18000,0)
    return True

# Fix lag
@hook.command("fixlag", description="Clears out minecarts,arrows,items, etc.")
def onCommandFixLag(sender, args):
    bukkit.Bukkit.dispatchCommand(sender, "rem items -1")
    bukkit.Bukkit.dispatchCommand(sender, "rem arrows -1")
    bukkit.Bukkit.dispatchCommand(sender, "rem boats -1")
    bukkit.Bukkit.dispatchCommand(sender, "rem paintings -1")
    bukkit.Bukkit.dispatchCommand(sender, "rem xp -1")

    bukkit.Bukkit.dispatchCommand(sender, "butcher -f")

    sudo("save-all")

    sender.sendMessage("You fixed teh lags!")
    return True
    
# Effects
@hook.command("e", description="List potion effect NBT values.")
def onCommandE(sender,args):
    if args[0] == "2":
        sender.sendMessage("06 - \u00A74Health")
        sender.sendMessage("07 - \u00A70Damage")
        sender.sendMessage("08 - \u00A75Jump Boost")
        sender.sendMessage("09 - \u00A77Nausea")
        sender.sendMessage("10 - \u00A7dRegeneration")
        sender.sendMessage("\u00A76Page \u00A7c2 \u00A76of \u00A7c4")
        return True
    if args[0] == "3":
        sender.sendMessage("11 - \u00A75Resistance")
        sender.sendMessage("12 - \u00A76Fire Resistance")
        sender.sendMessage("13 - \u00A73Water Breathing")
        sender.sendMessage("14 - \u00A78Invisibility")
        sender.sendMessage("15 - \u00A70Blindness")
        sender.sendMessage("\u00A76Page \u00A7c3 \u00A76of \u00A7c4")
        return True
    if args[0] == "4":
        sender.sendMessage("16 - \u00A74Night Vision")
        sender.sendMessage("17 - \u00A7aHunger")
        sender.sendMessage("18 - \u00A78Weakness")
        sender.sendMessage("19 - \u00A72Poison")
        sender.sendMessage("20 - \u00A70Wither")
        sender.sendMessage("\u00A76Page \u00A7c3 \u00A76of \u00A7c4")
        return True
    sender.sendMessage("01 - \u00A7bSpeed")
    sender.sendMessage("02 - \u00A79Slowness")
    sender.sendMessage("03 - \u00A7eHaste")
    sender.sendMessage("04 - \u00A78Mining Fatigue")
    sender.sendMessage("05 - \u00A7cStrength")
    sender.sendMessage("\u00A76Page \u00A7c1 \u00A76of \u00A7c4")
    return True

# Show chat colors
@hook.command("c", description="Display each color with its respective character.")
def onCommandC(sender, args):
    sender.sendMessage(''.join([color("f"), "f ", color("7"), "7 ", color("e"), "e ", color("c"), "c ", color("d"), "d ", color("9"), "9 ", color("b"), "b ", color("a"), "a"]))
    sender.sendMessage(''.join([color("0"), "0 ", color("8"), "8 ", color("6"), "6 ", color("4"), "4 ", color("5"), "5 ", color("1"), "1 ", color("3"), "3 ", color("2"), "2"]))
    
    return True
    
# AFK
@hook.command("afk", description="Don't you dare.")
def onCommandAFK(sender, args):
    sender.sendMessage("Please do not go AFK, it wastes my bandwidth")
    sender.sendMessage("Instead, please log off the server")
    return True

# Save all
@hook.command("save", description="Saves the map.")
def onCommandSave(sender, args):                         
    sudo("save-all")
    return True

# Random number
@hook.command("random", description="Produce a random number.")
def onCommandRandom(sender,args):
    if len(args) == 1 and args[0].isdigit() == True:
        sender.sendMessage(str(random.randint(0,args[0])))
    if len(args) == 2 and args[0].isdigit() == True and args[1].isdigit() == True:
        sender.sendMessage(str(random.randint(int(args[0]),int(args[1]))))
    if len(args) == 1:
        sender.sendMessage(str(random.randint(0,10)))
    if len(args) > 2:
        sender.sendMessage("\u00a7cUse the syntax &u00a76/random [a] [b]")
        return False
    return True
                           
# Item Renaming
@hook.command("itemname", description="Rename and recolour an item!")
def onCommandItemname(sender,args):
    addpos = 0
    namestring = list(args[0])
    for x in range(1,len(args)):
        addpos = addpos + 1
        for i in range(0, len(args[x])):
            if itemnamewhitelist.count((args[x])[i]) == 1:
                namestring.insert(addpos-1,"\u00A7")
                namestring.insert(addpos,(args[x])[i])
                addpos = addpos + 2
            else:
                sender.sendMessage("\u00a74I'm sorry, the format",(args[x])[i],"\u00a7is not availible.")
    str(namestring)
    sender.getInventory().setDisplayName(sender.getItemInHand(),namestring)
    print(namestring)
    return True


