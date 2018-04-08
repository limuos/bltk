# STANDARD WORD TOKENIZE
def word_tokenize(inp):
    tokens, token = [], ""
    for index in range(len(inp)):
        if inp[index] != " ":
            token += inp[index]
        if inp[index] == " " or index == len(inp)-1:
            tokens.append(token)
            token = ""
    return tokens
