from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['#' , 'Pokemon Name', 'Type']
table.add_row(["001","Bulbasaur","Grass"])
table.add_row(["002","Ivysaur","Poison"])
table.add_row(["003","Venasaur","Poison"])
table.add_row(["004","Charmander","Fire"])
table.add_row(["005","Charmelon","Fire"])
table.add_row(["006","Charizard","Fire"])
table.add_row(["007","Squirtle","Water"])
table.add_row(["008","Wartortle","Water"])
table.add_row(["009","Blastoise","Water"])
table.add_row(["010","Caterpie","Bug"])
table.add_row(["011","Pikachiu","Electric"])
table.add_row(["012","Evie","Normal"])
print(table)