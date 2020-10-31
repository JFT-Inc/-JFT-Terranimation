import os

print("Testing the pipenv...\n")

toollist = ""
command_result = os.system("pipenv")

def yesno_question():
	print("Select option:Yes/No (Y/N)\n>")
	
	if selection.count('Y') + selection.count("y") + selection.count("Yes") + selection.count("yes"):
		return True
		
	elif selection.count("N") + selection.count("n") + selection.count("No") + selection.count("no"):
		return False
	else:
		None


if command_result == 0:
	print("Grait!")

else:
	selection = input("Oh... pipenv is not ready. So, I will do it for you! Warning: thid will reinstall virtualenv\n>")
	
	selection = yesno_question()
	
	if selection == None:
		print("Wrong input...")
	
	
	if selection:
		print("Installing pipenv right now...")
		
		print("uninstalling virtualenv")
		command_result = os.system("pip uninstall virtualenv")
		print("uninstalling pipenv for make shure")
		command_result = os.system("pip uninstall pipenv")
		
		print("\ninstalling virtualenv")
		command_result = os.system("pip install virtualenv")
		print("installing pipenv for make shure")
		command_result = os.system("pip install pipenv")
		
		print("\nNow testing pipenv!")
		command_result = os.system("pipenv")
		
		if command_result == 0:
			print("Gr8!")
		else:
			print("Somthing was wrong...")
	
	elif selection == False:
		print("Alright...")

print("Now we will install following tools\n" + toollist)
print("\ndo you want to install them?\n")
selection = yesno_question()

#if selection:
#elif selection:
#else: