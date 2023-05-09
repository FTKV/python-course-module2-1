is_admin = True
is_active = False
age = 22
can_write = False

if ((is_admin or can_write) and age == 22) or is_active:
    print("admin")

if is_admin or can_write and age == 22 or is_active:
    print("admin")

is_admin = False
is_active = False
age = 22
can_write = False

if ((is_admin or can_write) and age == 22) or is_active:
    print("admin")

if is_admin or can_write and age == 22 or is_active:
    print("admin")
