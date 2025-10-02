# https://informatics.msk.ru/mod/statements/view.php?chapterid=111312

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = alphabet.upper()

def CaesarCipher(S, k):
  result = ''
  for i in S:
    if i in alphabet:
      result += alphabet[(alphabet.index(i) + k) % len(alphabet)]
    elif i in ALPHABET:
      result += ALPHABET[(ALPHABET.index(i) + k) % len(ALPHABET)]
    else:
      result += i
  return result

print(CaesarCipher(input(), 3))
