import os


def main():
    print_header()
    get_or_create_output_folder()
    # download cats
    # display cats
    print('hello from main')


def print_header():
    print('--------------------------')
    print('         CAT FACTORY')
    print('--------------------------')


def get_or_create_output_folder():
    folder = 'cat_pictures'
    full_path = os.path.abspath(os.path.join('.', folder))
    print(full_path)


if __name__ == '__main__':
    main()