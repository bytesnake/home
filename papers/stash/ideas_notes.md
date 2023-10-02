
# Ideas for note taking extensions

### Important

Having notes on my mobile phone is a good way to find reading space. I would
like to make this process as easy as possible, and publish to Mastodon, where
toots can be shared and liked from other users in other instances.

 - publish notes to zettelhaus in pre-commit hook
   - write binary parses and updates zettelhaus notes
   - amend number of notes and some metadata to commit message

I found CodiMD a great way to write the Application for prototypefund and hosted
it at `pad.zettel.haus`. We could also put literature notes there, that would
even make it possible to edit them collaboratively. There should be some way of
hosting the PDF, if possibly open, on CodiMD.
Notes can then link to read-only CodiMD document sections, though there is the
need for someone to translate this automatically.

 - sync literature notes on CodiMD
    - bring the whole document up to the CodiMD instance
    - sync PDFs behind password-wall (can we also use SVG for that?)

### Not so important

 - writing mathematical notation
   - create file with latex notation; possible with preamble
   - how to publish to zettelhaus? include as svg?
   - pros: abbreviations, correct notations
   - cons: separate parser for LaTeX seems extensive addition
