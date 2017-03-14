import sys
if __name__ == '__main__':
    lines = sys.stdin.readlines()
    props = lines[0].split()
    scores = []
    for i in range(1, int(props[1]) + 1):
        scores.append(lines[i].split())
    average = [];
    temp = 0;

    for i in range(0, int(props[0])):
        for j in range(0, int(props[1])):
            temp += float(scores[j][i])
        average.append(temp/int(props[1]))
        print(temp/int(props[1]))
        temp = 0