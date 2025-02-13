def VaildatePassword(Pass):
    UpperCount, LowerCount, NumberCount = 0, 0, 0
    for j in range(len(Pass)):
        current_letter = Pass[j:j+1]
        current_ascii = ord(current_letter)

        if (current_ascii > 64 and current_ascii < 91) or (current_ascii > 96 and current_ascii < 123):
            if current_letter == str(current_letter):
                if current_letter != (current_letter).upper(): UpperCount += 1
                elif current_letter != (current_letter).lower(): LowerCount += 1
        elif current_ascii > 47 and current_ascii < 58: NumberCount += 1
        else: return False
    
    if UpperCount > 1 and LowerCount > 1 and NumberCount > 2: return True
    else: return False
    
print(VaildatePassword("AApp333"))