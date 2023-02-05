# You're going to be learning about How to Make Caesar Cipher (Functions with Input, Arguments & Parameters)

def exe0():
  '''
  Exercise 0 : Functions with Input
  '''
  # Simple Function
  def greet():
    print("Hello Angela")
    print("How do you do Jack Bauer?")
    print("Isn't the weather nice today?")
  greet()

  #Function that allows for input
  #'name' is the parameter.
  #'Jack Bauer' is the argument.
  def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
  greet_with_name("Jack Bauer")

  #Functions with more than 1 input
  def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

  #Calling greet_with() with Positional Arguments
  greet_with("Jack Bauer", "Nowhere")
  #vs.
  greet_with("Nowhere", "Jack Bauer")

  #Calling greet_with() with Keyword Arguments
  greet_with(location="London", name="Angela")

def exe1():
  '''
  Exercise 1 - Paint Area Calculator
  '''
  # Write your code below this line 👇

  from math import ceil

  def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

  # Write your code above this line 👆

  # 🚨 Don't change the code below 👇
  test_h = int(input("Height of wall: "))
  test_w = int(input("Width of wall: "))
  coverage = 5
  paint_calc(height=test_h, width=test_w, cover=coverage)

def exe2():
  '''
  Exercise 2 - Prime Numbers
  '''
  # Write your code below this line 👇
  def prime_checker(number):
    is_prime = True
    for i in range(2, number):
      if number % i == 0:
        is_prime = False
    if is_prime:
      print("It's a prime number.")
    else:
      print("It's not a prime number.")

  # Write your code above this line 👆

  # Do NOT change any of the code below👇
  n = int(input("Check this number: "))
  prime_checker(number=n)

def cipher_1_encryption():
  '''
  Caesar Cipher Part 1 - Encryption
  '''
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #Don't change the code above 👆

  #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
  def encrypt(plain_text, shift_amount):
    #TODO-2: Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    cipher_text = ""
    for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      new_letter = alphabet[new_position]
      cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

  #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
  encrypt(plain_text=text, shift_amount=shift)

def cipher_2_decryption():
  '''
  Caesar Cipher Part 2 - Decryption
  '''
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")

  #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
  def decrypt(cipher_text, shift_amount):
    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    #e.g.
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"
    plain_text = ""
    for letter in cipher_text:
      position = alphabet.index(letter)
      new_position = position - shift_amount
      plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")


  #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
  if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
  elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)

def cipher_3_combine():
  '''
  Caesar Cipher Part 3 - Reorganising our Code
  '''
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
  def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
      shift_amount *= -1
    for letter in start_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      end_text += alphabet[new_position]

    print(f'The {cipher_direction}d text is {end_text}')

  #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

def cipher_4_end():
  '''
  Caesar Cipher Part 4 - User Experience Improvements & Final Touches
  '''
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
              'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
      shift_amount *= -1
    for char in start_text:
      #TODO-3: What happens if the user enters a number/symbol/space?
      #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
      #e.g. start_text = "meet me at 3"
      #end_text = "•••• •• •• 3"
      if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
      else:
        end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

  #TODO-1: Import and print the logo from art.py when the program starts.
  from art import logo_caesar_cipher
  print(logo_caesar_cipher)

  #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
  #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
  #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
  #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
  should_end = False
  while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    #Hint: Think about how you can use the modulus (%).
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
      should_end = True
      print("Goodbye")

def program():
  if choice == 0:
    exe0()
  elif choice == 1:
    exe1()
  elif choice == 2:
    exe2()
  elif choice == 3:
    cipher_1_encryption()
  elif choice == 4:
    cipher_2_decryption()
  elif choice == 5:
    cipher_3_combine()
  elif choice == 6:
    cipher_4_end()
  else:
    print('You not type the selected choice, please "RUN" again.')

should_end = False
while not should_end:
  choice = int(input('What is your choice ? ("0", "1", "2", "3", "4", "5", "6")\n'))
  program()

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")