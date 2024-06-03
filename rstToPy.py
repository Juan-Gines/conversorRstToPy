import doctest
from docutils.core import publish_doctree

def rst_to_doctest(rst_file, py_file):
    # Leer el archivo rst
    with open(rst_file, 'r') as f:
        rst_content = f.read()

    # Convertir el contenido rst a un árbol doctree
    doctree = publish_doctree(rst_content)

    # Extraer los bloques de código de los nodos doctest
    code_blocks = []
    for node in doctree.traverse():
        if node.tagname == 'literal_block' and 'python' in node.attributes['classes']:
            code_blocks.append(node.rawsource)

    # Escribir los bloques de código en un archivo Python
    with open(py_file, 'w') as f:
        f.write('\n'.join(code_blocks))

if __name__ == "__main__":
    rst_to_doctest('scenario_sale.rst', 'scenario_sale.py')
