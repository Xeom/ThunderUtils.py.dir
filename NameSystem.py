from Helper import color
from Helper import sudo

@hook.command("rainbowname", description="Give you a nice rainbow-coloured name(Fix with /resetname)")
def onCommandRainbowname(sender, args):
    SName=sender.getName()
    ResultName=''
    Colours='4c6e23915dd'
    GSize=len(SName)/10.0
    if GSize<=1:
       for i in range(len(SName)):
            ResultName+='&'+Colours[i:i+1]+SName[i:i+1]
    else:
        j=0
        for i in range(len(SName)):
            ResultName+='&'+Colours[j:j+1]+SName[i:i+1]
            if i-1 == int(j*GSize):
                j+=1
            
    sudo(''.join(['/nick ',SName,' ',ResultName]))
    
    return True
    
@hook.command("resetname", description="Resets any name changes.")
def onCommandResetname(sender, args):
    sudo(''.join(['/nick ',sender.getName(),' ',sender.getName()]))
    return True

@hook.command("tags", description="View the tags of the RDF")
def onCommandTags(sender, args):
    sender.sendMessage(''.join([color("c"), "M", color("f"), " - Moderator"]))
    sender.sendMessage(''.join([color("4"), "A", color("f"), " - Admin"]))
    sender.sendMessage(''.join([color("4"), "F", color("f"), " - Founder"]))
    sender.sendMessage(''.join([color("4"), "SA", color("f"), " - ServerAdmin"]))
    sender.sendMessage(''.join([color("2"), "D", color("f"), " - Donator ($7-$19.99)"]))
    sender.sendMessage(''.join([color("6"), "D", color("f"), " - Donator ($20-$49.99)"]))
    sender.sendMessage(''.join([color("5"), "W", color("f"), " - Writer"]))
    sender.sendMessage(''.join([color("7"), "H", color("f"), " - Helper"]))
    sender.sendMessage(''.join([color("2"), "S", color("f"), " - Sponsor ($50-$99.99)"]))
    sender.sendMessage(''.join([color("6"), "S", color("f"), " - Sponsor ($100-$150)"]))
    sender.sendMessage(''.join([color("1"), "S", color("f"), " - Sponsor ($150+)"]))

    return True

@hook.command("tag",description="Change a user's tags")
def onCommandTag(sender, args):
    if len(args) < 3:
        return False

    # TODO: Add error checking and better formatting

    sudo(''.join(["/pex user ", args[2], " group ", args[0], args[1]]))
    return True

@hook.command("skillup", description="Promote a user.")
def onCommandSkillup(sender, args):
    return True
        
@hook.command("skilldown", description="Demote a user.")
def onCommandSkilldown(sender,args):
    return True

@hook.command("fixname")
def onCommandFixname(sender, args):
    # WIP

    return True
