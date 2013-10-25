## Changelog
current version 0.0.11

### v0.0.11
* The walker now checks for a limiting attr on the Graphable interface. You can change the name of this attribute from its default of ``` _dict_attrs ```. The reason it's private is because it's really meta data.

### v0.0.10
* Changed the walker to use explicit iterable types so as to avoid unexpected behavior with types that have an ``` '__iter__' ``` property but are not really iterable...

### v0.0.9
* Changed the way the recursive walker works. Got rid of the ``` DictInterface ```. The implmentation for the interface is now up to the application developer. The ``` fxn.to_dict(o, limit=()) ``` and the ``` fxn.walk(o, graph_max=None, graph_interface=None) ``` functions provide the abstract functionality necessary to traverse and convert an arbitrary set of data structures / objects into a dictionary with full or limited recursion. The application developer merely specifies the ``` graph_interface ``` argument so that the walker knows when to treat a value as a graphable object. Otherwise, it just treats basic structures.

### v0.0.8
* List recursion bug-fix. Make the list walker subject to the same recursion level constraints as a regular dict interface...

### v0.0.7
* Added support for the ``` recursion=True ``` or ``` recursion=n ``` for the ``` to_dict ``` property. Specify ``` True ``` for unlimited traversal, specify a number for a max levels of recursion.
* Breaking Change: ``` recursive=True ``` no longer a parameter for ``` to_dict ```

### v0.0.6
* Fixed recursion bug.

### v0.0.5
* Added a date_format argument to the ``` to_dict ``` method because other wise specifiing the output date format of any datetime field becomes a project. Was on the fence about this one, but the responsibility would be obtuse if left up to the application I think.

### v0.0.4
* Fixed some bugs in the attribute filtering behavior of the ``` DictInterface ```

### v0.0.2
* Added the ``` DictInterface ``` to support ``` as_dict ``` and ``` to_dict(only=['limit', 'to', 'fields']) ``` -- recursively turns object graph into dictionary. Breaks recursion at backreferences.