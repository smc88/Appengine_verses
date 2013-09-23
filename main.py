#!/usr/bin/env python

import os
import cgi
import urllib
import webapp2
import jinja2
from output import book
from google.appengine.api import users
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'])
MAIN_PAGE = """
<html>
  <body>
    <form action="/" >
      <div><textarea type="number" name="verseId" rows="3" cols="10"></textarea></div>
      <div><input method="get" type="submit" value="find Verse"></div>
      <div><input method="next" type="submit" value="next"></div>      
    </form>
  </body>
</html>
"""
VERSE_ID = 1
DEFAULT_BOOK_VERSE_KEY='default_verse'

def book_verse_key(verse_key=DEFAULT_BOOK_VERSE_KEY):
  return ndb.key('Verse', verse_key)
  
class BookVerse(ndb.Model):
  verse_id = ndb.IntegerProperty(indexed=True)
  text = ndb.StringProperty(indexed=True)
  book = ndb.StringProperty(indexed=True)
  chapter = ndb.IntegerProperty(indexed=True)
  verse_number = ndb.IntegerProperty(indexed=True)
  verse = ndb.StringProperty(indexed=False)

class MainPage(webapp2.RequestHandler):

  def post(self,verse):
    for value1 in verse:
      self.response.write('<br> text len: ' + str(len(value1.text)))
      self.response.out.write('<br>    verse: ' + str(value1.verse_id))
      self.response.out.write('<br>     book: ' + str(value1.book))
      self.response.out.write('<br>     text: ' + str(value1.text))
      self.response.out.write('<br>  chapter: ' + str(value1.chapter))
      self.response.out.write('<br>verse_num: ' + str(value1.verse_number))
      self.response.out.write('<br>    verse:' + str(value1.verse))
  
  def next(self,VERSE_ID=VERSE_ID):
    VERSE_ID = VERSE_ID + 1
    verse = BookVerse.gql("where verse_id = :1", VERSE_ID)
    self.post(verse)

  def get(self,VERSE_ID=VERSE_ID):
    user = users.get_current_user()
    if user:
      self.response.write(MAIN_PAGE)
    else:
      self.redirect(users.create_login_url(self.request.uri))
    try:
      VERSE_ID = int(self.request.get('verseId'))
    except:
      pass    
    verse = BookVerse.gql("where verse_id = :1", VERSE_ID)
    self.post(verse)
app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)

"""        value = book[str(3)]
        self.response.write('<br> text len: ' + str(len(value[1])))
        self.response.out.write('<br>    verse: ' + str(3))
        self.response.out.write('<br>     book: ' + str(value[0]))
        self.response.out.write('<br>     text: ' + str(value[1]))
        self.response.out.write('<br>  chapter: ' + str(value[2]))
        self.response.out.write('<br>verse_num: ' + str(value[3]))
        self.response.out.write('<br>    verse:' + str(value[4]))

  
        book1 = BookVerse()
        book1.verse_id = verse_id
        book1.book = value[0]
        book1.text = value[1]
        book1.chapter = int(value[2])
        book1.verse_number = int(value[3])
        book1.verse = value[4]
        book1.put()
"""
'''      try:
        value = book[str(verse_id)]
        book1 = BookVerse()
        book1.verse_id = verse_id
        book1.book = value[0]
        book1.text = value[1]
        book1.chapter = int(value[2])
        book1.verse_number = int(value[3])
        book1.verse = value[4]
        book1.put()
        self.response.write('<br><br> new record added')
      except:
        self.response.write('<br><br>record already exists')
    def post(self):
      for key, value in book.iteritems():
        book1 = BookVerse()
        book1.verse_id = int(key)
        book1.book = value[0]
        book1.text = value[1]
        book1.chapter = int(value[2])
        book1.verse_number = int(value[3])
        book1.verse = value[4]
        book1.put()
      self.response.out.write(str(key))  
'''
'''
#        self.response.out.write('<br>' + str(value.verse_id))
#        self.response.out.write(book[str(value.verse_id)])
#        self.response.out.write('<br>' + str(value.book))
#        self.response.out.write('<br>' + str(value.text))
#        self.response.out.write('<br>' + str(value.chapter))
#        self.response.out.write('<br>' + str(value.verse_number))
#        self.response.out.write('<br>' + str(value.verse))
'''
'''
class Verses(webapp2.RequestHandler):
  def post(self):
    verse_id = 1
    verse_id = BookVerse(parent=book_verse_key(verse_id))
    verse_id.verse = self.request.get('verse')
    return verse_id
'''