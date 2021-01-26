def test_palindrome(cara):
    cara_original = cara
    # cara = cara.strip()
    # cara = cara.lower()
    # cara = cara.split(" ")
    # cara = "".join(cara)

    cara = "".join(cara.strip().lower().split(" "))

    tmp = ""
    for i in range(len(cara),0,-1):
        tmp += cara[i-1]
    if tmp == cara:
        print("\"{}\" est un palindrome".format(cara_original))
    else:
        print("\"{}\" n est pas un palindrome".format(cara_original))

test_palindrome("ressasser")
test_palindrome("engage le jeu que je le gagne")
test_palindrome("radar")
test_palindrome("never odd or even")
test_palindrome("karine alla en Iran")
test_palindrome("un roc si biscornu")
