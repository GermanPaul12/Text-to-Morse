#Coverting the text to upper letters 

keep_going = True
#Dictionary with letters and associated morse code
morse_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 
              'H':'....', 'I':'..', 'J':'.---', 'K':'-.-'
              , 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 
              'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 
              'X':'-..-', 'Y':'-.--', 'Z':'--..', ' ':'       ', 
              '1':'.----', '2':'..---', '3': '...--', '4':'....-', 
              '5':'.....', '6':'-....',
              '7':'--...', '8':'---..', '9':'----.', '0':'-----'}
#Converting the keys, values to lists so i can transform the values "morse code" to letters
key_list = list(morse_dict.keys())
val_list = list(morse_dict.values())

#For loops to iterate over the morse_dict and print the morse code

def encode(encoding_data):
    global output
    output = ''
    for k in data: 
        if k not in morse_dict.keys():
            continue
        if k in morse_dict.keys():
            output = (output + morse_dict[k])
            output = output + '   '
    print(output)    
    
    
def decode(decoding_data):
    global data
    global output
    output = ''
    data = data.split('       ')
    for i in range(len(data)):
        data[i] = data[i].split('   ')
        for z in range(len(data[i])):
            if data[i][z] not in morse_dict.values():
                continue
            position = val_list.index(data[i][z])
            output = output + key_list[position]
        output = output + ' '      
    print(output)
while keep_going:
    mode = input('Do you want to encode then input "e" or decode then input "d" or input "q" to quit: ')
    if mode == 'q':
        keep_going = False
    if mode == 'e':
        text = input('Input the text which you want to covert in morse code: ')
        data = text.upper()
        encode(data)
    if mode == 'd':
        data = input('Input the morse code which you want to decode: ')    
        decode(data)