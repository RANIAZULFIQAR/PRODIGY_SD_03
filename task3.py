class contact_information:
    def __init__(self,name=None,email=None,number=None,address=None, filepath= 'task3.txt') :
        self.name= name
        self.email= email
        self.number=number
        self.address=address
        self.filepath=filepath
    def __str__(self):
        return f"{self.name},{self.email},{self.number},{self.address}"
    
    def add(self,contact):
        with open(self.filepath,'a' ) as file:
            file.write(str(contact)+ '\n')

    def update(self, name):
        with open(self.filepath, 'r') as file:
            lines = file.readlines()
        
        updated = False
        with open(self.filepath, 'w') as file:
            for line in lines:
                contact = line.strip().split(',')
                if contact[0] == name:
                    
                    print('1. Edit name')
                    print('2. Edit email')
                    print('3. Edit number')
                    print('4. Edit address')
                    choice = int(input())
                    
                    if choice == 1:
                        new_name = input("Enter new name: ")
                        contact[0] = new_name
                    elif choice == 2:
                        new_email = input("Enter new email: ")
                        contact[1] = new_email
                    elif choice == 3:
                        new_number = input("Enter new number: ")
                        contact[2] = new_number
                    elif choice == 4:
                        new_address = input("Enter new address: ")
                        contact[3] = new_address
                    
                    file.write(','.join(contact) + '\n')
                    updated = True
                    print('Contact updated successfully!')
                else:
                    file.write(line)
        
        if not updated:
            print(f"Contact '{name}' not found.")
  
    def view(self):
        try:      
            with open(self.filepath, 'r') as file:

                contact=file.read()
                if contact:
                  print('contact list : ')                         
                  print(contact)
                  return contact
                else:
                    print('NO CONTACT PRESENT! ')
        except FileNotFoundError:
            print('contact not found')
    
    def delete(self, name):
        try:
            with open(self.filepath, 'r') as file:
                lines = file.readlines()
            
            with open(self.filepath, 'w') as file:
                found = False
                for line in lines:
                    if not line.startswith(name + ","):
                        file.write(line)
                    else:
                        found = True
                
                if found:
                    print(f"Contact '{name}' deleted successfully.")
                else:
                    print(f"Contact '{name}' not found.")
        except FileNotFoundError:
            print("No contacts to delete.")
                   
def main():

    while True:
        
        manager=contact_information()
        print('ENTER YOUR CHOICE: ')

        print('1. ADD CONTACT')
        print('2. VIEW CONTACT')
        print('3. DELETE CONTACT')
        print('4. UPDATE CONTACT')
        print('5. EXIT')
        choice =int(input())

        if choice==1:


            name= input('enter the name you want to add :')
            email= input('enter the email address :')
            number= input('enter the number :')
            address= input('enter the address of the new contact :')
            contact=contact_information(name,email,number,address, 'task3.txt')
            manager.add(contact)
            print('CONTACT HAS BEEN ADDED SUCCESSFULLY !!!!')

        elif choice==2 :
            contact= manager.view()                   

        elif choice==3:
            
            print('enter the name you want to delete : ')
            name=str(input())
            manager.delete(name)
        elif choice==4:
            found= False
            name = input('Enter the name of the contact you want to update: ')
            
            manager.update(name)
          
        elif choice==5:
            print('Exiting Progam ....')
            break
             
        else :                                                               
           print('invalid choice entered')
        
if __name__ == "__main__":
    main()
   

    
  



