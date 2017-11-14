# gtlb - a tool to open Gitlab projects in a browser from the command line
![](https://gitlab.com/gitlab-com/gitlab-artwork/raw/master/logo/logo-square.png)

## Overview
* Install and execute to open a Gitlab project in your browser from the command line
* Useful for command line git users e.g. to push changes and open up a Merge Request `git push origin feature/mything && gtlb --pulls`
* Must from within the root directory of a checked out repo

### Install the CLI and view the available options
```bash
$ pip install gtlb
$ gtlb --help
```

### Open a projects merge requests page
```bash
$ cd your-repo-dir
$ gtlb --merge
```

### Open a projects releases page
```bash
$ cd your-repo-dir
$ gtlb -r
```

### Available options as of 0.0.1
```
  -h, --help          show this help message and exit
  --home              Open at the home page (Default action)
  -m, --merges        Open at Merge Requests page
  -b, --branches      Open at Branches page
  -s, --settings      Open at Settings page
  -r, --releases      Open at Releases page
  -t, --tags          Open at Tags page
  -M, --members       Open at members page
  -w, --wiki          Open at Wiki
  -i, --issues        Open at Issues page
  -a, --activity      Open at Activity page
  -I, --integrations  Open at Integrations page
  -c, --cicd          Open at CI/CD page
  -d, --debug         Enable debug output
  -v, --version       Show the installed version of gtlb
```

## Feel free to fork/PR any contributions
