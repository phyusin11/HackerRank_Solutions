def minion_game(string):
    # your code goes here
    Kevin = Stuart = 0
    vowel="AEIOU"
    size = len(string)
    for i in range(size):
        if string[i] in vowel:
            Kevin += size -i
        else:
            Stuart+= size -i
    
    if Kevin > Stuart:
        print(f'Kevin {Kevin}')
    elif Stuart>Kevin:
        print(f'Stuart {Stuart}')
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)