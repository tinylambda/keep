import base64
import textwrap


if __name__ == '__main__':
    with open(__file__, 'r', encoding='utf-8') as f:
        raw = f.read()
        initial_data = raw.split('#end_pymotw_header')[1]

    byte_string = initial_data.encode('utf-8')
    encoded_data = base64.b64encode(byte_string)

    num_initial = len(byte_string)

    # There will never be more than 2 padding bytes.
    padding = 3 - (num_initial % 3)

    print(f'{num_initial} bytes before encoding')
    print(f'Expect {padding} padding bytes')
    print(f'{len(encoded_data)} bytes after encoding\n')
    print(encoded_data)
