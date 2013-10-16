# -*- coding: utf-8 -*-


class DictInterface(object):

	_dict_attrs = ()

	@property
	def as_dict(self):
		return self.to_dict()

	def to_dict(self, only=[], caller=None, depth=0):	
		names = self._dict_attrs or filter(lambda x: not x.startswith('_'), vars(self))
		if only:
			names = list(set(only).intersection(set(names)))

		attrs = {}
		for name in names:
			attr = getattr(self, name)
			if isinstance(attr, DictInterface):
				if depth < 3:
					attrs[name] = attr.to_dict(caller=self, depth=depth + 1)
			else:
				attrs[name] = attr
		return attrs