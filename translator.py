#Import the translate file from pip install translate
from translate import Translator

#for Decor purpose this part was create for the user
print("Choose your language to translate:")
print("Latin","\nFrench","\nChinese")
userchoice= str(input("Choose 1 from above: "))


#main translate over here in this library file you can add more language too
choiceLatin = Translator(to_lang="Latin") 
choiceFrench = Translator(to_lang="French")
choiceChinese = Translator(to_lang="Chinese")


#User String input
userinput = str(input("Type here:"))

#the if and elif use properly and in a simple manner
if (userchoice == "Latin"):
    choiceLatin = choiceLatin.translate(userinput)
    print(choiceLatin)
elif(userchoice == "French"):
    choiceFrench = choiceFrench.translate(userinput)
    print(choiceFrench)
elif(userchoice == "Chinese"):
    choiceChinese = choiceChinese.translate(userinput)
    print(choiceChinese)

