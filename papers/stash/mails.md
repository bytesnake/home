I would like to have mail client based on Git, working together with the Vim
fugitive plugin. This entails that new mails in INBOX are added existing
workspace and mails are sent out, once a commit is issued. I use as middleware
the `himalaya` project.

I divide mails roughly in `git` based, `mail` normal mails, `brief` friends
mail and `work` mail for work. The Vim command `:Mails`, pulls all mails from
INBOX into their respective folder and opens then fugitive `:Git` overview in a
new tab.

 - slugify title for file-name
 - if file-name already exists, then add a new entry in markdown
 - once everything merged run `git clean -fd` for removing remaining files, not
     in index

We work with the following format

```
<global header>

# <nmbr> <title>

<local header>
<content>
```

The header defines from, to, cc etc. The local header modifies a subset of the
global one. The number references to mail at server side, if it is missing, then
a number is added after sending out.

 - invoke special script in pre-commit hook
 - find all entries where number is missing
 - create mail out of these and send them out
 - add number afterwards and amend commit

To make this procedure more easy we also add special Git commands for creating
reply, forward etc. They invoke the `himalaya template` subcommand based on the
ID of the last entry.
