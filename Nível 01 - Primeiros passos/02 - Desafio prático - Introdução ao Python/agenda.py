def add_contact(name, phone, email, favorite=False):
  contact = {
    "name": name,
    "phone": phone,
    "email": email,
    "favorite": favorite
  }
  
  contacts.append(contact)
  
  print(f"{name} adicionado com sucesso!")

def view_contacts():
  for index, contact in enumerate(contacts):
    print("="*40)
    print(f"Contato {index + 1}")
    print(f"Nome: {contact['name']}")
    print(f"Telefone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    
    if contact['favorite']:
      print(f"⭐")
    
    print("="*40)

def update_contact(index, name, phone, email):
  contacts[index]['name'] = name
  contacts[index]['phone'] = phone
  contacts[index]['email'] = email
  
  print(f"Contato {contacts[index]['name']} atualizado com sucesso!")

def mark_favorite(index):
  contacts[index]['favorite'] = not contacts[index]['favorite']
  
  if contacts[index]['favorite']:
    print(f"Contato {contacts[index]['name']} marcado como favorito!")
  else:
    print(f"Contato {contacts[index]['name']} desmarcado como favorito!")

def view_favorites():
  for index, contact in enumerate(contacts):
    if contact['favorite']:
      print("="*40)
      print(f"Contato {index + 1}")
      print(f"Nome: {contact['name']}")
      print(f"Telefone: {contact['phone']}")
      print(f"Email: {contact['email']}")
      print(f"⭐")
      print("="*40)

def delete_contact(index):
  contact = contacts.pop(index)
  print(f"Contato {contact[index]['name']} deletado com sucesso!")

contacts = []
favorites = []

while True:
  print("="*40)
  print("Agenda de contatos automática")
  print("="*40)
  print("1. Adicionar um novo contato")
  print("2. Ver contatos")
  print("3. Atualizar um contato")
  print("4. Marcar / Desmarcar um contato como favorito")
  print("5. Ver contatos favoritos")
  print("6. Deletar um contato")
  print("0. Sair")
  print("="*40)
  
  choice = input("Digite a sua escolha: ")

  if choice == "1":
    name = input("Digite o nome do contato: ")
    phone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    add_contact(name, phone, email)
  elif choice == "2":
    view_contacts()
  elif choice == "3":
    view_contacts()
    
    index = int(input("Digite o número do contato que deseja atualizar: ")) - 1
    
    name = input("Digite o nome do contato: ")
    phone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    
    update_contact(index, name, phone, email)
  elif choice == "4":
    view_contacts()
    
    index = int(input("Digite o número do contato que deseja marcar como favorito: ")) - 1
    
    mark_favorite(index)
  elif choice == "5":
    view_favorites()
  elif choice == "6":
    view_contacts()
    
    index = int(input("Digite o número do contato que deseja deletar: ")) - 1
    
    delete_contact(index)
  elif choice == "0":
    break
  
print("Programa finalizado")