**Problem:** Some boorus tag kantai collection characters with a `(kancolle)`
suffix, while others tag them with a `(kantai collection)` suffix. As far as
Hydrus is concerned, `admiral (kancolle)` and `admiral (kantai collection)` are
now two entirely different people!

So, I wrote a script that should help alleviate the manual labor involved in
assigning a sibling to every `(kancolle)` tag

First, gather up all the `(kancolle)` variants. I find the easiest way to do
this is to go to the search bar on the left and type in `kancolle`. You can see
how all the kancolle tags pop up. Select them all, and copy them all.

Your clipboard should now look like...

```
character:kaga (kancolle)
character:nagato (kancolle)
character:iowa (kancolle)
character:zuikaku (kancolle)
character:katsuragi (kancolle)
character:mutsu (kancolle)
(and so on...)
```

Paste them into a file named `kancolle.txt` (the name isn't really all that
important but I'll be using this filename for the rest of the tutorial)

Note that if there are some stray false positives, such as `title:my kancolle
fanart`, the script will ignore any tag that doesn't start with `character:` and
doesn't end with `(kancolle)` so you can leave those strays in there.

Now you have to run the script. Hopefully you know how to start a python script
on your OS. If you don't, now would be a good time to open another tutorial. You
also should know how to redirect IO to and from files.

On my Operating System (an Ubuntu derivative), I run

```
python3 kancolle_convert.py < kancolle.txt > siblings.txt
```

On Windows, you might have something similar. The important part is that the
script is invoked, it takes input from `kancolle.txt`, and puts its output into
`siblings.txt`

Open up `siblings.txt` and copy all the output to your clipboard.

Open `tags -> tag siblings`, click import, and then import the text that was
generated.

Now we see that the `(kancolle)` tags will be replaced by their `(kantai
collection)` equivalent:

![picture
1](images/87fbdd30bb8f357e2ac53ca39ca67e54fbf06c6fb0f49ac71ea3dd54489a112d.png)

Click `apply`

Now, in the future, suppose that you imported more files, and some more
`(kancolle)` tags found their way into the system. Simply repeat this process,
and add the new siblings. Note that the script only pays attention to tags that
end with `(kancolle)`, so any `(kantai collection)` false positives you paste in
should be ignored.
