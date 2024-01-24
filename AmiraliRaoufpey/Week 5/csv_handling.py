
# file csv ba library pandas be rahati handel mishe, vali mishe ba modele txt va khundane khat ha va split:

user_list = []
id_list = []
name_list = []
surname_list = []

with open('sample.csv', 'r') as file:
    for line in file:
        fields = line.strip().split(';')
        user_list.append(fields[0])
        id_list.append(fields[1])
        name_list.append(fields[2])
        surname_list.append(fields[3])
        user_list.append('\t')
        id_list.append('\t')
        name_list.append('\t')
        surname_list.append('\t')

with open('csv split results', 'w') as file:
    file.writelines('Users: ')
    file.writelines(user_list)
    file.writelines('\n')
    file.writelines('IDs: ')
    file.writelines(id_list)
    file.writelines('\n')
    file.writelines('Names: ')
    file.writelines(name_list)
    file.writelines('\n')
    file.writelines('Surnames: ')
    file.writelines(surname_list)
    file.writelines('\n')
