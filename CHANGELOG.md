## Changelog
current version 0.0.6

## v0.0.6
* Fixed recursion bug.

## v0.0.5
* Added a date_format argument to the ``` to_dict ``` method because other wise specifiing the output date format of any datetime field becomes a project. Was on the fence about this one, but the responsibility would be obtuse if left up to the application I think.

## v0.0.4
* Fixed some bugs in the attribute filtering behavior of the ``` DictInterface ```

## v0.0.2
* Added the ``` DictInterface ``` to support ``` as_dict ``` and ``` to_dict(only=['limit', 'to', 'fields']) ``` -- recursively turns object graph into dictionary. Breaks recursion at backreferences.