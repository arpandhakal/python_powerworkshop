import markdown

md = markdown.Markdown()
appended = []

with open('markdown-sample.md') as fp:
    line = fp.readline()
    convert = md.convert(line)
    appended.append(convert)

with open('converted.html') as fp:
    for a in appended:
        fp.write(a + '\n')

