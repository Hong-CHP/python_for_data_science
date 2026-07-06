ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# your code here
ft_list.remove("tata!")
ft_list.append("World!")

temp = list(ft_tuple)
temp[1] = "France!"
ft_tuple = tuple(temp)

temp = list(ft_set)
temp[1] = "Nice!"
ft_set = set(temp)

ft_dict["Hello"] = "42Nice!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
