# g - a tool to open Gitlab projects in a browser from the command line
![](https://gitlab.com/gitlab-com/gitlab-artwork/raw/master/logo/logo-square.png)

## Overview
* Install and execute to open a Gitlab project in your browser from the command line
* Useful for command line git users e.g. to push changes and open up a Merge Request `git push origin feature/mything && g --pulls`
* Must from within the root directory of a checked out repo

### Install the CLI and view the available options
```bash
$ pip install g
$ g --help
```

### Open a projects merge requests page
```bash
$ cd your-repo-dir
$ g --merge
```

### Open a projects releases page
```bash
$ cd your-repo-dir
$ g -r
```

### Available options as of 0.0.3
```
  --home               Open the Home page (Default action)
  -p, --pulls          Open the Pull requests page
  -b, --branches       Open the Branches page
  -s, --settings       Open the Settings page
  -r, --releases       Open the Releases page
  -t, --tags           Open the Tags page
  -c, --collaboration  Open the Collaboration page
  -w, --wiki           Open the Wiki
  -i, --issues         Open the Issues page
```

## Feel free to fork/PR any contributions
