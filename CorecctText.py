from autocorrect import Speller

def main():
    spell = Speller('uk')
    text = input('Введіть текст з помилками: ')
    corrected_text = spell(text)
    print('Виправлений текст:', corrected_text)

if __name__ == "__main__":
    main()
