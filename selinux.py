import argparse
import re

def filter_selinux_denials(input_file_path, output_file_path):
    regex = re.compile(r'.*avc:  denied.*', re.IGNORECASE)

    with open(input_file_path, 'r', encoding='utf-8', errors='ignore') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            if re.search(regex, line):
                output_file.write(line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filter logcat file based on SELinux denials.')
    parser.add_argument('input_file_path', help='Path to the input logcat file')
    parser.add_argument('output_file_path', help='Path to the output filtered logcat file')
    args = parser.parse_args()

    filter_selinux_denials(args.input_file_path, args.output_file_path)
    print(f"Filtered SELinux denials saved to {args.output_file_path}.")
