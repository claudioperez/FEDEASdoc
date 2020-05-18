import yaml

with open('matlib.yaml') as read_file:
    lib = yaml.full_load(read_file)

with open('../docs/matlib.md','w+') as output:
    output.write('# Material Library\n')
    for mat in lib:
        output.write('## {}\n'.format(mat['name']))
        output.write('<details>\n')
        output.write('<summary>{}</summary>\n'.format( mat['description']) )
        try: 
            output.write('\n**Parameters**\n')
            output.write('<ul>\n')
            for param in mat['parameters']:
                output.write('<li> `{}`: {}</li>\n'.format(param['name'],param['description']) )
            output.write('</ul>\n')
        except:
            pass
        try: 
            output.write('\n**State**\n')
            output.write('<ul>\n')
            for param in mat['state']:
                output.write('<li> `{}`: {}</li>\n'.format(param['name'],param['description']) )
            output.write('</ul>\n')
        except:
            pass
        output.write('</details>\n\n')

