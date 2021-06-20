def repeated_word(string):
  first_word = ''
  first_word_location = 0
  second_word = ''
  second_word_location = 0
  repeated_once = False
  found = False
  for char in string:
    if repeated_once:
      first_word = ''
      repeated_once = False
    if char !=" ":
      if char != ',' or char != '.':
        first_word += char.lower()
    else:
      comparison_word = ''
      counter = 0
      repeated_once = False
      repeated_twice = False
      for char in string:
        if char !=" ":
          if char != ',' or char != '.':
            comparison_word += char.lower()
        else:
          if comparison_word == first_word:
            if not repeated_once:
              repeated_once = True
            else:
              repeated_twice = True
              first_word_location = counter
            comparison_word = ''
          else:
            counter += 1
            comparison_word = ''
        if repeated_twice:
          if first_word_location < second_word_location or second_word_location == 0:
            second_word = first_word
            second_word_location = first_word_location
            first_word = ""
            found = True
            break
  if not found:
    return False
  return second_word

if __name__ == '__main__':
  print(repeated_word("Once upon a time, there was a brave princess who..."))
  print(repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))
  print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))
  print(repeated_word("Once upon a time, there was no brave princess who..."))
