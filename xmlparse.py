class XML:
  """Class to build python objects from an xml input"""
  
  # This Element subclass is currently dead code
  # alternative to using a dictionary to store kvpairs - this would preserve
  # multiple values for duplicate tags, which is currently a bug
  # 
  class Element:
    """Smallest element of XML: e.g. <tag attr=attrvalue>content</tag>"""
    tag = ""
    content = ""
    attributes = None

    def __init__(self, chunk = ""):
      ante, post = '<', '>'
      index, outdex = 0, 0
      index = chunk.find(ante) + len(ante)
      outdex = chunk.find(post)
      tag = chunk[index:outdex]
      attr_scan = tag.find('=')
      if attr_scan > -1: # if there are '='s in <> block, there are kv attributes
        attributes = {}
        while index < attr_scan < outdex:
          key = tag[:attr_scan].split()[-1] # assign attr as dict key in <tag attr = ..."
          value = tag[attr_scan+1:].split()[0] # <tag ... attr = [value] .... >
          attributes[key] = value # save in dictionary (temp)
          search = tag[attr_scan+1:].find('=')
          if search == -1:
            break
          attr_scan = attr_scan + tag[attr_scan + 1:].find('=') + 1
        tag = tag.split()[0] # only first word of xml is a proper tag
        self.attributes = attributes # make temp dictionary a field
      self.tag = tag # save temporary tag to Element instance
      
      index = outdex + len(post) # set index to character after '>' of tag
      outdex = index + self.string[index:].find(post) # set outdex to next '<'
      content = chunk[index:outdex]
      self.content = content

    def __repr__(self):
      return '<' + self.tag + '>' + content + '</' + tag + '>'
    
  # End dead code

 
  
  string = ""
  tags = (,) # tuple
  kvpairs = None # list of Elements
  
  def _strip_tags(self):
    """Scan the XML object's string and return a generator object"""
    ante, post = '<', '>'
    index, outdex = 0, 0
    while outdex < len(self.string):
      print('\t' + self.string[outdex:])
      index = self.string[outdex:].find(ante) + len(ante) + outdex
      outdex = self.string[outdex + 1:].find(post) + outdex + 1
      if index >= outdex:
        break
      elif self.string[index:outdex].find('/') == -1: # ignore closing tags
        yield self.string[index:outdex]

  def value_by_tag(self, tag = ""):
    """Search XML object's basic string and return the value between the given tag"""
    if tag == "":
      return None
    ante = ('<' , tag, '>')
    post = ('</', tag, '>')
    anteStr = ''.join(ante)
    postStr = ''.join(post)
    index = self.string.find(anteStr) + len(anteStr)
    outdex = self.string.find(postStr)
    if index == -1 or outdex == -1:
      return None
    assert outdex >= index
    value = self.string[index:outdex]
    print('successful <{0}> tag extract: {1}'.format(tag, value))
    return value

  def get_element_by_tag(self, tag = ""):
    ante = ('<' , tag, '>')
    post = ('</', tag, '>')
    anteStr = ''.join(ante)
    postStr = ''.join(post)
    index = self.string.find(anteStr)
    outdex = self.string.find(postStr) + len(postStr)
    return self.string[index:outdex]

  def __str__(self):
    return self.string

  def __repr__(self):
    return self.string

  def __eq__(self, XML = None):
    if XML is None:
      return None
    elif self.kvpairs == XML.kvpairs:
      return True
    else:
      return False

  def __init__(self, string = ""):
    """ Create an XML object from a string containing xml"""
    self.string = string
    print(string)
    temp_tags = []
    tag_gen = self._strip_tags()
    self.kvpairs = {}
    for t in tag_gen:
      print("Tag yielded from self._strip_tags():\n{0}".format(str(t)))
      temp_tags.append(t)
      value = self.value_by_tag(t)
      if value and value.find('<') == -1:
        self.append(self.Element(
      elif value:
        self.kvpairs[t] = XML(value)
    self.tags = tuple(temp_tags)

if __name__ == '__main__':
  x = XML(*args, **kwargs)
