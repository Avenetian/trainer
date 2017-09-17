#! /usr/bin/python3

# openTraining - A program that saves and plays custom training sessions

import time
import datetime
import shelve
import os
# main Menu - Gives simple choices to navigate through the program
def mainMenu():
	print ('\nWelcome to openTraining! Choose from the options below!\n')
	print('1.-Play Saved-\n2.-Make Training-\n3.-Quit-')
	mainChoice = input()
	if mainChoice=='1':
		playSaved()
	elif mainChoice=='2':
		makeTraining()
	elif mainChoice=='3':
		quit()
	else:
		print('There is no such menu option!')
		mainMenu()


# playSaved - Lists and Opens trainings saved in the Make Training Menu.
# Todo - List the saved trainings, from the dir.
# Todo - open and play the whole training with breaks between exercises (maybe sounds)
def playSaved():
	print('\n---Choose from the saved trainings!(Write the name of the training)---\n')
	print('1.-Back to Main Menu-')
	cnt=2	
	for filename in os.listdir(os.getcwd()):		
		if filename.endswith('_tr'):
			print(str(cnt)+'.'+filename)
			cnt+=1
		
	
		
	
	print()
	playSavedChoice=input()
	if playSavedChoice=='1':
		mainMenu()
	elif playSavedChoice in os.listdir(os.getcwd()):
		shelfFile=shelve.open(playSavedChoice)
		nameList=shelfFile['NaList']
		duraList=shelfFile['DuList']
		breakList=shelfFile['BrList']
		print('Training '+playSavedChoice+' has started!')
		for i in range(len(nameList)):
			print('Break, next Exercise: ' +nameList[i])
			countdown(breakList) 
			print ('Exercise: '+nameList[i])
			countdown(duraList[i])
		print('\nNo more exercises, training is over!\n')
		mainMenu()		



#makeTraining - Only a Menu to navigate through the options
#todo - Make a modifyTrainings function to open and write existing trainings
def makeTraining():
	print('\n---Make your own training!---\n')
	print('1.-Training Maker-')
	print('2.-Back to Main Menu-')
	
	makeTrainingChoice=input()
	if makeTrainingChoice=='2':
		mainMenu()
	elif makeTrainingChoice=='1':
		tMaker()

#tMaker - It asks for the characteristics of the training and its exercises.
#todo - make the file/files store every datas of the training
def tMaker():
	tName=input('Write the name of your training: ')
	shelfFile=shelve.open(tName+'_tr')
	namelist=list()
	durlist=list()
	breaklist=int()
	exCount=input('How many exercises do you want in your training? ')
	exBreakTime=input('How much time do you need between exercises?(10 seconds default)')
	breaklist=(int(exBreakTime))
	for i in range(int(exCount)):
		exName=input('What is the name of your exercise? ')
		namelist.append(exName)		
		exDuration=input('How many seconds is your exercise? ')
		durlist.append(int(exDuration))
	shelfFile['NaList']=namelist
	shelfFile['DuList']=durlist
	shelfFile['BrList']=breaklist
	shelfFile.close()
	print(namelist,durlist,breaklist)
	makeTraining()
def countdown(t):
	while t:
		mins, secs=divmod(t,60)
		timeformat='{:02d}:{:02d}'.format(mins,secs)
		print(timeformat,end='\r')
		time.sleep(1)
		t-=1	
mainMenu()

	