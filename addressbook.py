import pickle
import os

class PersonInfo:
	def __init__(self, contactname, contactnumber, email):
		self.contactname = contactname
		self.contactnumber = int(contactnumber)
		self.email = email

	def change_name(self, contactname):
		self.contactname = contactname

	def change_email(self, email):
		self.email = email

	def change_number(self, contactnumber):
		self.contactnumber = contactnumber

# global dictionary
# initialized at script startup
people = dict()

# filename
filename = 'addressbook.data'

def add_contact(filename, add_object):
	# check if file does not exist
	if not os.path.isfile(filename):
		with open(filename, 'wb') as file:
			pickle.dump(add_object, file)
	else:		
		unpickle = list()
		with open(filename, 'rb') as file:
			while True:
				try:
					unpickle.append(pickle.load(file))
				except EOFError:
					break

		# construct a dictionary of contact names
		for each_obj in unpickle:
			people[each_obj.contactname] = each_obj

		# check if contact name exists in address book
		search_key = add_object.contactname
		if search_key not in people:
			people[search_key] = add_object
			with open(filename, 'ab') as file:
				pickle.dump(add_object, file)
			print('Contact Added!\n')
		else:
			inp = input(('Contact Name already exists. Do you wish to modify the contact:{}? [y/n]').format(search_key))
			if (inp == 'y') or (inp == 'Y'):
				modify_contact(filename, search_key)
			elif (inp == 'n') or (inp == 'N'):
				pass
			else:
				print('Invalid Input. Modify operation aborted.')			
	
def del_contact(filename, del_str):
	if not os.path.isfile(filename):
		print('File does not exist!')
	else:
		unpickle = list()
		with open(filename, 'rb') as file:
			while True:
				try:
					unpickle.append(pickle.load(file))
				except EOFError:
					break

		if len(unpickle) == 0:
			print('Address Book is empty.')
		else:
			try:
				del people[del_str]
			except KeyError:
				print('Contact Not Found!')
			else:
				print(('Contact {} deleted successfully.\n').format(del_str))
				# empty the file
				with open(filename, 'wb') as file:
					file.seek(0)
					file.truncate()
					# update the file
					for key, value in people.items():
						pickle.dump(value, file)						

def browse_addrbook(filename):
	try:
		unpickle = list()
		with open(filename, 'rb') as file:
			while True:
				try:
					unpickle.append(pickle.load(file))
				except EOFError:
					break
	except FileNotFoundError:
		print('\nAddress Book does not exist!\n')
	else:
		for each_obj in unpickle:
			print('\nContact Name:', each_obj.contactname)
			print('Contact number:', each_obj.contactnumber)
			print('Email:', each_obj.email, '\n')

def modify_contact(filename, inp_str):
	if not os.path.isfile(filename):
		print('File does not exist!')
	else:
		unpickle = list()
		with open(filename, 'rb') as file:
			while True:
				try:
					unpickle.append(pickle.load(file))
				except EOFError:
					break

		if len(unpickle) == 0:
			print('Address Book is empty.')
		else:
			if inp_str in people:
				print(('Modify details for contact: {}').format(inp_str))
				obj = people.get(inp_str)

				print('Name:', obj.contactname)
				get_inp = input('Do you wish to modify Contact Name? [y/n] ')
				if (get_inp == 'y') or (get_inp == 'Y'):
					obj.change_name(input('Enter new name: '))						
				elif (get_inp == 'n') or (get_inp == 'N'):
					pass
				else:
					print('Entered option {} is invalid. Name unchanged.')

				print('Number:', obj.contactnumber)
				get_inp = input('Do you wish to modify Contact Number? [y/n] ')
				if (get_inp == 'y') or (get_inp == 'Y'):
					obj.change_number(input('Enter new number: '))						
				elif (get_inp == 'n') or (get_inp == 'N'):
					pass
				else:
					print('Entered option {} is invalid. Number unchanged.')

				print('Email:', obj.email)
				get_inp = input('Do you wish to modify Email? [y/n] ')
				if (get_inp == 'y') or (get_inp == 'Y'):
					obj.change_email(input('Enter new email: '))						
				elif (get_inp == 'n') or (get_inp == 'N'):
					pass
				else:
					print('Entered option {} is invalid. Email unchanged.')

				# print new values of modified contact
				print('\nModified Contact-')
				print('Contact Name:', obj.contactname)
				print('Contact number:', obj.contactnumber)
				print('Email:', obj.email)
				print()

				# pushing new values to dictionary and data file
				people[obj.contactname] = people.pop(inp_str)
				with open(filename, 'wb') as file:
					# empty the file
					file.seek(0)
					file.truncate()
					# write contents to the file
					for key, value in people.items():
						pickle.dump(value, file)	
			else:
				pass

def search_contact(filename, search_str):
	if not os.path.isfile(filename):
		print('File does not exist!')
	else:
		unpickle = list()
		with open(filename, 'rb') as file:
			while True:
				try:
					unpickle.append(pickle.load(file))
				except EOFError:
					break

		if len(unpickle) == 0:
			print('Address Book is empty.')
		else:
			if search_str in people:
				print('Contact Found!')
				obj = people.get(search_str)
				print('Contact Name', obj.contactname)
				print('Contact Number', obj.contactnumber)
				print('Email', obj.email)
			else:
				print('Contact Not Found!')

def main():
	print('ADDRESS BOOK')
	
	while True:
		choice = input('1. Browse\n2. Add\n3. Delete\n4. Search\n5. Modify\nq|Q. Exit\nEnter Option: ')
		if choice == '1':
			browse_addrbook(filename)
		elif choice == '2':
			# check here if contact is already in dict
			name = input('\nEnter name of the person: ')
			number = input('Enter contact number of the person: ')
			email = input('Enter email of the person: ')
			Person = PersonInfo(name, number, email)
			add_contact(filename, Person)
		elif choice == '3':
			name = input('Name of the person to be deleted: ')
			del_contact(filename, name)
		elif choice == '4':
			name = input('Name of the person to be searched in the address book: ')
			search_contact(filename, name)
		elif choice == '5':
			name = input('Enter name of the contact to be modified: ')
			modify_contact(filename, name)
		elif (choice == 'q') or (choice == 'Q'):
			print('Exiting ...')
			break
		else:
			print(('InvalidInputError: Entered option {} is invalid.\n').format(choice))
	else:
		pass

if __name__ == "__main__":
	main()