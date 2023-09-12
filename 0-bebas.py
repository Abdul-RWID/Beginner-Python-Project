should_end = False

while not should_end:
    shift = int(input('angka '))
    shift = shift % 26
    print(f'hasil {shift}')

    result = input('continue : yes or no\n')
    if result == 'no':
        should_end = True
        print('Goodbye')