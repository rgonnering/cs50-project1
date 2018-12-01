# dictionary_list.py
# ------------------

# function to initialize dictionary if it does not exist
def mt(id, notes):              
    if id not in notes:
        notes[id] = []
        return notes

# function to print the list of notes for an id
def display(id):
    for msg in notes[id]:
        print("   ", msg)

# global dictionary
notes = {}

id = 1
note = "note 1"
mt(id, notes)
notes[id].append(note)

id = 2
note = "note 2"
mt(id, notes)
notes[id].append(note)

id = 1
note = "note 3"
mt(id, notes)
notes[id].append(note)

id = 2
note = "note 4"
mt(id, notes)
notes[id].append(note)

id = 1
note = "note 5"
mt(id, notes)
notes[id].append(note)

id = 2
note = "note 6"
mt(id, notes)
notes[id].append(note)

id = 3
note = "note 7"
mt(id, notes)
notes[id].append(note)


print(notes)

for i in range(1, 4):
    print(notes[i])
    print("ID: ", i)
    display(i)





"""
==========================================================
>>> notes = {}


>>> note="note 1"                   Check is there is a note
>>> id = 1
>>> if note:
...     print ("y")
...
y




>>> def mt(id, notes):              function to initialize dictionary for id
...     if id not in notes:
...             notes[id] = []
...     return notes

>>> if id not in notes:             initialize dictionary for id
...     notes[id] = []
...


>>> notes                           initialized dictionary
{1: []}


>>> notes[id].append(note)          Add note to dictionary for id=1
>>> notes
{1: ['note 1']}


>>> note="note 2"                   Add note to id=2
>>> id=2
>>> def mt(id, notes):
...     if id not in notes:
...             notes[id] = []
...     return notes
>>> mt(id,notes)
>>> notes[2].append(note)
>>> notes
{1: ['note 1'], 2: ['note 2']}



>>> id=2                             Add another note to id=2
>>> note="note 3"
>>> notes[id].append(note)
>>> notes
{1: ['note 1'], 2: ['note 2', 'note 3']}



>>> id=3                             Add note to id=3
>>> note="note 4"
>>> mt(id,notes)
{1: ['note 1'], 2: ['note 2', 'note 3'], 3: []}
>>> notes[id].append(note)
>>> notes
{1: ['note 1'], 2: ['note 2', 'note 3'], 3: ['note 4']}




>>> id=2                             Add another note to id=2
>>> note="note 5"
>>> notes[id].append(note)
>>> notes
{1: ['note 1'], 2: ['note 2', 'note 3', 'note 5'], 3: ['note 4']}




>>> for msg in notes[id]:           print notes for id=2
...     print(msg)
            note 2
            note 3
            note 5
"""