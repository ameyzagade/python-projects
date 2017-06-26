class PersonInfo:
	def store_details(self, contactname, email, contactnumber, relation):
		self.contactname = contactname
		self.email = email
		self.contactnumber = contactnumber
		self.relation = relation

	def print_details(self):
		print('Contact Name:', self.contactname)
		print('Email:', self.email)
		print('Contact Number:', self.contactnumber)
		print('Relation:', self.relation)


# exception classes
class InvalidInputError(Exception):
	def __init__(self, entered_key):
		Exception.__init__(self)
		self.entered_key = entered_key

class NoContactsException(Exception):
	def __init__(self):
		Exception.__init__(self)
		self.needed = 1

class addressbook:
	Person_details = dict()
	
	def add(self):
		self.add_more = True

		while self.add_more:
			print('\nEnter contact details--')
			self.contactname = input('Enter Name: ')
			self.email = input('Enter Email: ')
			self.contactnumber = input('Enter Phone Number: ')
			self.relation = input('Enter Relation: ')

			obj = PersonInfo()
			obj.store_details(self.contactname, self.email, int(self.contactnumber), self.relation)

			print()
			self.Person_details[self.contactname] = obj

			print('Contact Added:', self.contactname)

			try:
				self.inp = input('Do you wish to add another contact? [y/n] ')
				if (self.inp == 'y') or (self.inp == 'Y'):
					self.add_more = True
				elif (self.inp == 'n') or (self.inp == 'N'):
					self.add_more = False
				else:
					raise InvalidInputError(self.inp)
			except InvalidInputError as ex:
				print(("InvalidInputError: Entered option '{}' is invalid.").format(ex.entered_key))
				break
			else:
				if not self.add_more:
					break
				print()
	
	def browse(self):
		try:
			if not bool(self.Person_details):
				raise NoContactsException()
		except NoContactsException as e:
			print(("\nNoContactsException: No contacts in the Address Book. Atleast need {0} contact.\n").format(e.needed))
		else:
			print('\nADDRESS BOOK')
		finally:
			for key, value in sorted(self.Person_details.items()):
				print('Contact Details for', value.contactname)
				value.print_details()
				print()

	def search(self):
		self.srch_name = input("\nEnter name of the contact to search it's details: ")
		self.found = False

		for key,value in self.Person_details.items():
			if key == self.srch_name:
				self.found = True
				print()
				value.print_details()
				print()
		if not self.found:
			print('Details for contact name', self.srch_name, 'does not exist in the address book.')
			print()

	def modify(self):
		self.mod_name = input('Name of the contact to be modified: ')
		self.found = False

		for key, value in self.Person_details.items():
			if key == self.mod_name:
				self.found = True
				print('Modify details for contact, ', key)

				print('Name:', value.contactname)
				try:
					self.inp = input('Do you wish to modify Contact Name? [y/n] ')
					if (self.inp == 'y') or (self.inp == 'Y'):
						temp = input('Enter new name: ')
						value.contactname = temp
						key = temp
					elif (self.inp == 'n') or (self.inp == 'N'):
						pass
					else:
						raise InvalidInputError(self.inp)
				except InvalidInputError as ex:
					print(("InvalidInputError: Entered option '{}' is invalid.").format(ex.entered_key))
					break
				else:
					pass

				print()
				print('Email:', value.email)
				try:
					self.inp = input('Do you wish to modify Email? [y/n] ')
					if (self.inp == 'y') or (self.inp == 'Y'):
						temp = input('Enter new email: ')
						value.email = temp
					elif (self.inp == 'n') or (self.inp == 'N'):
						pass
					else:
						raise InvalidInputError(self.inp)
				except InvalidInputError as ex:
					print(("InvalidInputError: Entered option '{}' is invalid.").format(ex.entered_key))
					break
				else:
					pass		

				print()
				print('Contact Number:', value.contactnumber)
				try:
					self.inp = input('Do you wish to modify Contact Number? [y/n] ')
					if (self.inp == 'y') or (self.inp == 'Y'):
						temp = input('Enter new number: ')
						value.contactnumber = temp
					elif (self.inp == 'n') or (self.inp == 'N'):
						pass
					else:
						raise InvalidInputError(self.inp)
				except InvalidInputError as ex:
					print(("InvalidInputError: Entered option '{}' is invalid.").format(ex.entered_key))
					break
				else:
					pass

				print()
				print('Relation:', value.relation)
				try:
					self.inp = input('Do you wish to modify Relation? [y/n] ')
					if (self.inp == 'y') or (self.inp == 'Y'):
						temp = input('Enter relationr: ')
						value.relation = temp
					elif (self.inp == 'n') or (self.inp == 'N'):
						pass
					else:
						raise InvalidInputError(self.inp)
				except InvalidInputError as ex:
					print(("InvalidInputError: Entered option '{}' is invalid.").format(ex.entered_key))
					break
				else:
					pass

		print()
		if self.found:
			for key, value in self.Person_details.items():
				if key == value.contactname:
					value.print_details()
					print()
		else:
			print('Contact name', self.mod_name, 'does not exist in the address book.')

	def delete(self):
		self.rem_name = input("\nEnter name of the contact to remove it: ")
		self.found = False

		for key, value in self.Person_details.items():
			if key == self.rem_name:
				self.found = True

		if self.found:
			del self.Person_details[key]
			print('Details for', self.rem_name, 'deleted!\n')
		else:
			print(self.rem_name, 'not found!\n')


def main():
	print('ADDRESS BOOK')

	loop = True
	while loop:
		try:
			choice = input('1. Browse\n2. Add\n3. Delete\n4. Search\n5. Modify\nq|Q. Exit\nEnter Option: ')
			addr = addressbook()

			if choice == '1':
				addr.browse()
			elif choice == '2':
				addr.add()
			elif choice == '3':
				addr.delete()
			elif choice == '4':
				addr.search()
			elif choice == '5':
				addr.modify()
			elif choice == 'q' or choice == 'Q':
				print('Exiting ...')
				break
			else:
				raise InvalidInputError(choice)
		except InvalidInputError as excep:
			print(('InvalidInputError: Entered option {} is invalid.\n').format(excep.entered_key))
		else:
			pass


if __name__ == '__main__':
	main()