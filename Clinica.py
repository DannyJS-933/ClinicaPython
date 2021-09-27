#Ingresar los detalles es la primera parte

newUserList = []
def menu():
    newUserList = []
    option = int(input('Seleccione una opcion, 1 Agregar usuario, 2 eliminar usuario, cualquier otra tecla para salir: '))

    while option == 1:

       for i in range(option):
            enterUser = (input('Escriba el nombre del usuario: '))
            enterID = input(('Ingrese su ID: '))
            enterLastName = input(('Ingrese su apellido: '))
            enterPhoneNumber = input(('Ingrese su numero de telefono: '))
            enterAddress = input(('Ingrese su direccion de casa: '))
            newUserList.append(enterUser)
            newUserList.append(enterLastName)
            newUserList.append(enterID)
            newUserList.append(enterPhoneNumber)
            newUserList.append(enterAddress)
            string = ','.join([str(item) for item in newUserList])
            print(string)
            newUserList += '\n'
            with open('database.txt', mode='w') as file_creation:
                file_creation.write(string)
            option = int(input('Desea agregar otro usuario? 1 para si o 2 para eliminar un usuario: '))

    while option == 2:
        with open('database.txt', 'r') as just_reading:
            lines = just_reading.readline()


        with open('database.txt', 'w') as deleting_user:
            for line in lines:
                deleteUser = input('Ingrese el ID del usuario a eliminar')
                if deleteUser == enterID:
                    deleting_user.write(line)
                    string = ','.join([str(item) for item in newUserList])
                    print(string)

                    option = int(input('Desea agregar otro usuario? 1 para si o 2 para eliminar un usuario: '))
                    break
                else:
                    print('User not found, confirm the user exists or the list is not empty')
                    option = int(input('Desea agregar un usuario? 1 para si o cualquier otro numero para salir: '))

    else:
        print('Closing applicaction')
        string = ','.join([str(item) for item in newUserList])
        print(string)





menu()


