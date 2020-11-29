def enum(**enums):
    return type('Enum', (), enums)

States = enum(MENU=1, ACTION=2, PROCCESS=3)
Actions = enum(ENCODE=1, DECODE=2, END=3, UNKNOWN=4)
