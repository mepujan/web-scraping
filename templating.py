from string import Template
t = Template("$village folk send $price to $cause")
print(t.substitute(village = "morang", price = '$10',cause = "the ditch fund"))
