import read 
import write
def main():
    file_path = "land.txt"
    lands_data = read.available_land(file_path)

    while True:    
        print("Enter 'rent' to rent the land, 'return' to return the land, or 'exit' to quit: ")
        user_input = input().strip().lower() 
        
        if user_input == 'rent':
            write.rent(lands_data)
        
        elif user_input == 'return':
            write.return_land(lands_data)
            
        elif user_input == 'exit':
            break
        
        else:
            print("Invalid input. Fill the form again!")
          
            
if __name__ == "__main__":
    main()


