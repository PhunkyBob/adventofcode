import regex as re

def test_match_tags():
    """ Matching HTML tags. """
    sample = r'''
<b>Bold</b><i>Italics</i>
<b><i>Bold Italics</i></b>
<mod>Mod</mod><em>Emphasis</em>
<h2>Level 2 Header</h2>
<code>Bad code match</cod>
<h1>Bad header match</h3>
'''
        
    regex = re.compile(r'''
(?P<tag>
<(?P<otag>\w+)> # opening tag
(?P<text>[^<]*)|(?P>tag) # contents
</(?P<ctag>(?P=otag))> # closing tag
)''', re.VERBOSE)
        
    print('\nUsing references:\notag ctag text')
    for match in regex.finditer(sample):
        print('{otag:8}{ctag:8}{text:12}'.format(
            **match.groupdict()))
    
test_match_tags()