def modify(letter,word,fword):
	indx=fword.find(letter)
	l=list(word)
	l[indx]=letter
	return ''.join(l)



def fst(length):
	file=open('words-in-code.txt')
	data=file.read().split(',')
	f=False
	while(not f):
		word=random.choice(data)
		if(len(word)!=length):
			continue
		else:
			return word



def dis(length):
	l=[]
	attempts=((2*length)-2)
	fword=fst(length)
	#print(fword)
	word='*' * length
	i=0
	z=0
	while(i<attempts and word!=fword):
		
		print("word : %s" % word)
		print("Attempts remaining : %s" % (attempts-i) )
		print("previous guesses : %s" % l)
		letter=input("please enter a guess : ").lower()

		if(letter not in l):
			if(not letter.isalpha()):
				print("Entered character should be in range of 'A-Z or 'a-z ")
				continue
			else:
				z+=1
				l.append(letter)
				if letter in fword:
					print("Letter '%s' is in the word"% letter)
					word=modify(letter,word,fword)
					i+=1
				else:
					print("Letter '%s' is not in the word"% letter)
					i+=1
		else:
			print("Already guessed this character")
			continue

	print("Attempts remaining : %s" % (attempts-i) )
	print(l)
	return fword,z

		






    
import random
flag=False
while(not flag):
	print("Starting HANGMAN game")
	length=int(input("enter word length :"))
	if(length<3 or length>6):
		print("choose word length in between [3,6]")
		continue
	else:
		word,value=dis(length)

	print("\n\n")

	attempts=((2*length)-2)
	if(value==attempts):
		print("You ran out of tries. \n The word was %s \n You are hanged \n may be next time. Good luck!"% word)
	else:
		print("Congratulations you won word is %s" % word)

	
	

	print("\n\n")

	x=input("Do you want to play again? [Y/N] : ").lower()
	if(x=='y'):
		continue
	else:
		flag=True