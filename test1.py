# test

from os import chdir

def test(*args, **kwargs):
  chdir('/py32Tools')
  from xmlparse import XML
  
  flatSingleWorking = """<fsw1>Wasdlk asdfk asdf</fsw1>"""
  flatMultipleWorking = """<fmw1>asdflkjadsfkjl</fmw1><fmw2>asdflkhjaghoiadsf</fmw2><fmw3>dslkfh asdlfk asfd</fmw3><fmw4>28sad asdk fadsf</fmw4>"""
  nestedSingleWorking = """<nestA><testsub1>asdfasdf</testsub1><testsub2>mn.mn,.,mn</testsub2></nestA>"""
  flatOpenInitialTag = """<invalid1asdflkasdfkl</invalid1><invaltest1>asdf</invaltest1</invaltest1>"""

  strings = [flatSingleWorking
             , flatMultipleWorking
             , flatOpenInitialTag
             #, nestedSingleWorking
             ]
  
  for string in strings:
    yield(XML(string))
