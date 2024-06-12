import doctest
import os

def extract_doctests_to_py(rst_file, py_file):
    # Leer el contenido del archivo RST
    with open(rst_file, 'r') as f:
        rst_content = f.read()

    # Crear un parser de doctest
    parser = doctest.DocTestParser()

    # Parsear el contenido del archivo RST
    doctests = parser.parse(rst_content, name=rst_file)

    # Filtrar solo los bloques de ejemplo de doctest
    doctest_strings = []
    current_docstring = []
    inside_doctest = False

    for item in doctests:
        if isinstance(item, doctest.Example):
            if not inside_doctest:
                inside_doctest = True
                if current_docstring:
                    doctest_strings.append(''.join(current_docstring))
                current_docstring = []
            if item.want:
                if item.exc_msg:
                    indexMsg = item.exc_msg.find(':')
                    indexSource = item.source.find('#')
                    current_docstring.append(f'with assertRaises({item.exc_msg[:indexMsg].strip()}):\n    {item.source[:indexSource].strip()}\n')
                else:
                    current_docstring.append(f'assertEqual({item.source.strip()}, {item.want.strip()})\n')
            else:
                current_docstring.append(f'{item.source}')
        else:
            if inside_doctest:
                inside_doctest = False
                doctest_strings.append(''.join(current_docstring))
                current_docstring = []
            if isinstance(item, str) and item.strip() or item == '\n':
                if item == '\n':
                    current_docstring.append(item)
                else:
                    splitItem = item.split('\n')
                    filteredItem = ''.join('# ' + line + '\n' for line in splitItem if line.strip())
                    filteredItem = filteredItem.split('\n')
                    for i in range(len(filteredItem)):
                        if filteredItem[i].endswith('::'):
                            filteredItem[i] = '\n' + filteredItem[i].replace('::', '')
                        else:
                            filteredItem[i] = filteredItem[i] + '\n'
                    filteredItem = ''.join(filteredItem)
                    current_docstring.append(filteredItem)

    if current_docstring:
        doctest_strings.append(''.join(current_docstring))

    # Crear el contenido del archivo Python
    py_content = ''.join(doctest_strings)

    # Escribir los doctests en el archivo Python
    with open(py_file, 'w') as f:
        f.write(py_content)

def process_directory(directory):
    # Recorrer todos los archivos en la carpeta y subcarpetas
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.rst'):
                rst_file = os.path.join(root, file)
                py_file = os.path.splitext(rst_file)[0] + '.py'
                extract_doctests_to_py(rst_file, py_file)

def process_file(file):
    rst_file = file
    py_file = os.path.splitext(rst_file)[0] + '.py'
    extract_doctests_to_py(rst_file, py_file)
if __name__ == "__main__":
    # Pedir la ruta de la carpeta, sino se usa la actual
    route = input('Introdueix la ruta a la carpeta o a l\'arxiu: ').strip()
    if not route:
        route = os.getcwd()
    if route.endswith('.rst'):
        process_file(route)
    else:
        process_directory(route)
