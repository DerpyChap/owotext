# owotext
A Python library for converting text strings into OwO, inspired by [Douglas Gardner's work](https://github.com/zuzak/owo/).

## Installing
```
pip install owotext
```

## Usage
You can use owotext in your Python projects like so:
```py
# OwO Impowt da wibwawy ÙωÙ
from owotext import OwO

# Huohhhh. Setup da convewtew ʕʘ‿ʘʔ
uwu = OwO()

# HIIII! Convewt a stwing into OwO speak Huoh.
print(uwu.whatsthis('In the beginning the Universe was created. '
                    'This had made many people very angry and has '
                    'been widely regarded as a bad move.'))
```
Example output:
```
Huohhhh. In da beginning da Univewse was cweated. This had made many peopwe vewy angwy and haz been widewy wegawded as a bad move. Huoh.
```

You can also call owotext from the command line by using the `owo` command:
```
owo You know something? I really hate people! They're selfish, ignorant, loud obnoxious pricks, with basically no redeeming qualities whatsoever. I mean really, look at all they've achieved! Genocide, global warming, reality TV, and just a never ending parade of failures and fuck ups! They are, without question, a complete write-off of a species
```
Example output:
```
Huohhhh. You knuw something? I weawwy hate peopwe! Theywe sewfish, ignuwant, woud obnuxious pwicks, with basicawwy nu wedeeming quawities whatsoevew. I mean weawwy, wook at aww theyve achieved! Genucide gwobaw wawming weawity TV and just a nevew ending pawade of faiwuwes and fuck ups! They awe without question a compwete wwite-off of a species (　'◟ ')
```

## Customization
`OwO()` accepts custom lists of prefixes, suffixes and substitutions.
```py
OwO(prefixes, suffixes, substitutions)
```
Things should be fairly self explanatory here; `prefixes` and `sufffixes` should be `List` objects and `substitutions` should be a `Dict`.

## Requirements
 - Python 3
 - A lack of self worth