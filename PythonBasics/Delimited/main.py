def split_and_join(line):
    separated = line.split(" ")
    return "-".join(separated)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)