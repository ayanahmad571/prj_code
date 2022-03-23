def write_txt(file_name, data):
    with open(file_name, 'w') as f:
        for l in data:
            f.write('%s\n' % l)