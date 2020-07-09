import json, sys

import json_schema_for_humans.generate as mdjs 


with open('make.json') as f: build_opts = json.load(f)

###########################################################################
# SRC
###########################################################################
import matlab.engine



###########################################################################
# API
###########################################################################

build_opts['api']['kwds'] = dict(
    schema_file_name='../../FedeasAPI/schemas/post.schema.json',
    result_file_name='../docs/sch/index.md',
    minify=True,
    expand_buttons=True
)
# mdjs.generate_from_filename(**api_options)


if __name__ == "__main__":
    eng = matlab.engine.start_matlab()
    eng.addpath('m2html/')

    if 'serve' in sys.argv:
        pass

    while True:
        option = input('^^')
        if option == 'exit':
            break 
        elif option == 'src':
            with open('make.json') as f: build_opts = json.load(f)['src']
            eng.m2html(*build_opts['args'],nargout=0)
        elif option == 'api':
            with open('make.json') as f: build_opts = json.load(f)['api']
            mdjs.generate_from_filename(**build_opts['kwds'])

