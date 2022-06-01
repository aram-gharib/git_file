# tuple methods

# sample_tuple = (1, 2, 3, True, "bmw")
# one_element_tuple = ("one")
# print(sample_tuple[-1][-1], "returns W from bmw")
# print(sample_tuple[-1].isalpha, "check if the last element is alpha")
#
# # tuple(1) >>>will raise error
# print(id(sample_tuple))
# sample_tuple_change = (2,) + sample_tuple[1:]
# sample_tuple =sample_tuple_change
# print(sample_tuple)
# print(len(sample_tuple))
# print(sample_tuple.index("bmw"))
# print(sample_tuple.count("bmw"))
# print(sample_tuple.count(1))
#
# del sample_tuple # dellet
# # sample_tuple #

def sum_tuple_num(tuple_1: tuple)-> float:
    type_of_numbers =(int, float)
    sum_ = 0
    for i in tuple_1:
        if type(i) in type_of_numbers:
             sum_ += i
    return sum_
sample_tuple = (1, 20, 22,"bmw")
sample_tuple_2 = (2, 4, 5, "bmw")
result = sum_tuple_num(sample_tuple)
print(result)

def sum_numbers_inmultiple_tuples(*args):
    total_sum = 0
    for tup in args:
        total_sum += tup
    return total_sum

sum_numbers_inmultiple_tuples(sum_tuple_num)
print(sum_numbers_inmultiple_tuples(sample_tuple, sample_tuple_2))


tuple_1 = (1, 2, 3)
print(tuple_1)
# print(*tuple_1)