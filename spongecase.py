# Converts text to Spongecase

try:
    import pyperclip
except ImportError:
    pass

def convert_to_spongecase(text):
    spongecase = ''

    for i in range(len(text)):
        if i % 2 == 0:
            spongecase += text[i].lower()
        else:
            spongecase += text[i].upper()
    
    return spongecase

def main():
    print('eNtEr YoUr MeSsAgE:')
    text = input('> ')
    
    text = convert_to_spongecase(text)

    print(text)

    try:
        pyperclip.copy(text)
        print('(cOpIed SpOnGeTexT to ClIpbOaRd.)')
    except:
        pass

if __name__ == '__main__':
    main()