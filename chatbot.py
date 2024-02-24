# -*- coding: utf-8 -*-
"""Chatbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12aMrTaYztPsPkGMhiJ4YTWDqzRVEXGll
"""

from nltk.chat.util import Chat,reflections

pairs=[
  [
      r"(.*my name is(.*))",
      ["Hello %2,How are you today?",]
  ],
  [
      r"(.*help(.*))",
      ["I can help you",]
  ],
  [
      r"(.*)your name ? ",
      ["My name is thecleverprogrammer,but you can just call me robot and I'm a chatbot .",]
  ],
  [
      r"sorry(.*)",
      ["It's alright","Its OK,never mind that",]
  ],
  [
      r"i'm(.*)(good|well|okay|ok)",
      ["Nice to hear that","Alright,great!",]
  ],
  [
      r"(hi|hey|hello|hola|holla)(.*)",
      ["Hello","Hey there",]
  ],
  [
      r"What (.*) want ?",
      ["Make me an offer Ican't refuse",]
  ],
  [
      r"(.*)created(.*)",
      ["Tesnim Strazimiri created me using Python'NLTK library","top secre ;)",]
  ],
  [
      r"(.*)(location|city) ? ",
      ['Istanbul,Turkey',]
  ],
  [
      r"(.*raining in(.*))",
      ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
  ],
  [
      r"how (.*) helath (.*)",
      ["Health is very important,but I am a computer,so Idon't need to worry about my health",]
  ],
  [
      r"(.*)(sports|game|sport)(.*)",
      ["I'm very big fan of Cricket",]
  ],
  [
      r"who (.*)(Cricketer|Batsman)?",
      ["Virat Kohli"]
  ],
  [
      r"quit",
      ["Bye for now.See you soon :)","It was nice talking to you.See you soon :)"]
  ],
  [
      r"(.*)",
      ['That is nice to hear']
  ],
]

#default message at the start of chat
print("Hi,I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation.Type quit to leave")

#Create chat bot
chat=Chat(pairs,reflections)

#start conversation
chat.converse()