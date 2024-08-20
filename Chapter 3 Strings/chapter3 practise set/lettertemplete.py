# Write a progarm to fill in a letter templete given below with name and date
                      # letter = *********
                      # Dear <|Name|> ,
                      #You are selected
                      # <|Date|>
                      # ....              
letter = '''Dear <|Name|> ,
           You are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Bimal").replace(" <|Date|>","08 August"))