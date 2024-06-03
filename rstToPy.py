import re
import os

def rst_to_py(rst_file):
    py_file = f"{os.path.splitext(rst_file)[0]}.py"

    with open(rst_file, 'r') as rst, open(py_file, 'w') as py:
        lines = rst.readlines()
        in_code_block = False
        previous_code_line = ""

        for i, line in enumerate(lines):
            stripped_line = line.strip()

            # Detect start of a code block
            if re.match(r'^\s*>>>\s+', line):
                in_code_block = True
                previous_code_line = line.lstrip(' ').lstrip('> ')
            elif in_code_block:
                # Check if line is a continuation of the code block
                if re.match(r'^\s*\.\.\.\s+', line):
                    # Preserve the indentation of continuation lines
                    indent = line.find('...')
                    py.write(' ' * indent + line.lstrip('. '))
                    previous_code_line = line.lstrip('. ')
                else:
                    # Check if the next line is an indented value and not empty
                    if i + 1 < len(lines) and re.match(r'^\s+\S+', lines[i + 1]):
                        indented_value = lines[i + 1].strip()
                        py.write(f"assert {previous_code_line.strip()} == {indented_value}\n")
                        previous_code_line = ""
                    else:
                        if previous_code_line:
                            py.write(previous_code_line)
                        previous_code_line = ""
                        in_code_block = False
            if not in_code_block:
                # Write non-code lines as comments
                if stripped_line:
                    py.write(f"# {line}")
                else:
                    py.write(line)
            if in_code_block and not re.match(r'^\s*>>>\s+', line):
                previous_code_line = ""

if __name__ == "__main__":
    rst_file = input("Por favor, ingrese la ruta del archivo RST: ")
    if os.path.isfile(rst_file):
        rst_to_py(rst_file)
        print(f"Convertido {rst_file} a {os.path.splitext(rst_file)[0]}.py")
    else:
        print("El archivo especificado no existe.")
