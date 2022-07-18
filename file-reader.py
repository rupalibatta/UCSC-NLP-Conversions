def read_AMRs_from_file(filename):
    corpus = {}

    f = open(filename, 'r')
    text = f.read()
    f.close()

    data_items = text.split("\n\n")

    for item in data_items[1:]:
        lines = item.split("\n#")
        sent = amr = fname = ""
        for line in lines:
            if '::snt' in line:
                sent = line[7:]
                # print(sent)
            elif '::save-date' in line:
                amr_info_list = line.split(".txt\n")
                fname = amr_info_list[0][36:]
                # print(fname)
                amr = amr_info_list[1]
                # print(amr)

        corpus[fname] = {"sent": sent, "amr": amr}

    return corpus


if __name__ == "__main__":
    # read_AMRs_from_file('data/amr-test.txt')

    corpus = read_AMRs_from_file('data/amr-little-prince-v1.6.txt')
    print(corpus)
    print(len(corpus))

