f = open("out.txt","r")
fl = f.readlines()

text_file = open("Lender.txt", "w")
extensionsToCheck = ['(C) Lender is ', '(C)Lender is ']
for line in enumerate(fl):
    
    if any(ext in line[1] for ext in extensionsToCheck):
        count = 0
        # print(line[1])
        split_after_bracket = line[1].split('C)')
        # print(split_after_bracket[1])

        # # lets try counting the number of punctation marks in the sentence.
        # for i in range(0, len (split_after_bracket[1])):
        #     # print(i)  
        #     #Checks whether given character is a punctuation mark  
        #     if split_after_bracket[1][i] in ("."):  
        #         count = count + 1;  
        # print("the total number of punctuation character :" + str(count) )



        string_split1 = split_after_bracket[1]
        str_sp1 = string_split1.split('Lender is ')
        # print(str_sp1)
        print(str_sp1[1])
        text_file.write(str_sp1[1])
        print('\n\n\n\n')
    
    text_file.write('\n\n')


text_file.close()

f.close()
