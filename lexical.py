operator_symbol_unique = [".", ",", ";", "[", "]", "(", ")", "+", "-", "*", "/", "%", "?", "!", "=", ">", "<"]
operator_symbol_dict = {
    "=":"tkn_assign",
    "==":"tkn_equal",
    
    "!=":"tkn_neq",
    
    ".":"tkn_period",
    ",":"tkn_comma",
    ";":"tkn_semicolon",
    "]":"tkn_closing_bra",
    "[":"tkn_opening_bra",
    ")":"tkn_closing_par",
    "(":"tkn_opening_par",
    "+":"tkn_plus",
    "-":"tkn_minus",
    "*":"tkn_times",
    "/":"tkn_div",
    "%":"tkn_mod",
    "?":"tkn_question_mark",
    
    "<":"tkn_less",
    "<=":"tkn_leq",
    
    ">":"tkn_greater",
    ">=":"tkn_geq"
    
}

saved_words = "Get,next,input,Put,to,output,if,elseif,else,while,integer,float,and,or,not,array,Function,returns,nothing,SquareRoot,RaiseToPower,AbsoluteValue,RandomNumber,SeedRandomNumbers,Main,size,for,evaluates,with,decimal,places"
saved_words = saved_words.split(",")

row_counter = 0
passes = 0

error =  False
while(True):
    if error:
        break
    try:
        row_counter += 1
        coral_code_row = list(input())
        coral_code_row.append("end")
    except EOFError:
        break
    else:
        for i in range(len(coral_code_row)):
            
            if error:
                break
            
            if passes>0:
                
                passes-=1
                continue
            
            current_letter = coral_code_row[i]
            
            if current_letter == "end":
                break;
            
            next_letter = coral_code_row[i+1]
            
            #If it is a comment
            comment_non_intruder_flag = True
            if coral_code_row[0] + coral_code_row[1]  == "//":
                break;
            elif coral_code_row.count("/")>1 and coral_code_row[coral_code_row.index("/")+1]=="/":
                first_pos = coral_code_row.index("/")
                for k in range(first_pos):
                    if coral_code_row[k] == " ":
                        continue
                    comment_non_intruder_flag = False
                    break
                if comment_non_intruder_flag:
                    break
            
            #If it is a space key
            if current_letter == " ":
                continue
            
            #If it is a symbol or an operator
            if current_letter in operator_symbol_unique:
                if current_letter == ".":
                    print("<{0},{1},{2}>".format(operator_symbol_dict[current_letter],row_counter,i+1))
                    continue
                elif current_letter in [",",";","[","]","(",")","+","-","*","/","%","?"]:
                    print("<{0},{1},{2}>".format(operator_symbol_dict[current_letter],row_counter,i+1))
                    continue
                elif current_letter == "!":
                    if next_letter == "=":
                        print("<{0},{1},{2}>".format(operator_symbol_dict[current_letter+next_letter],row_counter,i+1))
                        passes=1
                        continue
                    print(">>> Error lexico (linea: {0}, posicion: {1})".format(row_counter,i+1))
                    error = True
                    break
                elif current_letter == "=":
                    if next_letter == "=":
                        print("<{0},{1},{2}>".format(operator_symbol_dict[current_letter+next_letter],row_counter,i+1))
                        passes=1
                        continue
                    print("<{0},{1},{2}>".format(operator_symbol_dict[current_letter],row_counter,i+1))
                    continue
                    
                elif current_letter == ">":
                    if next_letter == "=":
                        print("<{0},{1},{2}>".format(operator_symbol_dict[current_letter+next_letter],row_counter,i+1))
                        passes=1
                        continue
                    print("<{0},{1},{2}>".format(operator_symbol_dict[current_letter],row_counter,i+1))
                    continue
                    
                elif current_letter == "<":
                    if next_letter == "=":
                        print("<{0},{1},{2}>".format(operator_symbol_dict[current_letter+next_letter],row_counter,i+1))
                        passes=1
                        continue
                    print("<{0},{1},{2}>".format(operator_symbol_dict[current_letter],row_counter,i+1))
                    continue
            
            #If it is a number
            if current_letter>= "0" and current_letter<="9":
                
                numbers = ""
                number_counter = 0
                
                for j in range(i,len(coral_code_row)):
                    
                    number_counter+=1
                    possible_number = coral_code_row[j]
                    
                    if possible_number>= "0" and possible_number<="9":
                        numbers+=possible_number
                        continue
                    elif possible_number == ".":
                        numbers+=possible_number
                        if numbers.count(possible_number) >1:
                            if numbers[-1]=="." and numbers[-2] == ".":
                                print("<tkn_integer,{0},{1},{2}>".format(numbers[:-2],row_counter,i+1))
                                passes = number_counter - 3
                                break
                            elif numbers[-1]=="." and not numbers[-2] == ".":
                                print("<tkn_float,{0},{1},{2}>".format(numbers[:-1],row_counter,i+1))
                                passes = number_counter - 2
                                break
                        continue
                    elif numbers.count(".")==1:
                        if numbers[-1]==".":
                            print("<tkn_integer,{0},{1},{2}>".format(numbers[:-1],row_counter,i+1))
                            passes = number_counter - 3
                            break
                        elif not(numbers[-1]=="."):
                            print("<tkn_float,{0},{1},{2}>".format(numbers,row_counter,i+1))
                            passes = number_counter - 2
                            break
                    elif numbers.count(".")==0:
                        print("<tkn_integer,{0},{1},{2}>".format(numbers,row_counter,i+1))
                        passes = number_counter - 2
                        break
                continue
                    
            #If it is an identifier
            if current_letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                case = 0
                identifier=""
                #identifier_counter = 0
                
                for j in range(i,len(coral_code_row)):
                    possible_identifier_letter = coral_code_row[j]
                    if case ==0:
                        if possible_identifier_letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                            identifier+=possible_identifier_letter
                            case = 1
                            continue
                    elif case ==1:
                        if possible_identifier_letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' or\
                            possible_identifier_letter in '0123456789' or \
                            possible_identifier_letter == "_":
                            
                            identifier+=possible_identifier_letter
                            case=1
                            continue
                        if identifier in saved_words:
                            print("<{0},{1},{2}>".format(identifier,row_counter,i+1))
                            passes = len(identifier) - 1 
                            break
                        print("<id,{0},{1},{2}>".format(identifier,row_counter,i+1))
                        passes = len(identifier) - 1 #Using a switch statement is only necessary to delete the first element because the last one is not added to identifier-variable
                        break
                continue
            
            #If it is a string
            if current_letter == '"':
                case = 0 
                string = ""
                string_flag = False
                for j in range(i,len(coral_code_row)):
                    possible_string = coral_code_row[j]
                    if case ==0:
                        #This case is like repeating the principal if of this section
                        if possible_string == '"':
                            #string+=possible_string   //I don't add anything because I don't want to delete "" after
                            case=1
                            continue
                    elif case == 1:
                        if possible_string == '"':
                            if ord(coral_code_row[j-1]) == 92:
                                string+=possible_string
                                continue
                            #string+=possible_string
                            print("<tkn_str,{0},{1},{2}>".format(string,row_counter,i+1))
                            passes = len(string) + 2 - 1 #2 because the pair of "" and 1 because the first symbol is already consumed
                            break
                        else:
                            if possible_string == "end":
                                print(">>> Error lexico (linea: {0}, posicion: {1})".format(row_counter,i+1))
                                error = True
                                break
                            if ord(possible_string) == 92:
                                string+=chr(92)
                                continue         
                            string+=possible_string
                            continue
                continue
            
            print(">>> Error lexico (linea: {0}, posicion: {1})".format(row_counter,i+1))
            error = True
            break