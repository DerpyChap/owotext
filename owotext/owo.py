import argparse
import random
import sys

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
    ' ( ͡° ᴥ ͡°)',
    ' (´・ω・｀)',
    ' (ʘᗩʘ\')',
    ' (இωஇ )',
    ' (๑•́ ₃ •̀๑)',
    ' (• o •)',
    ' (⁎˃ᆺ˂)',
    ' (╯﹏╰）',
    ' (●´ω｀●)',
    ' (◠‿◠✿)',
    ' (✿ ♡‿♡)',
    ' (❁´◡`❁)',
    ' (　\'◟ \')',
    ' (人◕ω◕)',
    ' (；ω；)',
    ' (｀へ´)',
    ' ._.',
    ' :3',
    ' :D',
    ' :P',
    ' ;-;',
    ' ;3',
    ' ;_;',
    ' <{^v^}>',
    ' >_<',
    ' >_>',
    ' UwU',
    ' XDDD',
    ' ^-^',
    ' ^_^',
    ' x3',
    ' x3',
    ' xD',
    ' ÙωÙ',
    ' ʕʘ‿ʘʔ',
    ' ㅇㅅㅇ',
    ', fwendo',
    '（＾ｖ＾）'
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
    'The ': 'Da ',
    'THE ': 'DA '
}


class OwO:
    # noinspection PyDefaultArgument
    def __init__(self, _prefixes=prefixes, _suffixes=suffixes, _substitutions=substitutions):
        self.prefixes = _prefixes
        self.suffixes = _suffixes
        self.substitutions = _substitutions

    def whatsthis(self, text: str):
        for key, value in self.substitutions.items():
            text = text.replace(key, value)
        if self.prefixes:
            text = (random.choice(self.prefixes) + text)
        if self.suffixes:
            text = (text + random.choice(self.suffixes))
        return text


def main():
    parser = argparse.ArgumentParser(
        description='A Python library for converting text strings into OwO',
        epilog='https://github.com/DerpyChap/owotext')

    parser.add_argument('text', type=str, nargs='*', help='The text to OwO',
                        default=["Please give me some text to OwO"])

    args = parser.parse_args()
    text = ' '.join(args.text)

    if not sys.stdin.isatty():
        text = sys.stdin.read().rstrip()

    o = OwO()
    print(o.whatsthis(text))


if __name__ == '__main__':
    main()
