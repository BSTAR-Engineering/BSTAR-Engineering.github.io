# Website Generation
## Layout
 * The generated HTML lives in `website`
 * The Website Content lives in `website-source/content` as a series of YAML files.
 * The Template the content is applied to lives in `website-source/template`

## Scripts
 * The script that applies the content to the template is `generateWebsite.py`
 * The script that pushes the website to the master branch and makes it live is `pushWebsite.py`
 * The script that starts up a local webserver and hosts the generated site while watching for changes in the source and updating the content is `previewUpdate.py`

## How does the templating work?
  * We will use the mustache templating language.
  * The script will run through the template directory and copy it to the website directory while running any file ending in .stsh through moustache and stripping off the .stsh ending.
