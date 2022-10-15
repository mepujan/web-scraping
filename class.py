# class Try:
#     # def __repr__(self):
#     #     return "Hello Pujan"
#     pass

# t = Try()
# print(t)

# class Complex:
#     def __init__(self,real,imag):
#         self.real = real
#         self.imag = imag
    
#     def add(self,other):
#         # self.real += other.real
#         # self.imag +=other.imag
#         return self.real+other.real ,"+",self.imag+other.imag,"j"


# class Dog:
#     kind ="german shepard"
#     def __init__(self,name):
#         self.name = name
#         self.tricks =[]

#     def add_tricks(self,trick):
#         self.tricks.append(trick)

# d = Dog("hello")
# e= Dog("hi")
# d.add_tricks("jumping")
# e.add_tricks("rolling")
# print(d.kind)
# print(d.tricks)
# print(e.kind)
# print(e.tricks)


# iter method

# class Reverse:
#     def __init__(self,data):
#         self.data = data
#         self.index = len(data)
    
#     def __iter__(self):
#         return self
    
#     def __repr__(self):
#         return "<__main__. Reverse data given by user >"

#     def __next__(self):
#         if self.index ==0:
#             raise StopIteration
#         self.index -= 1
#         return self.data[self.index]

# reverse = Reverse('Pujan')
# print(reverse)
# for i in reverse:
#     print(i)


# Generators

# Generators are a simple and powerful tool for creating iterators.

# def reverse(data):
#     for index in range(len(data)-1,-1,-1):
#         yield data[index]

# for char in reverse("Pujan"):
#     print(char)

# import sys
# print(sys.argv)
