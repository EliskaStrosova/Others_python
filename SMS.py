# # ukol-03: SMS brána

# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

# - Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
# - Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.

# Tvůj program bude obsahovat dvě funkce:
# - První funkce ověří délku telefonního čísla. Uvažuj, že telefonní číslo může být
# devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Nemusíte kontrolovat, 
# zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
# Pokud je číslo platné, funkce vrátí hodnotu `True`, jinak vrátí hodnotu `False`.
# - Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.

# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné,
# vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou
# vypíše uživateli.

# ## Nápověda
# Pokud chcete zkontrolovat předvolbu, stačí využít podmínku`+420 in cislo`, alternativně můžete využít
# indexy: Python umožňuje kromě jednoho znaku z řetězce získat i více znaků, a to
# pomocí dvojtečky. Pokud budete chtít získat první čtyři znaky, napište `cislo[0:4]`. Pak můžete vytvořit podmínku
# `cislo[0:4] == "+420"`.




users_phone_num= input("Telefonní číslo:")

def check_input(number):
    if len(users_phone_num) == 9:
        return True
    elif len(users_phone_num) == 13:
        return True 
    else:
        return False  

print(check_input(users_phone_num))

#pokud check_input True program bude pokračovat k users_text, pokud False, program se zastaví a vyzve k opakování users_phone_num - využití while loop?

users_text = input("SMS:")
charact_price = 3

def check_input_sms(numb):
    if len(users_text) <= 180:
        print("Zpráva bude stát", charact_price, "Kč")
    elif len(users_text) >= 180: #pro každých 180 znaků * charact_price - cyklus for? 
        print("Zpráva bude stát", charact_price * 2, "Kč")
    
check_input_sms()
