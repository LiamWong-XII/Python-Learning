# letter = 'P'                # A string could be a single character or a bunch of texts
# print(letter)               # P
# print(len(letter))          # 1 sacar la longitud de la cadena length
# greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
# print(greeting)             # Hello, World!
# print(len(greeting) <= 142)        # 13
# sentence = "I hope you are enjoying 30 days of Python Challenge ' I am enjoying it"
# print(sentence)
print("El Principito" == "El Principito")

def text_size_valid(text):
    if len(text) > 142:
        return  "Your text size is: " + str(len(text)) + ". The text is too long"
    else:
        print("Your text size is: " + str(len(text)) + ". >>> The text size is valid.\n")
        return save_text(text)
    
def save_text(text):
    fwrite = open("biblioteca.txt", "w")
    fwrite.write(text)
    return "Se guardara en la Base de datos."

def read_text(text):
    print("Se leera de la Base de datos.\n")
    variable_lectura = open("biblioteca.txt", "r")
    return print(variable_lectura.read())

def modify_text(text):
    fwrite = open("biblioteca.txt", "w")
    fwrite.write(text)
    return "Se modificara en la Base de datos."

def delete_text(text):
    variable_lectura = open("biblioteca.txt", "r")
    if text == variable_lectura.read():
        fwrite = open("biblioteca.txt", "w")
        fwrite.write("")
        return "Se eliminara de la Base de datos"
    
    return "No se encontro el texto"

#print(text_size_valid(input("Welcome to your library. Please set the name of a book you want to store in the library: ")))
#print(read_text("biblioteca.txt"))
# print(modify_text("biblioteca.txt"))
#print(delete_text("El Principito"))


#Actividad y Replicar la Libreria en puro texto
#ciclos for, while
#listas, diccionarios
#funciones crear menu para el usuario
# for book in library:
#     if user_input == book: 
#         #eliminar book
#         #modificar book
#         #leer book
#         #guardar book no exista el book con anterioridad



def menu():
    print("Welcome to your library. Select an option from the menu: \n 1. Add a book \n 2. Read a book \n 3. Modify a book \n 4. Delete a book \n 5. Exit")
    user_input = input("Please select an option from the menu: ")
    return library(user_input)

def library(user_input):
    library = []
    if user_input == "1":
        text = input("Please set the name of a book you want to store in the library: ")
        return menu()
