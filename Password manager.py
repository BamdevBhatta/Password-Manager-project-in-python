from cryptography.fernet import Fernet


'''
def write_key ():
  key = Fernet.generate_key()
  with open("key.key", "wb") as  key_file:
    key_file.write(key)
'''

def load_key ():
  file = open("key.key", "rb")#reading byte
  key = file.read()
  file.close()
  return key

master_pwd = input("What is the master password? ")


key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
  with open('password manager.txt', 'r') as f:
    for line in f.readlines():
      data = (line.rstrip())
      user, password = data.split("|")
      print("User: ", user, " | Password: ", fer.decrypt(password.encode()).decode())


def add():
  name = input("Account Name:")
  password = input("Password: ")

  with open('password manager.txt','a') as f:
    f.write(name + "|" +  fer.encrypt(password.encode()).decode()+"\n")

while True:
  mode = input("would you like to add a new password or view existing ones(view,add) or press Q to quit: ").lower()
  if mode == "q":
    break
  
  if mode == "view":
    view()
  
  elif mode == "add":
    add()

  else:
    print("Invalid mode. ")
    continue