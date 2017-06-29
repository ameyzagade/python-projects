import os
import pickle

# PersonInfo object
class PersonInfo:
	def __init__(self, contactname, contactnumber, email, tag):
		self.name = contactname
		self.number = int(contactnumber)
		self.email = email
		self.tag = tag

	def change_name(self, contactname):
		self.name = contactname

	def change_number(self, contactnumber):
		self.number = int(contactnumber)

	def change_email(self, email):
		self.email = email

	def change_tag(self, tag):
		self.tag = tag

filename = 'addressbook.data'

people = dict()

def create_dict():
	file_data = list()
	with open(filename, 'rb') as file:
		while  True:
			try:
				file_data.append(pickle.load(file))
			except EOFError:
				break
	# construct a dictionary of contacts
	for each_object in file_data:
		people[each_object.name] = each_object

	return people

def update_dict(flag, *passed_value):
	# when flag is 0, add new key-value pair
	# when flag is 1, remove the selected key
	# passed_value is a tuple with two values
	# first value is an object, second value is key
	temp_dict = create_dict()
	if flag == 0:
		to_add = passed_value[0]
		temp_dict[to_add.name] = to_add
		people = temp_dict
		return people
	else:
		delkey = passed_value[1]
		del temp_dict[delkey]
		people = temp_dict
		return people

def add_contact(contact_object):
	# check if file does not exist
	if not os.path.isfile(filename):
		with open(filename, 'wb') as file:
			pickle.dump(contact_object, file)
	else:
		temp_dict = create_dict()
		# check if contact does not exist
		if contact_object.name not in temp_dict:
			# add contact name to dict and data to the file
			flag = 0
			temp_dict = update_dict(flag, contact_object, None)
			with open(filename, 'ab') as file:
				pickle.dump(contact_object, file)
			print('Contact added successfully!\n')		
		else:
			get_input = input(('Contact Name already exists. Do you wish to modify the contact:{}? [y/n]').format(search_key))
			if (get_input == 'y') or (get_input == 'Y'):
				name = input('Which contact to modify? :')
				modify_contact(name)
			elif (get_input == 'n') or (get_input == 'N'):
				pass
			else:
				print('InvalidInputError: Contact unmodified.\n')

def del_contact(delete_string):
	if not os.path.isfile(filename):
		print('File does not exist!\n')
	else:
		temp_dict = create_dict()
		# check if file is empty
		if len(temp_dict) == 0:
			print('Address Book is empty!\n')
		# check if contact does not exist
		else:
			try:
				del temp_dict[delete_string]
			except KeyError:
				print('No such contact!\n')
			else:
				flag = 1
				temp_dict = update_dict(flag, None, delete_string)
				print(('Contact {} deleted successfully.\n').format(delete_string))
				# empty the file
				with open(filename, 'wb') as file:
					file.seek(0)
					file.truncate()
					# update the file
					for key, value in temp_dict.items():
						pickle.dump(value, file)	

def search_contact(search_string):
	if not os.path.isfile(filename):
		print('File does not exist!\n')
		return_data = (False, None)
		return return_data
	else:
		temp_dict = create_dict()
		if len(temp_dict) == 0:
			print('Address Book is empty.\n')
			return_data = (False, None)
			return return_data
		else:
			# check if contact exists
			if search_string in temp_dict:
				obj = temp_dict.get(search_string)
				print('\nContact Name:', obj.name)
				print('Contact Number:', obj.number)
				print('Email:', obj.email)
				print()
				return_data = (True, obj)
				return return_data
			else:
				print('Contact Not Found!')
				return_data = (False, None)
				return return_data

def modify_contact(input_string):
	existence, get_obj = search_contact(input_string)
	if not existence:
		pass
	else:
		if get_obj is not None:
			temp_dict = create_dict()
			# new values for contact
			get_input = input('\nEnter new name: ')
			get_obj.change_name(get_input)

			try:
				get_input = input('Enter new number: ')
				val = int(get_input)
			except ValueError:
				print('Not a valid number! Number unchanged')
				get_obj.change_number(get_obj.number)
			else:
				get_obj.change_number(val)

			get_input = input('Enter new email: ')
			get_obj.change_email(get_input)

			get_input = input('Enter new tag: ')
			get_obj.change_tag(get_input)
			# print new values of modified contact
			print('\nModified Contact-')
			print('Contact Name:', get_obj.name)
			print('Contact number:', get_obj.number)
			print('Email:', get_obj.email)
			print('Tag:', get_obj.tag)
			print()

			# push modified values to dict and file
			flag = 0
			temp_dict[get_obj.name] = temp_dict.pop(input_string)
			temp_dict = update_dict(flag, get_obj, None)
			with open(filename, 'wb') as file:
				file.seek(0)
				file.truncate()
				for key, value in temp_dict.items():
					pickle.dump(value, file)

def browse_addrbook():
	try:
		unpickle = list()
		with open(filename, 'rb') as file:
			while  True:
				try:
					unpickle.append(pickle.load(file))
				except EOFError:
					break
	except FileNotFoundError:
		print('\nAddress Book does not exist! Create one by adding one contact.\n')
	else:
		if len(unpickle) == 0:
			print('Address Book is empty.\n')
		else:
			for each_object in unpickle:
				print('\nContact Name:', each_object.name)
				print('Contact number:', each_object.number)
				print('Email:', each_object.email)
				print('Tag:', each_object.tag)
				print()

def  main():
	print('ADDRESS BOOK')
	while True:
		choice = input('1. Browse\n2. Add\n3. Delete\n4. Search\n5. Modify\nq|Q. Exit\nEnter Option: ')
		if choice == '1':
			browse_addrbook()
		elif choice == '2':
			# check here if contact is already in dict
			name = input('\nEnter name of the person: ')
			try:
				number = input('Enter contact number of the person: ')
				val = int(number)
			except ValueError:
				print('Not a valid number! Enter number again.')
				number = input('Enter contact number of the person: ')
				val = int(number)
			else:
				number = val
				email = input('Enter email of the person: ')
				tag = input('Enter tag: ')
				Person = PersonInfo(name, number, email, tag)
				add_contact(Person)
		elif choice == '3':
			name = input('Name of the person to be deleted: ')
			del_contact(name)
		elif choice == '4':
			name = input('Name of the person to be searched in the address book: ')
			search_contact(name)
		elif choice == '5':
			name = input('Enter name of the contact to be modified: ')
			modify_contact(name)
		elif (choice == 'q') or (choice == 'Q'):
			print('Exiting ...')
			break
		else:
			print(('InvalidInputError: Entered option {} is invalid.\n').format(choice))
	else:
		pass

if __name__ == "__main__":
	main()