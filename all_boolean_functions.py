def all_zeros_gate(a, b):
    return a and not a

def second_one_gate(a, b):
    return a and not b

def a_gate(a, b):
    return a

def not_a_gate(a, b):
    return not a 

def b_gate(a, b):
    return b

def not_b_gate(a, b):
    return not b

def and_gate(a, b):
    return a and b

def nand_gate(a, b):
    return not (a and b)

def xor_gate(a, b):
    return not a and b or a and not b

def equal_gate(a, b):
    return (a or not b) and (not a or b)

def or_gate(a, b):
    return a or b

def nor_gate(a, b):
    return not (a or b)

def imply_gate(a, b):
    return not a or b

def rev_imply_gate(a, b):
    return a or not b

def all_ones_gate(a, b):
    return a or not a

def test_bool_func(func):
    print("A B  F")
    print(f"1 1  {int(func(True, True))}")
    print(f"1 0  {int(func(True, False))}")
    print(f"0 1  {int(func(False, True))}")
    print(f"0 0  {int(func(False, False))}")

for f in [
all_zeros_gate,
second_one_gate,
a_gate,
not_a_gate,
b_gate,
not_b_gate,
and_gate,
nand_gate,
xor_gate,
equal_gate,
or_gate,
nor_gate,
imply_gate,
rev_imply_gate,
all_ones_gate]:
    print(str(f))
    test_bool_func(f)
    