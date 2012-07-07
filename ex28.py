list = ['True and True','False and True','1==1 and 2==1','"test"=="test"','1==1 and 2!=1','True and 1==1','False and 0!=0','True or 1==1','"test"=="testing"','1!=0 and 2==1','"test" != "testing"','"test"==1','not(True and False)','not(1==1 and 0!=1)','not(10==1 or 1000==1000)','not(1!=10 or 3==4)','not("testing"=="testing"and"Zed"=="Cool Guy")','1==1 and not("testing"==1 or 1==0)','"chunky"=="bacon" and not(3==4 or 3==3)','3==3 and not ("testing"=="testing" or "Python"=="Fun")']
score = 0

for index,item in enumerate(list):
    print "%d. %s" % (index+1,item)
    print "\tI say:\t\t",
    answer = raw_input()
    print "\tComputer says:\t%r" % (eval(item))
    if answer == str(eval(item)):
        score += 1
        print "Your score is now: %d" % score

print "Your final score was %d (%d%%)." %(score,score*10/len(list)*10)