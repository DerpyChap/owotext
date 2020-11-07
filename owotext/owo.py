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
        """
        UwU Convewts da specified stwing into OwO speak ʕʘ‿ʘʔ

        :param text: Huohhhh. Da text uu want to convewt..
        :return: OWO Da convewted stwing (人◕ω◕)
        """
        text = self.translate(text)
        if self.prefixes:
            text = (random.choice(self.prefixes) + text)
        if self.suffixes:
            text = (text + random.choice(self.suffixes))
        return text

    def translate(self, text: str):
        """
        Convewts da specified stwing into OwO speak, without a pwefix ow suffix

        :param text: Da text uu want to convewt
        :return: Da convewted stwing
        """
        for key, value in self.substitutions.items():
            text = text.replace(key, value)
        return text


# noinspection PyProtectedMember
def main():
    o = OwO()

    parser = argparse.ArgumentParser(add_help=False,
                                     description=o.whatsthis(
                                         'A Python library for converting text strings into OwO speak'),
                                     epilog='https://github.com/DerpyChap/owotext')

    parser._positionals.title = o.translate(parser._positionals.title)
    parser._optionals.title = o.translate(parser._optionals.title)

    parser.add_argument('-t', '--translate', action='store_true',
                        help=o.translate('translate the text without a prefix or suffix'))
    parser.add_argument('text', type=str, nargs='+', help=o.whatsthis('the text to convert'))
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help=o.whatsthis('show this help message and exit'))
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    text = ' '.join(args.text)

    if not sys.stdin.isatty():
        text = sys.stdin.read().rstrip()
    if args.translate:
        print(o.translate(text))
    else:
        print(o.whatsthis(text))


if __name__ == '__main__':
    main()
