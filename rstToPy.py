import doctest

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
        print (item)
        if isinstance(item, doctest.Example):
            if not inside_doctest:
                inside_doctest = True
                if current_docstring:
                    doctest_strings.append(''.join(current_docstring))
                current_docstring = []
            if  item.want:
                current_docstring.append(f'assertEqual({item.source}, {item.want})')
            else:
                current_docstring.append(f'{item.source}')
        else:
            if inside_doctest:
                inside_doctest = False
                doctest_strings.append(''.join(current_docstring))
                current_docstring = []
            if isinstance(item, str) and item.strip():
                current_docstring.append(f'# {item}\n')

    if current_docstring:
        doctest_strings.append(''.join(current_docstring))

    # Crear el contenido del archivo Python
    py_content = '' + '\n'.join(doctest_strings)

    # Limpiar líneas en blanco innecesarias y comentarios
    py_content = '\n'.join(line for line in py_content.split('\n') if line.strip())

    # Escribir los doctests en el archivo Python
    with open(py_file, 'w') as f:
        f.write(py_content)

if __name__ == "__main__":
    rst_file = 'scenario_sale.rst'
    py_file = 'doctests_scenario_sale.py'
    extract_doctests_to_py(rst_file, py_file)
