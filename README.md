TrelloHub
====

A tool for bidirectional integration between Trello and Github. See the wiki
for how Trello and Github items are mapped to each other.

The idea is that this is a static web page that acts basically as a Javascript
client between the two services. It should require minimal configuration besides
entering credentials information. Your data is not hosted or transfered anywhere
but in between the two services and in your browser's memory.

Building
====

This project is based on the HTML5 Boilerplate project and uses its buildfile and
structure with some minor changes. The project structure is also conformant to
Eclipse's static/dynamic web project structure.

**Changes to the build setup**
* The "publish" directory is "WebContent". This is to have the script build into the "live" version
Eclipse updates uses to update your live copy.
* Project files/assets are under the directory "trellohub". The build.xml file is still top-level

Deploying
====
This project builds with Ant and deploys using Fabric. If you need more information on
this deployment framework please see [fabfile.org](http://www.fabfile.org).

**Full-hook test/update/deploy**
`fab dropthehammer`

**Deploy**
`fab deploy`

**Undeploy**
`fab undeploy`

**Run Unit Tests**
`fab unittest`

**Update Github**
`fab github`

Libraries/Structure
====
This app uses the following
* Require.js
* jQuery, jQueryUI
* Bootstrap
* Backbone.js
* Hogan
* Nodeunit
* Underscore.js
* Trello REST API
* Github REST API