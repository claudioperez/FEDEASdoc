# Claudio Perez
# May 2020 
# FEDEASLab documentation

def detail2(item,output):
    output.write('<tr class="hide-table-padding"> \n <td></td> \
                  <td colspan="3">  \
                  <div id="collapse{}" class="collapse in p-3">'.format(item['name']))
    # output.write('<div class="row">')
    # output.write('<div class="col-6">')
    try: 
        output.write('\n<b>Parameters</b>\n')
        output.write('<ul>\n')
        for param in item['parameters']:
            output.write('<li> <code>{}</code>: {}</li>\n'.format(param['name'],param['description']) )
        output.write('</ul>\n')
    except: pass
    try: 
        output.write('\n<b>State</b>\n')
        output.write('<ul>\n')
        for param in item['state']:
            output.write('<li> <code>{}</code>: {}</li>\n'.format(param['name'],param['description']) )
        output.write('</ul>\n')
    except: pass

    try:
        output.write('<div class="col-6"><img src="../img/{}.png"></div>'.format(item['name'])) 
    except: pass
    output.write('</td> \n </tr>')


def row2(item,output):
    output.write('\n\t<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordion{}" data-parent="#accordion{}" href="#collapse{}">'.format(*[item['name']]*3))
    output.write('<td class="expand-button"></td>')
    output.write('\n\t<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="{}.html">{}</a></td>'.format(*[item['name']]*2))
    output.write('\n\t<td>{} </td></tr>'.format(item['description']))
    # output.write('\n\t<td><a href="#" id="show_1">Details</a></td>')
    # output.write('\n\t<td>\n<div id="extra_1" style="display: none;">') #colspan="5"
    # output.write('\n\t</tr>')
    detail2(item,output)

    # output.write('\n\t</div>\n</td>\n</tr>')

##############################################################################

import yaml

with open('elemlib.yml') as read_file:
    data = yaml.full_load(read_file)

with open('../docs/elemlib.md', 'w+') as output:
    output.write('---\nhide_toc: true\n...\n')
    output.write('# Element Library')

    output.write('<div class="table-responsive">\n<table class="table">')

    output.write('<thead> \n \
        <tr> \n \
            <th scope="col">#</th> \n \
            <th scope="col">Element</th> \n \
            <th scope="col">Description</th> \n \
        </tr> \n \
        </thead> \n <tbody>')
    for item in data:
        row2(item,output)

    output.write('</tbody> \n </table>')

    output.write('<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" \
			  integrity="sha256-4+XzXVhsDmqanXGHaHvgh1gMQKX40OUvDEBTu8JcmNs=" \
			  crossorigin="anonymous"></script>')

    output.write('<script>')
    s1 = '$("a[id^=show_]").click(function(event) {'
    s2 = '$("#extra_" + $(this).attr('
    s3 = "'id').substr(5)).slideToggle("
    s4 = '"fast"); \n event.preventDefault();})' 
    output.write(s1+s2+s3+s4)
    output.write('</script>')

