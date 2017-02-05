import sys
import string

class Morseifier:
    alpha = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8",
                "9", "0", " " ];
    morse = [ ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                "-.--", "--..", ".----", "..---", "...--", "....-", ".....",
                "-....", "--...", "---..", "----.", "-----", "/" ];

    translatedict={}
    def __init__(self):
        for i in range(0,len(self.alpha)):
            self.translatedict[self.alpha[i]] = self.morse[i]
            self.translatedict[self.morse[i]] = self.alpha[i]
            
    def translate(self,text):
        sentence = list(text)
        morsesentence=""
        i=0
        for letter in sentence:
            if i==len(sentence)-1:
                morsesentence+=self.translatedict[letter]
                return morsesentence
            morsesentence+=self.translatedict[letter]+' '
            i+=1
        return morsesentence

    def untranslate(self,morse):
        morsesentence = morse.split()
        sentence=""
        for letter in morsesentence:
            sentence+=self.translatedict[letter]
        return sentence



























def main():
    m = Morseifier()

    tests = [('MORSE CODE','-- --- .-. ... . / -.-. --- -.. .'),
            ('INSPECTOR MORSE','.. -. ... .--. . -.-. - --- .-. / -- --- .-. ... .'), \
            ('',''), \
            ('LAST OF THE MORSICANS','.-.. .- ... - / --- ..-. / - .... . / -- --- .-. ... .. -.-. .- -. ...')]

    errors = 0
    for text, morse in tests:
        yourMorse = m.translate(text)
        yourText = m.untranslate(morse)

        if yourMorse != morse:
            print('Error when translating {}'.format(text))
            print('Yours  : "{}"'.format(yourMorse))
            print('Correct: "{}"'.format(morse))
            print()
            errors += 1

        if yourText != text:
            print('Error when translating {}'.format(morse))
            print('Yours  : "{}"'.format(yourText))
            print('Correct: "{}"'.format(text))
            print()
            errors += 1

    if errors == 0:
        print('Congratulations, no errors')
        print('-.-. --- -. --. .-. .- - ..- .-.. .- - .. --- -. ... / -. --- / . .-. .-. --- .-. ...')
    else:
        print('Uh oh, {} error/s remain'.format(errors))
        print('..- .... / --- .... / . .-. .-. --- .-. ... / .-. . -- .- .. -.')

    return errors

if __name__ == '__main__':
    sys.exit(main())
