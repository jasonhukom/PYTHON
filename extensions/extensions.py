def main():
    suffix = input('File name: ')
    mime = mime_type(suffix)
    match mime:
        case 'gif' | 'png':
            print(f"image/{mime}")
        case 'jpg' | 'jpeg':
            print('image/jpeg')
        case 'pdf' | 'zip':
            print(f"application/{mime}")
        case 'txt':
            print(f"text/plain")
        case _:
            print('application/octet-stream')

def mime_type(exten):
    x = ['0', '']
    for i in range(len(exten)):
        if exten[i:i + 1] == '.':
            x.insert(0, i)


    y = int(x[0])
    return exten[y + 1:].lower().strip()


main()

