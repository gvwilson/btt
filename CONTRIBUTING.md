# Contributing

Contributions are very welcome;
please file an issue or submit a pull request to [our website][config_website]
or [contact us by email][config_email].
All contributors must abide by our Code of Conduct.
This material uses [Ark][ark] with some custom extensions in `./lib/mccole/extensions`.
Please run `make` in the root directory to get a list of available commands,
several of which on scripts in the `./lib/mccole/bin/` directory.

## Chapters and Appendices

1.  Each chapter or appendix has a unique slug such as `topic`.
    Its prose lives in <code>./src/<em>topic</em>/index.md</code>
    and its slides (if any) in <code>./src/<em>topic</em>/slides.md</code>,
    and there is an entry for it in the `chapters` or `appendices` dictionary
    in Ark's configuration file `./config.py`.
    The order of entries in these two dictionaries
    determines the order of the chapters and appendices.

1.  Prose and slides do *not* have YAML headers;
    their metadata is taken from the `mccole.yml` file in their sub-directory.

## Slides

1.  Slides are written in Markdown.
    Each starts with a level-2 header,
    and slides are separated from each other by triple dashes (`---`).

1.  Put a comment `<!--# class="aside" -->` at the top of a slide
    to format it as an aside,
    or a comment `<!--# class="exercise" -->`
    to format it as an exercise.

## Prose

Each section within an `index.md` file must use a heading like this:

```markdown
## Some Title {: #topic-sometitle}
```

This creates an `h2`-level heading with the HTML ID `topic-sometitle`.
Please use the page's slug instead of `topic`
and hyphenate the words in the ID.

## Cross-References

To create a cross-reference to a chapter or appendix write:

```markdown
[%x topic %]
```

where `topic` is the slug of the chapter being referred to.
This shortcode is converted to `Chapter N` or `Appendix N`
or the equivalent in other languages.
Please only refer to chapters or appendices, not to sections.

## External Links

1.  The table of external links lives in `./info/links.yml`.
    Please add entries as needed,
    or add translations of URLs to existing entries using
    a two-letter language code as a key.

1.  To refer to an external link write:

    ```markdown
    [body text][link_key]
    ```

Please do *not* add links directly with `[text](http://some.url)`:
keeping the links in `./info/links.yml` ensures consistency
and makes it easier to create a table of external links.

## Code Inclusions

To include an entire file as a code sample write:

```markdown
[% inc file="some_name.py" %]
```

The file must be in or below the directory containing the Markdown file.

## Figures

1.  Put the image file in the same directory as the chapter or appendix
    and use this to include it:

    ```markdown
    [% figure
       slug="topic-some-key"
       img="some_file.svg"
       caption="Short sentence-case caption."
       alt="Long text describing the figure for the benefit of visually impaired readers."
    %]
    ```

    Please use underscores in filenames rather than hyphens:
    Python source files' names have to be underscored so that they can be imported,
    so all other filenames are also underscored for consistency.
    (Internal keys are hyphenated to avoid problems with LaTeX during PDF generation.)

1.  To refer to a figure write:

    ```markdown
    [%f topic-some-key %]
    ```

    This is converted to `Figure N.K`.

1.  Use [drawio.com][draw_io] to create SVG diagrams
    in black and white with a 12-point Helvetica font for all text.

1.  Please avoid screenshots or other pixellated images:
    making them display correctly in print is difficult.

## Tables

1.  Put the Markdown version of the table in a file ending in `.tbl`
    and reference it like this:

    ```markdown
    [% table
       slug="meetings-log"
       tbl="meetings-log.tbl"
       caption="An example of team status updates."
    %]
    ```

1.  To refer to a table write:

    ```markdown
    [%t topic-some-key %]
    ```

    This is converted to `Table N.K`.

## Bibliography

1.  The BibTeX bibliography lives in `./info/bibliography.bib`.
    Please add entries as needed;
    you may find <https://doi2bib.org> useful for creating entries.
    Please format keys as `Author1234`,
    where `Author` is the first author's family name
    and `1234` is the year of publication.
    (Use `Author1234a`, `Author1234b`, etc. to resolve conflicts.)

1.  To cite bibliography entries write:

    ```markdown
    [%b key1 key2 key3 %]
    ```

## Minor Formatting

1.  To create a callout box, use:

    ```
    <div class="callout" markdown="1">

    ### Title of Callout

    text of callout

    </div>
    ```

    Use "Sentence Case" for the callout's title,
    and put blank lines before and after the opening and closing `<div>` markers.
    You *must* include `markdown="1"` in the opening `<div>` tag
    to ensure that Markdown inside the callout is processed.

[ark]: https://www.dmulholl.com/docs/ark/main/
[config_email]: mailto:gvwilson@third-bit.com
[config_website]: https://github.com/gvwilson/btt/
[draw_io]: https://www.drawio.com/
