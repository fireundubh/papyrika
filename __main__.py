import argparse
import glob
import os
import re


def get_scriptname_declaration(lines: list) -> tuple:
    for line_index, line_content in enumerate(lines):
        result = line_content.strip()

        if result.lower().startswith('scriptname'):
            return line_index, line_content

    return None, None


def main():
    input_path = os.path.abspath(args.input)

    if not os.path.exists(input_path):
        exit('Path does not exist: {}'.format(input_path))

    files = glob.glob(os.path.join(input_path, '**\*.psc' if args.recursive else '*.psc'), recursive=args.recursive)

    for script_path in files:
        _, tail = os.path.split(script_path)
        file_name, _ = os.path.splitext(tail)

        with open(script_path, mode='r') as data:
            lines = data.readlines()

            # trry to get scriptname declaration
            i, scriptname_declaration = get_scriptname_declaration(lines)

            if scriptname_declaration is None:
                print('Cannot find ScriptName declaration in file:', script_path)
                continue

            # try to get preceding whitespace
            whitespace = re.match('^(\s+).*$', scriptname_declaration)
            whitespace = whitespace.group(0) if whitespace else ''

            # parse declaration
            scriptname_keyword, script_path, *declaration_suffixes = scriptname_declaration.strip().split(' ')

            # parse script path
            *script_path_prefixes, script_name = script_path.split(':')

            if not (script_name == file_name):
                path_elements = [*script_path_prefixes, file_name]
                fixed_script_path = ':'.join(path_elements)

                line_elements = [scriptname_keyword, fixed_script_path, *declaration_suffixes]
                lines[i] = whitespace + ' '.join(line_elements) + '\n'

                with open(script_path, mode='w') as out:
                    out.writelines(lines)
                    print('Fixed:', script_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Papyrika')
    parser.add_argument('-i', '--input', action='store', required=True, help='Source folder')
    parser.add_argument('--recursive', action='store_true', default=False, help='Recursively process scripts in source folder')
    args = parser.parse_args()
    main()
