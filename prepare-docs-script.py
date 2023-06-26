with open('./docs/index_copy.html', 'r') as f:  # gh action gives file not found; try forward slash
    contents = f.read()
#    output = contents.format('testtext'='<br>Hello world, from python action!')
#    f.seek(0)  # move pointer back to beginning
#    f.write(output)
#    f.truncate()  # remove anything existing after the place that was written to
output = contents.format(testtext = '<br>Hello world, from python action!')
with open('./docs/index.html', 'w') as f:
    f.write(output)
    f.flush()
