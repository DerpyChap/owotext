import random
import argparse

prefixes = [
  '<3 ',
  '0w0 ',
  'H-hewwo?? ',
  'HIIII! ',
  'Haiiii! ',
  'Huohhhh. ',
  'OWO ',
  'OwO ',
  'UwU '
]

suffixes = [
  ' :3',
  ' UwU',
  ' ÙωÙ',
  ' ʕʘ‿ʘʔ',
  ' ʕ•̫͡•ʔ',
  ' >_>',
  ' ^_^',
  '..',
  ' Huoh.',
  ' ^-^',
  ' ;_;',
  ' ;-;',
  ' xD',
  ' x3',
  ' :D',
  ' :P',
  ' ;3',
  ' XDDD',
  ', fwendo',
  ' ㅇㅅㅇ',
  ' (人◕ω◕)',
  '（＾ｖ＾）',
  ' Sigh.',
  ' x3',
  ' ._.',
  ' (　\'◟ \')',
  ' (• o •)',
  ' (；ω；)',
  ' (◠‿◠✿)',
  ' >_<'
]

substitutions = {
  'r': 'w',
  'l': 'w',
  'R': 'W',
  'L': 'W',
  'no': 'nu',
  'has': 'haz',
  'have': 'haz',
  'you': 'uu',
  'the ': 'da ',
  'The ': 'Da '
}

class OwO:
    def __init__(self, prefixes=prefixes, suffixes=suffixes, substitutions=substitutions):
        self.prefixes = prefixes
        self.suffixes = suffixes
        self.substitutions = substitutions

    def whatsthis(self, text: str):
        for key, value in self.substitutions.items():
            text = text.replace(key, value)
        return random.choice(self.prefixes) + text + random.choice(suffixes)

def main(args=None):
  parser = argparse.ArgumentParser(
        description='A Python library for converting text strings into OwO',
        epilog='https://github.com/DerpyChap/owotext')
    
  parser.add_argument('text', type=str, nargs='+', help='The text to OwO')

  args = parser.parse_args()
  o = OwO()
  text = ' '.join(args.text)
  print(o.whatsthis(text))

if __name__ == '__main__':
    main()
