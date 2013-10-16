# -*- coding: utf-8 -*-

from pprint import pprint

from nose.tools.trivial import assert_equal, assert_true, assert_in

from mrpython.mixin import DictInterface

class SomeDictClass(DictInterface):

	def __init__(self):
		self.name = 'Fred'
		self.email = 'datfredguy@gmail.com'
		self.password = 'whyismyencryptionnotworking'
		self.my_favorite_number = 7

class AnotherDictClass(DictInterface):
	_dict_attrs = ('name', 'email')

	def __init__(self):
		self.name = 'Test Guy'
		self.email = 'test@nowhere.com'
		self.password = 'omgplaintextsoinsecure'

class ParentClass(DictInterface):

	def __init__(self):
		self.name = 'Frank the Dad'
		self.child = ChildClass(self)

class ChildClass(DictInterface):

	def __init__(self, parent):
		self.name = 'Bobby the Kid'
		self.parent = parent
		self.billy = LostChildClass(self, parent)
		self.friend = f

class LostChildClass(DictInterface):

	def __init__(self, sibling, parent):
		self.name = 'Lost Little Billy'
		self.sibling = sibling
		self.parent = parent
		self.friend = f

class FriendZone(DictInterface):

	def __init__(self):
		self.name = 'Super Friendly'

f = FriendZone()

def test_dict_interface():
	'''
	s = SomeDictClass()
	assert_equal(s.to_dict(), {'name': 'Fred', 'email': 'datfredguy@gmail.com', 'password': 'whyismyencryptionnotworking', 'my_favorite_number': '7'})
	assert_equal(s.to_dict(strings=False), {'name': 'Fred', 'email': 'datfredguy@gmail.com', 'password': 'whyismyencryptionnotworking', 'my_favorite_number': 7})
	assert_equal(s.to_dict(only=['name']), {'name': 'Fred'})

	a = AnotherDictClass()
	assert_equal(a.to_dict(), {'name': 'Test Guy', 'email': 'test@nowhere.com'})
	assert_in('name', p.to_dict().keys())
	assert_in('child', p.to_dict().keys())
	
	'''
	
	p = ParentClass()
	pprint(p.to_dict())

