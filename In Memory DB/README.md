# In Memory Database

## Implemented following features for the data base:
 - Implemented operations like Put, Get, Remove to insert, retreive and delete data from the database.
 - Used ***COMMAND PATTERN*** to facilitate transaction control (like *undo* and *redo*) for above operations.
 - Used ***MEMENTO PATTERN*** to facilitate *current state snapshots* and sequential list of *commands executed* on the database.
 - Used ***OBSERVER PATTERN*** to implement a Cursor for the database, which holds a value and observes changes made to it.
 - Developed ***UNIT TESTS*** to test functionality of the above code.