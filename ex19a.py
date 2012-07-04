def total_defense(str=1.00, end=1.00, agi=1.00, dex=1.00):
    print "The total defense of this character is determined in the following manner:"
    print "Strength (%r) times Endurance (%r) = %r" % (str, end, str*end)
    print "Agility (%r) plus Dexterity (%r) = %r" % (agi, dex, agi+dex)
    print "Strength * Endurance (%r) divided by Agility + Dexterity (%r) = %r" % (str*end, agi+dex, round((str*end)/(agi+dex),3))
    print
    return (str*end)/(agi+dex)

total_defense(2.50,4.00,6.50,1.00) # decimal numbers
total_defense(2.00,5.00*5.00,6.00/6.00,9.00-9.00) # mathematical operations
total_defense(dex=638.00,agi=461.00,str=578.00,end=380.00) # assigned values


dex=15.00
end=16.00
agi=44.00
str=17.00

total_defense(str,end,agi,dex) # variables
total_defense(dex=dex,end=end,agi=agi,str=str) # assigned variables
total_defense(str+3.00,end-3.00,agi*3.00,dex/3.00) # variables and mathematics
total_defense(dex=dex+4.00,str=str+4.00,end=end+4.00,agi=agi+4.00) # assigned variables and mathematics
total_defense() # use the function's default values

defense = total_defense(dex=51.00) # grab the returned value, while setting the dex to 51.00
print "The total defense is %r!" % round(defense*100,3)