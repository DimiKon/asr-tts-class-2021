import sys
 
general_lexicon = sys.argv[1]
wordlist = sys.argv[2]
output_file = sys.argv[3]
 
with open(general_lexicon, encoding='ISO 8859-7') as lex:
    with open(wordlist, encoding = 'utf-8') as wlist:
        with open(output_file, 'w', encoding = 'ISO 8859-7') as ofile:
            gen_lex = {}   
            a_list = []         
            
            for line in lex:
                cline = line.rstrip()
                line_info = cline.split(" ")
                word = line_info[0]
                pronunciation = " ".join(line_info[1:])
                
                if word in gen_lex:
                    a_list.append(pronunciation)
                    gen_lex[word] = a_list
                else:   
                    a_list = [pronunciation]
                    gen_lex[word] = a_list
            
            for line in wlist:
                word = line.rstrip()
                if word in gen_lex:
                    for pron in gen_lex[word]:
                        ofile.write("{} {}\n".format(word, pron))
                else:
                    print("Unknown pronunciation for word: {}".format(word))